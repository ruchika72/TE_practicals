import random

# Define responses based on user input
responses = {
    "hi": ["Hello!", "Hi there!", "Hey!"],
    "how are you": ["I'm good, thank you!", "Feeling great!", "Pretty good!"],
    "bye": ["Goodbye!", "See you later!", "Bye! Have a nice day!"],
    "what's your name": ["I'm a chatbot!", "You can call me ChatBot.", "I don't have a name, I'm just a bot."],
    "who created you": ["I was created by a programmer.", "I'm a creation of human intelligence.", "My creator is someone smart!"],
    "what is the weather today": ["I'm sorry, I don't have access to weather information.", "You can check a weather website or app for that information."],
    "tell me a joke": ["Why was the math book sad? Because it had too many problems!", "Why don't skeletons fight each other? They don't have the guts!", "I'm not very good at telling jokes, but here's one: Why did the scarecrow win an award? Because he was outstanding in his field!"],
    "thank you": ["You're welcome!", "No problem!", "Glad I could help!"],
    "default": ["I'm not sure I understand.", "Could you please rephrase that?", "Sorry, I didn't get that."]
}

# Function to generate response
def respond(message):
    message = message.lower()  # Convert message to lowercase
    response = responses.get(message, responses["default"])  # Get response from dictionary
    return random.choice(response)  # Return a random response from the list

# Main function to interact with the user
def main():
    print("Chatbot: Hello! How can I assist you today? (Type 'bye' to exit)")
    while True:
        user_input = input("User: ")
        if user_input.lower() == "bye":
            print("Chatbot: Goodbye!")
            break
        else:
            print("Chatbot:", respond(user_input))

if __name__ == "__main__":
    main()
