from openai import OpenAI

client = OpenAI(api_key="YOUR_API_KEY")

def chatbot():
    while True:
        user_input = input("You: ")
        
        if user_input.lower() == "exit":
            print("Bot: Goodbye!")
            break
        
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "user", "content": user_input}
            ]
        )
        
        print("Bot:", response.choices[0].message.content)

chatbot()
