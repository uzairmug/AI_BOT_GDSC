# Import Required Pakages
import os
import google.generativeai as genai

# Send our API Key to google for authentication
GOOGLE_API_KEY = "AIzaSyDcx80pzVdDVBFrjDWqRord4Ru7aArAA84"
genai.configure(api_key=GOOGLE_API_KEY)

# Commented out, normally used to get a list of available models
"""for m in genai.list_models():
  if 'generateContent' in m.supported_generation_methods:
    print(m.name)"""

# Creates a chat using a gemini model, in this case the latest version of the 1.5-flash-8b model
model = genai.GenerativeModel('gemini-1.5-flash-8b-latest')
chat = model.start_chat(history=[])

# Main loop used to allow the user to communicate with the AI
print()
while True:
    prompt = input("Ask me anything: ").strip()                     # Remove leading/trailing spaces
    # "exit" is used to exit out of the chat
    if prompt.lower() == "exit":
        break
    # Only send a response if the prompt is not empty
    if prompt:
        response = chat.send_message(prompt, stream=True)
        # Print the response from the AI
        for chunk in response:
            if chunk.text:
                print(chunk.text)