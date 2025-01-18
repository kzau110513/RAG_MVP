import psycopg2

def get_connection():
    try:
        # Connection parameters
        host = "localhost"
        port = "5432"
        dbname = "postgres"  # Default database name
        user = "postgres"
        password = "mysecretpassword"  # Replace with your actual password

        # Establishing the connection
        connection = psycopg2.connect(
            host=host,
            port=port,
            dbname=dbname,
            user=user,
            password=password
        )
        return connection
    except Exception as error:
        print("Error while connecting to PostgreSQL:", error)
        return None
