import json

# Load the original JSON data
input_file = 'C://Users//Jayashrinidhi V//OneDrive//Documents//VScode//Justice_bot//doj_full_scrape.json'
output_file = 'C://Users//Jayashrinidhi V//OneDrive//Documents//VScode//Justice_bot//converted_data.json'

# Load the data
with open(input_file, 'r') as file:
    data = json.load(file)

# Initialize the new dataset structure
intents = []

# Process each item in the original data
for item in data:
    page_content = item.get('page_content', '').strip()
    if page_content:
        # Define the tag based on content or other criteria
        tag = 'Department of Justice'  # Update this based on your actual needs or derive it dynamically
        response = "Here is the information about the Department of Justice..."  # Customize your response

        # Add to intents list
        intents.append({
            'tag': tag,
            'patterns': [response],
            'responses': [page_content]
        })

# Write the new dataset to a JSON file
with open(output_file, 'w') as file:
    json.dump({'intents': intents}, file, indent=4)

print(f"Data has been converted and saved to {output_file}")
