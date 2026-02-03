import { useState, useRef, useEffect } from 'react'
import { motion, AnimatePresence } from 'framer-motion'
import { 
  Send, 
  Bot, 
  User, 
  RotateCcw, 
  HelpCircle, 
  Download,
  ExternalLink,
  AlertCircle,
  CheckCircle,
  Clock,
  ThumbsUp,
  ThumbsDown,
  Zap,
  FileText,
  Shield,
  Settings
} from 'lucide-react'
import ReactMarkdown from 'react-markdown'
import { enhancedAPI, demoResponses } from '../services/enhanced_api'
import DocumentViewer from './DocumentViewer'

const QUICK_SUGGESTIONS = {
  'digital-guide': [
    'Welke stakeholders moet ik betrekken bij een AI implementatie?',
    'Hoe zorg ik voor draagvlak in de organisatie?',
    'Wat zijn de belangrijkste risico\'s die ik moet managen?'
  ],
  'civil-servant': [
    'Welke GDPR maatregelen zijn nodig voor een chatbot?',
    'Hoe ga ik om met de AI Act verplichtingen?',
    'Wat zijn best practices voor transparantie?'
  ],
  'it-manager': [
    'Welke architectuur principes moet ik volgen?',
    'Hoe voorkom ik vendor lock-in?',
    'Welke security maatregelen zijn essentieel?'
  ],
  'project-manager': [
    'Hoe plan ik een AI implementatie stap voor stap?',
    'Welke success metrics moet ik definiëren?',
    'Hoe manage ik risico\'s bij AI projecten?'
  ],
  'developer': [
    'Welke open standaarden moet ik gebruiken?',
    'Hoe implementeer ik Common Ground principes?',
    'Welke APIs zijn beschikbaar voor gemeentes?'
  ],
  'other': [
    'Waar moet ik beginnen met digitale transformatie?',
    'Welke regelgeving is relevant voor mijn project?',
    'Wie kan me verder helpen?'
  ]
}

