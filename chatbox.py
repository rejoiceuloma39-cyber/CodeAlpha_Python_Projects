print("🤖 Welcome to Rejoice's Chatbot!")
print("Type 'bye' to exit.")

while True:
    user = input("You: ").lower()

    if user == "hello":
        print("Rex: Hi!")

    elif user == "how are you":
        print("Rex: I'm fine, thanks! How are you doing?")
        
    elif user == "i'm doing good, thank you":
        print("Rex: you are welcome.")
        
    elif user == "what is your name":
        print("Rex: My name is Rejoice")

    elif user == "thank you":
        print("Rex: You're welcome! 😊")

    elif user == "bye":
        print("Rex: Goodbye! 👋")
        break

    else:
        print("Rex: Sorry, I don't understand that.")	