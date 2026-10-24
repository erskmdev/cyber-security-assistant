# cyber-security-assistant
Cyber-Security-Assistant is an Agentic AI application designed to assist users with cybersecurity-related queries, threat analysis, and vulnerability assessment. It leverages intelligent AI agents to identify potential security risks, provide actionable recommendations, and support proactive vulnerability management.


Step1. cis-basic>python ingestion/ingest-st.py 

output :
``` 
C:\Users\user\Desktop\sharad-ai\shared\ey-ai-upskill-13\17-capstone-part-1\cis-basic\ingestion\ingest-st.py:4: DeprecationWarning: `langchain-community` is being sunset and is no longer actively maintained. See https://github.com/langchain-ai/langchain-community/issues/674 for details and migration guidance toward standalone integration packages.
  from langchain_community.document_loaders import PyPDFLoader

📄 Loading CIS document...
✅ Loaded 1454 pages

✂️ Splitting into chunks...
✅ Created 3205 chunks

🧠 Generating embeddings...
Loading weights: 100%|████████████████████████████████████████████████| 103/103 [00:00<00:00, 1130.59it/s]
Warning: You are sending unauthenticated requests to the HF Hub. Please set a HF_TOKEN to enable higher rate limits and faster downloads.

📦 Storing in FAISS vector DB...

🎉 Ingestion complete! Vector store saved.

(langflow) C:\Users\user\Desktop\sharad-ai\shared\ey-ai-upskill-13\17-capstone-part-1\cis-basic>

```


Step2: cis-basic>uvicorn api:app --reload

Output: 
```
(langflow) C:\Users\user\Desktop\sharad-ai\shared\ey-ai-upskill-13\17-capstone-part-1\cis-basic>uvicorn api:app --reload
INFO:     Will watch for changes in these directories: ['C:\\Users\\user\\Desktop\\sharad-ai\\shared\\ey-ai-upskill-13\\17-capstone-part-1\\cis-basic']
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [4644] using WatchFiles
Loading weights: 100%|████████████████████████████████████████████████| 103/103 [00:00<00:00, 1213.88it/s]
Warning: You are sending unauthenticated requests to the HF Hub. Please set a HF_TOKEN to enable higher rate limits and faster downloads.
INFO:     Started server process [11284]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     127.0.0.1:51818 - "GET / HTTP/1.1" 404 Not Found
INFO:     127.0.0.1:51818 - "GET /favicon.ico HTTP/1.1" 404 Not Found
INFO:     127.0.0.1:51819 - "GET /doc HTTP/1.1" 404 Not Found
INFO:     127.0.0.1:51821 - "GET / HTTP/1.1" 404 Not Found
INFO:     127.0.0.1:51822 - "GET /docs HTTP/1.1" 200 OK
INFO:     127.0.0.1:51822 - "GET /openapi.json HTTP/1.1" 200 OK
INFO:     127.0.0.1:51846 - "POST /ask HTTP/1.1" 500 Internal Server Error
WARNING:  WatchFiles detected changes in 'assistants\policy_agent_enhanced.py'. Reloading...
 INFO:     Shutting down
INFO:     Waiting for application shutdown.
INFO:     Application shutdown complete.
INFO:     Finished server process [11284]
Loading weights: 100%|████████████████████████████████████████████████| 103/103 [00:00<00:00, 1610.57it/s]
Warning: You are sending unauthenticated requests to the HF Hub. Please set a HF_TOKEN to enable higher rate limits and faster downloads.
INFO:     Started server process [8352]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     127.0.0.1:51872 - "POST /ask HTTP/1.1" 200 OK
INFO:     127.0.0.1:52176 - "POST /ask HTTP/1.1" 200 OK
INFO:     127.0.0.1:52286 - "POST /ask HTTP/1.1" 200 OK
INFO:     127.0.0.1:52305 - "POST /ask HTTP/1.1" 200 OK
INFO:     127.0.0.1:52332 - "POST /ask HTTP/1.1" 200 OK
INFO:     127.0.0.1:52360 - "POST /ask HTTP/1.1" 200 OK
```

Step 3: Create Tool for above API expose 

ChatGPT : 
promt: create a lanchain tool to consume localhost:8080/ask whose server code is as below '''

@app.post("/ask", response_model=QueryResponse)
async def ask_assistant(request: QueryRequest):
    try:
        result = assistant(request.query)

        return QueryResponse(
            answer=result["answer"]
        )

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )
    
'''

output: 

```

import requests
from langchain_core.tools import tool


API_URL = "http://localhost:8080/ask"


@tool
def ask_local_assistant(query: str) -> str:
    """Ask the local assistant a question and return its answer.

    Use this tool when a question needs to be answered
    by the assistant running on localhost:8080.
    """
    try:
        response = requests.post(
            API_URL,
            json={"query": query},
            timeout=60,
        )

        response.raise_for_status()
        data = response.json()

        return data["answer"]

    except requests.exceptions.Timeout:
        return "Error: The local assistant API request timed out."

    except requests.exceptions.ConnectionError:
        return (
            "Error: Could not connect to the local assistant API. "
            "Ensure the FastAPI server is running on port 8080."
        )

    except requests.exceptions.HTTPError as e:
        return f"API HTTP error: {e.response.text}"

    except (ValueError, KeyError) as e:
        return f"Invalid API response: {e}"

```

Step 4: Add Tool in - C:\Users\user\Desktop\capstone-ai\cyber-security-assistant\Capstone_Project\30-agentic-capstone\agentic-capstone-part-2.ipynb

API_KEY => open api and NVE registration 

Output:

till phase 3: 
C:\Users\user\Desktop\capstone-ai\cyber-security-assistant\Capstone_Project\data\agentic-capstone-part-2.html


