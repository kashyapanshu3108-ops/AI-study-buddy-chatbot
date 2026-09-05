# AI STUDY BUDDY CHATBOT
print("HELLLO! WELCOME TO THE CHATBOT")
print("You can ask me basic questions, type 'bye' to exit from the bot.")

# chatbot memory creation [dictionary of responses]
responses = {
     "hello": "hi, welcome. how can i help you?",
     "how are you": "i am very fine. thank you", # Removed the extra space after 'you'
     "who are you": "i am a smart chatbot",
     "motivate me": "keep going. every bug in your project makes you a better developer",
     "happy": "happy to hear that",
     "meaning of love":"The true meaning of love is to feel a sense of joy when we see our partner happy. When we see that they are sad or depressed, we feel their blue mood, too. With love comes empathy for the other person’s emotional state. 3. Love means compromise",
}

# method to get response of chatbot  
def getresponseofbot(userquestion):
   userquestion = userquestion.lower()
   for eachkey in responses:
      if eachkey in userquestion:
         return responses[eachkey]

   return "i am not able to tell that yet"

# Take user input
while True:
    userinput = input("please ask your question: ")
    
    # Check for exit condition first
    if "bye" in userinput.lower():
        print("Chatbot: Bye! Take care.")
        break
        
    reply = getresponseofbot(userinput)
    
    # MISSING LINE: Print the bot's reply!
    print("Chatbot:", reply)