// Utility function to clean raw Python object responses
const cleanRawResponse = (rawText) => {
  if (!rawText || typeof rawText !== 'string') return rawText
  
  // Check if this is a raw Python object string (contains field assignments)
  if (rawText.includes('solution_approach=') || 
      rawText.includes('TechnicalGuidance:') ||
      rawText.includes('architecture_recommendations=') ||
      rawText.includes('implementation_steps=')) {
    try {
      // Try to extract the main content from solution_approach field
      const solutionMatch = rawText.match(/solution_approach="([^"]*(?:\\.[^"]*)*)"/s)
      if (solutionMatch) {
        let content = solutionMatch[1]
          .replace(/\\n/g, '\n')
          .replace(/\\"/g, '"')
          .replace(/\\'/g, "'")
          .trim()
        
        // If it has a clear structure, use it
        if (content.length > 50 && content.includes('\n')) {
          return content
        }
      }
      
      // Look for patterns like "Hoofdrespons:\nActual content"
      const hoofdMatch = rawText.match(/Hoofdrespons:\s*([^]*?)(?=\s*Concrete|$)/i)
      if (hoofdMatch) {
        return hoofdMatch[1].trim()
      }
      
      // Fallback: extract meaningful lines (filter out Python object syntax)
      const lines = rawText.split('\n')
      const meaningfulLines = lines.filter(line => {
        const trimmed = line.trim()
        return trimmed.length > 20 && 
               !trimmed.includes('=') && 
               !trimmed.startsWith('[') && 
               !trimmed.startsWith('ActionItem(') &&
               !trimmed.includes('priority=') &&
               !trimmed.includes('timeline=') &&
               !trimmed.includes("'high'") &&
               !trimmed.includes("'medium'") &&
               !trimmed.includes("'low'") &&
               !trimmed.match(/^[\w_]+=['"]/) // Field assignments
      })
      
      if (meaningfulLines.length > 0) {
        return meaningfulLines.join('\n').trim()
      }
    } catch (e) {
      console.warn('Failed to parse raw response:', e)
    }
  }
  
  return rawText
}

const EnhancedChatInterface = ({ userContext, onRestart }) => {
  const [messages, setMessages] = useState([])
  const [inputValue, setInputValue] = useState('')
  const [isLoading, setIsLoading] = useState(false)
  const [showSuggestions, setShowSuggestions] = useState(true)
  const [viewingDocument, setViewingDocument] = useState(null)
  const messagesEndRef = useRef(null)
  const inputRef = useRef(null)

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' })
  }

  useEffect(() => {
    scrollToBottom()
  }, [messages])

  useEffect(() => {
    // Welcome message with enhanced context
    const welcomeMessage = {
      id: Date.now(),
      type: 'ai',
      content: generateWelcomeMessage(userContext),
      timestamp: new Date(),
      suggestions: QUICK_SUGGESTIONS[userContext.role?.id] || QUICK_SUGGESTIONS.other,
      enhanced: true
    }
    setMessages([welcomeMessage])
  }, [userContext])

  const generateWelcomeMessage = (context) => {
    const { role, projectPhase, focusAreas, customContext } = context
    
    let message = `# 🤖 Welkom bij de Enhanced Gemeente AI Assistant!

Hoi! Ik ben je **verbeterde** AI assistant met toegang tot **189 gemeente documenten** en **structured outputs**.

**Je profiel:**
- **Rol:** ${role?.name || 'Niet gespecificeerd'}
- **Fase:** ${projectPhase || 'Niet gespecificeerd'}
- **Focus:** ${focusAreas?.map(area => area.name).join(', ') || 'Algemeen'}`
    
    if (customContext) {
      message += `\n- **Context:** ${customContext}`
    }
    
    message += `

## 🚀 Nieuwe Features:
- **Knowledge Base**: Real-time zoeken in 189 officiële documenten
- **Structured Outputs**: Georganiseerde antwoorden met actiepunten
- **Smart Routing**: Automatische detectie van vraagtype
- **Compliance Analysis**: Gespecialiseerde GDPR/AI Act checks

**Waarschuwing:** Je praat met een AI systeem. Voor complexe juridische zaken verwijs ik je door naar een expert.

Stel je vraag of kies een suggestie hieronder! 👇`
    
    return message
  }


  const handleSendMessage = async (message = inputValue.trim()) => {
    if (!message || isLoading) return

    const userMessage = {
      id: Date.now(),
      type: 'user',
      content: message,
      timestamp: new Date()
    }

    setMessages(prev => [...prev, userMessage])
    setInputValue('')
    setIsLoading(true)
    setShowSuggestions(false)

    try {
      let response

      // Always use structured response with sources
      try {
        response = await enhancedAPI.sendStructuredMessage(message, userContext)
        
        
      } catch (apiError) {
        console.warn('API call failed, using fallback:', apiError)
        // Simplified fallback response
        response = {
          main_answer: `## API Error - Fallback Response

Er ging iets mis met de API verbinding. Dit is een fallback response.

**Oorspronkelijke vraag:** ${message}

### Troubleshooting:
1. Check of de backend draait op http://localhost:8000
2. Controleer of de OpenAI API key correct is geconfigureerd
3. Bekijk de browser console voor meer details

**Error:** ${apiError.message}`,
          response_type: "error_fallback",
          confidence_level: "low",
          knowledge_sources: [],
          follow_up_suggestions: [],
          needs_human_expert: true,
          processing_time_ms: 100
        }
      }

      // Always use structured response format
      let mainContent = response.main_answer || 'Geen antwoord beschikbaar'
      let actionItems = response.action_items || []
      let complianceChecks = response.compliance_checks || []
        // ComplianceAnalysis response - Use main_answer field if available
        mainContent = response.main_answer || response.immediate_actions?.[0]?.description || 'Compliance analyse voltooid.'
        
        // All action items (no filtering needed)
        actionItems = response.immediate_actions || []
        
        // Enhanced compliance checks with better structure
        complianceChecks = [{
          regulation: response.regulation_type,
          status: response.compliance_status,
          requirements: response.requirements || [],
          recommendations: response.gaps || [],
          risk_level: response.risk_assessment?.includes('Medium') ? 'medium' : 
                     response.risk_assessment?.includes('High') ? 'high' : 'low',
          timeline: response.timeline,
          budget: response.budget_implications,
          risk_details: response.risk_assessment
        }]
        
      } else if (selectedMode === 'technical' && response.solution_approach) {
        // TechnicalGuidance response - Extract AI response from solution_approach
        let aiResponse = response.implementation_steps?.[0]?.description || response.solution_approach || ''
        
        // Clean raw response if needed
        aiResponse = cleanRawResponse(aiResponse)
        
        const fullAiText = aiResponse.split('Analyseer de technische guidance: ')[1] || 
                          aiResponse.split('AI aanbeveling: ')[1] || aiResponse
        
        mainContent = `${fullAiText}

---

## ⚙️ Technische Implementatie Samenvatting

### 🎯 Aanbevolen Aanpak:
${response.solution_approach?.replace('AI aanbeveling: ', '') || 'Zie bovenstaande AI analyse'}

### 🏗️ Architectuur Aanbevelingen:
${response.architecture_recommendations?.map(rec => `- ${rec}`).join('\n') || ''}

### 💻 Technology Stack:
${response.technology_stack?.map(tech => `- ${tech}`).join('\n') || ''}

### ✅ Best Practices:
${response.best_practices?.map(practice => `- ${practice}`).join('\n') || ''}

### ⚠️ Veelvoorkomende Valkuilen:
${response.common_pitfalls?.map(pitfall => `- ${pitfall}`).join('\n') || ''}

${response.testing_strategy ? `\n### 🧪 **Testing Strategie:** ${response.testing_strategy}` : ''}

### 📊 Monitoring Vereisten:
${response.monitoring_requirements?.map(req => `- ${req}`).join('\n') || ''}`
        
        actionItems = response.implementation_steps || []
        
      } else if (selectedMode === 'quick' && response.answer) {
        // QuickAnswer response - check if answer contains raw Python object string
        let cleanAnswer = cleanRawResponse(response.answer)
        
        // Additional cleaning for specific patterns in quick answers
        if (cleanAnswer.includes('Review de gegenereerde analyse:')) {
          let extractedContent = cleanAnswer.split('Review de gegenereerde analyse: ')[1]
          if (extractedContent) {
            extractedContent = extractedContent
              .replace(/^["']/, '')
              .replace(/["']$/, '')
              .replace(/\\n/g, '\n')
              .replace(/\\"/g, '"')
              .replace(/\\'/g, "'")
              
            const nextFieldMatch = extractedContent.match(/^(.*?)(?:, priority=|$)/s)
            if (nextFieldMatch) {
              cleanAnswer = nextFieldMatch[1].trim()
            } else {
              cleanAnswer = extractedContent
            }
          }
        }
        
        mainContent = `${cleanAnswer}

${response.sources?.length > 0 ? `\n**Bronnen:** ${response.sources.join(', ')}` : ''}
${response.follow_up ? `\n**Vervolgvraag:** ${response.follow_up}` : ''}`
        
      } else {
        // Auto-detect response type and handle accordingly
        if (response.regulation_type && response.compliance_status) {
          // This is actually a ComplianceAnalysis response
          const aiResponse = response.immediate_actions?.[0]?.description || response.risk_assessment || ''
          const fullAiText = aiResponse.split('Review de gegenereerde analyse: ')[1] || aiResponse
          
          mainContent = `${fullAiText}

---

## 📋 Compliance Analyse Samenvatting

**Status:** ${response.compliance_status}
**Risico Assessment:** ${response.risk_assessment}
**Timeline:** ${response.timeline}
**Budget Impact:** ${response.budget_implications}

### ✅ Vereisten:
${response.requirements?.map(req => `- ${req}`).join('\n') || ''}

### ⚠️ Geïdentificeerde Gaps:
${response.gaps?.map(gap => `- ${gap}`).join('\n') || ''}

### 📝 Volgende Stappen:
Zie actiepunten hieronder voor concrete implementatie stappen.`
          
          actionItems = response.immediate_actions?.filter((item, index) => 
            index !== 0 || !item.description.includes('Review de gegenereerde analyse:')
          ) || []
          
          complianceChecks = [{
            regulation: response.regulation_type,
            status: response.compliance_status,
            requirements: response.requirements || [],
            recommendations: response.gaps || [],
            risk_level: 'medium'
          }]
          
        } else if (response.solution_approach) {
          // This is actually a TechnicalGuidance response
          let aiResponse = response.implementation_steps?.[0]?.description || response.solution_approach || ''
          
          // Clean raw response if needed
          aiResponse = cleanRawResponse(aiResponse)
          
          const fullAiText = aiResponse.split('Analyseer de technische guidance: ')[1] || 
                            aiResponse.split('AI aanbeveling: ')[1] || aiResponse
          
          mainContent = `${fullAiText}

---

### 🎯 Aanbevolen Aanpak:
${response.solution_approach?.replace('AI aanbeveling: ', '') || 'Zie bovenstaande AI analyse'}

### 🏗️ Architectuur Aanbevelingen:
${response.architecture_recommendations?.map(rec => `- ${rec}`).join('\n') || ''}

### 💻 Technology Stack:
${response.technology_stack?.map(tech => `- ${tech}`).join('\n') || ''}

### ✅ Best Practices:
${response.best_practices?.map(practice => `- ${practice}`).join('\n') || ''}

### ⚠️ Veelvoorkomende Valkuilen:
${response.common_pitfalls?.map(pitfall => `- ${pitfall}`).join('\n') || ''}

${response.testing_strategy ? `\n### 🧪 **Testing Strategie:** ${response.testing_strategy}` : ''}

### 📊 Monitoring Vereisten:
${response.monitoring_requirements?.map(req => `- ${req}`).join('\n') || ''}`
          
          actionItems = response.implementation_steps || []
          
        } else {
          // StructuredAIResponse or fallback
          let rawContent = response.main_answer || response.answer || response.solution_approach || 
                          (typeof response === 'string' ? response : 'Geen response ontvangen')
          
          // Clean raw response if needed
          mainContent = cleanRawResponse(rawContent)
          
          actionItems = response.action_items || response.implementation_steps || []
          complianceChecks = response.compliance_checks || []
        }
      }

      const aiMessage = {
        id: Date.now() + 1,
        type: 'ai',
        content: mainContent,
        timestamp: new Date(),
        enhanced: true,
        responseType: selectedMode,
        structured: response,
        confidence: response.confidence_level || response.confidence || 'medium',
        sources: response.knowledge_sources || response.sources || [],
        actionItems: actionItems,
        complianceChecks: complianceChecks,
        followUpSuggestions: response.follow_up_suggestions || [],
        needsHumanHelp: response.needs_human_expert || response.needs_human_help || false,
        processingTime: response.processing_time_ms || response.responseTime
      }

      setMessages(prev => [...prev, aiMessage])
    } catch (error) {
      console.error('Enhanced chat error:', error)
      const errorMessage = {
        id: Date.now() + 1,
        type: 'ai',
        content: 'Sorry, er ging iets mis. Dit kan komen doordat de OpenAI API key niet is geconfigureerd. Probeer het opnieuw of neem contact op met een expert.',
        timestamp: new Date(),
        isError: true,
        needsHumanHelp: true
      }
      setMessages(prev => [...prev, errorMessage])
    } finally {
      setIsLoading(false)
    }
  }

  const handleKeyPress = (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault()
      handleSendMessage()
    }
  }

  const handleSuggestionClick = (suggestion) => {
    handleSendMessage(suggestion)
  }

  const handleFeedback = (messageId, isPositive) => {
    console.log(`Feedback for message ${messageId}: ${isPositive ? 'positive' : 'negative'}`)
  }

  const handleDocumentClick = (url) => {
    // Extract document ID from URL
    const match = url.match(/\/api\/knowledge\/document\/(.+)$/)
    if (match) {
      const documentId = match[1]
      setViewingDocument(documentId)
    }
  }

  const ApiModeSelector = () => (
    <div className="flex items-center space-x-2 text-sm">
      <span className="text-gemeente-neutral-600">Mode:</span>
      <select 
        value={apiMode}
        onChange={(e) => setApiMode(e.target.value)}
        className="text-xs border border-gemeente-neutral-300 rounded px-2 py-1"
      >
        <option value="auto">🤖 Auto</option>
        <option value="structured">📋 Structured</option>
        <option value="quick">⚡ Quick</option>
        <option value="compliance">🔒 Compliance</option>
        <option value="technical">⚙️ Technical</option>
      </select>
    </div>
  )

  const renderEnhancedMessage = (message) => {
    if (!message.enhanced) {
      return <ReactMarkdown className="prose prose-sm max-w-none">{message.content}</ReactMarkdown>
    }

    return (
      <div className="space-y-4">
        <ReactMarkdown className="prose prose-sm max-w-none">{message.content}</ReactMarkdown>
        
        {/* Action Items */}
        {message.actionItems && message.actionItems.length > 0 && (
          <div className="bg-blue-50 border border-blue-200 rounded-lg p-4">
            <h4 className="font-semibold text-blue-800 mb-2 flex items-center">
              <CheckCircle className="w-4 h-4 mr-2" />
              Actiepunten
            </h4>
            <div className="space-y-2">
              {message.actionItems.map((item, index) => (
                <div key={index} className="flex items-start space-x-2">
                  <span className={`px-2 py-1 rounded text-xs font-medium ${
                    item.priority === 'high' ? 'bg-red-100 text-red-800' :
                    item.priority === 'medium' ? 'bg-yellow-100 text-yellow-800' :
                    'bg-green-100 text-green-800'
                  }`}>
                    {item.priority}
                  </span>
                  <div className="flex-1">
                    <p className="font-medium text-sm">{item.title}</p>
                    <p className="text-xs text-gemeente-neutral-600">{item.description}</p>
                    {item.timeline && (
                      <p className="text-xs text-gemeente-neutral-500">⏱️ {item.timeline}</p>
                    )}
                  </div>
                </div>
              ))}
            </div>
          </div>
        )}

        {/* Enhanced Compliance Checks */}
        {message.complianceChecks && message.complianceChecks.length > 0 && (
          <div className="bg-amber-50 border border-amber-200 rounded-lg p-4">
            <h4 className="font-semibold text-amber-800 mb-3 flex items-center">
              <Shield className="w-4 h-4 mr-2" />
              Compliance Analyse
            </h4>
            {message.complianceChecks.map((check, index) => (
              <div key={index} className="space-y-3">
                {/* Status Overview */}
                <div className="grid grid-cols-2 gap-4 text-sm">
                  <div>
                    <span className="font-medium text-amber-800">Regelgeving:</span>
                    <div className="mt-1">
                      <span className="px-2 py-1 bg-amber-100 text-amber-800 rounded text-xs font-medium">
                        {check.regulation?.toUpperCase()}
                      </span>
                    </div>
                  </div>
                  <div>
                    <span className="font-medium text-amber-800">Status:</span>
                    <div className="mt-1">
                      <span className={`px-2 py-1 rounded text-xs font-medium ${
                        check.status === 'compliant' ? 'bg-green-100 text-green-800' :
                        check.status === 'non_compliant' ? 'bg-red-100 text-red-800' :
                        'bg-yellow-100 text-yellow-800'
                      }`}>
                        {check.status?.replace('_', ' ')}
                      </span>
                    </div>
                  </div>
                </div>

                {/* Risk Assessment */}
                {check.risk_details && (
                  <div className="bg-white rounded-lg p-3 border border-amber-200">
                    <div className="flex items-center justify-between mb-2">
                      <span className="font-medium text-amber-800 text-sm">Risico Assessment</span>
                      <span className={`px-2 py-1 rounded text-xs font-medium ${
                        check.risk_level === 'critical' ? 'bg-red-100 text-red-800' :
                        check.risk_level === 'high' ? 'bg-orange-100 text-orange-800' :
                        check.risk_level === 'medium' ? 'bg-yellow-100 text-yellow-800' :
                        'bg-green-100 text-green-800'
                      }`}>
                        {check.risk_level} risico
                      </span>
                    </div>
                    <p className="text-xs text-amber-700">{check.risk_details}</p>
                  </div>
                )}

                {/* Timeline & Budget */}
                {(check.timeline || check.budget) && (
                  <div className="grid grid-cols-1 md:grid-cols-2 gap-3">
                    {check.timeline && (
                      <div className="bg-white rounded-lg p-3 border border-amber-200">
                        <span className="font-medium text-amber-800 text-sm">⏱️ Timeline</span>
                        <p className="text-xs text-amber-700 mt-1">{check.timeline}</p>
                      </div>
                    )}
                    {check.budget && (
                      <div className="bg-white rounded-lg p-3 border border-amber-200">
                        <span className="font-medium text-amber-800 text-sm">💰 Budget Impact</span>
                        <p className="text-xs text-amber-700 mt-1">{check.budget}</p>
                      </div>
                    )}
                  </div>
                )}

                {/* Requirements */}
                {check.requirements && check.requirements.length > 0 && (
                  <div>
                    <span className="font-medium text-amber-800 text-sm">✅ Vereisten:</span>
                    <ul className="text-xs space-y-1 mt-2">
                      {check.requirements.map((req, i) => (
                        <li key={i} className="flex items-start">
                          <span className="text-green-600 mr-2">•</span>
                          <span className="text-amber-700">{req}</span>
                        </li>
                      ))}
                    </ul>
                  </div>
                )}

                {/* Gaps/Recommendations */}
                {check.recommendations && check.recommendations.length > 0 && (
                  <div>
                    <span className="font-medium text-amber-800 text-sm">⚠️ Geïdentificeerde Gaps:</span>
                    <ul className="text-xs space-y-1 mt-2">
                      {check.recommendations.map((rec, i) => (
                        <li key={i} className="flex items-start">
                          <span className="text-amber-600 mr-2">•</span>
                          <span className="text-amber-700">{rec}</span>
                        </li>
                      ))}
                    </ul>
                  </div>
                )}
              </div>
            ))}
          </div>
        )}
      </div>
    )
  }

  return (
    <div className="h-screen flex flex-col bg-white">
      {/* Enhanced Header */}
      <div className="border-b border-gemeente-neutral-200 p-4">
        <div className="max-w-4xl mx-auto flex items-center justify-between">
          <div className="flex items-center space-x-3">
            <div className="flex items-center space-x-2">
              <div className="relative">
                <Bot className="w-6 h-6 text-gemeente-primary" />
                <Zap className="w-3 h-3 text-yellow-500 absolute -top-1 -right-1" />
              </div>
              <div>
                <h1 className="text-xl font-semibold text-gemeente-neutral-800">
                  Enhanced AI Assistant
                </h1>
                <div className="text-xs text-gemeente-neutral-500">
                  Structured Outputs • Knowledge Base • 189 Documenten
                </div>
              </div>
            </div>
            <div className="hidden md:flex items-center space-x-2 text-sm text-gemeente-neutral-600">
              <span>•</span>
              <span>{userContext.role?.name}</span>
              {userContext.projectPhase && (
                <>
                  <span>•</span>
                  <span>{userContext.projectPhase}</span>
                </>
              )}
            </div>
          </div>
          
          <div className="flex items-center space-x-4">
            <ApiModeSelector />
            
            <button className="btn-secondary text-sm px-4 py-2 flex items-center space-x-2">
              <HelpCircle className="w-4 h-4" />
              <span>Expert</span>
            </button>
            
            <button 
              onClick={onRestart}
              className="btn-secondary text-sm px-4 py-2 flex items-center space-x-2"
            >
              <RotateCcw className="w-4 h-4" />
              <span>Reset</span>
            </button>
          </div>
        </div>
      </div>

      {/* Enhanced Chat Messages */}
      <div className="flex-1 overflow-y-auto p-4 pb-20">
        <div className="max-w-4xl mx-auto space-y-6">
          <AnimatePresence>
            {messages.map((message) => (
              <motion.div
                key={message.id}
                initial={{ opacity: 0, y: 20 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ duration: 0.3 }}
                className={`flex ${message.type === 'user' ? 'justify-end' : 'justify-start'}`}
              >
                <div className={`max-w-4xl ${message.type === 'user' ? 'ml-12' : 'mr-12'}`}>
                  {/* Message Header */}
                  <div className={`flex items-center space-x-2 mb-2 ${
                    message.type === 'user' ? 'justify-end' : 'justify-start'
                  }`}>
                    {message.type === 'ai' && (
                      <div className="flex items-center space-x-1">
                        <Bot className="w-4 h-4 text-gemeente-primary" />
                        {message.enhanced && <Zap className="w-3 h-3 text-yellow-500" />}
                      </div>
                    )}
                    <span className="text-xs text-gemeente-neutral-500">
                      {message.type === 'ai' ? 'Enhanced AI' : 'Je'}
                      {message.responseType && ` • ${message.responseType}`}
                    </span>
                    <span className="text-xs text-gemeente-neutral-400">
                      {message.timestamp.toLocaleTimeString('nl-NL', { 
                        hour: '2-digit', 
                        minute: '2-digit' 
                      })}
                    </span>
                    {message.type === 'user' && <User className="w-4 h-4 text-gemeente-neutral-600" />}
                  </div>

                  {/* Message Content */}
                  <div className={`${
                    message.type === 'user' 
                      ? 'chat-bubble-user' 
                      : `chat-bubble-ai ${message.isError ? 'border-gemeente-error bg-red-50' : ''}`
                  }`}>
                    {message.type === 'ai' ? renderEnhancedMessage(message) : <p>{message.content}</p>}
                  </div>

                  {/* Enhanced Metadata */}
                  {message.type === 'ai' && message.enhanced && (
                    <div className="mt-3 space-y-3">
                      {/* Performance & Confidence */}
                      <div className="flex items-center space-x-4 text-xs">
                        {message.confidence && (
                          <div className="flex items-center space-x-1">
                            {message.confidence === 'high' || message.confidence > 0.8 ? (
                              <CheckCircle className="w-3 h-3 text-green-600" />
                            ) : message.confidence === 'medium' || message.confidence > 0.6 ? (
                              <Clock className="w-3 h-3 text-yellow-600" />
                            ) : (
                              <AlertCircle className="w-3 h-3 text-red-600" />
                            )}
                            <span className="text-gemeente-neutral-500">
                              Vertrouwen: {typeof message.confidence === 'string' ? message.confidence : `${Math.round(message.confidence * 100)}%`}
                            </span>
                          </div>
                        )}
                        
                        {message.processingTime && (
                          <span className="text-gemeente-neutral-500">
                            ⚡ {message.processingTime}ms
                          </span>
                        )}
                      </div>

                      {/* Knowledge Sources */}
                      {message.sources && message.sources.length > 0 && (
                        <div className="border-t border-gemeente-neutral-200 pt-2">
                          <p className="text-xs text-gemeente-neutral-500 mb-2 font-medium">
                            📚 Bronnen uit Knowledge Base:
                          </p>
                          <div className="space-y-1">
                            {message.sources.slice(0, 3).map((source, index) => (
                              <div key={index} className="flex items-center justify-between text-xs">
                                <button
                                  onClick={() => handleDocumentClick(source.url)}
                                  className="flex items-center space-x-1 text-gemeente-primary hover:underline flex-1 text-left"
                                >
                                  <FileText className="w-3 h-3" />
                                  <span className="truncate">{source.title}</span>
                                </button>
                                <span className="text-gemeente-neutral-400 ml-2">
                                  {Math.round((source.relevance_score || 0.5) * 100)}%
                                </span>
                              </div>
                            ))}
                          </div>
                        </div>
                      )}

                      {/* Follow-up Suggestions */}
                      {message.followUpSuggestions && message.followUpSuggestions.length > 0 && (
                        <div className="space-y-2">
                          <p className="text-sm text-gemeente-neutral-600 font-medium">
                            💡 Vervolgvragen:
                          </p>
                          {message.followUpSuggestions.slice(0, 2).map((suggestion, index) => (
                            <button
                              key={index}
                              onClick={() => handleSuggestionClick(suggestion.question)}
                              className="block w-full text-left text-sm bg-gemeente-neutral-50 hover:bg-gemeente-neutral-100 border border-gemeente-neutral-200 rounded-lg p-3 transition-colors duration-200"
                            >
                              <div className="flex items-center justify-between">
                                <span>{suggestion.question}</span>
                                <span className="text-xs text-gemeente-neutral-400">
                                  {suggestion.category}
                                </span>
                              </div>
                            </button>
                          ))}
                        </div>
                      )}

                      {/* Human Expert Recommendation */}
                      {message.needsHumanHelp && (
                        <div className="bg-yellow-50 border border-yellow-200 rounded-lg p-3">
                          <div className="flex items-start space-x-2">
                            <AlertCircle className="w-4 h-4 text-yellow-600 flex-shrink-0 mt-0.5" />
                            <div>
                              <p className="text-sm text-yellow-800 font-medium mb-1">
                                Expert Consultatie Aanbevolen
                              </p>
                              <p className="text-xs text-yellow-700 mb-2">
                                Dit onderwerp vereist mogelijk menselijke expertise voor juridische of technische details.
                              </p>
                              <button className="btn-primary text-xs px-3 py-1">
                                Contact Expert
                              </button>
                            </div>
                          </div>
                        </div>
                      )}

                      {/* Feedback */}
                      <div className="flex items-center space-x-2 pt-2 border-t border-gemeente-neutral-100">
                        <span className="text-xs text-gemeente-neutral-500">Nuttig antwoord?</span>
                        <button
                          onClick={() => handleFeedback(message.id, true)}
                          className="p-1 hover:bg-gemeente-neutral-100 rounded"
                        >
                          <ThumbsUp className="w-3 h-3 text-gemeente-neutral-400 hover:text-green-600" />
                        </button>
                        <button
                          onClick={() => handleFeedback(message.id, false)}
                          className="p-1 hover:bg-gemeente-neutral-100 rounded"
                        >
                          <ThumbsDown className="w-3 h-3 text-gemeente-neutral-400 hover:text-red-600" />
                        </button>
                      </div>
                    </div>
                  )}

                  {/* Legacy suggestions */}
                  {message.suggestions && showSuggestions && (
                    <motion.div
                      initial={{ opacity: 0, height: 0 }}
                      animate={{ opacity: 1, height: 'auto' }}
                      className="mt-4 space-y-2"
                    >
                      <p className="text-sm text-gemeente-neutral-600 font-medium">
                        🚀 Probeer deze vragen:
                      </p>
                      {message.suggestions.map((suggestion, index) => (
                        <button
                          key={index}
                          onClick={() => handleSuggestionClick(suggestion)}
                          className="block w-full text-left text-sm bg-gemeente-neutral-50 hover:bg-gemeente-neutral-100 border border-gemeente-neutral-200 rounded-lg p-3 transition-colors duration-200"
                        >
                          {suggestion}
                        </button>
                      ))}
                    </motion.div>
                  )}
                </div>
              </motion.div>
            ))}
          </AnimatePresence>

          {/* Enhanced Loading Indicator */}
          {isLoading && (
            <motion.div
              initial={{ opacity: 0 }}
              animate={{ opacity: 1 }}
              className="flex justify-start"
            >
              <div className="chat-bubble-ai max-w-md">
                <div className="flex items-center space-x-3">
                  <div className="flex space-x-1">
                    <div className="w-2 h-2 bg-gemeente-primary rounded-full animate-bounce" />
                    <div className="w-2 h-2 bg-gemeente-primary rounded-full animate-bounce" style={{ animationDelay: '0.1s' }} />
                    <div className="w-2 h-2 bg-gemeente-primary rounded-full animate-bounce" style={{ animationDelay: '0.2s' }} />
                  </div>
                  <div className="text-sm text-gemeente-neutral-600">
                    <div>🧠 AI analyseert je vraag...</div>
                    <div className="text-xs text-gemeente-neutral-500 mt-1">
                      📚 Doorzoekt knowledge base • {apiMode} mode
                    </div>
                  </div>
                </div>
              </div>
            </motion.div>
          )}

          <div ref={messagesEndRef} />
        </div>
      </div>

      {/* Enhanced Input Area */}
      <div className="border-t border-gemeente-neutral-200 p-4 bg-white">
        <div className="max-w-4xl mx-auto">
          <div className="flex space-x-4">
            <div className="flex-1 relative">
              <textarea
                ref={inputRef}
                value={inputValue}
                onChange={(e) => setInputValue(e.target.value)}
                onKeyPress={handleKeyPress}
                placeholder="Stel je vraag over digitale transformatie... (Enter = verzenden, Shift+Enter = nieuwe regel)"
                className="w-full p-4 pr-12 border border-gemeente-neutral-300 rounded-lg focus:border-gemeente-primary focus:ring-2 focus:ring-gemeente-primary focus:ring-opacity-20 resize-none"
                rows={1}
                style={{ minHeight: '52px', maxHeight: '120px' }}
              />
              <button
                onClick={() => handleSendMessage()}
                disabled={!inputValue.trim() || isLoading}
                className="absolute right-3 bottom-3 p-2 text-gemeente-primary hover:bg-gemeente-primary hover:text-white rounded-lg transition-colors duration-200 disabled:opacity-50 disabled:cursor-not-allowed"
              >
                <Send className="w-5 h-5" />
              </button>
            </div>
          </div>
          
          <div className="mt-2 flex justify-between items-center text-xs text-gemeente-neutral-500">
            <div className="flex items-center space-x-4">
              <span>🔍 Knowledge Base: 189 documenten</span>
              <span>⚡ Mode: {apiMode}</span>
              <span>🤖 Enhanced AI</span>
            </div>
            <span>{inputValue.length}/2000</span>
          </div>
        </div>
      </div>

      {/* Document Viewer Modal */}
      {viewingDocument && (
        <DocumentViewer
          documentId={viewingDocument}
          onClose={() => setViewingDocument(null)}
        />
      )}
    </div>
  )
}

export default EnhancedChatInterface