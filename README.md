# PR Review Agent

An AI-powered agent for automatically reviewing pull requests across multiple git servers (GitHub, GitLab, Bitbucket). This tool analyzes code changes, runs static analysis, and provides constructive feedback to improve code quality.

## 🚀 Features

- **Multi-Platform Support**: Works with GitHub, GitLab, and Bitbucket
- **Static Code Analysis**: Integrates with pylint, flake8, black, and other tools
- **Security Analysis**: Uses bandit and safety for security vulnerability detection
- **AI-Powered Suggestions**: Optional AI-generated improvement recommendations
- **RESTful API**: FastAPI-based backend with comprehensive documentation
- **Modular Architecture**: Easy to extend and customize
- **Real-time Analysis**: Fast and efficient code review process

## 📁 Project Structure

```
pr-review-agent/
├── backend/
│   └── app.py              # FastAPI application
├── frontend/               # Optional React frontend (future)
├── requirements.txt        # Python dependencies
├── .gitignore             # Git ignore rules
└── README.md              # Project documentation
```

## 🛠️ Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Git

### Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd pr-review-agent
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   # Create .env file in the root directory
   touch .env
   ```
   
   Add the following to your `.env` file:
   ```env
   # GitHub API Token (optional, for private repos)
   GITHUB_TOKEN=your_github_token_here
   
   # OpenAI API Key (optional, for AI suggestions)
   OPENAI_API_KEY=your_openai_key_here
   
   # API Configuration
   API_HOST=0.0.0.0
   API_PORT=8000
   ```

## 🚀 Usage

### Running the API Server

1. **Start the FastAPI server**
   ```bash
   cd backend
   python app.py
   ```

2. **Access the API documentation**
   - Swagger UI: http://localhost:8000/docs
   - ReDoc: http://localhost:8000/redoc

### API Endpoints

#### Health Check
```http
GET /health
```

#### Test Endpoint
```http
GET /review
```

#### Review Pull Request
```http
POST /review
Content-Type: application/json

{
  "pr_url": "https://github.com/owner/repo/pull/123",
  "include_ai_suggestions": true,
  "analysis_depth": "standard"
}
```

#### Get Supported Platforms
```http
GET /supported-platforms
```

### Example Usage with curl

```bash
# Test the API
curl http://localhost:8000/health

# Review a pull request
curl -X POST "http://localhost:8000/review" \
     -H "Content-Type: application/json" \
     -d '{
       "pr_url": "https://github.com/owner/repo/pull/123",
       "include_ai_suggestions": true,
       "analysis_depth": "standard"
     }'
```

## 🔧 Configuration

### Analysis Depth Options

- **basic**: Quick analysis with essential checks
- **standard**: Comprehensive analysis with style and quality checks
- **comprehensive**: Full analysis including security and performance checks

### Supported Git Platforms

- **GitHub**: Full API support with authentication
- **GitLab**: Full API support with authentication
- **Bitbucket**: Full API support with authentication

## 🧪 Testing

Run the test suite:

```bash
# Install test dependencies
pip install pytest pytest-asyncio pytest-cov

# Run tests
pytest

# Run tests with coverage
pytest --cov=backend
```

## 📊 Code Quality Tools

This project uses several code quality tools:

- **pylint**: Python code analysis
- **flake8**: Style guide enforcement
- **black**: Code formatting
- **isort**: Import sorting
- **mypy**: Static type checking
- **bandit**: Security analysis
- **safety**: Dependency vulnerability scanning

Run code quality checks:

```bash
# Format code
black backend/

# Sort imports
isort backend/

# Run linting
pylint backend/

# Type checking
mypy backend/

# Security analysis
bandit -r backend/
```

## 🚀 Deployment

### Using Docker (Recommended)

1. **Create Dockerfile**
   ```dockerfile
   FROM python:3.9-slim
   
   WORKDIR /app
   COPY requirements.txt .
   RUN pip install -r requirements.txt
   
   COPY backend/ ./backend/
   EXPOSE 8000
   
   CMD ["uvicorn", "backend.app:app", "--host", "0.0.0.0", "--port", "8000"]
   ```

2. **Build and run**
   ```bash
   docker build -t pr-review-agent .
   docker run -p 8000:8000 pr-review-agent
   ```

### Using Heroku

1. **Create Procfile**
   ```
   web: uvicorn backend.app:app --host 0.0.0.0 --port $PORT
   ```

2. **Deploy**
   ```bash
   git add .
   git commit -m "Deploy to Heroku"
   git push heroku main
   ```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🎯 Hackathon Information

This project was developed for the CodeMate Hackathon (September 20-21, 2024).

### Mandatory Requirements Met

- ✅ Compatibility with multiple git servers (GitHub, GitLab, Bitbucket)
- ✅ Feedback generation on code structure, standards, and possible bugs
- ✅ Written in Python with modular structure
- ✅ Uses CodeMate Build and CodeMate Extension (as required)

### Possible Enhancements Implemented

- ✅ AI-driven feedback with automated suggestions
- ✅ Inline review comments system
- ✅ Integration-ready for CI/CD pipelines
- ✅ Scoring system for PR quality assessment

## 📞 Support

For questions or support, please open an issue in the repository or contact the development team.

---

**Happy Coding! 🚀**