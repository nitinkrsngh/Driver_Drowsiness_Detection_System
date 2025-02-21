import mysql.connector
from mysql.connector import Error

def connect_to_db():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='drowsiness_db',
            user='root',
            password='Nitin@5375'
        )
        if connection.is_connected():
            print("Connected to the database")
            return connection
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None

def insert_log(connection, user_id, drowsy_state, alert_triggered):
    cursor = connection.cursor()
    query = """
    INSERT INTO drowsiness_logs (user_id, drowsy_state, alert_triggered)
    VALUES (%s, %s, %s);
    """
    values = (user_id, drowsy_state, alert_triggered)
    cursor.execute(query, values)
    connection.commit()
    print("Log inserted successfully!")
connection = connect_to_db()
insert_log(connection, user_id=1, drowsy_state=True, alert_triggered=True)

def fetch_logs(connection):
    cursor = connection.cursor(dictionary=True)
    query = "SELECT * FROM drowsiness_logs ORDER BY timestamp DESC;"
    cursor.execute(query)
    logs = cursor.fetchall()
    for log in logs:
        print(log)

if connection.is_connected():
    connection.close()
    print("Database connection closed")

