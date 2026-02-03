import { useState } from 'react'
import { motion } from 'framer-motion'
import { 
  User, 
  Briefcase, 
  Monitor, 
  Users, 
  ArrowRight, 
  ArrowLeft,
  Building,
  Code,
  FileText
} from 'lucide-react'

const ROLES = [
  {
    id: 'digital-guide',
    name: 'Digitalisering Adviseur',
    description: 'Barry - Ik adviseer over digitale beleid en implementatie',
    icon: Building,
    color: 'bg-chatbot-light text-chatbot-primary',
    commonQuestions: [
      'Welke digitale standaarden moet ik volgen?',
      'Hoe implementeer ik Common Ground?',
      'Wat zijn de beste governance practices?'
    ]
  },
  {
    id: 'civil-servant',
    name: 'Gemeente Ambtenaar',
    description: 'Sandra - Ik werk aan beleid en uitvoering',
    icon: User,
    color: 'bg-white text-chatbot-secondary',
    commonQuestions: [
      'Welke regelgeving is van toepassing?',
      'Hoe check ik compliance?',
      'Wat zijn best practices?'
    ]
  },
  {
    id: 'it-manager',
    name: 'IT Manager',
    description: 'Marc - Ik zorg voor technische implementatie',
    icon: Monitor,
    color: 'bg-chatbot-light text-chatbot-primary',
    commonQuestions: [
      'Welke architectuur moet ik kiezen?',
      'Hoe voorkom ik vendor lock-in?',
      'Wat zijn security requirements?'
    ]
  },
  {
    id: 'project-manager',
    name: 'Projectleider',
    description: 'Ik leid digitale transformatieprojecten',
    icon: Briefcase,
    color: 'bg-white text-chatbot-neutral-700',
    commonQuestions: [
      'Hoe plan ik een AI implementatie?',
      'Welke risico\'s moet ik managen?',
      'Hoe meet ik succes?'
    ]
  },
  {
    id: 'developer',
    name: 'Ontwikkelaar',
    description: 'Ik bouw digitale gemeenschapsgoederen',
    icon: Code,
    color: 'bg-chatbot-light text-chatbot-secondary',
    commonQuestions: [
      'Welke standaarden moet ik volgen?',
      'Hoe implementeer ik Common Ground?',
      'Welke APIs kan ik gebruiken?'
    ]
  },
  {
    id: 'other',
    name: 'Anders',
    description: 'Mijn rol staat er niet tussen',
    icon: Users,
    color: 'bg-white text-chatbot-neutral-600',
    commonQuestions: [
      'Algemene informatie over digitalisering',
      'Waar moet ik beginnen?',
      'Wie kan me verder helpen?'
    ]
  }
]

const RoleSelection = ({ onRoleSelect, onBack }) => {
  const [selectedRole, setSelectedRole] = useState(null)
  const [isAnimating, setIsAnimating] = useState(false)

  const handleRoleClick = (role) => {
    if (selectedRole?.id === role.id) {
      // Double click or already selected - proceed
      handleContinue()
    } else {
      setSelectedRole(role)
    }
  }

  const handleContinue = async () => {
    if (!selectedRole) return
    
    setIsAnimating(true)
    await new Promise(resolve => setTimeout(resolve, 300))
    onRoleSelect({ role: selectedRole })
  }

  return (
    <div className="min-h-screen p-4 pb-20">
      <div className="max-w-4xl mx-auto pt-8">
        {/* Header */}
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          className="text-center mb-8"
        >
          <h1 className="text-3xl md:text-4xl font-bold text-chatbot-neutral-800 mb-4">
            Wat is je rol?
          </h1>
          <p className="text-lg text-chatbot-neutral-600 max-w-2xl mx-auto">
            Vertel me over je rol zodat ik je beter kan helpen met relevante informatie en suggesties
          </p>
        </motion.div>

        {/* Role Cards Grid */}
        <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-6 mb-8">
          {ROLES.map((role, index) => (
            <motion.div
              key={role.id}
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ delay: index * 0.1 }}
              whileHover={{ scale: 1.02 }}
              whileTap={{ scale: 0.98 }}
              className={`role-card ${selectedRole?.id === role.id ? 'selected' : ''}`}
              onClick={() => handleRoleClick(role)}
            >
              <div className="flex flex-col h-full">
                <div className="flex items-start space-x-4 mb-4">
                  <div className={`p-3 rounded-xl ${role.color}`}>
                    <role.icon className="w-6 h-6" />
                  </div>
                  <div className="flex-1">
                    <h3 className="font-semibold text-chatbot-neutral-800 mb-1">
                      {role.name}
                    </h3>
                    <p className="text-sm text-chatbot-neutral-600">
                      {role.description}
                    </p>
                  </div>
                </div>

                {/* Common Questions Preview */}
                <div className="mt-auto">
                  <p className="text-xs text-chatbot-neutral-500 mb-2 font-medium">
                    Veelgestelde vragen:
                  </p>
                  <ul className="space-y-1">
                    {role.commonQuestions.slice(0, 2).map((question, qIndex) => (
                      <li key={qIndex} className="text-xs text-chatbot-neutral-600 flex items-start">
                        <span className="text-chatbot-primary mr-2">•</span>
                        {question}
                      </li>
                    ))}
                  </ul>
                </div>
              </div>
            </motion.div>
          ))}
        </div>

        {/* Selected Role Summary */}
        {selectedRole && (
          <motion.div
            initial={{ opacity: 0, height: 0 }}
            animate={{ opacity: 1, height: 'auto' }}
            className="card mb-8 bg-chatbot-primary bg-opacity-5 border-chatbot-primary"
          >
            <div className="flex items-center justify-between">
              <div className="flex items-center space-x-4">
                <div className={`p-3 rounded-xl ${selectedRole.color}`}>
                  <selectedRole.icon className="w-6 h-6" />
                </div>
                <div>
                  <h3 className="font-semibold text-chatbot-neutral-800">
                    Gekozen: {selectedRole.name}
                  </h3>
                  <p className="text-sm text-chatbot-neutral-600">
                    {selectedRole.description}
                  </p>
                </div>
              </div>
              <button
                onClick={handleContinue}
                disabled={isAnimating}
                className="btn-primary flex items-center space-x-2 disabled:opacity-50"
              >
                <span>Doorgaan</span>
                <ArrowRight className="w-4 h-4" />
              </button>
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
          
          <div className="text-sm text-chatbot-neutral-500">
            Stap 1 van 3
          </div>
        </div>
      </div>
    </div>
  )
}

export default RoleSelection