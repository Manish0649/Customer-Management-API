from fastapi import FastAPI, HTTPException, status
from psycopg2.errors import UniqueViolation

from schemas import CustomerCreate
from crud import (
    create_customer,
    get_customers,
    get_customer_by_id,
    update_customer,
    delete_customer
)


app = FastAPI(
    title="Customer Management API",
    description="CRUD API using FastAPI and PostgreSQL",
    version="1.0.0"
)

@app.get("/")
def root():
    return {"message": "Welcome to the Customer Management API"}

# CREATE
@app.post("/customers", status_code=status.HTTP_201_CREATED)
def create_customer_api(customer: CustomerCreate):

    try:
        customer_id = create_customer(customer)

    except UniqueViolation:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Email already exists"
        )

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


# UPDATE
@app.put("/customers/{customer_id}")
def update_customer_api(
    customer_id: int,
    customer: CustomerCreate
):

    try:
        updated = update_customer(customer_id, customer)

    except UniqueViolation:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Email already exists"
        )

    if not updated:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Customer not found"
        )

    return {
        "message": "Customer updated successfully"
    }

# DELETE
@app.delete("/customers/{customer_id}")
def delete_customer_api(customer_id: int):

    deleted = delete_customer(customer_id)

    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Customer not found"
        )

    return {
        "message": "Customer deleted successfully"
    }