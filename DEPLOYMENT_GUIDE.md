# 🚀 PR Review Agent - Deployment Guide

## 📋 **Deployment-Ready Project Structure**

```
pr-review-agent/
├── main.py                          # Main entry point for deployment
├── requirements.txt                 # Production dependencies
├── vercel.json                     # Vercel configuration
├── railway.json                    # Railway configuration
├── render.yaml                     # Render configuration
├── Procfile                        # Heroku configuration
├── runtime.txt                     # Python version specification
├── env.example                     # Environment variables template
├── .gitignore                      # Git ignore rules
├── README.md                       # Project documentation
├── backend/
│   ├── simple_pr_app.py           # Main FastAPI application
│   └── analyzers/                 # Analysis modules
│       ├── __init__.py
│       ├── github_client.py
│       ├── static_analysis.py
│       └── ai_feedback.py
├── frontend/                       # Empty (ready for future frontend)
└── quality_trends.db              # SQLite database (created at runtime)
```

## 🎯 **Supported Deployment Platforms**

### **1. Vercel (Recommended for Hackathons)**
- ✅ **Fastest deployment**
- ✅ **Automatic HTTPS**
- ✅ **Custom domain support**
- ✅ **Serverless functions**

### **2. Railway**
- ✅ **Easy database management**
- ✅ **Persistent storage**
- ✅ **Automatic deployments**

### **3. Render**
- ✅ **Free tier available**
- ✅ **Persistent storage**
- ✅ **Custom domains**

## 🚀 **Step-by-Step Deployment Instructions**

### **Option 1: Vercel Deployment (Recommended)**

#### **Step 1: Prepare Your Repository**
```bash
# 1. Initialize git repository
git init
git add .
git commit -m "Initial commit: PR Review Agent ready for deployment"

# 2. Create GitHub repository
# Go to GitHub.com → New Repository → Create
# Copy the repository URL

# 3. Connect local repository to GitHub
git remote add origin https://github.com/yourusername/pr-review-agent.git
git branch -M main
git push -u origin main
```

#### **Step 2: Deploy to Vercel**
```bash
# 1. Install Vercel CLI
npm i -g vercel

# 2. Login to Vercel
vercel login

# 3. Deploy from project directory
vercel

# 4. Follow the prompts:
# - Set up and deploy? Y
# - Which scope? (your account)
# - Link to existing project? N
# - Project name: pr-review-agent
# - Directory: ./
# - Override settings? N
```

#### **Step 3: Configure Environment Variables**
```bash
# Set environment variables in Vercel dashboard or CLI
vercel env add GITHUB_TOKEN
vercel env add OPENAI_API_KEY
vercel env add ANTHROPIC_API_KEY
```

#### **Step 4: Test Deployment**
```bash
# Get your deployment URL
vercel ls

# Test the API
curl https://your-app.vercel.app/health
curl https://your-app.vercel.app/docs
```

### **Option 2: Railway Deployment**

