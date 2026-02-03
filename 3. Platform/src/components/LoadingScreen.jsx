import { motion } from 'framer-motion'
import { Bot, Loader2 } from 'lucide-react'

const LoadingScreen = () => {
  return (
    <div className="min-h-screen flex items-center justify-center">
      <motion.div
        initial={{ opacity: 0, scale: 0.9 }}
        animate={{ opacity: 1, scale: 1 }}
        exit={{ opacity: 0, scale: 1.1 }}
        transition={{ duration: 0.3 }}
        className="text-center"
      >
        <div className="mb-6">
          <motion.div
            className="inline-flex items-center justify-center w-16 h-16 bg-chatbot-primary rounded-2xl mb-4"
            animate={{ rotate: [0, 360] }}
            transition={{ duration: 2, repeat: Infinity, ease: "linear" }}
          >
            <Bot className="w-8 h-8 text-white" />
          </motion.div>
          
          <h2 className="text-xl font-semibold text-chatbot-neutral-800 mb-2">
            Even geduld...
          </h2>
          
          <div className="flex items-center justify-center space-x-2 text-chatbot-neutral-600">
            <Loader2 className="w-4 h-4 animate-spin" />
            <span>Ik bereid alles voor je voor</span>
          </div>
        </div>

        <motion.div
          className="w-48 h-1 bg-chatbot-neutral-200 rounded-full mx-auto overflow-hidden"
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          transition={{ delay: 0.2 }}
        >
          <motion.div
            className="h-full bg-chatbot-primary rounded-full"
            initial={{ width: "0%" }}
            animate={{ width: "100%" }}
            transition={{ duration: 0.8, ease: "easeInOut" }}
          />
        </motion.div>
      </motion.div>
    </div>
  )
}

export default LoadingScreen