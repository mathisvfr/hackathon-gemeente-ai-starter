import React, { useState, useEffect } from 'react'
import { X, FileText, ExternalLink, AlertCircle } from 'lucide-react'
import ReactMarkdown from 'react-markdown'
import { enhancedAPI } from '../services/enhanced_api'

const DocumentViewer = ({ documentId, onClose }) => {
  const [document, setDocument] = useState(null)
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState(null)

  useEffect(() => {
    const fetchDocument = async () => {
      try {
        setLoading(true)
        setError(null)
        
        // Try enhanced RAG endpoint first, fallback to regular endpoint
        let doc
        try {
          doc = await enhancedAPI.getEnhancedRAGDocument(documentId)
        } catch (enhancedError) {
          console.warn('Enhanced RAG endpoint failed, trying regular endpoint:', enhancedError)
          doc = await enhancedAPI.getDocument(documentId)
        }
        
        setDocument(doc)
      } catch (err) {
        console.error('Error fetching document:', err)
        setError('Document kon niet worden geladen.')
      } finally {
        setLoading(false)
      }
    }

    if (documentId) {
      fetchDocument()
    }
  }, [documentId])

  if (loading) {
    return (
      <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center p-4 z-50">
        <div className="bg-white rounded-lg shadow-xl max-w-4xl w-full max-h-[90vh] overflow-hidden">
          <div className="p-6 flex items-center justify-center">
            <div className="animate-spin rounded-full h-8 w-8 border-b-2 border-chatbot-primary"></div>
            <span className="ml-3 text-chatbot-neutral-600">Document wordt geladen...</span>
          </div>
        </div>
      </div>
    )
  }

  if (error) {
    return (
      <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center p-4 z-50">
        <div className="bg-white rounded-lg shadow-xl max-w-md w-full p-6">
          <div className="flex items-center mb-4">
            <AlertCircle className="w-6 h-6 text-red-500 mr-2" />
            <h3 className="text-lg font-semibold text-red-900">Fout</h3>
          </div>
          <p className="text-chatbot-neutral-600 mb-4">{error}</p>
          <button
            onClick={onClose}
            className="w-full px-4 py-2 bg-chatbot-primary text-white rounded-lg hover:bg-chatbot-primary-hover transition-colors"
          >
            Sluiten
          </button>
        </div>
      </div>
    )
  }

  return (
    <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center p-4 z-50">
      <div className="bg-white rounded-lg shadow-xl max-w-4xl w-full max-h-[90vh] overflow-hidden">
        {/* Header */}
        <div className="flex items-center justify-between p-6 border-b border-chatbot-neutral-200">
          <div className="flex items-center space-x-3">
            <FileText className="w-6 h-6 text-chatbot-primary" />
            <div>
              <h2 className="text-xl font-semibold text-chatbot-neutral-900">
                {document?.title || 'Document'}
              </h2>
              <div className="flex flex-col space-y-1 mt-1">
                <div className="flex items-center space-x-4">
                  <span className="text-sm text-chatbot-neutral-500">
                    Type: {document?.type || 'Onbekend'}
                  </span>
                  <span className="text-sm text-chatbot-neutral-500">
                    Domein: {document?.domain || 'Onbekend'}
                  </span>
                </div>
                {/* Enhanced RAG metadata */}
                {(document?.file_path || document?.section_title || (document?.chunk_index !== undefined)) && (
                  <div className="flex flex-col space-y-1">
                    {document.file_path && (
                      <span className="text-xs text-chatbot-neutral-500">
                        📁 Bestand: {document.file_path.split('/').pop().replace('.md', '')}
                      </span>
                    )}
                    {document.section_title && (
                      <span className="text-xs text-chatbot-neutral-500">
                        📄 Sectie: {document.section_title}
                      </span>
                    )}
                    {document.chunk_index !== undefined && document.total_chunks > 1 && (
                      <span className="text-xs text-chatbot-neutral-500">
                        📋 Deel {document.chunk_index + 1} van {document.total_chunks}
                      </span>
                    )}
                  </div>
                )}
              </div>
            </div>
          </div>
          <div className="flex items-center space-x-2">
            {/* Prefer original_url if available */}
            {document?.original_url && document.original_url !== '' && (
              <a
                href={document.original_url}
                target="_blank"
                rel="noopener noreferrer"
                className="flex items-center space-x-1 px-3 py-1 text-sm text-chatbot-primary hover:bg-chatbot-primary hover:text-white rounded-lg transition-colors"
              >
                <ExternalLink className="w-4 h-4" />
                <span>Originele bron</span>
              </a>
            )}
            {/* Fallback to source_url if no original_url */}
            {!document?.original_url && document?.source_url && document.source_url !== '' && !document.source_url.startsWith('#') && (
              <a
                href={document.source_url}
                target="_blank"
                rel="noopener noreferrer"
                className="flex items-center space-x-1 px-3 py-1 text-sm text-chatbot-primary hover:bg-chatbot-primary hover:text-white rounded-lg transition-colors"
              >
                <ExternalLink className="w-4 h-4" />
                <span>Originele bron</span>
              </a>
            )}
            <button
              onClick={onClose}
              className="p-2 text-chatbot-neutral-400 hover:text-chatbot-neutral-600 hover:bg-chatbot-neutral-100 rounded-lg transition-colors"
            >
              <X className="w-5 h-5" />
            </button>
          </div>
        </div>

        {/* Content */}
        <div className="p-6 overflow-y-auto max-h-[calc(90vh-200px)]">
          {document?.summary && (
            <div className="bg-chatbot-neutral-50 rounded-lg p-4 mb-6">
              <h3 className="text-sm font-semibold text-chatbot-neutral-700 mb-2">Samenvatting</h3>
              <p className="text-sm text-chatbot-neutral-600">{document.summary}</p>
            </div>
          )}

          <div className="prose max-w-none prose-headings:text-chatbot-neutral-900 prose-p:text-chatbot-neutral-800 prose-a:text-chatbot-primary hover:prose-a:text-chatbot-primary-hover prose-strong:text-chatbot-neutral-900 prose-code:text-chatbot-primary prose-code:bg-chatbot-neutral-100 prose-code:px-1 prose-code:py-0.5 prose-code:rounded">
            <ReactMarkdown 
              className="leading-relaxed"
              components={{
                a: ({ node, ...props }) => (
                  <a {...props} target="_blank" rel="noopener noreferrer" />
                )
              }}
            >
              {document?.content || 'Geen content beschikbaar.'}
            </ReactMarkdown>
          </div>
        </div>

        {/* Footer */}
        <div className="border-t border-chatbot-neutral-200 p-4 bg-chatbot-neutral-50">
          <div className="flex justify-between items-center text-sm text-chatbot-neutral-500">
            <span>Document ID: {documentId}</span>
            <button
              onClick={onClose}
              className="px-4 py-2 bg-chatbot-primary text-white rounded-lg hover:bg-chatbot-primary-hover transition-colors"
            >
              Sluiten
            </button>
          </div>
        </div>
      </div>
    </div>
  )
}

export default DocumentViewer