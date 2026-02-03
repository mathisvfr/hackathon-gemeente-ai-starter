import { useState } from 'react'
import { motion } from 'framer-motion'
import { 
  ArrowRight, 
  ArrowLeft, 
  Search, 
  Settings, 
  CheckCircle,
  AlertTriangle,
  FileText,
  Users,
  Zap
} from 'lucide-react'

const PROJECT_PHASES = {
  'digital-guide': [
    { id: 'exploration', name: '🔍 Verkenning & Planning', description: 'Project wordt verkend en gepland' },
    { id: 'development', name: '🛠️ Ontwikkeling & Implementatie', description: 'Actief aan het bouwen en implementeren' },
    { id: 'management', name: '⚙️ Beheer & Onderhoud', description: 'Systeem draait en wordt onderhouden' }
  ],
  'civil-servant': [
    { id: 'policy', name: '📋 Beleidsontwikkeling', description: 'Bezig met beleid en regelgeving' },
    { id: 'implementation', name: '🚀 Implementatie', description: 'Beleid wordt uitgevoerd' },
    { id: 'monitoring', name: '📊 Monitoring & Evaluatie', description: 'Resultaten worden gemonitord' }
  ],
  'it-manager': [
    { id: 'architecture', name: '🏗️ Architectuur & Design', description: 'Technische architectuur bepalen' },
    { id: 'implementation', name: '⚡ Implementatie & Integratie', description: 'Systemen bouwen en integreren' },
    { id: 'operations', name: '🔧 Operations & Maintenance', description: 'Systemen beheren en onderhouden' }
  ],
  'project-manager': [
    { id: 'initiation', name: '🎯 Project Initiatie', description: 'Project wordt opgezet' },
    { id: 'execution', name: '🚀 Project Uitvoering', description: 'Project wordt uitgevoerd' },
    { id: 'closure', name: '✅ Project Afsluiting', description: 'Project wordt afgerond' }
  ],
  'developer': [
    { id: 'design', name: '🎨 Ontwerp & Specificatie', description: 'Technisch ontwerp maken' },
    { id: 'development', name: '💻 Development', description: 'Code schrijven en testen' },
    { id: 'deployment', name: '🚀 Deployment & Monitoring', description: 'Live zetten en monitoren' }
  ],
  'other': [
    { id: 'learning', name: '📚 Oriëntatie & Leren', description: 'Informatie verzamelen' },
    { id: 'planning', name: '📋 Planning & Voorbereiding', description: 'Plannen maken' },
    { id: 'execution', name: '⚡ Uitvoering', description: 'Actief bezig met implementatie' }
  ]
}

const FOCUS_AREAS = [
  { id: 'compliance', name: 'Compliance & Regelgeving', icon: FileText, color: 'text-red-600' },
  { id: 'technology', name: 'Technologie & Architectuur', icon: Settings, color: 'text-blue-600' },
  { id: 'process', name: 'Proces & Organisatie', icon: Users, color: 'text-green-600' },
  { id: 'innovation', name: 'Innovatie & AI', icon: Zap, color: 'text-purple-600' }
]

