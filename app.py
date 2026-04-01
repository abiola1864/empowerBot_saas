from flask import Flask, send_from_directory
import os

app = Flask(__name__, static_folder='.')

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/public/<path:filename>')
def public(filename):
    return send_from_directory('public', filename)

if __name__ == '__main__':
    app.run()