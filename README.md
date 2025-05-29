# UCLA Clubs RAG API

A Retrieval Augmented Generation (RAG) API that provides intelligent responses about UCLA student organizations and clubs using natural language processing.

## Overview

This project implements a RAG pipeline that combines a vector database with a Large Language Model to provide accurate, contextual information about UCLA clubs and organizations. The system processes queries in natural language and returns relevant information by searching through a curated database of UCLA club descriptions.

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
- OpenAI API Key (see API_Key_Guide.rtf for setup)

## Installation

1. Clone this repository:
```bash
git clone https://github.com/your-username/ucla_clubs_rag_api.git
cd ucla_clubs_rag_api
```

2. Set up your OpenAI API key following the instructions in `API_Key_Guide.rtf`

3. Build and run with Docker:
```bash
docker compose up -d
```

## Usage

The API provides endpoints for querying information about UCLA clubs. You can use the provided `curl_test.sh` script to test the API endpoints.

Example query:
```bash
curl -X POST "http://localhost:8000/query" \
     -H "Content-Type: application/json" \
     -d '{"question": "Tell me about computer science clubs at UCLA"}'
```

## Data

The system uses a cleaned dataset of UCLA organizations (`ucla_orgs_cleaned_unique.csv`) which contains information about various student clubs and organizations. This data is processed and stored in a Chroma vector database for efficient semantic search.

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

## License

[Your chosen license]

## Contributors

- [Your Name]
- [Other Contributors]

## Acknowledgments

- UCLA for providing the organizations data
- OpenAI for the LLM capabilities
- Chroma for the vector database
