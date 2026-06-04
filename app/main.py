from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder

from app.schemas import SalesTransaction


app = FastAPI(
    title="Sales ETL Microservice",
    description="HTTP-triggered ETL microservice for validating, transforming, and loading sales transactions into BigQuery.",
    version="1.0.0",
)


@app.get("/")
def root():
    return {
        "message": "Sales ETL Microservice is running",
        "status": "ok",
    }


@app.get("/health")
def health_check():
    return {
        "service": "sales-etl-microservice",
        "status": "healthy",
    }


@app.post("/transactions")
def receive_transaction(transaction: SalesTransaction):
    validated_transaction = jsonable_encoder(transaction)

    return {
        "message": "Transaction validated successfully",
        "validated_payload": validated_transaction,
    }
