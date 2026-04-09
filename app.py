from flask import Flask, send_from_directory, abort
import os

app = Flask(__name__)
ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route('/')
def index():
    return send_from_directory(ROOT, 'index.html')

@app.route('/<string:page>.html')
def html_page(page):
    filepath = os.path.join(ROOT, f'{page}.html')
    if os.path.isfile(filepath):
        return send_from_directory(ROOT, f'{page}.html')
    return send_from_directory(ROOT, 'index.html'), 404

# Serve from /public/ folder
@app.route('/public/<path:filename>')
def public_files(filename):
    pub = os.path.join(ROOT, 'public')
    fp = os.path.join(pub, filename)
    if os.path.isfile(fp):
        return send_from_directory(pub, filename)
    abort(404)

# Serve from /assets/ folder (legacy path)
@app.route('/assets/<path:filename>')
def assets_files(filename):
    assets = os.path.join(ROOT, 'assets')
    fp = os.path.join(assets, filename)
    if os.path.isfile(fp):
        return send_from_directory(assets, filename)
    abort(404)

# Fallback for any other static file
@app.route('/<path:filename>')
def static_files(filename):
    filepath = os.path.join(ROOT, filename)
    if os.path.isfile(filepath):
        return send_from_directory(ROOT, filename)
    abort(404)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)