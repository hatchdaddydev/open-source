from asyncio import sleep

import requests

# Initialize page number
page = 1

while True:
    # Make a GET request to the URL
    response = requests.get(f"https://server.jpgstoreapis.com/policy/verified?page={page}")

    if response.status_code == 429:
        print(f"Rate limited at page: {page}")
        sleep(5)
        continue

    # Check if the request was successful
    if response.status_code != 200:
        print(f"Failed to fetch data for page: {page}")
        break

    # Load the data from the response
    data = response.json()

    # If data is empty, break the loop
    if not data:
        break

    # Process the data (placeholder for your data processing code)
    # loop through the data and save the policy id to a file
    for item in data:
        policy_id = item['policy_id']
        with open('responses/policy_ids.txt', 'a') as f:
            f.write(f"{policy_id}\n")

    # Increment the page number
    page += 1
