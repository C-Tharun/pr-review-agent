"""
Simple PR Review App - FastAPI Application

This is the main FastAPI application for the PR Review Agent.
It provides endpoints for PR analysis and review functionality.

"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from pydantic import BaseModel
from typing import List
import os

# Create FastAPI app
app = FastAPI(
    title="PR Review Agent",
    description="AI-powered PR review and analysis tool",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Pydantic models
class PRReviewRequest(BaseModel):
    pr_url: str
    repository: str
    pr_number: int
    include_ai_suggestions: bool = True  # optional, defaults to True

class PRReviewResponse(BaseModel):
    analysis: str
    suggestions: List[str]
    score: float

# Root endpoint: redirect to docs
@app.get("/", include_in_schema=False)
async def root_redirect():
    return RedirectResponse(url="/docs")

# Health check endpoint
@app.get("/health")
async def health_check():
    return {"status": "healthy", "service": "pr-review-agent"}

# PR review endpoint
@app.post("/review", response_model=PRReviewResponse)
async def review_pr(request: PRReviewRequest):
    """
    Review a pull request and provide analysis
    """
    try:
        # Placeholder implementation
        # In a real implementation, this would analyze the PR
        analysis = f"Analysis for PR #{request.pr_number} in {request.repository}"
        suggestions = [
            "Consider adding more unit tests",
            "Review code complexity",
            "Check for security vulnerabilities"
        ]
        score = 8.5
        
        return PRReviewResponse(
            analysis=analysis,
            suggestions=suggestions,
            score=score
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Additional endpoint: list analyzers
@app.get("/analyzers")
async def list_analyzers():
    """List available analyzers"""
    return {
        "analyzers": [
            "static_analysis",
            "ai_feedback",
            "github_client"
        ]
    }

# Run locally
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