#### **Step 1: Connect to Railway**
1. Go to [railway.app](https://railway.app)
2. Sign up with GitHub
3. Click "New Project" → "Deploy from GitHub repo"
4. Select your `pr-review-agent` repository

#### **Step 2: Configure Environment**
1. Go to your project dashboard
2. Click on "Variables" tab
3. Add environment variables:
   - `PORT`: `8000`
   - `GITHUB_TOKEN`: `your_github_token`
   - `OPENAI_API_KEY`: `your_openai_key`

#### **Step 3: Deploy**
1. Railway will automatically detect `railway.json`
2. Click "Deploy" button
3. Wait for deployment to complete

### **Option 3: Render Deployment**

#### **Step 1: Connect to Render**
1. Go to [render.com](https://render.com)
2. Sign up with GitHub
3. Click "New" → "Web Service"
4. Connect your GitHub repository

#### **Step 2: Configure Service**
1. **Name**: `pr-review-agent`
2. **Environment**: `Python 3`
3. **Build Command**: `pip install -r requirements.txt`
4. **Start Command**: `python main.py`
5. **Health Check Path**: `/health`

#### **Step 3: Set Environment Variables**
1. Go to "Environment" tab
2. Add variables:
   - `PORT`: `10000`
   - `GITHUB_TOKEN`: `your_github_token`
   - `OPENAI_API_KEY`: `your_openai_key`

## 🔧 **Environment Variables Configuration**

### **Required Variables**
```bash
# Server Configuration
PORT=8000
HOST=0.0.0.0
```

### **Optional Variables (for enhanced features)**
```bash
# GitHub API (for private repositories)
GITHUB_TOKEN=ghp_your_github_token_here

# OpenAI API (for AI features)
OPENAI_API_KEY=sk-your_openai_api_key_here

# Anthropic API (for alternative AI features)
ANTHROPIC_API_KEY=your_anthropic_api_key_here
```

### **How to Get API Keys**

#### **GitHub Token**
1. Go to GitHub.com → Settings → Developer settings
2. Personal access tokens → Tokens (classic)
3. Generate new token
4. Select scopes: `repo`, `public_repo`
5. Copy the token

#### **OpenAI API Key**
1. Go to [platform.openai.com](https://platform.openai.com)
2. Sign up/Login
3. Go to API Keys
4. Create new secret key
5. Copy the key

## 🧪 **Testing Your Deployment**

### **1. Health Check**
```bash
curl https://your-app-url.com/health
```

### **2. API Documentation**
Visit: `https://your-app-url.com/docs`

### **3. Test PR Review**
```bash
curl -X POST "https://your-app-url.com/review" \
  -H "Content-Type: application/json" \
  -d '{
    "repo_url": "https://github.com/test/repo",
    "pr_number": 1,
    "include_ai_suggestions": true
  }'
```

### **4. Test with Different Platforms**
```bash
# Test with PowerShell
Invoke-WebRequest -Uri "https://your-app-url.com/health" -Method GET

# Test with Python
python -c "import requests; print(requests.get('https://your-app-url.com/health').json())"
```

## 📊 **Database Management**

### **SQLite Database**
- The `quality_trends.db` file is created automatically
- Data persists between deployments on most platforms
- For production, consider upgrading to PostgreSQL

### **Database Backup**
```bash
# Download database file
curl -O https://your-app-url.com/quality_trends.db

# Or use platform-specific backup tools
```

## 🎯 **Hackathon Demo Checklist**

### **Before Demo**
- [ ] Deploy to chosen platform
- [ ] Test all endpoints work
- [ ] Verify API documentation loads
- [ ] Test with sample PR data
- [ ] Prepare demo script
- [ ] Have backup deployment ready

### **Demo Script**
1. **Show API Documentation**: `https://your-app-url.com/docs`
2. **Test Health Endpoint**: `https://your-app-url.com/health`
3. **Demo PR Review**: Use the interactive docs to test POST /review
4. **Show AI Features**: Highlight pr_summary, auto_fixes, priority_scores
5. **Explain Architecture**: Show modular structure and analyzers

### **Demo Data Examples**
```json
{
  "repo_url": "https://github.com/microsoft/vscode",
  "pr_number": 1,
  "include_ai_suggestions": true,
  "analysis_depth": "comprehensive"
}
```

## 🚨 **Troubleshooting**

### **Common Issues**

#### **1. Import Errors**
```bash
# Check PYTHONPATH is set correctly
export PYTHONPATH=/var/task/backend
```

#### **2. Database Path Issues**
```bash
# Ensure database path is absolute
db_path = os.path.join(os.getcwd(), "quality_trends.db")
```

#### **3. Port Issues**
```bash
# Use environment variable for port
port = int(os.environ.get("PORT", 8000))
```

#### **4. CORS Issues**
```bash
# Check CORS configuration in app.py
app.add_middleware(CORSMiddleware, allow_origins=["*"])
```

## 📈 **Performance Optimization**

### **For Production**
1. **Add caching** for repeated requests
2. **Implement rate limiting** for API endpoints
3. **Add monitoring** and logging
4. **Use connection pooling** for database
5. **Add error handling** and retries

### **Scaling Considerations**
- Vercel: Serverless, auto-scaling
- Railway: Container-based, manual scaling
- Render: Container-based, auto-scaling

## 🎉 **Success!**

Your PR Review Agent is now deployment-ready! 

**Live URL**: `https://your-app-url.com`
**API Docs**: `https://your-app-url.com/docs`
**Health Check**: `https://your-app-url.com/health`

**Ready for your hackathon demo! 🚀**
