from database import get_connection
from psycopg2.errors import UniqueViolation


# CREATE
def create_customer(customer):
    connection = get_connection()
    cursor = connection.cursor()

    query = """
        INSERT INTO customers (name, email, phone, city, age)
        VALUES (%s, %s, %s, %s, %s)
        RETURNING customer_id;
    """

    try:
        cursor.execute(
            query,
            (
                customer.name,
                customer.email,
                customer.phone,
                customer.city,
                customer.age
            )
        )

        customer_id = cursor.fetchone()[0]

        connection.commit()

        return customer_id

    except UniqueViolation:
        connection.rollback()
        raise

    finally:
        cursor.close()
        connection.close()


# READ - All Customers
def get_customers():
    connection = get_connection()
    cursor = connection.cursor()

    query = """
        SELECT customer_id, name, email, phone, city, age, created_at
        FROM customers
        ORDER BY customer_id;
    """

    cursor.execute(query)

    rows = cursor.fetchall()

    cursor.close()
    connection.close()

    customers = []

    for row in rows:
        customers.append({
            "customer_id": row[0],
            "name": row[1],
            "email": row[2],
            "phone": row[3],
            "city": row[4],
            "age": row[5],
            "created_at": row[6]
        })

    return customers


# READ - Customer by ID
def get_customer_by_id(customer_id):
    connection = get_connection()
    cursor = connection.cursor()

    query = """
        SELECT customer_id, name, email, phone, city, age, created_at
        FROM customers
        WHERE customer_id = %s;
    """

    cursor.execute(query, (customer_id,))

    row = cursor.fetchone()

    cursor.close()
    connection.close()

    if row is None:
        return None

    return {
        "customer_id": row[0],
        "name": row[1],
        "email": row[2],
        "phone": row[3],
        "city": row[4],
        "age": row[5],
        "created_at": row[6]
    }


# UPDATE
def update_customer(customer_id, customer):
    connection = get_connection()
    cursor = connection.cursor()

    query = """
        UPDATE customers
        SET
            name = %s,
            email = %s,
            phone = %s,
            city = %s,
            age = %s
        WHERE customer_id = %s;
    """

    try:
        cursor.execute(
            query,
            (
                customer.name,
                customer.email,
                customer.phone,
                customer.city,
                customer.age,
                customer_id
            )
        )

        updated = cursor.rowcount > 0

        connection.commit()

        return updated

    except UniqueViolation:
        connection.rollback()
        raise

    finally:
        cursor.close()
        connection.close()

# DELETE
def delete_customer(customer_id):
    connection = get_connection()
    cursor = connection.cursor()

    query = """
        DELETE FROM customers
        WHERE customer_id = %s;
    """

    cursor.execute(query, (customer_id,))

    deleted = cursor.rowcount > 0

    connection.commit()

    cursor.close()
    connection.close()

    return deleted