# AI Support Bot

A sophisticated AI-powered customer support chatbot that uses OpenAI's GPT models and a vector database for intelligent FAQ retrieval and conversation management.

## Features

- 🤖 **AI-Powered Responses**: Uses OpenAI's GPT-3.5-turbo for intelligent conversation
- 📚 **FAQ Knowledge Base**: ChromaDB vector database for semantic FAQ search
- 💬 **Conversation History**: Maintains context across multiple messages
- 🎨 **Modern Web Interface**: Beautiful, responsive chat UI
- 🔍 **Semantic Search**: Finds relevant FAQs using vector similarity
- 📱 **Mobile Friendly**: Responsive design that works on all devices

## Architecture

### Backend (Flask)
- **Flask Web Server**: Handles HTTP requests and serves the chat interface
- **OpenAI Integration**: Generates intelligent responses using GPT-3.5-turbo
- **ChromaDB**: Vector database for storing and retrieving FAQ embeddings
- **Conversation Management**: Tracks chat history for context-aware responses

### Frontend (HTML/CSS/JavaScript)
- **Responsive Design**: Modern, mobile-friendly chat interface
- **Real-time Communication**: AJAX-based chat without page refreshes
- **Typing Indicators**: Visual feedback during AI response generation
- **Error Handling**: Graceful error messages and connection management

## Installation

1. **Clone or download the project**
   ```bash
   git clone <repository-url>
   cd ai-support-bot
   ```

2. **Install Python dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up OpenAI API Key**
   - Get your API key from [OpenAI Platform](https://platform.openai.com/api-keys)
     ```
   - Set environment variable directly
     ```bash
     # Windows (PowerShell)
     $Env:OPENAI_API_KEY="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"
    The API key shown above is only an example. Please replace it with your actual key when running the application. I cannot include a real API key in a public repository, as it would be exposed and automatically disabled.
     ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Open your browser**
   Navigate to `http://localhost:5000`

## Usage

### For End Users
1. Open the web interface in your browser
2. Type your questions or concerns in the chat input
3. The AI will respond based on the FAQ knowledge base and conversation context
4. Ask follow-up questions - the bot maintains conversation history

### For Administrators
- **Add New FAQs**: Use the `/add_faq` endpoint to add new knowledge base entries
- **View FAQs**: Use the `/get_faqs` endpoint to retrieve all stored FAQs
- **Monitor Conversations**: Check the `conversations` dictionary in the Flask app

## API Endpoints

### POST `/chat`
Send a message to the AI bot
```json
{
  "message": "How do I reset my password?",
  "conversation_id": "optional-uuid"
}
```

### POST `/add_faq`
Add a new FAQ to the knowledge base
```json
{
  "question": "What is your refund policy?",
  "answer": "We offer a 30-day money-back guarantee..."
}
```

### GET `/get_faqs`
Retrieve all FAQs from the knowledge base

## Configuration

### Environment Variables
- `OPENAI_API_KEY`: Your OpenAI API key (required)
  - Loaded from `.env` if present (via `python-dotenv`)

### Customization
- **System Prompt**: Modify the `system_prompt` in the `AISupportBot` class
- **Model Settings**: Change the OpenAI model, temperature, or max_tokens in the `generate_response` method
- **FAQ Retrieval**: Adjust the number of relevant FAQs retrieved by modifying `n_results` parameter

## Sample FAQs Included

The bot comes pre-loaded with sample FAQs covering:
- Password reset procedures
- Business hours and contact information
- Refund policies
- Account management
- General support inquiries

## Technical Details

### Vector Database
- Uses ChromaDB for efficient semantic search
- Automatically generates embeddings for FAQ content
- Supports similarity-based retrieval

### Conversation Management
- Maintains conversation history per session
- Limits history to last 10 messages for context
- Generates unique conversation IDs for tracking

### Error Handling
- Graceful fallbacks for API failures
- User-friendly error messages
- Connection retry logic

## Troubleshooting

### Common Issues

1. **OpenAI API Key Error**
   - Ensure your API key is set correctly
   - Check that you have sufficient credits in your OpenAI account

2. **ChromaDB Issues**
   - The database will be created automatically on first run
   - Check file permissions in the project directory

3. **Port Already in Use**
   - Change the port in `app.py` if 5000 is occupied
   - Update the URL in your browser accordingly

### Performance Optimization
- Adjust the number of FAQ results retrieved
- Modify conversation history length
- Consider using a more powerful OpenAI model for better responses

## Future Enhancements

- [ ] User authentication and session management
- [ ] Multi-language support
- [ ] Sentiment analysis for customer satisfaction
- [ ] Integration with external CRM systems
- [ ] Advanced analytics and reporting
- [ ] Voice input/output capabilities
- [ ] File upload support for document queries

## License

This project is open source and available under the MIT License.

## Support

For technical support or questions about this AI Support Bot, please create an issue in the repository or contact the development team.




