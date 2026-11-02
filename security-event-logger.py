# Task 2 - Security Event Logger

# Step 1 - Import datetime to record the date and time of login attempts
from datetime import datetime

# Step 2 - Store the correct username and password
correct_username = "admin"
correct_password = "password123"

# Step 3 - Create an empty list to store login attempts
security_events = []

# Step 4 - Create a counter to give each login attempt a unique event ID
event_id = 1

# Step 5 - Keep asking for login details until authentication succeeds
while True:
    # Step 6 - Ask the user to enter their login details
    username = input("Enter username: ")
    password = input("Enter password: ")
    # Step 7 - Check if the username and password are correct
    if username == correct_username and password == correct_password:
        event_type = "Successful Login"
    else:
        event_type = "Failed Login"
    # Step 8 - Record the date and time of the login attempt
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # Step 9 - Create a dictionary to store the login event details
    event = {
            "event_id": event_id,
            "username": username,
            "ip_address": "192.168.1.10",
            "event_type": event_type,
            "timestamp": timestamp
        }
    # Step 10 - Add the login event to the security events list
    security_events.append(event) 
    # Step 11 - Increase the event ID for the next login attempt
    event_id += 1
    # Step 12 - Display the login event details
    print("\nSecurity Event Log")
    print("Event ID:", event["event_id"])
    print("Username:", event["username"])
    print("IP Address:", event["ip_address"])
    print("Event:", event["event_type"])
    print("Timestamp:", event["timestamp"])
    # Step 13 - Stop the loop when login is successful
    if event_type == "Successful Login":
	    break