def chatbot():
    while True:
        user_input = input("You: ")
        
        if user_input.lower() == "exit":
            print("Bot: Goodbye!")
            break
        
        if "ai" in user_input.lower():
            print("Bot: AI stands for Artificial Intelligence.")
        elif "hello" in user_input.lower():
            print("Bot: Hello! How can I help you?")
        else:
            print("Bot: I'm a simple chatbot. I can answer basic questions.")

chatbot()
