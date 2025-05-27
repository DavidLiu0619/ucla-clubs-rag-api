#!/bin/bash

curl http://localhost:5002/

# Test the Flask app running on localhost:5002
curl -H "Content-Type: application/json" -X POST -d '{"question":"I am a freshman student. Can you recommend some UCLA clubs?"}' "http://localhost:5002/ask"

curl -H "Content-Type: application/json" -X POST -d '{"question":"I am looking for clubs related to technology and innovation. Can you suggest some?"}' "http://localhost:5002/ask"

curl -H "Content-Type: application/json" -X POST -d '{"question":"I am interested in data science, AI, statistics. Can you suggest some?"}' "http://localhost:5002/ask"

# Test the Flask app running on Google Cloud Run
curl -X POST "https://ucla-clubs-rag-api-980752141572.us-central1.run.app/ask" -H "Content-Type: application/json" -d '{"question":"I am a freshman student. Can you recommend some UCLA clubs?"}'

curl -X POST "https://ucla-clubs-rag-api-980752141572.us-central1.run.app/ask" -H "Content-Type: application/json" -d '{"question":"I am looking for clubs related to technology and innovation. Can you suggest some?"}'

curl -X POST "https://ucla-clubs-rag-api-980752141572.us-central1.run.app/ask" -H "Content-Type: application/json" -d '{"question":"I am interested in data science, AI, statistics. Can you suggest some?"}'
