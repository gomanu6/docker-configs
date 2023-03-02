import http.server
import socketserver
import os

print(os.environ.get('PORT'))
PORT = 8002

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()