"#app" 
from flask import Flask

app = Flask(__name__)

@app.router("/")
def home():
    return "api funcionando"

app.run(debug=True)

