import os
import json
from typing import List, Dict, Optional, Tuple
from pathlib import Path
import tiktoken
from loguru import logger

class KnowledgeBase:
    """
    Knowledge base service voor gemeente-specifieke informatie
    Integreert met de geschrapte documenten uit het project
    """
    
    def __init__(self):
        self.documents = {}
        self.embeddings = {}  # Voor toekomstige vector search
        self.load_knowledge_base()
        
    def load_knowledge_base(self):
        """Laad knowledge base van geschrapte gemeente documenten"""
        try:
            # Path naar de geschrapte documenten
            content_path = Path("/home/tr17711/Dev/Hackathon II/Hackathon_II-C-III/1. Datasets/Scrapen/scraped_content/content")
            
            if not content_path.exists():
                logger.warning(f"Knowledge base path niet gevonden: {content_path}")
                return
                
            # Laad alle .md bestanden
            document_count = 0
            for md_file in content_path.glob("*.md"):
                try:
                    with open(md_file, 'r', encoding='utf-8') as f:
                        content = f.read()
                        
                    # Extract metadata van filename en frontmatter
                    filename = md_file.stem
                    doc_info = self._parse_document(content, filename)
                    
                    self.documents[filename] = {
                        'content': doc_info.get('content', content),
                        'source_url': doc_info.get('source_url', ''),
                        'title': doc_info.get('title', filename),
                        'domain': doc_info.get('domain', ''),
                        'type': self._classify_document_type(content, filename),
                        'tokens': self._count_tokens(content),
                        'summary': self._extract_summary(doc_info.get('content', content))
                    }
                    document_count += 1
                    
                except Exception as e:
                    logger.error(f"Error loading {md_file}: {e}")
                    
            logger.info(f"Loaded {document_count} documents into knowledge base")
            
        except Exception as e:
            logger.error(f"Error loading knowledge base: {e}")
    
    def _parse_document(self, content: str, filename: str) -> Dict[str, str]:
        """Parse document voor metadata uit YAML frontmatter en filename"""
        import re
        
        # Try to extract YAML frontmatter
        frontmatter_match = re.match(r'^---\n(.*?)\n---\n(.*)$', content, re.DOTALL)
        
        if frontmatter_match:
            try:
                import yaml
                frontmatter_str = frontmatter_match.group(1)
                document_content = frontmatter_match.group(2)
                
                # Parse YAML frontmatter
                frontmatter = yaml.safe_load(frontmatter_str)
                
                # Extract URL from different possible fields
                source_url = frontmatter.get('url', frontmatter.get('source_url', ''))
                title = frontmatter.get('title', filename)
                
                # Extract domain from URL
                domain = 'unknown'
                if source_url:
                    try:
                        from urllib.parse import urlparse
                        parsed_url = urlparse(source_url)
                        domain = parsed_url.netloc.replace('www.', '')
                    except:
                        pass
                
                return {
                    'source_url': source_url,
                    'title': title,
                    'domain': domain,
                    'content': document_content
                }
                
            except Exception as e:
                logger.warning(f"Error parsing YAML frontmatter in {filename}: {e}")
        
        # Fallback to filename parsing
        return self._parse_filename_fallback(filename)
    
    def _parse_filename_fallback(self, filename: str) -> Dict[str, str]:
        """Fallback parsing gebaseerd op filename alleen"""
        parts = filename.replace('_', ' ').replace('-', ' ')
        
        # Extract domain als eerste deel van filename
        domain_parts = filename.split('_')
        domain = domain_parts[0] if domain_parts else 'unknown'
        
        return {
            'title': parts.replace('.md', ''),
            'domain': domain,
            'source_url': '',
            'content': ''
        }
    
    def _classify_document_type(self, content: str, filename: str) -> str:
        """Classificeer document type gebaseerd op content en filename"""
        content_lower = content.lower()
        filename_lower = filename.lower()
        
        if any(term in content_lower for term in ['gdpr', 'avg', 'privacy', 'persoonsgegevens']):
            return 'privacy_law'
        elif any(term in content_lower for term in ['ai act', 'kunstmatige intelligentie', 'algoritme']):
            return 'ai_regulation'
        elif any(term in content_lower for term in ['woo', 'openbaarheid', 'transparantie']):
            return 'transparency_law'
        elif any(term in content_lower for term in ['common ground', 'architectuur', 'api']):
            return 'technical_standard'
        elif any(term in content_lower for term in ['gemeente', 'digitalisering', 'transformatie']):
            return 'municipal_guidance'
        elif any(term in filename_lower for term in ['vng', 'digitaleoverheid', 'logius']):
            return 'official_guidance'
        else:
            return 'general'
    
    def _count_tokens(self, text: str) -> int:
        """Count tokens in text"""
        try:
            encoding = tiktoken.get_encoding("cl100k_base")
            return len(encoding.encode(text))
        except:
            return len(text.split())  # Fallback to word count
    
    def _extract_summary(self, content: str, max_length: int = 200) -> str:
        """Extract eerste zinnen als summary"""
        lines = content.split('\n')
        summary_lines = []
        char_count = 0
        
        for line in lines:
            line = line.strip()
            if line and not line.startswith('#') and char_count < max_length:
                summary_lines.append(line)
                char_count += len(line)
                if char_count >= max_length:
                    break
        
        return ' '.join(summary_lines)[:max_length] + "..." if char_count >= max_length else ' '.join(summary_lines)
    
    def search_documents(self, 
                        query: str, 
                        document_types: Optional[List[str]] = None,
                        max_results: int = 5) -> List[Dict]:
        """
        Zoek relevante documenten gebaseerd op query
        TODO: Implement proper vector search with embeddings
        """
        query_lower = query.lower()
        query_terms = set(query_lower.split())
        
        scored_docs = []
        
        for doc_id, doc_data in self.documents.items():
            # Filter op document type indien gespecificeerd
            if document_types and doc_data['type'] not in document_types:
                continue
                
            # Simple keyword matching (upgrade to semantic search later)
            content_lower = doc_data['content'].lower()
            title_lower = doc_data['title'].lower()
            
            # Scoring gebaseerd op keyword matches
            score = 0
            
            # Title matches krijgen hoge score
            title_matches = sum(1 for term in query_terms if term in title_lower)
            score += title_matches * 3
            
            # Content matches
            content_matches = sum(1 for term in query_terms if term in content_lower)
            score += content_matches
            
            # Bonus voor exact phrase matches
            if query_lower in content_lower:
                score += 5
            if query_lower in title_lower:
                score += 10
                
            if score > 0:
                scored_docs.append({
                    'document_id': doc_id,
                    'score': score,
                    'title': doc_data['title'],
                    'summary': doc_data['summary'],
                    'type': doc_data['type'],
                    'domain': doc_data['domain'],
                    'url': doc_data['source_url'],
                    'relevance_score': min(score / 10.0, 1.0),  # Normalize score to 0-1
                    'content_snippet': self._extract_relevant_snippet(doc_data['content'], query_terms)
                })
        
        # Sorteer op score en return top results
        scored_docs.sort(key=lambda x: x['score'], reverse=True)
        return scored_docs[:max_results]
    
    def _extract_relevant_snippet(self, content: str, query_terms: set, snippet_length: int = 300) -> str:
        """Extract relevant snippet rondom query terms"""
        content_lower = content.lower()
        
        # Vind eerste match
        best_position = 0
        for term in query_terms:
            pos = content_lower.find(term)
            if pos != -1:
                best_position = max(0, pos - snippet_length // 2)
                break
        
        # Extract snippet
        snippet = content[best_position:best_position + snippet_length]
        
        # Clean up snippet
        if best_position > 0:
            snippet = "..." + snippet
        if best_position + snippet_length < len(content):
            snippet = snippet + "..."
            
        return snippet.strip()
    
    def get_compliance_documents(self, regulation_type: str) -> List[Dict]:
        """Haal documenten op specifiek voor compliance type"""
        type_mapping = {
            'gdpr': ['privacy_law'],
            'ai_act': ['ai_regulation'], 
            'woo': ['transparency_law'],
            'common_ground': ['technical_standard'],
            'general': ['municipal_guidance', 'official_guidance']
        }
        
        relevant_types = type_mapping.get(regulation_type, ['general'])
        return self.search_documents('', document_types=relevant_types, max_results=10)
    
    def get_role_specific_documents(self, role: str) -> List[Dict]:
        """Haal documenten op specifiek voor gebruikersrol"""
        role_queries = {
            'digital-guide': 'projectmanagement digitale transformatie draagvlak',
            'civil-servant': 'beleid regelgeving compliance gdpr woo',
            'it-manager': 'architectuur technische implementatie security common ground',
            'project-manager': 'projectmanagement planning risico implementatie',
            'developer': 'api ontwikkeling common ground standaarden code',
            'other': 'digitalisering gemeente algemeen'
        }
        
        query = role_queries.get(role, role_queries['other'])
        return self.search_documents(query, max_results=8)
    
    def get_document_by_id(self, document_id: str) -> Optional[Dict]:
        """Haal een specifiek document op via ID"""
        return self.documents.get(document_id)
    
    def get_statistics(self) -> Dict:
        """Krijg statistics over knowledge base"""
        if not self.documents:
            return {'total_documents': 0}
            
        doc_types = {}
        total_tokens = 0
        domains = set()
        
        for doc_data in self.documents.values():
            doc_type = doc_data['type']
            doc_types[doc_type] = doc_types.get(doc_type, 0) + 1
            total_tokens += doc_data['tokens']
            domains.add(doc_data['domain'])
        
        return {
            'total_documents': len(self.documents),
            'document_types': doc_types,
            'total_tokens': total_tokens,
            'unique_domains': len(domains),
            'average_tokens_per_doc': total_tokens // len(self.documents) if self.documents else 0
        }