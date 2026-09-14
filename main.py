from fastapi import FastAPI, HTTPException, status

from schemas import CustomerCreate
from crud import (create_customer,get_customers,get_customer_by_id,update_customer,delete_customer)


app = FastAPI(
    title="Customer Management API",
    description="CRUD API using FastAPI and PostgreSQL",
    version="1.0.0"
)


# CREATE
@app.post("/customers", status_code=status.HTTP_201_CREATED)
def create_customer_api(customer: CustomerCreate):

    customer_id = create_customer(customer)

    return {
        "message": "Customer created successfully",
        "customer_id": customer_id
    }


# READ - All Customers
@app.get("/customers")
def get_all_customers():

    return get_customers()


# READ - Customer by ID
@app.get("/customers/{customer_id}")
def get_customer(customer_id: int):

    customer = get_customer_by_id(customer_id)

    if customer is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Customer not found"
        )

    return customer

