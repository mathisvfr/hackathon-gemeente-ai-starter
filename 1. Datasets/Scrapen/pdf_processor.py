#!/usr/bin/env python3
"""
PDF processor script for scraped markdown content.
Finds markdown files that reference PDFs, downloads them, converts to markdown, and replaces the original files.
"""

import re
import argparse
import requests
import tempfile
from pathlib import Path
import logging
from urllib.parse import urljoin, urlparse
import time
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

try:
    import pypdf
    PYPDF_AVAILABLE = True
except ImportError:
    PYPDF_AVAILABLE = False
    logger.warning("pypdf not available. Install with: pip install pypdf")

try:
    import fitz  # PyMuPDF
    PYMUPDF_AVAILABLE = True
except ImportError:
    PYMUPDF_AVAILABLE = False
    logger.warning("PyMuPDF not available. Install with: pip install PyMuPDF")


class PDFProcessor:
    def __init__(self, input_dir, dry_run=False, delay=1.0):
        self.input_dir = Path(input_dir)
        self.dry_run = dry_run
        self.delay = delay  # Delay between requests to be respectful
        self.stats = {
            'files_found': 0,
            'pdfs_downloaded': 0,
            'pdfs_converted': 0,
            'files_replaced': 0,
            'errors': 0
        }
        
        # Check if we have PDF processing capabilities
        if not PYPDF_AVAILABLE and not PYMUPDF_AVAILABLE:
            raise ImportError("Neither pypdf nor PyMuPDF is available. Install one with: pip install pypdf OR pip install PyMuPDF")

    def is_pdf_placeholder(self, file_path):
        """Check if a markdown file is a PDF placeholder."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Look for PDF placeholder patterns
            patterns = [
                r'# PDF Document',
                r'This is a PDF document\. Please download directly from the source\.',
                r'PDF document.*download.*source'
            ]
            
            for pattern in patterns:
                if re.search(pattern, content, re.IGNORECASE):
                    return True
            
            return False
        except Exception as e:
            logger.error(f"Error reading {file_path}: {e}")
            return False

    def extract_pdf_url(self, file_path):
        """Extract PDF URL from a placeholder markdown file."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Look for URL patterns
            url_patterns = [
                r'URL:\s*(https?://[^\s\n]+\.pdf)',
                r'Source:\s*(https?://[^\s\n]+\.pdf)',
                r'(https?://[^\s\n)]+\.pdf)'
            ]
            
            for pattern in url_patterns:
                match = re.search(pattern, content, re.IGNORECASE)
                if match:
                    return match.group(1).strip()
            
            return None
        except Exception as e:
            logger.error(f"Error extracting URL from {file_path}: {e}")
            return None

    def download_pdf(self, url, timeout=30):
        """Download PDF from URL and return the content."""
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
            }
            
            logger.info(f"Downloading PDF from: {url}")
            response = requests.get(url, headers=headers, timeout=timeout, stream=True)
            response.raise_for_status()
            
            # Check if content is actually a PDF
            content_type = response.headers.get('content-type', '').lower()
            if 'pdf' not in content_type and not url.lower().endswith('.pdf'):
                logger.warning(f"URL might not be a PDF: {url} (content-type: {content_type})")
            
            return response.content
        except requests.exceptions.RequestException as e:
            logger.error(f"Error downloading PDF from {url}: {e}")
            return None

    def extract_text_pypdf(self, pdf_content):
        """Extract text from PDF using pypdf."""
        try:
            import io
            from pypdf import PdfReader
            
            pdf_file = io.BytesIO(pdf_content)
            reader = PdfReader(pdf_file)
            
            text_parts = []
            for page_num, page in enumerate(reader.pages, 1):
                try:
                    text = page.extract_text()
                    if text.strip():
                        text_parts.append(f"## Page {page_num}\n\n{text}\n")
                except Exception as e:
                    logger.warning(f"Error extracting text from page {page_num}: {e}")
                    text_parts.append(f"## Page {page_num}\n\n[Error extracting text from this page]\n")
            
            return '\n'.join(text_parts)
        except Exception as e:
            logger.error(f"Error extracting text with pypdf: {e}")
            return None

    def extract_text_pymupdf(self, pdf_content):
        """Extract text from PDF using PyMuPDF."""
        try:
            import io
            import contextlib
            from io import StringIO
            
            # Capture stderr to suppress MuPDF error messages
            stderr_capture = StringIO()
            
            with contextlib.redirect_stderr(stderr_capture):
                pdf_file = io.BytesIO(pdf_content)
                doc = fitz.open(stream=pdf_file, filetype="pdf")
                
                text_parts = []
                for page_num in range(len(doc)):
                    try:
                        page = doc[page_num]
                        text = page.get_text()
                        if text.strip():
                            text_parts.append(f"## Page {page_num + 1}\n\n{text}\n")
                        else:
                            text_parts.append(f"## Page {page_num + 1}\n\n[No extractable text on this page]\n")
                    except Exception as e:
                        logger.warning(f"Error extracting text from page {page_num + 1}: {e}")
                        text_parts.append(f"## Page {page_num + 1}\n\n[Error extracting text from this page]\n")
                
                doc.close()
            
            # Log if there were stderr messages but don't fail
            stderr_output = stderr_capture.getvalue()
            if stderr_output:
                logger.debug(f"PyMuPDF warnings/errors (non-fatal): {len(stderr_output.splitlines())} messages")
            
            return '\n'.join(text_parts) if text_parts else None
        except Exception as e:
            logger.error(f"Error extracting text with PyMuPDF: {e}")
            return None

    def pdf_to_markdown(self, pdf_content, title, url):
        """Convert PDF content to markdown format."""
        text = None
        extraction_method = "unknown"
        
        # Try PyMuPDF first (generally better text extraction), then fallback to pypdf
        if PYMUPDF_AVAILABLE:
            logger.debug("Attempting text extraction with PyMuPDF...")
            text = self.extract_text_pymupdf(pdf_content)
            if text:
                extraction_method = "PyMuPDF"
        
        if not text and PYPDF_AVAILABLE:
            logger.debug("Attempting text extraction with pypdf...")
            text = self.extract_text_pypdf(pdf_content)
            if text:
                extraction_method = "pypdf"
        
        if not text:
            logger.warning(f"Could not extract text from PDF: {url}")
            # Create a placeholder markdown with download link
            markdown_content = f"""---
title: {title}
url: {url}
converted_at: {datetime.now().isoformat()}
source_type: PDF
extraction_status: failed
---

# {title}

Source: {url}

---

**Note: Text extraction from this PDF failed. Please download the original PDF from the source URL above.**

The PDF may contain:
- Scanned images that require OCR
- Corrupted or malformed content
- Encrypted or protected content
- Non-standard PDF formatting

---

*This document was processed but text extraction failed. Manual review may be required.*
"""
            return markdown_content
        
        # Create markdown header for successful extraction
        logger.info(f"Successfully extracted text using {extraction_method}")
        markdown_content = f"""---
title: {title}
url: {url}
converted_at: {datetime.now().isoformat()}
source_type: PDF
extraction_method: {extraction_method}
extraction_status: success
---

# {title}

Source: {url}

---

{text}

---

*This document was automatically converted from PDF using {extraction_method}. Some formatting may have been lost in the conversion process.*
"""
        
        return markdown_content

    def process_file(self, file_path):
        """Process a single PDF placeholder file."""
        try:
            if not self.is_pdf_placeholder(file_path):
                return False
            
            logger.info(f"Found PDF placeholder: {file_path}")
            self.stats['files_found'] += 1
            
            # Extract PDF URL
            pdf_url = self.extract_pdf_url(file_path)
            if not pdf_url:
                logger.error(f"Could not extract PDF URL from {file_path}")
                self.stats['errors'] += 1
                return False
            
            if self.dry_run:
                logger.info(f"Would download and convert: {pdf_url}")
                return True
            
            # Download PDF
            pdf_content = self.download_pdf(pdf_url)
            if not pdf_content:
                logger.error(f"Failed to download PDF from {pdf_url}")
                self.stats['errors'] += 1
                return False
            
            self.stats['pdfs_downloaded'] += 1
            
            # Convert to markdown
            title = file_path.stem.replace('_', ' ').replace('-', ' ').title()
            markdown_content = self.pdf_to_markdown(pdf_content, title, pdf_url)
            
            if not markdown_content:
                logger.error(f"Failed to convert PDF to markdown: {pdf_url}")
                self.stats['errors'] += 1
                return False
            
            self.stats['pdfs_converted'] += 1
            
            # Save the converted content
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(markdown_content)
            
            logger.info(f"Successfully converted and replaced: {file_path}")
            self.stats['files_replaced'] += 1
            
            # Be respectful to servers
            time.sleep(self.delay)
            
            return True
            
        except Exception as e:
            logger.error(f"Error processing {file_path}: {e}")
            self.stats['errors'] += 1
            return False

    def run(self):
        """Process all markdown files in the input directory."""
        if not self.input_dir.exists():
            logger.error(f"Input directory does not exist: {self.input_dir}")
            return False
        
        # Find all markdown files
        md_files = list(self.input_dir.rglob("*.md"))
        
        if not md_files:
            logger.warning(f"No markdown files found in {self.input_dir}")
            return False
        
        logger.info(f"Scanning {len(md_files)} markdown files for PDF placeholders")
        
        success_count = 0
        for file_path in md_files:
            if self.process_file(file_path):
                success_count += 1
        
        # Print statistics
        logger.info("PDF processing completed!")
        logger.info(f"PDF placeholder files found: {self.stats['files_found']}")
        logger.info(f"PDFs successfully downloaded: {self.stats['pdfs_downloaded']}")
        logger.info(f"PDFs successfully converted: {self.stats['pdfs_converted']}")
        logger.info(f"Files successfully replaced: {self.stats['files_replaced']}")
        logger.info(f"Errors encountered: {self.stats['errors']}")
        
        return self.stats['errors'] == 0


def main():
    parser = argparse.ArgumentParser(description='Process PDF placeholder markdown files')
    parser.add_argument('input_dir', help='Input directory containing markdown files')
    parser.add_argument('--dry-run', action='store_true', help='Show what would be processed without making changes')
    parser.add_argument('--delay', type=float, default=1.0, help='Delay between requests in seconds (default: 1.0)')
    
    args = parser.parse_args()
    
    processor = PDFProcessor(
        input_dir=args.input_dir,
        dry_run=args.dry_run,
        delay=args.delay
    )
    
    success = processor.run()
    exit(0 if success else 1)


if __name__ == "__main__":
    main()