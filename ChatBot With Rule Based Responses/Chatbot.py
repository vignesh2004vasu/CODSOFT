import random

rules = {
    
    "hello": ["Hello!", "Hi there!", "Greetings!"],
    "how are you": ["I'm just a bot.", "I'm doing fine, thanks."],
    "bye": ["Goodbye!", "See you later!", "Take care!"],
    "what's your name": ["I'm a chatbot.", "I don't have a name, but you can call me ChatGPT."],
    "tell me a joke": ["Why don't scientists trust atoms? Because they make up everything!", "What do you call a fish with no eyes? Fsh!"],
    "weather": ["I'm sorry, I don't have access to real-time weather information."],
    "help": ["How can I assist you today?", "I'm here to answer your questions."],
    "age": ["I'm just a computer program, so I don't have an age."],
    "thanks": ["You're welcome!", "Anytime!", "No problem!"],
    "what can you do": ["I can answer questions, tell jokes, and have basic conversations."],
    "where are you from": ["I exist in the digital realm, so you can find me online."],
    "favourite color": ["I don't have preferences; I'm just a text-based program."],
    "tell me a fact": ["Sure! Did you know that honey never spoils? Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still perfectly edible."],
    "laptop":["The top laptop brands are Acer,Dell,Asus,HP "],
    "mobile":["The top mobile brands are"]
}

print("Greeting,Hi i am ChatBot with Rule-Based Responses")
print("You can ask me questions and i will answer to it based one the rules set ")

def generate_response(user_input):
    user_tokens = user_input.lower().split()
    response = "I'm not sure how to respond to that."

    for key in rules:
        key_tokens = key.split()
        if all(token in user_tokens for token in key_tokens):
            response = random.choice(rules[key])
            break

    if "hello" in user_tokens or "hi" in user_tokens:
        response = random.choice(rules["hello"])

    if "fact" in user_tokens:
        response = random.choice(rules["tell me a fact"])

    if "color" in user_tokens:
        response = random.choice(rules["favourite color"])

    if "joke" in user_tokens:
        response = random.choice(rules["tell me a joke"])

    if "laptop" in user_tokens:
        response = random.choice(rules["laptop"])

    return response

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Chatbot: Goodbye!")
        break
    else:
        response = generate_response(user_input)
        print("Chatbot:", response)
