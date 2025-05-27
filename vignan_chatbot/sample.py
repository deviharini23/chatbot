import google.generativeai as genai
import os

# Configure the API key
GOOGLE_API_KEY = "AIzaSyCcFfnOM5qndAZO3OM8VN-KT5zFqmtpPmI"  # Replace with your actual API key
genai.configure(api_key=GOOGLE_API_KEY)

# Initialize the model (using the correct model name)
model = genai.GenerativeModel('gemini-2.0-flash')

def chat_with_bot():
    # Start a new chat
    chat = model.start_chat(history=[])
    
    print("Chatbot: Hello! I'm your AI assistant. Type 'quit' to exit.")
    
    while True:
        # Get user input
        user_input = input("You: ").strip()
        
        # Check for quit command
        if user_input.lower() == 'quit':
            print("Chatbot: Goodbye!")
            break
        
        try:
            # Get response from the model
            response = chat.send_message(user_input)
            print("Chatbot:", response.text)
        except Exception as e:
            print("An error occurred:", str(e))

if __name__ == "__main__":
    chat_with_bot()