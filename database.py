"""from sqlalchemy import create_engine,text
import os

db_connection_string = os.environ['DB_CONNECTION_STRING']

engine = create_engine(db_connection_string)

with engine.connect() as conn:
    result = conn.execute(text("select * from users"))
  
    print(result.all())"""
from dotenv import load_dotenv
from sqlalchemy import create_engine, text
import os

load_dotenv()

db_connection_string = os.getenv('DB_CONNECTION_STRING')
print("DB string: ", db_connection_string)
engine = create_engine(db_connection_string)

if not db_connection_string:
    raise ValueError("DB_CONNECTION_STRING is missing in the environment variables.")

# Function to check user login credentials
def check_user(driver_id, password):
    with engine.connect() as conn:
        result = conn.execute(text(
            "SELECT * FROM users WHERE driver_id = :driver_id AND pass = :password"
        ), {"driver_id": driver_id, "password": password})
        user = result.fetchone()
        return user is not None  # True if user exists, else False

# Function to add a new user to the database
def add_user(name, age, driver_id, password, keyword):
    with engine.connect() as conn:
        conn.execute(text("""
            INSERT INTO users (user_name, age, driver_id, pass, keyword) 
            VALUES (:name, :age, :driver_id, :password, :keyword)
        """), {
            "name": name, 
            "age": age, 
            "driver_id": driver_id, 
            "password": password, 
            "keyword": keyword
        })
        conn.commit()
