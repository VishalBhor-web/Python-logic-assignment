import json

# Step 1: Store JSON formatted API response as a string
api_response = '''
{
  "id": "req_123",
  "status": "success",
  "result": {
    "text": "Hello world",
    "confidence": 0.98
  }
}
'''

# Step 2: Parse JSON string into Python dictionary
data = json.loads(api_response)

# Step 3: Extract required values
request_id = data["id"]
status = data["status"]
text_result = data["result"]["text"]
confidence_score = data["result"]["confidence"]

# Step 4: Print extracted values
print("Request ID:", request_id)
print("Status:", status)
print("Text Result:", text_result)
print("Confidence Score:", confidence_score)

# Step 5: Check confidence score
if confidence_score < 0.9:
    print("Warning: Confidence score is below 0.9")

# Step 6: Create new dictionary for follow-up result
follow_up_result = {
    "id": request_id,
    "status": "processed",
    "message": "Result processed successfully",
    "original_confidence": confidence_score
}

# Step 7: Convert dictionary to JSON string
json_output = json.dumps(follow_up_result, indent=4)

# Step 8: Write JSON output to file
with open("response.json", "w") as file:
    file.write(json_output)

print("Follow-up response saved to response.json")
