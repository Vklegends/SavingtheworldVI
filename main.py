from flask import Flask, render_template, request
import random
import datetime
import pytz
import requests
import json
import requests
import redirect

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
#define some error responses 
errorres = [
    "I'm sorry I do not understand",
  "I did not quite understant that" ,
  "I'm not sure I know the answer to that"
]
# Set the timezone to Singapore
sgt = pytz.timezone('Asia/Singapore')

# Get the current time in Singapore
now = datetime.datetime.now(tz=sgt)

current_date = datetime.date.today()


# Define a list of 50 funny jokes
jokes = [
    "Why don't scientists trust atoms? Because they make up everything.",
    "Why did the tomato turn red? Because it saw the salad dressing.",
    "Why don't skeletons fight each other? They don't have the guts.",
    "Why did the math book look so sad? Because it had too many problems.",
    "Why did the scarecrow win an award? Because he was outstanding in his field.",
    "Why did the chicken cross the playground? To get to the other slide.",
    "Why did the hipster burn his tongue? Because he drank his coffee before it was cool.",
    "Why did the cookie go to the doctor? Because it was feeling crumbly.",
    "Why did the tomato blush? Because it saw the salad dressing.",
    "Why did the banana go to the doctor? Because it wasn't peeling well.",
    "Why did the golfer wear two pairs of pants? In case he got a hole in one.",
    "Why don't seagulls fly by the bay? Because then they'd be bagels.",
    "Why don't vampires go to barbecues? They don't like steak.",
    "Why did the coffee file a police report? It got mugged.",
    "Why did the teddy bear say no to dessert? Because it was stuffed.",
    "Why did the snail paint an 'S' on his car? So people would say, 'Look at that S-car go!'",
    "Why was the math book sad? Because it had too many problems.",
    "Why did the robber take a bath? Because he wanted to make a clean getaway.",
    "Why don't ants get sick? They have tiny ant-bodies.",
    "Why did the banana go out with the prune? Because it couldn't get a date.",
    "Why did the orange stop rolling down the hill? It ran out of juice.",
    "Why did the pencil decide to break up with the eraser? It said their relationship was pointless.",
    "Why do bicycles fall over? Because they're two-tired.",
    "Why did the birdie go to the doctor? It needed tweetment.",
    "Why did the frog call his insurance company? He had a jump in his car.",
    "Why don't oysters give to charity? Because they're shellfish.",
    "Why did the scarecrow win an award? Because he was outstanding in his field.",
    "Why did the computer go to the doctor? Because it had a virus.",
    "Why did the tomato turn red? Because it saw the salad dressing.",
    "Why don't scientists trust atoms? Because they make up everything.",
    "Why don't blind people skydive? Because it scares the dog.",
    "Why did the hipster burn his tongue? Because he drank his coffee before it was cool.",
    "Why did the man put his money in the freezer? He wanted cold hard cash!",
    "Why did the scarecrow win an award? Because he was outstanding in his field.",
    "Why did the tree go to the dentist? To get a root canal.",
    "Why did the hipster burn his tongue? Because he drank his coffee before it was cool.",
    "Why did the tomato turn red? Because it saw the salad dressing.",
    "Why did the old man fall in the well? Because he couldn't see that well.",
    "Why did the belt go to jail? Because it held up a pair of pants.",
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    message = request.form['message']

    # Check for greetings
    if any(word in message.lower() for word in ['hi', 'hello', 'hey']):
        response = random.choice(responses['greeting'])
    # Check for goodbyes
    elif any(word in message.lower() for word in ['goodbye', 'bye']):
        response = random.choice(responses['goodbye'])
    # Check for thanks
    elif any(word in message.lower() for word in ['thanks', 'thank you']):
      response = random.choice(responses['thanks'])

    #user interaction
    
    elif any(word in message.lower() for word in ['how are you', 'how are u']) :
      response = 'Im great how are you by the way'
      
      useremotion = message
      if any(word in message.lower() for word in ['good', 'great']):
        response ='thats great to hear'
             # message = input()
      elif 'bad' in useremotion or 'not good'in useremotion:
              response = 'Ohh thats sad to hear but I am here for you!'
              #message = input()
    #elif any(word in message.lower() for word in ['123456', 'ngyu']) :
     # return redirect(https://m.youtube.com/watch?v=6QCMGKUH6Ak)
      
    elif any(word in message.lower() for word in ['what is your name', 'name']) :
      response = "My name is Vi your personal Assistant."

    elif any(word in message.lower() for word in ['what time is it', 'time']) :
      response = "The current time in Singapore is:", sg_time_str
    elif any(word in message.lower() for word in ['what is the date', 'date']) :
      response = "The current date in Singapore is:", sg_time_str
    elif 'joke' in message:
      response = random.choice(jokes)
      return {'response': response}
    elif 'search' in message:
      try:
        response ='welcome to wikisearch eter your query'
          # Define the search ter
        return {'response': response}
        return {'message': message}
        search_term = message
        search_term = search_term.replace(" ", "_") 
        return {'search_term': message}
          # Define the URL for the API call
        url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{search_term}"

          # Make the API call
        response = requests.get(url)

          # Parse the response as JSON
        response = json.loads(response.text)
        data = json.loads(response.text)
          # Print the summary of the page
        response = data["extract"]
        x = 1 / 0
        return {'response': response}
     
  
      except Exception as e:
            # code to handle the exception
        print("An error occurred:", e, 'please be more specific')
        message = 'search'
        return {'message': message}
    
    elif "bye" in message or "goodbye" in message:
      response = "Goodbye!"  
          # Default response
    else:
      response = random.choice(errorres)

    return {'response': response}


    


app.run(host='0.0.0.0', port=81)
