import os
import openai
import json
import time

openai.api_type = "azure"
openai.api_base = "https://yguo262.openai.azure.com/"
openai.api_version = "2024-02-01"
openai.api_key = "c4019382c2d447b3beccf75ce0ddf76d"

system_message = {
    "role": "system",
    "content": "Are there any texts where demographic data appears? Only when specific data is mentioned it should be extracted. No need to infer from text. Demographic data includes: Age, sex, Race, Ethnicity, Religion, Gender, Sexual orientation, Socioeconomic status (SES), Immigration Status, Housing, Addiction, Cigarette smoking, Mental Health, Suicidal. If yes, please answer the specific location of the sentence (which line), which demographic it belongs to, and the specific text of the sentence. If not, please only answer 'no'."
}

file_path = '/Users/yaoge/Downloads/Immunology/Solid_Tumors.txt'

# Read the entire file into a list of lines
with open(file_path, 'r', encoding='utf-8') as file:
    lines = file.readlines()

# Define the batch size
batch_size = 10

# Process the file in batches
for i in range(0, len(lines), batch_size):
    batch_lines = lines[i:i+batch_size]

    # Skip empty batches
    if not batch_lines:
        continue
    
    # Join the lines into a single message content
    batch_content = ' '.join(line.strip() for line in batch_lines if line.strip())
    user_message = {"role": "user", "content": batch_content}
    
    # Construct messages for the current batch
    messages = [system_message, user_message]

    try:
        # Make the API call
        completion = openai.ChatCompletion.create(
            engine="app0212",
            messages=messages,
            temperature=0.2,
            max_tokens=4096,
            top_p=0.1,
            frequency_penalty=0,
            presence_penalty=0,
            stop=None
        )

        # Write the response to the output file
        with open('/Users/yaoge/Downloads/test_preds_Immunology_Solid_Tumors.txt', 'a', encoding='utf-8') as wf:
            print(user_message)
            wf.write(completion['choices'][0]['message']['content'] + "\n\n")

    except openai.error.RateLimitError:
        print("Rate limit exceeded. Waiting for 120 seconds...")
        time.sleep(120)
        continue

    # Add a delay to avoid rate limits
    time.sleep(50)
