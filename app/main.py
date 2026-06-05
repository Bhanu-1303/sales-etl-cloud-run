from fastapi import FastAPI

from app.schemas import SalesTransaction
from app.transform import transform_transaction


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
    transformed_record = transform_transaction(transaction)

    return {
        "message": "Transaction validated and transformed successfully",
        "transformed_record": transformed_record,
    }
