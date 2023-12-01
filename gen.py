import json
import random

# Function to generate random patterns
def generate_patterns():
    patterns = []
    for _ in range(random.randint(1, 5)):
        patterns.append(" ".join([word.capitalize() for word in ["how", "can", "i", "help", "you"]]))
    return patterns

# Function to generate a large JSON
def generate_large_json():
    intents = []

    for tag in ["greeting", "about_us", "products", "delivery", "contact", "order", "thanks"]:
        intent = {
            "tag": tag,
            "patterns": generate_patterns(),
            "responses": [
                f"This is a response for {tag}.",
                f"Thank you for asking about {tag}.",
                f"We are happy to help with {tag}."
            ]
        }
        intents.append(intent)

    large_json = {"intents": intents}
    return json.dumps(large_json, indent=2)

# Generate a large JSON
large_json_content = generate_large_json()

# Save the JSON to a file
with open("large_json_example.json", "w") as json_file:
    json_file.write(large_json_content)

print("Large JSON file generated and saved as 'large_json_example.json'.")
