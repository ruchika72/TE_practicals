import random
import string
import nltk
from nltk.chat.util import Chat, reflections

# Define pairs of patterns and responses
patterns = [
    (r'hello|hi|hey', ['Hello!', 'Hey there!', 'Hi!']),
    (r'how are you?', ["I'm doing well, thank you!", "I'm good, thanks!"]),
    (r'what can you do for me?', ["I can offer you a discount! Just tell me the total amount of your purchase."]),
    (r'bye|goodbye', ['Goodbye!', 'Have a great day!', 'Bye!']),
    (r'Thank you|Thx|thx|thank you', ['Welcome']),
    (r'Is there any other discount?',['Sorry! There are no other discounts.']),
    (r'On what categories the discounts are applied?',['Electronics, Accessories and many more']),
    (r'After what amount the discounts can be applied?',['It can be applied on any amount.']),
    (r'Till which date this discount is valid?',['Tomorrow']),
    (r'.*', ["I'm sorry, I didn't understand that.", "Could you please repeat that?"])
]

# Create a chatbot with the defined patterns
chatbot = Chat(patterns, reflections)

def generate_discount_code(length=8):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

def discount_chatbot():
    print("Welcome to our store! How can I assist you today?")
    while True:
        user_input = input().lower()

        # Check if the user input is a number (purchase cost)
        if user_input.isdigit():
            purchase_cost = float(user_input)
            discount_amount = purchase_cost * 0.10  # 10% discount
            discounted_total = purchase_cost - discount_amount
            print(f"With a 10% discount, your total amount is: ${discounted_total:.2f}")
            print(f"Your discount code is: {generate_discount_code()}")
            continue  # Skip the "I'm sorry" response

        response = chatbot.respond(user_input)
        print(response)

        if user_input.lower() in ['bye', 'goodbye', 'exit']:
            print("Thank you for visiting us. Have a great day!")
            break

if __name__ == "__main__":
    discount_chatbot()
