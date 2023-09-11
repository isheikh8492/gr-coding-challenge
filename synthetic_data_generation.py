import json
import random
import string


# Function to generate a unique ID
def generate_unique_id(e_ids):
    while True:
        prefix = ''.join(random.choice(string.ascii_uppercase) for _ in range(3))
        number = random.randint(100, 999)
        u_id = f"{prefix}{number}"
        if u_id not in e_ids:
            e_ids.add(u_id)
            return u_id


existing_ids = set()
last_timestamp = 1700000000

new_data = []
for _ in range(100000):
    unique_id = generate_unique_id(existing_ids)

    increment = random.randint(1, 6000)

    start_time = last_timestamp + increment
    last_timestamp = start_time
    duration = random.randint(20, 100000)
    end_time = start_time + duration
    start_comments = "No issues" if random.random() < 0.7 else "Minor issues"
    end_comments = "" if random.random() < 0.7 else "Major issues"

    new_data.append({
        "type": "START",
        "id": unique_id,
        "timestamp": str(start_time),
        "comments": start_comments,
    })
    new_data.append({
        "type": "END",
        "id": unique_id,
        "timestamp": str(end_time),
        "comments": end_comments,
    })

# Save new data to a JSON file
with open("synthetic_output.txt", "w") as f:
    json.dump(new_data, f, indent=2)
