from http.server import BaseHTTPRequestHandler, HTTPServer
import json

HOST = "0.0.0.0"
PORT = 3000

USER_DATA = {"username": "Asfa"}

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/api":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()

            self.wfile.write(json.dumps(USER_DATA).encode("utf-8"))
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"Not Found")

print(f"Starting server at http://{HOST}:{PORT}")
httpd = HTTPServer((HOST, PORT), SimpleHandler)
httpd.serve_forever()