const ContextGathering = ({ selectedRole, onContextSubmit, onBack }) => {
  const [selectedPhase, setSelectedPhase] = useState(null)
  const [selectedFocusAreas, setSelectedFocusAreas] = useState([])
  const [customContext, setCustomContext] = useState('')
  const [isSubmitting, setIsSubmitting] = useState(false)

  const phases = PROJECT_PHASES[selectedRole.id] || PROJECT_PHASES.other

  const handleFocusAreaToggle = (focusArea) => {
    setSelectedFocusAreas(prev => 
      prev.some(area => area.id === focusArea.id)
        ? prev.filter(area => area.id !== focusArea.id)
        : [...prev, focusArea]
    )
  }

  const handleSubmit = async () => {
    if (!selectedPhase) return
    
    setIsSubmitting(true)
    await new Promise(resolve => setTimeout(resolve, 500))
    
    onContextSubmit({
      projectPhase: selectedPhase.name,
      focusAreas: selectedFocusAreas,
      customContext: customContext.trim(),
      specificNeeds: selectedFocusAreas.map(area => area.name)
    })
  }

  const isFormValid = selectedPhase && selectedFocusAreas.length > 0

  return (
    <div className="min-h-screen p-4 pb-20">
      <div className="max-w-3xl mx-auto pt-8">
        {/* Header */}
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          className="text-center mb-8"
        >
          <div className="flex items-center justify-center space-x-3 mb-4">
            <div className={`p-3 rounded-xl ${selectedRole.color}`}>
              <selectedRole.icon className="w-6 h-6" />
            </div>
            <div>
              <h1 className="text-2xl md:text-3xl font-bold text-gemeente-neutral-800">
                Vertel meer over je situatie
              </h1>
              <p className="text-gemeente-neutral-600">
                {selectedRole.name}
              </p>
            </div>
          </div>
          <p className="text-lg text-gemeente-neutral-600 max-w-2xl mx-auto">
            Zo kan ik je de meest relevante informatie en suggesties geven
          </p>
        </motion.div>

        {/* Project Phase Selection */}
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.1 }}
          className="mb-8"
        >
          <h2 className="text-xl font-semibold text-gemeente-neutral-800 mb-4">
            In welke fase bevind je je?
          </h2>
          <div className="grid gap-4">
            {phases.map((phase, index) => (
              <motion.div
                key={phase.id}
                initial={{ opacity: 0, x: -20 }}
                animate={{ opacity: 1, x: 0 }}
                transition={{ delay: 0.2 + index * 0.1 }}
                className={`card cursor-pointer transition-all duration-200 ${
                  selectedPhase?.id === phase.id 
                    ? 'border-gemeente-primary bg-gemeente-primary bg-opacity-5' 
                    : 'hover:border-gemeente-primary'
                }`}
                onClick={() => setSelectedPhase(phase)}
              >
                <div className="flex items-center justify-between">
                  <div>
                    <h3 className="font-semibold text-gemeente-neutral-800 mb-1">
                      {phase.name}
                    </h3>
                    <p className="text-sm text-gemeente-neutral-600">
                      {phase.description}
                    </p>
                  </div>
                  {selectedPhase?.id === phase.id && (
                    <CheckCircle className="w-6 h-6 text-gemeente-primary" />
                  )}
                </div>
              </motion.div>
            ))}
          </div>
        </motion.div>

        {/* Focus Areas Selection */}
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.3 }}
          className="mb-8"
        >
          <h2 className="text-xl font-semibold text-gemeente-neutral-800 mb-4">
            Waar wil je je op focussen? <span className="text-sm text-gemeente-neutral-500">(meerdere opties mogelijk)</span>
          </h2>
          <div className="grid md:grid-cols-2 gap-4">
            {FOCUS_AREAS.map((area, index) => {
              const isSelected = selectedFocusAreas.some(selected => selected.id === area.id)
              return (
                <motion.div
                  key={area.id}
                  initial={{ opacity: 0, scale: 0.9 }}
                  animate={{ opacity: 1, scale: 1 }}
                  transition={{ delay: 0.4 + index * 0.1 }}
                  className={`card cursor-pointer transition-all duration-200 ${
                    isSelected 
                      ? 'border-gemeente-primary bg-gemeente-primary bg-opacity-5' 
                      : 'hover:border-gemeente-primary'
                  }`}
                  onClick={() => handleFocusAreaToggle(area)}
                >
                  <div className="flex items-center space-x-4">
                    <area.icon className={`w-6 h-6 ${area.color}`} />
                    <div className="flex-1">
                      <h3 className="font-semibold text-gemeente-neutral-800">
                        {area.name}
                      </h3>
                    </div>
                    {isSelected && (
                      <CheckCircle className="w-5 h-5 text-gemeente-primary" />
                    )}
                  </div>
                </motion.div>
              )
            })}
          </div>
        </motion.div>

        {/* Custom Context */}
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.5 }}
          className="mb-8"
        >
          <h2 className="text-xl font-semibold text-gemeente-neutral-800 mb-4">
            Wil je nog iets specifiek toevoegen? <span className="text-sm text-gemeente-neutral-500">(optioneel)</span>
          </h2>
          <textarea
            value={customContext}
            onChange={(e) => setCustomContext(e.target.value)}
            placeholder="Bijvoorbeeld: 'We implementeren een chatbot voor burgerservice en willen compliance met de AI Act checken...'"
            className="w-full p-4 border border-gemeente-neutral-300 rounded-lg focus:border-gemeente-primary focus:ring-2 focus:ring-gemeente-primary focus:ring-opacity-20 resize-none"
            rows={4}
          />
        </motion.div>

        {/* Summary */}
        {selectedPhase && selectedFocusAreas.length > 0 && (
          <motion.div
            initial={{ opacity: 0, height: 0 }}
            animate={{ opacity: 1, height: 'auto' }}
            className="card mb-8 bg-green-50 border-green-200"
          >
            <h3 className="font-semibold text-gemeente-neutral-800 mb-3 flex items-center">
              <CheckCircle className="w-5 h-5 text-green-600 mr-2" />
              Samenvatting van je context
            </h3>
            <div className="space-y-2 text-sm">
              <p><strong>Rol:</strong> {selectedRole.name}</p>
              <p><strong>Fase:</strong> {selectedPhase.name}</p>
              <p><strong>Focus:</strong> {selectedFocusAreas.map(area => area.name).join(', ')}</p>
              {customContext && (
                <p><strong>Extra context:</strong> {customContext}</p>
              )}
            </div>
          </motion.div>
        )}

        {/* Navigation */}
        <div className="flex justify-between items-center">
          <button
            onClick={onBack}
            className="btn-secondary flex items-center space-x-2"
          >
            <ArrowLeft className="w-4 h-4" />
            <span>Terug</span>
          </button>

          <div className="flex items-center space-x-4">
            <div className="text-sm text-gemeente-neutral-500">
              Stap 2 van 3
            </div>
            
            <button
              onClick={handleSubmit}
              disabled={!isFormValid || isSubmitting}
              className="btn-primary flex items-center space-x-2 disabled:opacity-50 disabled:cursor-not-allowed"
            >
              <span>{isSubmitting ? 'Bezig...' : 'Start gesprek'}</span>
              <ArrowRight className="w-4 h-4" />
            </button>
          </div>
        </div>

        {/* Validation Message */}
        {!isFormValid && selectedPhase && (
          <motion.div
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            className="mt-4 flex items-center justify-end space-x-2 text-sm text-amber-600"
          >
            <AlertTriangle className="w-4 h-4" />
            <span>Selecteer minstens één focusgebied om door te gaan</span>
          </motion.div>
        )}
      </div>
    </div>
  )
}

export default ContextGathering