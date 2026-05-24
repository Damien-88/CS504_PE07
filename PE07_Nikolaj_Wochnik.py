import mysql.connector

# Get user input for login form
username = input("Enter your username: ")
password = input("Enter your password: ")

# Create SQL query to chekck user's login credentials
# query = "SELECT * FROM users WHERE username = '" + username + "' AND password = '" + password + "';"
query = "SELECT * FROM users WHERE username = %s AND password = %s;" # Use parameterized query to prevent SQL injection

# Connect to database and execute query
db = mysql.connector.connect(
    host = '127.0.0.1', port = 6603,
    user = 'root', password = 'root', 
    database = 'dbe'
)
cursor = db.cursor()
# cursor.execute(query)
cursor.execute(query, (username, password)) # Pass parameters as a tuple to the execute method

# Fetch results
# result = cursor.fetchone()
result = cursor.fetchall()

# Check if user exists and password is correct
if result:
    print("Login successful!")
    for r in result:
        print(r)
else:
    print("Invalid username or password.")

# Close database connection
db.close()