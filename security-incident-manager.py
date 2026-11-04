# Task 4 - Security Incident Manager
# Step 1 - Create a dictionary to store security incident details

incident = {
	"username": "admin",
	"ip_address": "192.168.1.10",
	"event_type": "Failed Login",
	"risk_level": "High"
}

# Step 2 - Display the username and IP address
print("Username:", incident["username"])
print("IP Address:", incident["ip_address"])

# Step 3 - Add a status field to the security incident
incident["status"] = "Open"

# Step 4 - Update the risk level of the security incident
incident["risk_level"] = "Medium"

# Step 5 - Remove the event type from the security incident
del incident["event_type"]

# Step 6 - Display all keys and values in the dictionary
for key, value in incident.items():
	print(key, ":", value)

# Step 7 - Display the total number of entries in the dictionary
print("Total number of entries:", len(incident))

