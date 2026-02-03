#!/usr/bin/env python3
"""
Cleanup script for scraped markdown content.
Removes common issues from web scraping like JavaScript links, excessive whitespace, etc.
"""

import re
import argparse
from pathlib import Path
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


class MarkdownCleaner:
    def __init__(self, input_dir, output_dir=None, dry_run=False):
        self.input_dir = Path(input_dir)
        self.output_dir = Path(output_dir) if output_dir else self.input_dir
        self.dry_run = dry_run
        self.stats = {
            'files_processed': 0,
            'javascript_links_removed': 0,
            'blank_lines_reduced': 0,
            'empty_bullets_removed': 0,
            'wiki_links_cleaned': 0,
            'broken_images_removed': 0
        }

    def clean_javascript_links(self, content):
        """Remove javascript:void() links and clean up related text."""
        original_count = len(re.findall(r'javascript:void\([^)]*\)', content))
        
        # Remove javascript:void links
        content = re.sub(r'javascript:void\([^)]*\)', '', content)
        
        # Clean up links that became empty
        content = re.sub(r'\[[^\]]*\]\(\s*\)', '', content)
        
        # Clean up standalone [text] that lost their links
        content = re.sub(r'\[([^\]]+)\]\s*(?!\()', r'\1', content)
        
        self.stats['javascript_links_removed'] += original_count
        return content

    def reduce_blank_lines(self, content):
        """Reduce multiple consecutive blank lines to maximum 2."""
        original_lines = content.count('\n\n\n')
        
        # Replace 3+ consecutive newlines with 2
        content = re.sub(r'\n{3,}', '\n\n', content)
        
        self.stats['blank_lines_reduced'] += original_lines
        return content

    def clean_empty_bullets(self, content):
        """Remove empty bullet points and clean up list formatting."""
        lines = content.split('\n')
        cleaned_lines = []
        empty_bullets_removed = 0
        
        for line in lines:
            # Remove empty bullet points
            if re.match(r'^\s*[\*\-\+]\s*$', line):
                empty_bullets_removed += 1
                continue
            
            # Clean up bullets with only whitespace content
            if re.match(r'^\s*[\*\-\+]\s+\s*$', line):
                empty_bullets_removed += 1
                continue
                
            cleaned_lines.append(line)
        
        self.stats['empty_bullets_removed'] += empty_bullets_removed
        return '\n'.join(cleaned_lines)

    def clean_wiki_links(self, content):
        """Clean up MediaWiki-style links and formatting."""
        wiki_links_found = len(re.findall(r'/wiki/[^"\s)]+', content))
        
        # Remove wiki edit links
        content = re.sub(r'\[\[bewerken\]\([^)]*\)\]', '', content)
        
        # Clean up wiki-style section links
        content = re.sub(r'/wiki/[^"\s)]+', '', content)
        
        # Remove empty parentheses left behind
        content = re.sub(r'\(\s*\)', '', content)
        
        self.stats['wiki_links_cleaned'] += wiki_links_found
        return content

    def clean_broken_images(self, content):
        """Remove or fix broken image references."""
        broken_images = len(re.findall(r'!\[[^\]]*\]\([^)]*thumb[^)]*\)', content))
        
        # Remove broken thumbnail images
        content = re.sub(r'!\[[^\]]*\]\([^)]*thumb[^)]*\)', '', content)
        
        # Remove images with missing protocols
        content = re.sub(r'!\[[^\]]*\]\(/[^)]*\)', '', content)
        
        self.stats['broken_images_removed'] += broken_images
        return content

    def clean_navigation_elements(self, content):
        """Clean up navigation elements that don't render well in markdown."""
        # Remove "More" sections that are just navigation
        content = re.sub(r'^More\s*\n\s*\*.*?\n\n', '', content, flags=re.MULTILINE | re.DOTALL)
        
        # Clean up duplicate navigation sections
        lines = content.split('\n')
        cleaned_lines = []
        prev_line = ""
        
        for line in lines:
            # Skip duplicate navigation items
            if line.strip() and line.strip() == prev_line.strip() and re.match(r'^\s*\*\s*\[', line):
                continue
            cleaned_lines.append(line)
            prev_line = line
            
        return '\n'.join(cleaned_lines)

    def clean_content(self, content):
        """Apply all cleaning operations to the content."""
        content = self.clean_javascript_links(content)
        content = self.reduce_blank_lines(content)
        content = self.clean_empty_bullets(content)
        content = self.clean_wiki_links(content)
        content = self.clean_broken_images(content)
        content = self.clean_navigation_elements(content)
        
        # Final cleanup: remove trailing whitespace from lines
        lines = [line.rstrip() for line in content.split('\n')]
        content = '\n'.join(lines)
        
        # Ensure file ends with single newline
        content = content.rstrip() + '\n'
        
        return content

    def process_file(self, file_path):
        """Process a single markdown file."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                original_content = f.read()
            
            cleaned_content = self.clean_content(original_content)
            
            if self.dry_run:
                logger.info(f"Would clean: {file_path}")
                return True
            
            # Create output directory if it doesn't exist
            output_file = self.output_dir / file_path.relative_to(self.input_dir)
            output_file.parent.mkdir(parents=True, exist_ok=True)
            
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(cleaned_content)
            
            logger.info(f"Cleaned: {file_path}")
            self.stats['files_processed'] += 1
            return True
            
        except Exception as e:
            logger.error(f"Error processing {file_path}: {e}")
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
        
        logger.info(f"Found {len(md_files)} markdown files to process")
        
        success_count = 0
        for file_path in md_files:
            if self.process_file(file_path):
                success_count += 1
        
        # Print statistics
        logger.info("Cleanup completed!")
        logger.info(f"Files processed: {self.stats['files_processed']}")
        logger.info(f"JavaScript links removed: {self.stats['javascript_links_removed']}")
        logger.info(f"Blank line sections reduced: {self.stats['blank_lines_reduced']}")
        logger.info(f"Empty bullets removed: {self.stats['empty_bullets_removed']}")
        logger.info(f"Wiki links cleaned: {self.stats['wiki_links_cleaned']}")
        logger.info(f"Broken images removed: {self.stats['broken_images_removed']}")
        
        return success_count == len(md_files)


def main():
    parser = argparse.ArgumentParser(description='Clean up scraped markdown content')
    parser.add_argument('input_dir', help='Input directory containing markdown files')
    parser.add_argument('-o', '--output', help='Output directory (default: overwrite input)')
    parser.add_argument('--dry-run', action='store_true', help='Show what would be cleaned without making changes')
    
    args = parser.parse_args()
    
    cleaner = MarkdownCleaner(
        input_dir=args.input_dir,
        output_dir=args.output,
        dry_run=args.dry_run
    )
    
    success = cleaner.run()
    exit(0 if success else 1)


if __name__ == "__main__":
    main()