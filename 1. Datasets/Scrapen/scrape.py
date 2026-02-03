#!/usr/bin/env python3
"""
Web scraper voor het downloaden en converteren van webpagina's naar markdown files.
Leest URLs uit een markdown bestand en slaat de content op als individuele markdown files.
"""

import re
import time
import requests
from pathlib import Path
from urllib.parse import urlparse, unquote
from datetime import datetime
import html2text
from bs4 import BeautifulSoup
import logging
from typing import List, Tuple, Optional
import hashlib

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class MarkdownWebScraper:
    def __init__(self, input_file: str, output_dir: str = "scraped_content"):
        """
        Initialize the scraper.

        Args:
            input_file: Path to the markdown file containing links
            output_dir: Directory where scraped content will be saved
        """
        self.input_file = Path(input_file)
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)

        # Create subdirectories for organization
        self.content_dir = self.output_dir / "content"
        self.content_dir.mkdir(exist_ok=True)
        self.failed_dir = self.output_dir / "failed"
        self.failed_dir.mkdir(exist_ok=True)

        # Setup HTML to Markdown converter
        self.h2t = html2text.HTML2Text()
        self.h2t.ignore_links = False
        self.h2t.ignore_images = False
        self.h2t.body_width = 0  # Don't wrap lines

        # Headers voor requests
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }

        # Rate limiting
        self.delay = 1  # seconds between requests

        # Track statistics
        self.stats = {
            'total': 0,
            'success': 0,
            'failed': 0,
            'skipped': 0
        }

    def extract_urls_from_markdown(self) -> List[Tuple[str, str]]:
        """
        Extract all URLs from the markdown file.

        Returns:
            List of tuples (url, description)
        """
        urls = []

        with open(self.input_file, 'r', encoding='utf-8') as f:
            content = f.read()

        # Regex patterns voor verschillende link formats
        patterns = [
            r'https?://[^\s\)]+',  # Basic URL pattern
            r'\[([^\]]+)\]\((https?://[^\)]+)\)',  # [text](url)
            r'- (https?://[^\s]+)(?:\s+\(([^\)]+)\))?'  # - url (description)
        ]

        for pattern in patterns:
            matches = re.finditer(pattern, content)
            for match in matches:
                if len(match.groups()) >= 2:
                    # Markdown link format
                    description = match.group(1)
                    url = match.group(2)
                else:
                    # Plain URL
                    url = match.group(0).strip()
                    description = ""

                # Skip if URL is None
                if url is None:
                    continue

                # Clean up URL
                url = url.rstrip(')')

                # Skip duplicates
                if not any(u[0] == url for u in urls):
                    urls.append((url, description))

        logger.info(f"Found {len(urls)} unique URLs in {self.input_file}")
        return urls

    def generate_filename(self, url: str, description: str = "") -> str:
        """
        Generate a safe filename from URL and description.

        Args:
            url: The URL
            description: Optional description

        Returns:
            Safe filename string
        """
        parsed = urlparse(url)

        # Try to create meaningful filename
        parts = []

        # Add domain
        domain = parsed.netloc.replace('www.', '').replace('.', '_')
        parts.append(domain)

        # Add path info
        if parsed.path and parsed.path != '/':
            path_parts = [p for p in parsed.path.strip('/').split('/') if p]
            if path_parts:
                # Take last 2 parts of path
                parts.extend(path_parts[-2:])

        # Add description if available
        if description:
            desc_clean = re.sub(r'[^\w\s-]', '', description.lower())
            desc_clean = re.sub(r'[-\s]+', '-', desc_clean)[:50]
            if desc_clean:
                parts.append(desc_clean)

        # Create filename
        if parts:
            filename = '_'.join(parts)[:200]  # Limit length
        else:
            # Fallback to URL hash
            filename = hashlib.md5(url.encode()).hexdigest()[:10]

        # Clean filename
        filename = re.sub(r'[^\w\s-]', '_', filename)
        filename = re.sub(r'[-\s]+', '-', filename)

        return f"{filename}.md"

    def scrape_url(self, url: str) -> Optional[str]:
        """
        Scrape content from a URL and convert to markdown.

        Args:
            url: URL to scrape

        Returns:
            Markdown content or None if failed
        """
        try:
            logger.info(f"Scraping: {url}")

            # Make request
            response = requests.get(url, headers=self.headers, timeout=30)
            response.raise_for_status()

            # Check content type
            content_type = response.headers.get('Content-Type', '').lower()

            if 'application/pdf' in content_type:
                logger.warning(f"PDF content detected for {url}, skipping conversion")
                return f"# PDF Document\n\nURL: {url}\n\nThis is a PDF document. Please download directly from the source."

            # Parse HTML
            soup = BeautifulSoup(response.text, 'html.parser')

            # Remove script and style elements
            for script in soup(["script", "style"]):
                script.decompose()

            # Extract title
            title = soup.find('title')
            title_text = title.string if title else "Untitled"

            # Extract main content (try different selectors)
            main_content = None
            content_selectors = [
                'main', 'article', '[role="main"]', '.main-content',
                '#main', '#content', '.content', 'body'
            ]

            for selector in content_selectors:
                main_content = soup.select_one(selector)
                if main_content:
                    break

            if not main_content:
                main_content = soup.body if soup.body else soup

            # Convert to markdown
            markdown_content = self.h2t.handle(str(main_content))

            # Create final markdown with metadata
            final_content = f"""---
title: {title_text}
url: {url}
scraped_at: {datetime.now().isoformat()}
---

# {title_text}

Source: {url}

---

{markdown_content}
"""

            return final_content

        except requests.exceptions.RequestException as e:
            logger.error(f"Failed to scrape {url}: {e}")
            return None
        except Exception as e:
            logger.error(f"Unexpected error scraping {url}: {e}")
            return None

    def save_content(self, content: str, filename: str, failed: bool = False) -> bool:
        """
        Save content to file.

        Args:
            content: Content to save
            filename: Filename to use
            failed: Whether this is failed content

        Returns:
            True if saved successfully
        """
        try:
            target_dir = self.failed_dir if failed else self.content_dir
            filepath = target_dir / filename

            # Handle duplicate filenames
            if filepath.exists():
                base = filepath.stem
                counter = 1
                while filepath.exists():
                    filepath = target_dir / f"{base}_{counter}.md"
                    counter += 1

            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)

            logger.info(f"Saved: {filepath}")
            return True

        except Exception as e:
            logger.error(f"Failed to save {filename}: {e}")
            return False

    def create_index(self, urls: List[Tuple[str, str]]):
        """
        Create an index file with all URLs and their status.

        Args:
            urls: List of (url, description) tuples
        """
        index_content = f"""# Scraped Content Index

Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## Statistics
- Total URLs: {self.stats['total']}
- Successfully scraped: {self.stats['success']}
- Failed: {self.stats['failed']}
- Skipped: {self.stats['skipped']}

## URLs

"""

        # Group by category (based on the original markdown structure)
        for url, desc in urls:
            status = "✗"
            try:
                for f in self.content_dir.iterdir():
                    if f.is_file() and f.suffix == '.md':
                        try:
                            with open(f, 'r', encoding='utf-8') as file:
                                if url in file.read():
                                    status = "✓"
                                    break
                        except (UnicodeDecodeError, PermissionError):
                            continue
            except Exception:
                pass
            index_content += f"- [{desc or url}]({url}) {status}\n"

        index_path = self.output_dir / "index.md"
        with open(index_path, 'w', encoding='utf-8') as f:
            f.write(index_content)

        logger.info(f"Created index at {index_path}")

    def run(self):
        """
        Run the scraper on all URLs in the markdown file.
        """
        logger.info(f"Starting scraper for {self.input_file}")

        # Extract URLs
        urls = self.extract_urls_from_markdown()
        self.stats['total'] = len(urls)

        # Process each URL
        for i, (url, description) in enumerate(urls, 1):
            logger.info(f"Processing {i}/{len(urls)}: {url}")

            # Generate filename
            filename = self.generate_filename(url, description)

            # Check if already scraped
            if (self.content_dir / filename).exists():
                logger.info(f"Already scraped: {filename}")
                self.stats['skipped'] += 1
                continue

            # Scrape content
            content = self.scrape_url(url)

            if content:
                # Save content
                if self.save_content(content, filename):
                    self.stats['success'] += 1
                else:
                    self.stats['failed'] += 1
            else:
                # Save failed URL info
                failed_content = f"""---
title: Failed to scrape
url: {url}
failed_at: {datetime.now().isoformat()}
---

# Failed to scrape

URL: {url}
Description: {description}

This URL could not be scraped. Please visit the original source.
"""
                self.save_content(failed_content, filename, failed=True)
                self.stats['failed'] += 1

            # Rate limiting
            time.sleep(self.delay)

        # Create index
        self.create_index(urls)

        # Print summary
        logger.info("\n" + "=" * 50)
        logger.info("Scraping completed!")
        logger.info(f"Total URLs: {self.stats['total']}")
        logger.info(f"Successfully scraped: {self.stats['success']}")
        logger.info(f"Failed: {self.stats['failed']}")
        logger.info(f"Skipped (already scraped): {self.stats['skipped']}")
        logger.info(f"Output directory: {self.output_dir}")


def main():
    """
    Main function to run the scraper.
    """
    import argparse

    parser = argparse.ArgumentParser(description='Scrape URLs from a markdown file')
    parser.add_argument('input_file', help='Path to markdown file containing URLs')
    parser.add_argument('-o', '--output', default='scraped_content',
                        help='Output directory (default: scraped_content)')
    parser.add_argument('-d', '--delay', type=float, default=1.0,
                        help='Delay between requests in seconds (default: 1.0)')

    args = parser.parse_args()

    # Create scraper
    scraper = MarkdownWebScraper(args.input_file, args.output)
    scraper.delay = args.delay

    # Run scraper
    scraper.run()


if __name__ == "__main__":
    main()