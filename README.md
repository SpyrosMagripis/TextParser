# TextParser

This repository contains a simple Python utility for filtering lines in a text file based on multiple keywords.

## Usage

```
python filter_lines.py input.txt output.txt keyword1 keyword2 ...
```

The script writes lines that contain **all** provided keywords to the output file, prefixed with their original line numbers.

## Web App

A minimal Flask application is included for interactive use.

```
pip install -r requirements.txt
python app.py
```

Open your browser to `http://localhost:5000`, upload a text file and provide space-separated keywords. Matching lines with their line numbers will be displayed on the page.
