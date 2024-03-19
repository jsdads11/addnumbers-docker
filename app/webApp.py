# app.py #

######## Importing Libraries ########
from flask import Flask
import requests
from flask_restful import Api

# Creating a Flask instance and passing that instance to the API
app = Flask(__name__)
api = Api(app)

@app.route('/total')
def ConsumeApi():
    # HTTP get request to fetch the response from the pas
    response = requests.get('http://localhost:8000/total') # doesn't work
    # response = requests.get('https://api.github.com')     # works

    print('--------------------------------------')
    print('****** response.content    ***********')
    print(response.content)         # Printing the content
    print('--------------------------------------')

    print('--------------------------------------')
    print('****** response.status_code **********')
    print(response.status_code)     # Printing the status code
    print('--------------------------------------')

    print('--------------------------------------')
    print('****** response.text        **********')
    print(response.text)           # Printing the response text
    print('--------------------------------------')
    return response.text

# Calling method to Hit the url and get response
ConsumeApi()

