import argparse
import requests

def main():
    parser = argparse.ArgumentParser(description="AI-Powered Blog and Code Automation Agent")
    parser.add_argument("topic", type=str, help="The topic for the blog post")
    parser.add_argument("--language", type=str, default="python", help="Programming language for the code snippet")
    
    args = parser.parse_args()
    
    # Prepare the request payload
    payload = {
        "topic": args.topic,
        "language": args.language
    }
    
    # Send a POST request to the FastAPI endpoint
    response = requests.post("http://127.0.0.1:8000/generate-blog/", json=payload)
    
    if response.status_code == 200:
        data = response.json()
        print("Blog Content:\n", data["blog_content"])
        print("GitHub Repository URL:", data["repo_url"])
    else:
        print("Error:", response.status_code, response.text)

if __name__ == "__main__":
    main()
