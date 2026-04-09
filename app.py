from flask import Flask, send_from_directory, abort
import os

app = Flask(__name__)

# Root directory of the project
ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route('/')
def index():
    return send_from_directory(ROOT, 'index.html')

# Serve named HTML pages: /about.html, /pricing.html etc
@app.route('/<string:page>.html')
def html_page(page):
    filepath = os.path.join(ROOT, f'{page}.html')
    if os.path.isfile(filepath):
        return send_from_directory(ROOT, f'{page}.html')
    return send_from_directory(ROOT, 'index.html'), 404

# Serve files from /public/ folder (logos, images)
@app.route('/public/<path:filename>')
def public_files(filename):
    public_dir = os.path.join(ROOT, 'public')
    return send_from_directory(public_dir, filename)

# Serve any other static file (css, js, etc) from root
@app.route('/<path:filename>')
def static_files(filename):
    filepath = os.path.join(ROOT, filename)
    if os.path.isfile(filepath):
        return send_from_directory(ROOT, filename)
    abort(404)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)