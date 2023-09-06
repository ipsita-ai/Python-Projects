from flask import Flask, render_template, request,redirect,session

import api
from db import Database

app = Flask(__name__)
dbo = Database()

@app.route('/')
def index():
    return render_template('Login.html')
@app.route('/register')
def register():
    return render_template('Register.html')

@app.route('/perform_registration', methods= ['post'])
def perform_registration():
    name = request.form.get('user_name')
    email = request.form.get('user_email')
    password = request.form.get('user_password')

    response = dbo.insert(name,email,password)
    if response ==1 :
        return render_template('Login.html',message='Registration Successful.Please proceed to login.')
    else:
        return render_template('Register.html',message = 'Email already exists')
@app.route('/perform_login',methods=['post'])
def perform_login():
    email = request.form.get('user_email')
    password = request.form.get('user_password')
    response = dbo.search(email,password)
    if response:
        return redirect('/profile')
    else:
        return render_template('Login.html',message1 = 'Incorrect Credentials')

@app.route('/profile')
def profile():
    return render_template('Profile.html')

@app.route('/ner')
def ner():
    return render_template('NER.html')

@app.route('/perform_ner',methods = ['post'])
def perform_ner():
        text = request.form.get('ner_text')
        response = api.ner(text)
        print(response)
        return render_template('ner.html',response=response)

@app.route('/SentimentAnalysis')
def sentimentanalysis():
    return render_template('SentimentAnalysis.html')

@app.route('/perform_sentiment',methods = ['post'])
def perform_sentiment():
    text = request.form.get('sentiment_text')
    response = api.sentianalysis(text)
    print(response)
    return render_template('SentimentAnalysis.html',response= response)
@app.route('/EmotionAnalysis')
def emotionanalysis():
    return render_template('EmotionAnalysis.html')

@app.route('/perform_emotion',methods = ['post'])
def perform_emotion():
    text = request.form.get('emotion_text')
    response = api.emotionanalysis(text)
    print(response)
    return render_template('EmotionAnalysis.html', response=response)
app.run(debug=True)