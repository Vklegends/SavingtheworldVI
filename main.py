from flask import Flask, render_template, request, redirect, make_response, url_for
import random
import datetime
import pytz
import requests
import json
import requests


app = Flask(__name__)

# Set the timezone to Singapore
sgt = pytz.timezone('Asia/Singapore')

# Get the current time in Singapore
now = datetime.datetime.now(tz=sgt)

# set the timezone to Singapore
sg_timezone = datetime.timezone(datetime.timedelta(hours=8))

# get the current time in Singapore
sg_time = datetime.datetime.now(sg_timezone)

# format the time string
sg_time_str = sg_time.strftime("%Y-%m-%d %H:%M:%S")

# Define some responses
responses = {
    'greeting': ['Hello!', 'Hi there!', 'Hey!', 'Hi!'],
    'goodbye': ['Goodbye!', 'See you later!', 'Take care!', 'Bye!'],
    'thanks': ['You\'re welcome!', 'No problem!', 'My pleasure!', 'Anytime!'],
    'name': ['My name is Assistant.', 'I\'m Assistant.', 'I\'m your personal assistant.'],
}
# pick up lines
pickupline = [
  "A life without you, would be like a computer without an OS",
  "Are you a computer keyboard? Because you’re my type.",
  "Are you a computer whiz… it seems you know how to turn my software to hardware?",
  "You are my semicolon; always present in everything I do.",
  "Baby, there is no part of my body that is Micro or Soft.",
  "You are my loop condition. I keep coming back to you"
  "I will make sure to provide a great user experience."
  "Your name must be WiFi because I am feeling a connection. "
  "Your beauty has been rivaling the graphics of Call of Duty. "
  "If I were an operating system, your process would be my top priority. "
]
#define some error responses 
errorres = [
    "I'm sorry I do not understand",
  "I did not quite understant that" ,
  "I'm not sure I know the answer to that",
  "I'm sorry I do not have the answer to that"
]
# Set the timezone to Singapore
sgt = pytz.timezone('Asia/Singapore')

# Get the current time in Singapore
now = datetime.datetime.now(tz=sgt)

current_date = datetime.date.today()
sad = [
  "I promise I’ll be here when you are ready to talk.",
  "You are important to me, and I love you. Even when things are hard, you are not alone.",
  "I can’t begin to understand what you are going through, but you are strong, and you can get through this.",
  "Remember that everything that happens to you will ultimately make you stronger. When you get through this, and I know you will, you’ll have gained strength and wisdom. It might not make much sense today, but it will later." ,
  "Just know you are important and even though I am a computer program I do care about you!"

]

# Define a list of 50 funny jokes
jokes = [
    "Why don't skeletons fight each other? They don't have the guts.",
    "Why did the cookie go to the doctor? Because it was feeling crumbly.",
    "Why did the golfer wear two pairs of pants? In case he got a hole in one.",
    "Why don't seagulls fly by the bay? Because then they'd be bagels.",
    "Why did the coffee file a police report? It got mugged.",
    "Why did the teddy bear say no to dessert? Because it was stuffed.",
    "Why was the math book sad? Because it had too many problems.",
    "Why did the robber take a bath? Because he wanted to make a clean getaway.",
  "Why did the orange stop rolling down the hill? It ran out of juice.",
    "Why did the pencil decide to break up with the eraser? It said their relationship was pointless.",
    "Why do bicycles fall over? Because they're two-tired.",
    "Why did the birdie go to the doctor? It needed tweetment.",
    "Why don't oysters give to charity? Because they're shellfish.",
    "Why did the computer go to the doctor? Because it had a virus.",
    "Why did the tomato turn red? Because it saw the salad dressing.",
    "Why don't scientists trust atoms? Because they make up everything.",
    "Why don't blind people skydive? Because it scares the dog.",
    "Why did the man put his money in the freezer? He wanted cold hard cash!",
    "Why did the scarecrow win an award? Because he was outstanding in his field.",
    "Why did the tree go to the dentist? To get a root canal.",
    "Why did the old man fall in the well? Because he couldn't see that well.",
    "Why did the belt go to jail? Because it held up a pair of pants.",
]

@app.route('/')
def index():
  return render_template('index.html')
  if request.method == 'POST':
        message = request.form['message']
        print("User input:", message)  # Print user input before response
        return "You entered: " + message
  else:
    return '''
            <form method="post">
                <input type="text" name="user_input">
                <input type="submit" value="Submit">
            </form>
            '''

def check(inputs,userinput):
  for i in inputs:
    if i in userinput.lower():
      return True

  return False

@app.route('/ask', methods=['POST'])
def ask():
    message = request.form['message']
#check(['', ''], message):
    # Check for greetings
    if check(['hi', 'hello', 'hey'], message):
      response = random.choice(responses['greeting'])
    
    # Check for thanks
    elif check(['thanks', 'thank you',], message):
      response = random.choice(responses['thanks'])

    #user interaction
    
    elif check(['how are you', 'how r you'], message):
      response = 'Im great how are you by the way'      
    elif check(['I' and'good','I' and 'great'], message):
        response = 'thats great to hear!'
             # message = input()
    elif check(['bored','tired'], message):
      response = 'Ohh thats sad to hear but I am here for you!,type in jokes and ill tell you one if that can make you feel better!'
              #message = input()
    elif check(['name', 'what is your name'], message):
      response = "My name is Vi your personal Assistant."
    elif check(['depressed','I' and 'sad','I' and 'lonely', 'I' and 'unhappy' ], message):
      response = random.choice(sad) + 'if you want to feel better try type J O V A N'
    elif any(word in message.lower() for word in ['what time is it', 'time']) :
      response = "The current time in Singapore is:", sg_time_str
    elif any(word in message.lower() for word in ['what is the date', 'date']) :
      response = "The current date in Singapore is:", sg_time_str
    elif any(word in message.lower() for word in ['tell me a joke', 'joke']) :
      response = random.choice(jokes)
    elif check(['suicide','I' and 'kill','I' and 'die'], message):
      response = 'are you okay?, Please, Please contact 1767. Do know you are not alone and nothing is the end.'
    elif check(['pick up line','pick-up line', 'pul' ], message):
      response = random.choice(pickupline)
    elif check(['goodbye', 'bye',], message):
      response = random.choice(responses['goodbye'])

    else:
      response = random.choice(errorres)

    return {'response': response}


    


app.run(host='0.0.0.0', port=81)



#code dump
'''document.addEventListener('keyup', function(e) {
    keySequence.push(e.key);
    keySequence.splice(
        -konamiCode1.length - 1, 
        keySequence.length - konamiCode1.length
    );
    konamiString1 = konamiCode1.join('');

    if (keySequence.join('').includes(konamiString1)) {
       setTimeout(function() {
          window.open('https://www.sos.org.sg/');
       }, );
    }'''