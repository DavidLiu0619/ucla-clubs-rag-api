# UCLA Clubs RAG API

A Retrieval Augmented Generation (RAG) API that provides intelligent responses about UCLA student organizations and clubs using natural language processing.

## Overview

This project implements a RAG pipeline that combines a vector database with a Large Language Model to provide accurate, contextual information about UCLA clubs and organizations. The system processes queries in natural language and returns relevant information by searching through a curated database of UCLA club descriptions.

## Data

The system uses a cleaned dataset of UCLA organizations (`ucla_orgs_cleaned_unique.csv`) which contains information about various student clubs and organizations. This data is processed and stored in a Chroma vector database for efficient semantic search. 

The data is webscrapped from https://community.ucla.edu/studentorgs

## Repository Structure

| File | Description |
|------|-------------|
| `rag_pipeline.py` | Core RAG implementation for processing queries |
| `server.py` | FastAPI/Flask server that exposes the RAG endpoints |
| `ucla_clubs_rag_llm.ipynb` | Jupyter notebook for RAG pipeline development and testing |
| `ucla_orgs_cleaned_unique.csv` | Cleaned dataset of UCLA organizations |
| `requirements.txt` | Python dependencies |
| `Dockerfile` | Container configuration for deployment |
| `docker-compose.yml` | Local development container orchestration |
| `curl_test.sh` | Example API requests for testing |

## Prerequisites

- Python 3.8+
- Docker and Docker Compose
- Google Gemini API Key (see API_Key_Guide and Website for setup): https://ai.google.dev/gemini-api/docs/api-key

## Installation

1. Clone this repository:
```bash
git clone https://github.com/DavidLiu0619/ucla_clubs_rag_api.git
cd ucla_clubs_rag_api
```

2. Create your .env file and set up your Gemini API key in your .env file:

```bash
cat > .env <<EOF
GOOGLE_API_KEY=your_actual_gemini_api_key_here
EOF
```

3. Build and run with Docker:
```bash
docker compose up -d
```

## Usage

The API provides endpoints for querying information about UCLA clubs. You can use the provided `curl_test.sh` script to test the API endpoints.

Example query:
```bash
curl -H "Content-Type: application/json" -X POST -d '{"question":"I am a freshman student. Can you recommend some UCLA clubs?"}' "http://localhost:5002/ask"
```

Below command line after deployment to Google Cloud Run:

```bash
curl -X POST "https://ucla-clubs-rag-api-980752141572.us-central1.run.app/ask" -H "Content-Type: application/json" -d '{"question":"I am a freshman student. Can you recommend some UCLA clubs?"}'
```

You will receive the answer from Gemini, and if you want, you can modify the question and ask questions related to UCLA Organizations. 


## Architecture

1. **Vector Database**: Uses Chroma DB to store and retrieve club information embeddings
2. **RAG Pipeline**: Implements retrieval-augmented generation to combine retrieved context with LLM responses
3. **API Layer**: Exposes the functionality through a REST API

## Development

To contribute to the project:

1. Create a new branch for your feature
2. Make your changes
3. Test thoroughly
4. Submit a pull request

## MIT License

## Acknowledgments

- UCLA for providing the organizations data
- Gemini for the LLM capabilities
- Chroma for the vector database
