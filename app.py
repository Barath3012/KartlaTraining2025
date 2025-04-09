from flask import Flask, render_template, request
import random

app = Flask(__name__)

# Some fun moods to randomly choose from
moods = [
    "Energetic ⚡", "Chill 😌", "Focused 🎯", "Sleepy 😴", 
    "Joyful 😄", "Creative 🎨", "Mysterious 🕵️", "Hungry 🍕", "Adventurous 🧭"
]

@app.route('/')
def home():
    return '''
        <h1>Welcome to the Mood Predictor 🌈</h1>
        <form action="/predict" method="post">
            Enter your name: <input type="text" name="username" required>
            <input type="submit" value="Predict Mood">
        </form>
    '''

@app.route('/predict', methods=['POST'])
def predict():
    username = request.form['username']
    predicted_mood = random.choice(moods)
    return f'''
        <h1>Hi, {username}!</h1>
        <h2>Your mood for today is: <span style="color:green">{predicted_mood}</span></h2>
        <a href="/">Try again</a>
    '''

if __name__ == '__main__':
    app.run(debug=True)
