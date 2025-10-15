from flask import Flask, render_template, request, jsonify
import openai
import json
import os
from datetime import datetime
import chromadb
import uuid
from dotenv import load_dotenv
from config import *

app = Flask(__name__)

# Load environment variables from .env if present and initialize OpenAI
load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')

# Initialize ChromaDB for FAQ storage
try:
    client = chromadb.PersistentClient(path=CHROMA_PERSIST_DIRECTORY)
    # Get or create FAQ collection
    try:
        faq_collection = client.get_collection(CHROMA_COLLECTION_NAME)
    except:
        faq_collection = client.create_collection(CHROMA_COLLECTION_NAME)
except Exception as e:
    print(f"Warning: ChromaDB initialization failed: {e}")
    print("The application will run without FAQ functionality.")
    client = None
    faq_collection = None

# Store conversation history
conversations = {}

class AISupportBot:
    def __init__(self):
        self.system_prompt = SYSTEM_PROMPT

    def get_relevant_faqs(self, user_query, n_results=FAQ_RESULTS_COUNT):
        """Retrieve relevant FAQs from the knowledge base"""
        if faq_collection is None:
            return None
        try:
            results = faq_collection.query(
                query_texts=[user_query],
                n_results=n_results
            )
            return results
        except Exception as e:
            print(f"Error retrieving FAQs: {e}")
            return None

    def generate_response(self, user_message, conversation_id):
        """Generate AI response using OpenAI and FAQ context"""
        try:
            # Get relevant FAQs
            faq_results = self.get_relevant_faqs(user_message)
            
            # Build context from FAQs
            faq_context = ""
            if faq_results and faq_results['documents']:
                for i, doc in enumerate(faq_results['documents'][0]):
                    faq_context += f"FAQ {i+1}: {doc}\n\n"
            
            # Get conversation history
            conversation_history = conversations.get(conversation_id, [])
            
            # Build messages for OpenAI
            messages = [{"role": "system", "content": self.system_prompt}]
            
            # Add FAQ context if available
            if faq_context:
                messages.append({
                    "role": "system", 
                    "content": f"Relevant FAQ information:\n{faq_context}"
                })
            
            # Add conversation history
            for msg in conversation_history[-CONVERSATION_HISTORY_LIMIT:]:
                messages.append(msg)
            
            # Add current user message
            messages.append({"role": "user", "content": user_message})
            
            # Generate response
            response = openai.ChatCompletion.create(
                model=OPENAI_MODEL,
                messages=messages,
                max_tokens=OPENAI_MAX_TOKENS,
                temperature=OPENAI_TEMPERATURE
            )
            
            ai_response = response.choices[0].message.content
            
            # Update conversation history
            conversations[conversation_id].extend([
                {"role": "user", "content": user_message},
                {"role": "assistant", "content": ai_response}
            ])
            
            return ai_response
            
        except Exception as e:
            return f"I apologize, but I'm experiencing technical difficulties. Error: {str(e)}"

# Initialize bot
bot = AISupportBot()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()
        user_message = data.get('message', '').strip()
        conversation_id = data.get('conversation_id')
        
        if not user_message:
            return jsonify({'error': 'Message cannot be empty'}), 400
        
        # Generate new conversation ID if not provided
        if not conversation_id:
            conversation_id = str(uuid.uuid4())
            conversations[conversation_id] = []
        
        # Generate AI response
        ai_response = bot.generate_response(user_message, conversation_id)
        
        return jsonify({
            'response': ai_response,
            'conversation_id': conversation_id,
            'timestamp': datetime.now().isoformat()
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/add_faq', methods=['POST'])
def add_faq():
    """Add new FAQ to the knowledge base"""
    if faq_collection is None:
        return jsonify({'error': 'FAQ database not available'}), 503
    
    try:
        data = request.get_json()
        question = data.get('question', '').strip()
        answer = data.get('answer', '').strip()
        
        if not question or not answer:
            return jsonify({'error': 'Both question and answer are required'}), 400
        
        # Add to ChromaDB
        faq_collection.add(
            documents=[f"Q: {question}\nA: {answer}"],
            metadatas=[{"question": question, "answer": answer}],
            ids=[str(uuid.uuid4())]
        )
        
        return jsonify({'message': 'FAQ added successfully'})
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/get_faqs', methods=['GET'])
def get_faqs():
    """Get all FAQs from the knowledge base"""
    try:
        results = faq_collection.get()
        faqs = []
        for i, doc in enumerate(results['documents']):
            faqs.append({
                'id': results['ids'][i],
                'content': doc,
                'metadata': results['metadatas'][i]
            })
        return jsonify({'faqs': faqs})
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Load sample FAQs if collection is empty
    if faq_collection is not None:
        try:
            if faq_collection.count() == 0:
                for faq in SAMPLE_FAQS:
                    faq_collection.add(
                        documents=[f"Q: {faq['question']}\nA: {faq['answer']}"],
                        metadatas=[{"question": faq['question'], "answer": faq['answer']}],
                        ids=[str(uuid.uuid4())]
                    )
                print("Sample FAQs loaded successfully!")
        except Exception as e:
            print(f"Error loading sample FAQs: {e}")
    else:
        print("ChromaDB not available - running without FAQ functionality")
    
    app.run(debug=FLASK_DEBUG, host=FLASK_HOST, port=FLASK_PORT)
