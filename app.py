## Basic Flask application 

from flask import Flask 
import os 
app = Flask(__name__)

@app.route('/', methods = ['GET'])

def home():
    return("Hello! Welcome to the Web Page of G23AI2126")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port = 5000)

## host = "0.0.0.0" can access local ip address as well as host address. 