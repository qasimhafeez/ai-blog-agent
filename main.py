from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from services.blog_generator import generate_blog_post
from services.code_generator import create_github_repo

app = FastAPI()

class BlogRequest(BaseModel):
    topic: str
    language: str = "python"

@app.post("/generate-blog/")
async def generate_blog(request: BlogRequest):
    try:
        # Generate the blog content and code
        blog_content, code_snippet = generate_blog_post(request.topic, request.language)
        
        # Create a GitHub repository and push the code
        repo_url = create_github_repo(request.topic, code_snippet)
        
        return {
            "message": "Blog post generated successfully.",
            "blog_content": blog_content,
            "repo_url": repo_url
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
