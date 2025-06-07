# Legal Chatbot - Team SolArise

## 🏆 HackIndia Spark 9 - 2025

A multilingual legal assistant chatbot built with Flask, Google Gemini AI, and LangChain for intelligent legal document retrieval and question answering.

![Legal Chatbot](https://img.shields.io/badge/Legal-Chatbot-blue?style=for-the-badge&logo=law&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-2.0+-green?style=for-the-badge&logo=flask&logoColor=white)
![Gemini AI](https://img.shields.io/badge/Google-Gemini%20AI-orange?style=for-the-badge&logo=google&logoColor=white)

🎯 Overview
This legal chatbot provides AI-powered assistance for legal queries, specifically designed to help users understand Indian legal documents and procedures. The system uses vector-based document retrieval to provide contextually relevant answers to legal questions.
Key Capabilities

Legal Document Analysis: Processes and understands legal documents
Contextual Responses: Provides relevant answers based on document context
User-Friendly Interface: Clean, modern web interface with Flask
Multilingual Support: Designed for multilingual legal assistance
Vector Search: Efficient document retrieval using similarity search

✨ Features

🤖 AI-Powered Legal Assistant - Uses Google Gemini 1.5 Flash for intelligent responses
📚 Document Vectorization - Efficient storage and retrieval of legal documents
🔍 Similarity Search - Finds relevant document sections for user queries
💬 Interactive Chat Interface - Modern, responsive web-based chat
🎨 Beautiful UI/UX - Gradient designs with smooth animations
📱 Mobile Responsive - Works seamlessly on all devices
⚡ Fast Response Times - Optimized for quick legal assistance

🛠 Technology Stack
Backend

Python 3.8+ - Core programming language
Flask - Web framework
LangChain - LLM integration and document processing
Google Gemini AI - Language model for generating responses
Pickle - Vector store serialization

Frontend

HTML5 - Structure
CSS3 - Styling with gradients and animations
JavaScript - Interactive functionality

AI/ML

LangChain Google GenAI - Gemini integration
Vector Store - Document embedding and retrieval
Similarity Search - Context-aware document matching

🚀 Installation
Prerequisites

Python 3.8 or higher
Google Cloud API key for Gemini
pip package manager

Step 1: Clone the Repository
bashgit clone https://github.com/yourusername/HackIndia-Spark-9-2025-SolArise.git
cd HackIndia-Spark-9-2025-SolArise
Step 2: Create Virtual Environment
bashpython -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Step 3: Install Dependencies
bashpip install -r requirements.txt
Step 4: Set Up Environment Variables
Create a .env file in the root directory:
envGOOGLE_API_KEY=your_gemini_api_key_here
Step 5: Prepare Vector Store
Ensure you have a vectorstore.pkl file in the root directory containing your processed legal documents.
⚙️ Configuration
Google Gemini API Setup

Go to Google AI Studio
Create a new API key
Add it to your .env file (never hardcode in source files!)

Vector Store Configuration
The system expects a pickled vector store file (vectorstore.pkl) containing preprocessed legal documents. You can modify the loading path in chat_engine.py:
pythondef load_vectorstore(path: str = "vectorstore.pkl"):
    with open(path, "rb") as f:
        return pickle.load(f)
🎮 Usage
Running the Application
bashpython app.py
The application will start on http://localhost:5000 in debug mode.
Command Line Interface
You can also run the chat engine directly:
bashpython chat_engine.py
Using the Web Interface

Open your browser and navigate to http://localhost:5000
Type your legal question in the text area
Click the send button or press Enter
View the AI-generated response based on legal document context

Example Queries

"What are the requirements for filing a property dispute?"
"Explain the process of company registration in India"
"What are the rights of consumers under Indian law?"

📁 Project Structure
HackIndia-Spark-9-2025-SolArise/
│
├── app.py                 # Flask web application
├── chat_engine.py         # Core chat logic and AI integration
├── templates/
│   └── chat.html         # Web interface template
├── vectorstore.pkl       # Serialized vector store (legal documents)
├── requirements.txt      # Python dependencies
├── README.md            # Project documentation
├── .env                 # Environment variables (create this)
└── .gitignore          # Git ignore rules
📡 API Documentation
Chat Engine Functions
load_vectorstore(path: str = "vectorstore.pkl")

Purpose: Loads the serialized vector store
Parameters: path - Path to the pickle file
Returns: Vector store object

get_response_from_query(query: str) -> str

Purpose: Generates AI response for legal queries
Parameters: query - User's legal question
Returns: AI-generated response string

Flask Routes
GET/POST /

Purpose: Main chat interface
GET: Renders empty chat page
POST: Processes user query and returns response

🔧 Customization
Modifying the AI Model
You can change the Gemini model in chat_engine.py:
pythongemini_model = ChatGoogleGenerativeAI(
    model="gemini-1.5-pro",  # Change to gemini-1.5-pro for better performance
    temperature=0.7,
    max_tokens=1000  # Increase for longer responses
)
Updating the Prompt Template
Modify the prompt template in chat_engine.py to customize AI behavior:
pythonprompt_template = """
You are a specialized legal assistant for Indian law...
# Add your custom instructions here
"""
Styling Customization
The CSS in chat.html uses CSS variables for easy theme customization:

Primary colors: #7e5bc2 (purple), #10a37f (teal)
Gradient backgrounds with smooth animations
Responsive design for mobile compatibility

Requirements
txtflask>=2.0.0
langchain-google-genai>=1.0.0
langchain-core>=0.1.0
python-dotenv>=1.0.0
pickle5>=0.0.11
Security Notes

Never commit your .env file - it contains sensitive API keys
Never hardcode API keys in your source code
Regenerate API keys if accidentally exposed
The .gitignore file prevents accidental commits of sensitive files

🤝 Contributing
We welcome contributions! Please follow these steps:

Fork the repository
Create a feature branch (git checkout -b feature/AmazingFeature)
Commit your changes (git commit -m 'Add some AmazingFeature')
Push to the branch (git push origin feature/AmazingFeature)
Open a Pull Request

Development Guidelines

Follow PEP 8 style guidelines
Add comments for complex logic
Test your changes thoroughly
Update documentation as needed

👥 Team SolArise

Gourav Sahu - Lead Developer | AI/ML Engineer
Harsh Katariya - Frontend Developer
Nishant Saini - Backend Developer
Aman Verma - Data & Research Engineer

Troubleshooting
Common Issues
"GOOGLE_API_KEY environment variable is not set"

Make sure you've created a .env file with your API key
Verify the .env file is in the same directory as your script

"Invalid API key"

Check that your API key is correct in the .env file
Ensure your Google Cloud project has the Gemini API enabled

"Module not found" errors

Install all requirements: pip install -r requirements.txt
Make sure you're using the correct Python environment

Vector store loading issues

Ensure vectorstore.pkl exists in the root directory
Check file permissions and path accessibility

🙏 Acknowledgments

Google for providing the Gemini AI API
LangChain community for excellent documentation
HackIndia Spark 9 organizers for the opportunity
Open source community for various tools and libraries

📞 Support
For support, email us at team@solarise.dev or create an issue in the GitHub repository.
License
This project is licensed under the MIT License - see the LICENSE file for details.

Made with ❤️ by Team SolArise for HackIndia Spark 9 - 2025
**Made with ❤️ by Team SolArise for HackIndia Spark 9 - 2025**
