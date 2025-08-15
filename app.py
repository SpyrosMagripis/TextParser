from flask import Flask, request, render_template
from filter_lines import filter_lines_from_lines

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    results = None
    if request.method == 'POST':
        uploaded = request.files.get('file')
        keywords_raw = request.form.get('keywords', '')
        if uploaded and keywords_raw.strip():
            keywords = keywords_raw.split()
            # Read file content and filter lines
            text = uploaded.stream.read().decode('utf-8')
            lines = text.splitlines()
            results = filter_lines_from_lines(lines, keywords)
    return render_template('index.html', results=results)


if __name__ == '__main__':
    app.run(debug=True)
