"""
Configuration file for AI Support Bot
Modify these settings to customize the bot's behavior.
"""

# OpenAI Configuration
OPENAI_MODEL = "gpt-3.5-turbo"
OPENAI_MAX_TOKENS = 500
OPENAI_TEMPERATURE = 0.7

# FAQ Retrieval Configuration
FAQ_RESULTS_COUNT = 3  # Number of relevant FAQs to retrieve
CONVERSATION_HISTORY_LIMIT = 10  # Number of messages to keep in context

# Flask Configuration
FLASK_HOST = "0.0.0.0"
FLASK_PORT = 5000
FLASK_DEBUG = True

# ChromaDB Configuration
CHROMA_PERSIST_DIRECTORY = "./chroma_db"
CHROMA_COLLECTION_NAME = "faq_knowledge_base"

# System Prompt
SYSTEM_PROMPT = """You are a helpful AI customer support agent. Your role is to:
1. Answer customer questions based on the provided FAQ knowledge base
2. Be friendly, professional, and helpful
3. If you don't know the answer, politely say so and offer to connect them with a human agent
4. Keep responses concise but informative
5. Always maintain a positive tone"""

# Sample FAQs (loaded on first run)
SAMPLE_FAQS = [
    {
        "question": "How do I reset my password?",
        "answer": "To reset your password, go to the login page and click 'Forgot Password'. Enter your email address and follow the instructions sent to your email."
    },
    {
        "question": "What are your business hours?",
        "answer": "Our customer support is available Monday through Friday, 9 AM to 6 PM EST. We also provide 24/7 online support through our AI assistant."
    },
    {
        "question": "How can I contact customer support?",
        "answer": "You can contact us through this chat interface, email us at support@company.com, or call us at 1-800-SUPPORT during business hours."
    },
    {
        "question": "What is your refund policy?",
        "answer": "We offer a 30-day money-back guarantee for all purchases. Refunds are processed within 5-7 business days after approval."
    },
    {
        "question": "How do I update my account information?",
        "answer": "You can update your account information by logging into your account and going to the 'Account Settings' section. Click 'Edit Profile' to make changes."
    },
    {
        "question": "Do you offer technical support?",
        "answer": "Yes, we provide comprehensive technical support for all our products. You can reach our technical team through this chat or by emailing tech@company.com."
    },
    {
        "question": "What payment methods do you accept?",
        "answer": "We accept all major credit cards (Visa, MasterCard, American Express), PayPal, and bank transfers. All transactions are secure and encrypted."
    },
    {
        "question": "How long does shipping take?",
        "answer": "Standard shipping takes 3-5 business days, while express shipping takes 1-2 business days. International shipping may take 7-14 business days depending on the destination."
    }
]



