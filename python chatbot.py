def chatbot():
    print("🤖 Chatbot: Hello! I am your chatbot. Type 'bye' to end the chat.\n")

    while True:
        user_input = input("👤 You: ").lower().strip()

        if user_input == "hello":
            print("🤖 Chatbot: Hi there!")
        elif user_input == "how are you?":
            print("🤖 Chatbot: I'm fine, thanks! How about you?")
        elif user_input in ["hi", "hey"]:
            print("🤖 Chatbot: Hello! What can I help you with?")
        elif user_input == "what is your name?":
            print("🤖 Chatbot: I’m CodeAlpha Chatbot!")
        elif user_input == "bye":
            print("🤖 Chatbot: Goodbye! Have a great day 😊")
            break
        else:
            print("🤖 Chatbot: Sorry, I didn’t understand that.")