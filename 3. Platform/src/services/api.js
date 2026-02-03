import axios from 'axios'

const API_BASE_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000'

const api = axios.create({
  baseURL: API_BASE_URL,
  timeout: 30000,
  headers: {
    'Content-Type': 'application/json',
  },
})

// Request interceptor for debugging
api.interceptors.request.use(
  (config) => {
    console.log('API Request:', config.method?.toUpperCase(), config.url, config.data)
    return config
  },
  (error) => {
    console.error('API Request Error:', error)
    return Promise.reject(error)
  }
)

// Response interceptor for error handling
api.interceptors.response.use(
  (response) => {
    console.log('API Response:', response.status, response.data)
    return response
  },
  (error) => {
    console.error('API Response Error:', error.response?.data || error.message)
    
    if (error.response?.status === 429) {
      throw new Error('Te veel verzoeken. Probeer het over een moment opnieuw.')
    } else if (error.response?.status >= 500) {
      throw new Error('Server probleem. Probeer het later opnieuw.')
    } else if (error.code === 'ECONNABORTED') {
      throw new Error('Verzoek duurde te lang. Probeer het opnieuw.')
    }
    
    throw error
  }
)

export const sendMessage = async (message, userContext) => {
  try {
    const response = await api.post('/api/chat', {
      message: message.trim(),
      context: {
        role: userContext.role?.id,
        roleName: userContext.role?.name,
        projectPhase: userContext.projectPhase,
        focusAreas: userContext.focusAreas?.map(area => area.id) || [],
        specificNeeds: userContext.specificNeeds || [],
        customContext: userContext.customContext
      },
      timestamp: new Date().toISOString()
    })

    return {
      message: response.data.message || 'Sorry, ik kon geen antwoord genereren.',
      confidence: response.data.confidence || 0.7,
      sources: response.data.sources || [],
      needsHumanHelp: response.data.needsHumanHelp || false,
      suggestions: response.data.suggestions || []
    }
  } catch (error) {
    console.error('Error sending message:', error)
    
    // Fallback response for development/demo
    if (import.meta.env.DEV) {
      return generateMockResponse(message, userContext)
    }
    
    throw new Error(error.message || 'Er ging iets mis bij het versturen van je bericht.')
  }
}

// Mock response for development
const generateMockResponse = (message, userContext) => {
  const responses = {
    'gdpr': {
      message: `Voor GDPR compliance bij een chatbot als ${userContext.role?.name} moet je rekening houden met:

## Belangrijkste GDPR vereisten

1. **Rechtmatige grondslag** - Meestal gerechtvaardigd belang voor publieke dienstverlening
2. **Transparantie** - Duidelijk maken dat gebruikers met AI praten
3. **Dataminimalisatie** - Alleen noodzakelijke gegevens verzamelen
4. **Bewaartermijn** - Logs niet langer bewaren dan noodzakelijk

## Praktische stappen

- Implementeer een privacy notice
- Zorg voor opt-out mogelijkheden  
- Documenteer verwerkingsactiviteiten
- Train je model met geanonimiseerde data

Voor complexe juridische aspecten raad ik aan contact op te nemen met een privacy officer.`,
      confidence: 0.85,
      sources: [
        { title: 'GDPR Handreiking Gemeente', url: '#' },
        { title: 'Privacy by Design Principles', url: '#' }
      ],
      needsHumanHelp: false
    },
    'ai-act': {
      message: `De AI Act heeft specifieke verplichtingen voor overheidschatbots:

## Hoog-risico AI systeem classificatie

Als gemeente chatbot val je waarschijnlijk onder "hoog-risico" omdat je:
- Toegang geeft tot publieke diensten
- Burgers beïnvloedt in hun rechten

## Verplichtingen onder AI Act

1. **Risicobeheersysteem** implementeren
2. **Transparantie** - Gebruikers informeren over AI gebruik  
3. **Menselijk toezicht** - Altijd fallback naar mens
4. **Registratie** in EU database
5. **Conformiteitsbeoordeling** door derde partij

## Tijdlijn
- Augustus 2024: Verboden praktijken van kracht
- Augustus 2025: Verplichtingen hoog-risico systemen
- Augustus 2026: Algemene verplichtingen

Dit is complex juridisch terrein - ik raad sterk aan een AI Act specialist te raadplegen.`,
      confidence: 0.75,
      sources: [
        { title: 'AI Act Implementatie Gids', url: '#' },
        { title: 'Hoog-risico AI Classificatie', url: '#' }
      ],
      needsHumanHelp: true
    },
    'default': {
      message: `Bedankt voor je vraag! Als ${userContext.role?.name} in de ${userContext.projectPhase} fase kan ik je helpen met:

## Op basis van je context

${userContext.focusAreas?.map(area => `- **${area.name}**: Relevante richtlijnen en best practices`).join('\n') || ''}

## Aanbevolen volgende stappen

1. Check de relevante regelgeving voor je use case
2. Implementeer privacy by design principes  
3. Zorg voor transparantie naar gebruikers
4. Plan menselijke fallback opties

Stel gerust een specifiekere vraag over een van deze onderwerpen!`,
      confidence: 0.65,
      sources: [
        { title: 'Best Practices Gemeente Digitalisering', url: '#' }
      ],
      needsHumanHelp: false
    }
  }

  const messageKey = message.toLowerCase().includes('gdpr') || message.toLowerCase().includes('privacy') ? 'gdpr' :
                    message.toLowerCase().includes('ai act') || message.toLowerCase().includes('ai-act') ? 'ai-act' :
                    'default'

  return responses[messageKey]
}

export const getExpertContact = async () => {
  try {
    const response = await api.get('/api/expert-contact')
    return response.data
  } catch (error) {
    console.error('Error getting expert contact:', error)
    return {
      name: 'Digitalisering Support Team',
      email: 'digitalisering@gemeente.nl',
      phone: '+31 20 123 4567',
      available: 'ma-vr 09:00-17:00'
    }
  }
}

export const submitFeedback = async (messageId, isPositive, comment = '') => {
  try {
    const response = await api.post('/api/feedback', {
      messageId,
      isPositive,
      comment,
      timestamp: new Date().toISOString()
    })
    return response.data
  } catch (error) {
    console.error('Error submitting feedback:', error)
    throw error
  }
}

export default api