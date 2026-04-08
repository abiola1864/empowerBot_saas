from flask import Flask, send_from_directory
import os

app = Flask(__name__, static_folder='.')

# Serve index at root
@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

# Serve any .html file by name e.g. /pricing.html, /demo.html
@app.route('/<page>.html')
def page(page):
    filename = f'{page}.html'
    if os.path.exists(filename):
        return send_from_directory('.', filename)
    return send_from_directory('.', 'index.html'), 404

# Serve static assets (CSS, JS, images etc)
@app.route('/assets/<path:filename>')
def assets(filename):
    return send_from_directory('assets', filename)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)