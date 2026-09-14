from faker import Faker
from database import get_connection


fake = Faker()

cities = [
    "Delhi","Mumbai","Chandigarh","Bangalore","Amritsar",
    "Pune","Ahmedabad","Jaipur","Dehradun","Ludhiana"
]

def generate_customers(number_of_customers):
    connection = get_connection()
    cursor = connection.cursor()

    query = """
        INSERT INTO customers (name, email, phone, city, age)
        VALUES (%s, %s, %s, %s, %s);
    """

    for _ in range(number_of_customers):

        name = fake.name()
        email = fake.unique.email()
        phone = fake.numerify("##########")
        city = fake.random_element(cities)
        age = fake.random_int(min=18, max=70)

        cursor.execute(
            query,
            (name, email, phone, city, age)
        )

    connection.commit()

    cursor.close()
    connection.close()

    print(f"{number_of_customers} customers inserted successfully.")


generate_customers(100)