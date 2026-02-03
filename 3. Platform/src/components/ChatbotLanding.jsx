import { motion } from 'framer-motion'
import { Bot, HelpCircle, Settings, Rocket, ArrowRight, MessageCircle } from 'lucide-react'

const ChatbotLanding = ({ onChoiceSelect }) => {
  const choices = [
    {
      id: 'waarom',
      title: 'Waarom?',
      subtitle: 'Overtuig je organisatie',
      description: 'Waarom zou ik een chatbot willen? Welke problemen lost het op? Hoe kan ik mijn leidinggevende of organisatie overtuigen van de use case en voordelen?',
      icon: HelpCircle,
      color: 'from-chatbot-primary to-purple-600',
      iconBg: 'bg-chatbot-primary'
    },
    {
      id: 'wat',
      title: 'Wat?',
      subtitle: 'Verken de mogelijkheden',
      description: 'Welke soorten chatbots zijn er? Wordt het een interne of externe chatbot? Welke technologieën zijn er beschikbaar?',
      icon: Settings,
      color: 'from-chatbot-secondary to-blue-400',
      iconBg: 'bg-chatbot-secondary'
    },
    {
      id: 'hoe',
      title: 'Hoe?',
      subtitle: 'Van pilot naar productie',
      description: 'OK, we willen een chatbot en wat nu? Hoe komen we van pilot naar productie? Met welke wet- en regelgeving moeten we rekening houden? Wie moeten we betrekken?',
      icon: Rocket,
      color: 'from-green-500 to-emerald-600',
      iconBg: 'bg-chatbot-neutral-700'
    }
  ]

  return (
    <div className="min-h-screen bg-chatbot-light">
      <div className="max-w-6xl mx-auto px-6 py-12">
        {/* Hero Section */}
        <motion.div
          initial={{ opacity: 0, y: 30 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.8 }}
          className="text-center mb-16"
        >
          <div className="mb-8">
            <motion.div
              className="inline-flex items-center justify-center w-24 h-24 bg-chatbot-primary rounded-3xl mb-8 shadow-lg"
              initial={{ scale: 0, rotate: -180 }}
              animate={{ scale: 1, rotate: 0 }}
              transition={{ delay: 0.2, type: "spring", stiffness: 200, damping: 10 }}
            >
              <Bot className="w-12 h-12 text-white" />
            </motion.div>
            
            <motion.h1 
              className="text-5xl md:text-6xl font-bold text-chatbot-dark mb-6 leading-tight"
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ delay: 0.4 }}
            >
              Help, mijn organisatie wil{' '}
              <span className="text-chatbot-secondary">
                (misschien)
              </span>
              {' '}een chatbot
            </motion.h1>
            
            <motion.p 
              className="text-xl md:text-2xl text-chatbot-neutral-600 mb-8 max-w-4xl mx-auto leading-relaxed"
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ delay: 0.6 }}
            >
              Wij helpen overheidorganisaties bij het maken van weloverwogen beslissingen over chatbot-implementatie. 
              Van eerste verkenning tot succesvolle uitrol.
            </motion.p>

            <motion.div
              initial={{ opacity: 0, scale: 0.9 }}
              animate={{ opacity: 1, scale: 1 }}
              transition={{ delay: 0.8 }}
              className="bg-chatbot-light rounded-2xl p-6 max-w-2xl mx-auto border border-chatbot-neutral-200"
            >
              <p className="text-lg font-medium text-chatbot-dark mb-2">Waar wil je beginnen?</p>
              <p className="text-chatbot-neutral-600">Kies het onderwerp dat het beste bij jouw situatie past</p>
            </motion.div>
          </div>
        </motion.div>

        {/* Choice Cards */}
        <div className="grid md:grid-cols-3 gap-8 mb-16">
          {choices.map((choice, index) => (
            <motion.div
              key={choice.id}
              initial={{ opacity: 0, y: 50 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ delay: 0.9 + index * 0.2 }}
              whileHover={{ y: -10, scale: 1.02 }}
              whileTap={{ scale: 0.98 }}
              className="choice-card group"
              onClick={() => onChoiceSelect(choice.id)}
            >
              <div className={`w-16 h-16 rounded-2xl ${choice.iconBg} flex items-center justify-center mb-6 group-hover:scale-110 transition-transform duration-300 shadow-lg`}>
                <choice.icon className="w-8 h-8 text-white" />
              </div>
              
              <h2 className="text-3xl font-bold text-chatbot-dark mb-2">
                {choice.title}
              </h2>
              
              <p className="text-lg font-medium text-chatbot-secondary mb-4">
                {choice.subtitle}
              </p>
              
              <p className="text-chatbot-neutral-600 leading-relaxed mb-6 flex-1">
                {choice.description}
              </p>
              
              <div className="flex items-center justify-center text-chatbot-primary font-medium group-hover:text-chatbot-secondary transition-colors duration-300">
                <span>Verken deze route</span>
                <ArrowRight className="w-5 h-5 ml-2 group-hover:translate-x-1 transition-transform duration-300" />
              </div>
            </motion.div>
          ))}
        </div>

        {/* Bottom CTA */}
        <motion.div
          initial={{ opacity: 0, y: 30 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 1.5 }}
          className="text-center"
        >
          <div className="bg-white rounded-2xl shadow-lg border border-chatbot-neutral-200 p-8 max-w-3xl mx-auto">
            <div className="flex items-center justify-center mb-4">
              <MessageCircle className="w-8 h-8 text-chatbot-secondary mr-3" />
              <h3 className="text-2xl font-bold text-chatbot-dark">
                Nog geen idee waar te beginnen?
              </h3>
            </div>
            
            <p className="text-chatbot-neutral-600 mb-6 text-lg">
              Geen probleem! Onze AI-assistent kan je helpen met een gepersonaliseerd advies op basis van jouw specifieke situatie.
            </p>
            
            <button
              onClick={() => onChoiceSelect('general')}
              className="btn-secondary text-lg px-8 py-4 inline-flex items-center space-x-2 group"
            >
              <span>Start met algemeen advies</span>
              <ArrowRight className="w-5 h-5 group-hover:translate-x-1 transition-transform duration-200" />
            </button>
          </div>
        </motion.div>
      </div>
    </div>
  )
}

export default ChatbotLanding