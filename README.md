# Constitution Chatbot - Indian Constitution Knowledge Base

A comprehensive AI-powered chatbot providing detailed information about the Indian Constitution, legal procedures, and landmark Supreme Court judgments.

## Features

- **102 Constitutional Articles** covering all major Parts of the Constitution
- **4 Legal Procedures** (PIL, Writs, Constitutional Amendment, Impeachment)
- **10 Landmark Supreme Court Cases** (Kesavananda Bharati, Puttaswamy, Triple Talaq, etc.)
- **Smart Search** with keyword matching and contextual fallbacks
- **Interactive UI** with quick reply suggestions
- **Comprehensive Coverage** of Fundamental Rights, DPSP, Fundamental Duties, and more

## Database Statistics

| Category | Count | Coverage |
|----------|-------|----------|
| Constitutional Articles | 102 | Parts I-XXI (major articles) |
| Legal Procedures | 4 | PIL, Writs, Amendment, Impeachment |
| Landmark Cases | 10 | Major Supreme Court judgments |
| **Total Entries** | **116** | Comprehensive legal knowledge base |

## Tech Stack

- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS, JavaScript
- **Database**: JSON-based knowledge base
- **Deployment**: Gunicorn WSGI server

## Local Development

### Prerequisites
- Python 3.11 or higher
- pip (Python package manager)

### Installation

1. Clone the repository:
```bash
git clone <your-repo-url>
cd constitution-chatbot
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python app.py
```

4. Open your browser and navigate to:
```
http://localhost:5000
```

## Deployment

### Deploy to Render

1. Create a new Web Service on [Render](https://render.com)
2. Connect your GitHub repository
3. Configure:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
   - **Environment**: Python 3

### Deploy to Railway

1. Create a new project on [Railway](https://railway.app)
2. Connect your GitHub repository
3. Railway will auto-detect the configuration from `Procfile`

### Deploy to Heroku

1. Install Heroku CLI
2. Login and create app:
```bash
heroku login
heroku create your-app-name
```

3. Deploy:
```bash
git push heroku main
```

## Usage Examples

### Query Articles
- "What is Article 21?"
- "Tell me about fundamental rights"
- "Article 370"

### Query Legal Procedures
- "How to file PIL?"
- "What is the procedure for constitutional amendment?"
- "Writ petition procedure"

### Query Landmark Cases
- "Kesavananda Bharati case"
- "Right to privacy judgment"
- "Triple Talaq case"

## Project Structure

```
constitution-chatbot/
├── app.py                      # Main Flask application
├── data/
│   └── constitution_data.json  # Knowledge base (102 articles, 4 procedures, 10 cases)
├── templates/
│   └── index.html             # Frontend UI
├── static/
│   ├── css/
│   └── js/
├── requirements.txt           # Python dependencies
├── Procfile                   # Deployment configuration
├── runtime.txt               # Python version
└── README.md                 # This file
```

## API Endpoints

### GET /
Returns the main chat interface

### POST /chat
Handles chat queries
- **Request**: `{ "message": "your query" }`
- **Response**: `{ "success": true, "message": "response text" }`

### GET /quick-replies
Returns suggested quick reply questions
- **Response**: `{ "success": true, "replies": [...] }`

## Contributing

Contributions are welcome! To add more articles, procedures, or cases:

1. Edit `data/constitution_data.json`
2. Follow the existing JSON structure
3. Test locally before deploying

## License

This project is for educational purposes. Constitutional text is in the public domain.

## Acknowledgments

- Constitution of India (Government of India)
- Supreme Court of India judgments
- Legal procedures and documentation

## Support

For issues or questions, please open an issue on GitHub.

---

**Made with ❤️ for legal education and awareness**
