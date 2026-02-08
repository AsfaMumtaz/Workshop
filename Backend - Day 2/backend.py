from http.server import BaseHTTPRequestHandler, HTTPServer
import json

HOST = "0.0.0.0"
PORT = 3000

# Example username
USER_DATA = {"username": "Asfa"}

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Only respond to root path
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            # Allow CORS so frontend can fetch from another port
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()

            # Send JSON response
            self.wfile.write(json.dumps(USER_DATA).encode("utf-8"))
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"Not Found")

# Start server
print(f"Starting server at http://{HOST}:{PORT}")
httpd = HTTPServer((HOST, PORT), SimpleHandler)
httpd.serve_forever()
