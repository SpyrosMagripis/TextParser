from http.server import BaseHTTPRequestHandler, HTTPServer
import html
import cgi
from filter_lines import filter_lines_from_lines

FORM_PAGE = b"""<!doctype html>\n<html lang='en'>\n<head><meta charset='utf-8'><title>Text Parser</title></head>\n<body>\n  <h1>Text Parser</h1>\n  <form method='post' enctype='multipart/form-data'>\n    <label>Text file: <input type='file' name='file' required></label><br>\n    <label>Keywords (space-separated): <input type='text' name='keywords' required></label><br>\n    <button type='submit'>Parse</button>\n  </form>\n</body>\n</html>"""

class UploadHandler(BaseHTTPRequestHandler):
    def do_GET(self) -> None:
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(FORM_PAGE)

    def do_POST(self) -> None:
        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={
                "REQUEST_METHOD": "POST",
                "CONTENT_TYPE": self.headers.get("Content-Type"),
                "CONTENT_LENGTH": self.headers.get("Content-Length"),
            },
        )
        file_item = form["file"] if "file" in form else None
        keywords_raw = form.getvalue("keywords", "")
        if not file_item or not keywords_raw.strip():
            self.send_error(400, "File and keywords are required")
            return
        text = file_item.file.read().decode("utf-8")
        keywords = keywords_raw.split()
        lines = text.splitlines()
        results = filter_lines_from_lines(lines, keywords)
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(b"<!doctype html><html lang='en'><head><meta charset='utf-8'><title>Results</title></head><body>")
        self.wfile.write(b"<h1>Matches</h1><pre>")
        for line in results:
            self.wfile.write(html.escape(line).encode("utf-8") + b"\n")
        self.wfile.write(b"</pre></body></html>")


def run(host: str = "", port: int = 8000) -> None:
    server = HTTPServer((host, port), UploadHandler)
    print(f"Serving on http://{host or 'localhost'}:{port}")
    server.serve_forever()


if __name__ == "__main__":
    run()
