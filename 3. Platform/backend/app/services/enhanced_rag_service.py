"""
Enhanced RAG Service Wrapper for FastAPI Backend Integration
"""

import os
import sys
from typing import List, Dict, Optional, Tuple
from loguru import logger

# Add parent directory to Python path to import enhanced_rag
sys.path.append(os.path.join(os.path.dirname(__file__), '../../../'))

from enhanced_rag import EnhancedRAGSystem, RetrievalResult, DocumentChunk


class EnhancedRAGServiceWrapper:
    """
    Service wrapper to integrate the Enhanced RAG system into FastAPI backend
    """
    
    def __init__(self, documents_directory: str = None):
        """Initialize the Enhanced RAG Service"""
        if documents_directory is None:
            # Default to the documents directory relative to backend
            documents_directory = os.path.join(
                os.path.dirname(__file__), 
                '../../../..', 
                '1. Datasets/Scrapen/scraped_content/content'
            )
        
        self.documents_directory = os.path.abspath(documents_directory)
        self.rag_system: Optional[EnhancedRAGSystem] = None
        self._initialize_system()
    
    def _initialize_system(self):
        """Initialize the RAG system with error handling"""
        try:
            logger.info(f"Initializing Enhanced RAG system with documents from: {self.documents_directory}")
            self.rag_system = EnhancedRAGSystem(self.documents_directory)
            logger.info(f"Enhanced RAG system initialized successfully with {len(self.rag_system.chunks)} chunks")
        except Exception as e:
            logger.error(f"Failed to initialize Enhanced RAG system: {e}")
            self.rag_system = None
    
    def is_available(self) -> bool:
        """Check if the RAG system is available"""
        return self.rag_system is not None
    
    def get_statistics(self) -> Dict:
        """Get RAG system statistics"""
        if not self.rag_system:
            return {
                "status": "unavailable",
                "total_documents": 0,
                "total_chunks": 0,
                "error": "RAG system not initialized"
            }
        
        # Count unique documents
        unique_files = set(chunk.file_path for chunk in self.rag_system.chunks)
        
        return {
            "status": "available",
            "total_documents": len(unique_files),
            "total_chunks": len(self.rag_system.chunks),
            "document_types": {"markdown": len(unique_files)},
            "embedding_model": "text-embedding-3-small",
            "cache_available": os.path.exists(os.path.join(self.rag_system.cache_dir, "embeddings_cache.pkl"))
        }
    
    def search_documents(self, query: str, max_results: int = 5, document_types: List[str] = None) -> List[Dict]:
        """
        Search documents and return results compatible with the existing API
        """
        if not self.rag_system:
            logger.warning("RAG system not available for search")
            return []
        
        try:
            # Get retrieval results
            results = self.rag_system.retrieve_documents(query, k=max_results)
            
            # Convert to format compatible with existing knowledge base API
            formatted_results = []
            for result in results:
                chunk = result.chunk
                filename = os.path.basename(chunk.file_path)
                
                # Create a document entry compatible with existing API
                doc_entry = {
                    "document_id": f"{filename}_{chunk.chunk_index}",
                    "title": self._generate_document_title(chunk),
                    "content": chunk.content,
                    "summary": chunk.content[:200] + "..." if len(chunk.content) > 200 else chunk.content,
                    "content_snippet": chunk.content[:300] + "..." if len(chunk.content) > 300 else chunk.content,
                    "type": "guideline",  # Default type for markdown files
                    "domain": "government",
                    "source_url": chunk.original_url or f"/api/knowledge/document/{filename}_{chunk.chunk_index}",
                    "score": result.similarity_score * 10,  # Scale to 0-10 range
                    "relevance_score": result.similarity_score,
                    "file_path": chunk.file_path,
                    "section_title": chunk.section_title,
                    "chunk_index": chunk.chunk_index,
                    "total_chunks": chunk.total_chunks,
                    "original_url": chunk.original_url,
                    "document_title": chunk.document_title
                }
                
                formatted_results.append(doc_entry)
            
            return formatted_results
            
        except Exception as e:
            logger.error(f"Error searching documents: {e}")
            return []
    
    def _generate_document_title(self, chunk: DocumentChunk) -> str:
        """Generate a meaningful document title from chunk data"""
        # Use document title from frontmatter if available
        if chunk.document_title:
            base_title = chunk.document_title
        else:
            filename = os.path.basename(chunk.file_path)
            # Remove .md extension and replace underscores/hyphens with spaces
            base_title = filename.replace('.md', '').replace('_', ' ').replace('-', ' ')
        
        # Add section title if available
        if chunk.section_title:
            title = f"{chunk.section_title} - {base_title}"
        else:
            title = base_title
        
        # Add chunk info for multi-chunk documents
        if chunk.total_chunks > 1:
            title += f" (Deel {chunk.chunk_index + 1}/{chunk.total_chunks})"
        
        return title
    
    def get_context_for_query(self, query: str, max_chunks: int = 3) -> Tuple[str, List[Dict]]:
        """
        Get formatted context and detailed sources for a query
        """
        if not self.rag_system:
            return "", []
        
        try:
            context, source_names = self.rag_system.get_context_for_query(query, max_chunks)
            
            # Get detailed source information
            results = self.rag_system.retrieve_documents(query, k=max_chunks)
            detailed_sources = []
            
            for result in results:
                chunk = result.chunk
                filename = os.path.basename(chunk.file_path)
                
                source_info = {
                    "title": self._generate_document_title(chunk),
                    "url": chunk.original_url or f"/api/enhanced-rag/document/{filename}_{chunk.chunk_index}",
                    "snippet": chunk.content[:200] + "..." if len(chunk.content) > 200 else chunk.content,
                    "relevance_score": result.similarity_score,
                    "document_type": "guideline",
                    "document_id": f"{filename}_{chunk.chunk_index}",
                    "file_path": chunk.file_path,
                    "section_title": chunk.section_title,
                    "chunk_index": chunk.chunk_index,
                    "total_chunks": chunk.total_chunks,
                    "original_url": chunk.original_url,
                    "document_title": chunk.document_title
                }
                
                detailed_sources.append(source_info)
            
            return context, detailed_sources
            
        except Exception as e:
            logger.error(f"Error getting context for query: {e}")
            return "", []
    
    def get_role_specific_documents(self, role: str, max_results: int = 3) -> List[Dict]:
        """
        Get role-specific documents using keyword search
        """
        role_keywords = {
            "digital_guide": ["stakeholder", "implementatie", "draagvlak", "project", "management"],
            "civil_servant": ["gdpr", "privacy", "compliance", "wet", "regelgeving", "transparantie"],
            "it_manager": ["architectuur", "technisch", "systeem", "beveiliging", "api", "infrastructuur"],
            "project_manager": ["planning", "risico", "resources", "evaluatie", "monitoring"],
            "developer": ["standaarden", "common ground", "apis", "code", "implementatie", "ontwikkeling"],
            "other": ["overheid", "gemeente", "digitalisering", "best practices"]
        }
        
        keywords = role_keywords.get(role.lower(), role_keywords["other"])
        query = " ".join(keywords)
        
        return self.search_documents(query, max_results)
    
    def get_compliance_documents(self, regulation: str, max_results: int = 5) -> List[Dict]:
        """
        Get compliance-specific documents
        """
        regulation_keywords = {
            "gdpr": ["gdpr", "privacy", "gegevensbescherming", "avg", "dpia"],
            "ai_act": ["ai act", "kunstmatige intelligentie", "ai verordening"],
            "woo": ["woo", "openbaarheid", "transparantie", "wet open overheid"],
            "toegankelijkheid": ["toegankelijkheid", "wcag", "toegankelijk"],
            "archiefwet": ["archief", "archiefwet", "bewaring", "informatiebeheer"]
        }
        
        keywords = regulation_keywords.get(regulation.lower(), [regulation])
        query = " ".join(keywords)
        
        return self.search_documents(query, max_results)
    
    def get_document_by_id(self, document_id: str) -> Optional[Dict]:
        """
        Get a specific document by ID
        """
        if not self.rag_system:
            return None
        
        try:
            # Parse document_id to extract filename and chunk index
            if "_" in document_id:
                filename_part, chunk_index_str = document_id.rsplit("_", 1)
                try:
                    chunk_index = int(chunk_index_str)
                except ValueError:
                    # If not a valid chunk index, treat as filename
                    filename_part = document_id
                    chunk_index = None
            else:
                filename_part = document_id
                chunk_index = None
            
            # Find matching chunks
            for chunk in self.rag_system.chunks:
                chunk_filename = os.path.basename(chunk.file_path)
                if chunk_filename == filename_part or chunk_filename.replace('.md', '') == filename_part:
                    if chunk_index is None or chunk.chunk_index == chunk_index:
                        return {
                            "document_id": document_id,
                            "title": self._generate_document_title(chunk),
                            "content": chunk.content,
                            "summary": chunk.content[:500] + "..." if len(chunk.content) > 500 else chunk.content,
                            "type": "guideline",
                            "domain": "government", 
                            "source_url": "",
                            "file_path": chunk.file_path,
                            "section_title": chunk.section_title,
                            "chunk_index": chunk.chunk_index,
                            "total_chunks": chunk.total_chunks
                        }
            
            return None
            
        except Exception as e:
            logger.error(f"Error getting document by ID {document_id}: {e}")
            return None
    
    async def health_check(self) -> Dict:
        """Health check for the Enhanced RAG service"""
        if not self.rag_system:
            return {
                "status": "unhealthy",
                "error": "RAG system not initialized",
                "documents_directory": self.documents_directory
            }
        
        stats = self.get_statistics()
        return {
            "status": "healthy",
            "rag_system": "enhanced",
            "statistics": stats,
            "documents_directory": self.documents_directory
        }