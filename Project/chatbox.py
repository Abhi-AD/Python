import random
import re

patterns_responses = {
    r"(?i)hello|hi|hey": ["Hello!", "Hi there!", "Hey!", "Hi! How can I help you?", "Hello! How can I assist you?"],
    r"(?i)how are you|how's it going": ["I'm doing well, thank you!", "I'm fine, thank you for asking!", "All good, thanks!", "I'm just a chatbot. But thanks for asking!"],
    r"(?i)what is your name|who are you": ["I'm a simple chatbot. You can call me Chatbot.", "I am a Chatbot.", "I'm just a chatbot!", "You can call me ChatBot.", "I'm a simple chatbot."],
    r"(?i)what's your favorite color|favorite colour": ["I don't have preferences as I am a machine."],
    r"(?i)bye|goodbye|see you|take care": ["Goodbye! Have a great day!", "Goodbye!", "See you later!", "Have a great day!"],
    r"(?i)help": ["Sure! I'm here to help. How can I assist you?"],
    r"(?i)what is the weather today": ["I'm sorry, I don't have access to real-time data."],
    r"(?i)what time is it": ["I don't have access to your system's time. You can check your device clock."],
    r"(?i)what is your purpose|why were you created": ["I'm here to provide information and assist you with any questions you may have.", "My purpose is to help users with their inquiries.", "I was created to be a helpful chatbot."],
    r"(?i)tell me a joke": ["Why don't scientists trust atoms? Because they make up everything!", "Did you hear about the mathematician who’s afraid of negative numbers? He’ll stop at nothing to avoid them!"],
    r"(?i)what is the meaning of life": ["The meaning of life is a philosophical question. Many believe it's to find purpose and happiness.", "The meaning of life can vary for each individual. It's a complex and profound topic."],
    r"(?i)who is your creator|who made you": ["I was created by a team of developers at OpenAI.", "My creators are the engineers and developers at OpenAI."],
    r"(?i)what is the capital of (.*?)": ["The capital of {} is {}.", "It's {}.", "The capital city is {}."],
    r"(?i)how can I contact support|customer service": ["You can contact support through our website or call our helpline at 1-800-XXX-XXXX."],
    r"(?i)what is your favorite book": ["As a chatbot, I don't have preferences or personal favorites."],
    r"(?i)how do I reset my password": ["To reset your password, go to the login page and click on the 'Forgot Password' link. Follow the instructions to reset it."],
    r"(?i)what are the system requirements": ["The system requirements vary depending on the software or application you are using. Please check the official documentation for specific details."],
    r"(?i)where are you located": ["As an AI chatbot, I don't have a physical location. I exist in the digital world!"],
    r"(?i)what languages do you speak": ["I primarily speak English, but I can understand and respond to other languages as well."],
   r"(?i)do you have any siblings": ["As an AI chatbot, I don't have siblings or family. I'm a standalone program."],
}

def chatbot_response(user_input):
    for pattern, responses in patterns_responses.items():
        if re.search(pattern, user_input):
            return random.choice(responses).format(*re.findall(pattern, user_input)[0])
    return "I'm sorry, I don't understand. Can you please rephrase your question?"

def main():
    print("Chatbot: Hello! I'm here to chat with you. Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit', 'bye', 'goodbye','sorry','leave']:
            print("Thank you your are using this chatbox")
            break
        response = chatbot_response(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    main()


def chatbot_response(user_input):
    for pattern, responses in patterns_responses.items():
        if re.search(pattern, user_input):
            return random.choice(responses)
    return "I'm sorry, I don't understand. Can you please rephrase your question?"

def main():
    print("Chatbot: Hello! I'm here to chat with you. Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit', 'bye', 'goodbye','leave', 'sorry']:
            print("Chatbot: Goodbye! Have a great day!")
            break
        response = chatbot_response(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    main()
