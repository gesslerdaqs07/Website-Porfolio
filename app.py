from flask import Flask, render_template
from waitress import serve 

app = Flask(__name__)

@app.route('/')
def home():
    # This looks inside the 'templates' folder for index.html
    return render_template('index.html')

if __name__ == '__main__':
    print("Starting production server on http://localhost:8080...")
    serve(app, host='0.0.0.0', port=8080)
