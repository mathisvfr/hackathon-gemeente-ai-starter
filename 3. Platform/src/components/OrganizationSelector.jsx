import { useState } from 'react'
import { motion, AnimatePresence } from 'framer-motion'
import { Building, MapPin, Users, ArrowRight, ArrowLeft, Check } from 'lucide-react'

const OrganizationSelector = ({ selectedChoice, onOrganizationSelect, onBack }) => {
  const [selectedOrg, setSelectedOrg] = useState(null)
  const [hoveredOrg, setHoveredOrg] = useState(null)

  const organizations = [
    {
      id: 'local',
      name: 'Lokaal',
      subtitle: 'Gemeente',
      description: 'Ik werk voor een gemeente of lokale overheidsorganisatie',
      icon: Building,
      color: 'chatbot-primary',
      examples: ['Gemeente Amsterdam', 'Gemeente Rotterdam', 'Gemeente Utrecht', 'Waterschap']
    },
    {
      id: 'provincial',
      name: 'Provinciaal',
      subtitle: 'Provincie',
      description: 'Ik werk voor een provinciale overheidsorganisatie',
      icon: MapPin,
      color: 'chatbot-secondary',
      examples: ['Provincie Noord-Holland', 'Provincie Zuid-Holland', 'Provincie Utrecht']
    },
    {
      id: 'national',
      name: 'Landelijk',
      subtitle: 'Rijk',
      description: 'Ik werk voor een rijksoverheidsorganisatie',
      icon: Users,
      color: 'chatbot-neutral-700',
      examples: ['Ministerie BZK', 'Ministerie VWS', 'RVO', 'Belastingdienst']
    }
  ]

  const handleContinue = () => {
    if (selectedOrg) {
      onOrganizationSelect(selectedOrg)
    }
  }

  const getChoiceTitle = (choice) => {
    const titles = {
      'waarom': 'Waarom een chatbot?',
      'wat': 'Wat voor chatbot?',
      'hoe': 'Hoe implementeren?',
      'general': 'Algemeen advies'
    }
    return titles[choice] || 'Chatbot advies'
  }

  return (
    <div className="min-h-screen bg-chatbot-light">
      <div className="max-w-6xl mx-auto px-6 py-12">
        {/* Header */}
        <motion.div
          initial={{ opacity: 0, y: 30 }}
          animate={{ opacity: 1, y: 0 }}
          className="text-center mb-12"
        >
          <div className="bg-chatbot-light rounded-2xl p-4 max-w-lg mx-auto mb-8 border border-chatbot-neutral-200">
            <p className="text-chatbot-primary font-medium">Je hebt gekozen voor:</p>
            <h2 className="text-2xl font-bold text-chatbot-dark">{getChoiceTitle(selectedChoice)}</h2>
          </div>

          <h1 className="text-4xl md:text-5xl font-bold text-chatbot-dark mb-4">
            We helpen je graag verder
          </h1>
          
          <p className="text-xl text-chatbot-neutral-600 max-w-3xl mx-auto mb-8">
            Op welk overheidsniveau werk je? Dit helpt ons om je de meest relevante informatie en voorbeelden te geven.
          </p>
        </motion.div>

        {/* Netherlands Map + Organization Cards */}
        <div className="grid lg:grid-cols-2 gap-12 items-center mb-12">
          
          {/* Netherlands Map */}
          <motion.div
            initial={{ opacity: 0, x: -50 }}
            animate={{ opacity: 1, x: 0 }}
            transition={{ delay: 0.3 }}
            className="relative"
          >
            <div className="bg-white rounded-2xl p-8 shadow-lg border border-chatbot-neutral-200">
              <h3 className="text-2xl font-bold text-chatbot-dark mb-6 text-center">
                Nederland in Lagen
              </h3>
              
              <div className="relative w-full max-w-md mx-auto">
                <img 
                  src="/Nederland_gemeenten_2021.svg" 
                  alt="Kaart van Nederland met gemeenten" 
                  className="w-full h-auto opacity-80"
                />
                
                {/* Overlay indicators */}
                <div className="absolute inset-0 flex items-center justify-center">
                  <div className="grid grid-cols-1 gap-4 text-center">
                    {organizations.map((org, index) => (
                      <motion.div
                        key={org.id}
                        initial={{ opacity: 0, scale: 0 }}
                        animate={{ opacity: 1, scale: 1 }}
                        transition={{ delay: 0.5 + index * 0.2 }}
                        className={`px-4 py-2 rounded-lg text-sm font-medium border-2 transition-all duration-300 ${
                          selectedOrg?.id === org.id 
                            ? 'bg-chatbot-primary text-white border-chatbot-primary' 
                            : hoveredOrg === org.id
                            ? 'bg-chatbot-secondary/20 border-chatbot-secondary text-chatbot-dark'
                            : 'bg-white/90 border-chatbot-neutral-300 text-chatbot-neutral-600'
                        }`}
                      >
                        {org.name}
                      </motion.div>
                    ))}
                  </div>
                </div>
              </div>
            </div>
          </motion.div>

          {/* Organization Cards */}
          <div className="space-y-6">
            {organizations.map((org, index) => (
              <motion.div
                key={org.id}
                initial={{ opacity: 0, x: 50 }}
                animate={{ opacity: 1, x: 0 }}
                transition={{ delay: 0.4 + index * 0.1 }}
                whileHover={{ scale: 1.02 }}
                whileTap={{ scale: 0.98 }}
                className={`p-6 rounded-xl border-2 cursor-pointer transition-all duration-300 ${
                  selectedOrg?.id === org.id
                    ? 'border-chatbot-primary bg-chatbot-primary/5 shadow-lg'
                    : 'border-chatbot-neutral-200 bg-white hover:border-chatbot-secondary hover:shadow-md'
                }`}
                onClick={() => setSelectedOrg(org)}
                onMouseEnter={() => setHoveredOrg(org.id)}
                onMouseLeave={() => setHoveredOrg(null)}
              >
                <div className="flex items-start space-x-4">
                  <div className={`p-3 rounded-xl bg-${org.color} flex-shrink-0`}>
                    <org.icon className="w-6 h-6 text-white" />
                  </div>
                  
                  <div className="flex-1">
                    <div className="flex items-center space-x-2 mb-2">
                      <h3 className="text-xl font-bold text-chatbot-dark">
                        {org.name}
                      </h3>
                      <span className="text-sm font-medium text-chatbot-secondary">
                        ({org.subtitle})
                      </span>
                      {selectedOrg?.id === org.id && (
                        <Check className="w-5 h-5 text-chatbot-primary" />
                      )}
                    </div>
                    
                    <p className="text-chatbot-neutral-600 mb-3">
                      {org.description}
                    </p>
                    
                    <div className="flex flex-wrap gap-2">
                      {org.examples.slice(0, 3).map((example, idx) => (
                        <span 
                          key={idx}
                          className="text-xs px-3 py-1 bg-chatbot-neutral-100 text-chatbot-neutral-600 rounded-full"
                        >
                          {example}
                        </span>
                      ))}
                      {org.examples.length > 3 && (
                        <span className="text-xs px-3 py-1 bg-chatbot-neutral-100 text-chatbot-neutral-600 rounded-full">
                          +{org.examples.length - 3} meer
                        </span>
                      )}
                    </div>
                  </div>
                </div>
              </motion.div>
            ))}
          </div>
        </div>

        {/* Selected Organization Summary & Continue */}
        <AnimatePresence>
          {selectedOrg && (
            <motion.div
              initial={{ opacity: 0, height: 0 }}
              animate={{ opacity: 1, height: 'auto' }}
              exit={{ opacity: 0, height: 0 }}
              className="mb-8"
            >
              <div className="bg-white rounded-2xl shadow-lg border border-chatbot-primary p-6 max-w-2xl mx-auto">
                <div className="flex items-center justify-between">
                  <div className="flex items-center space-x-4">
                    <div className={`p-3 rounded-xl bg-${selectedOrg.color}`}>
                      <selectedOrg.icon className="w-6 h-6 text-white" />
                    </div>
                    <div>
                      <h3 className="text-xl font-bold text-chatbot-dark">
                        {selectedOrg.name} niveau gekozen
                      </h3>
                      <p className="text-chatbot-neutral-600">
                        We gaan je specifieke informatie geven voor {selectedOrg.subtitle.toLowerCase()} organisaties
                      </p>
                    </div>
                  </div>
                  
                  <button
                    onClick={handleContinue}
                    className="btn-primary flex items-center space-x-2"
                  >
                    <span>Verder</span>
                    <ArrowRight className="w-4 h-4" />
                  </button>
                </div>
              </div>
            </motion.div>
          )}
        </AnimatePresence>

        {/* Navigation */}
        <div className="flex justify-between items-center">
          <button
            onClick={onBack}
            className="btn-outline flex items-center space-x-2"
          >
            <ArrowLeft className="w-4 h-4" />
            <span>Terug naar keuzes</span>
          </button>
          
          <div className="text-sm text-chatbot-neutral-500">
            Stap 2 van 3
          </div>
        </div>
      </div>
    </div>
  )
}

export default OrganizationSelector