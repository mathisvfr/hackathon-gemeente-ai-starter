#!/usr/bin/env python3
"""
Test script for the Enhanced RAG System
"""

import os
import sys
from enhanced_rag import EnhancedRAGSystem, initialize_rag_system, chat

def test_basic_functionality():
    """Test basic RAG functionality"""
    print("=== Testing Enhanced RAG System ===\n")
    
    # Test document processing
    documents_dir = '../1. Datasets/Scrapen/scraped_content/content'
    
    if not os.path.exists(documents_dir):
        print(f"❌ Documents directory not found: {documents_dir}")
        print("Please ensure the documents directory exists and contains .md files")
        return False
    
    print("1. Initializing RAG system...")
    try:
        initialize_rag_system(documents_dir)
        print("✅ RAG system initialized successfully")
    except Exception as e:
        print(f"❌ Error initializing RAG system: {e}")
        return False
    
    # Test queries
    test_queries = [
        "Wat zijn chatbots?",
        "Hoe kan ik een chatbot opzetten voor de overheid?",
        "Wat zijn de voordelen van AI voor de overheid?",
        "Pizza recept"  # Should be marked as irrelevant
    ]
    
    print("\n2. Testing queries...")
    for i, query in enumerate(test_queries, 1):
        print(f"\n--- Test Query {i}: {query} ---")
        try:
            response = chat(query)
            print(f"Response length: {len(response)} characters")
            if "**Bronnen:**" in response:
                print("✅ Sources properly included in response")
            else:
                print("⚠️  No sources found in response")
        except Exception as e:
            print(f"❌ Error processing query: {e}")
            return False
    
    print("\n=== All tests completed ===")
    return True

def test_rag_components():
    """Test individual RAG components"""
    print("\n=== Testing RAG Components ===\n")
    
    documents_dir = '../1. Datasets/Scrapen/scraped_content/content'
    
    try:
        # Initialize RAG system
        rag_system = EnhancedRAGSystem(documents_dir)
        
        print(f"✅ Loaded {len(rag_system.chunks)} document chunks")
        
        if rag_system.embeddings is not None:
            print(f"✅ Created embeddings with shape: {rag_system.embeddings.shape}")
        else:
            print("❌ No embeddings created")
            return False
        
        # Test retrieval
        test_query = "chatbot overheid"
        print(f"\n--- Testing retrieval for: '{test_query}' ---")
        
        results = rag_system.retrieve_documents(test_query, k=3)
        print(f"✅ Retrieved {len(results)} results")
        
        for i, result in enumerate(results):
            print(f"  Result {i+1}:")
            print(f"    File: {os.path.basename(result.chunk.file_path)}")
            print(f"    Similarity: {result.similarity_score:.4f}")
            print(f"    Section: {result.chunk.section_title or 'N/A'}")
            print(f"    Chunk: {result.chunk.chunk_index + 1}/{result.chunk.total_chunks}")
            print(f"    Content length: {len(result.chunk.content)} chars")
        
    except Exception as e:
        print(f"❌ Error testing RAG components: {e}")
        return False
    
    return True

if __name__ == "__main__":
    print("Enhanced RAG System Test Suite")
    print("=" * 40)
    
    # Run tests
    success = True
    
    try:
        success &= test_rag_components()
        success &= test_basic_functionality()
    except KeyboardInterrupt:
        print("\n\nTest interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Unexpected error during testing: {e}")
        success = False
    
    if success:
        print("\n🎉 All tests passed!")
    else:
        print("\n❌ Some tests failed!")
        sys.exit(1)