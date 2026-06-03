# HTTP-Triggered ETL Microservice with CI/CD

## Project Overview

This project builds a Cloud Run HTTP microservice that accepts sales transaction JSON payloads, validates the data, transforms it, and loads the cleaned records into BigQuery.

## Architecture

Client / Postman / curl  
→ Cloud Run HTTP API  
→ JSON Schema Validation  
→ Transformation Logic  
→ BigQuery Table  
→ Cloud Build CI/CD  

## Tech Stack

- Python
- FastAPI
- Pydantic
- Pytest
- Docker
- Google Cloud Run
- Google BigQuery
- Google Cloud Build
- Artifact Registry
- GitHub

## Project Phases

1. Project setup
2. FastAPI service
3. JSON schema validation
4. Transformation logic
5. BigQuery setup
6. BigQuery loader
7. Unit testing
8. Docker containerization
9. Manual Cloud Run deployment
10. Cloud Build CI/CD