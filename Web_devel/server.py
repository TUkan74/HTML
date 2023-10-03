	
#!/usr/bin/env python3
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs, urlparse

 
HOST = "localhost"
PORT = 8080
 
class MyServer(BaseHTTPRequestHandler):
    
    def do_GET(self):        
        url = "http://example.com/path?name=Ailish&age=19"
        # Parse the URL to get the query string
        parsed_url = urlparse(url)
        query_params = parse_qs(parsed_url.query)

        # Extract values from the query parameters
        name = query_params.get('name', [''])[0]
        age = query_params.get('age', [''])[0]



        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(bytes("<!doctype html><title>My Page</title> XXXXX", "utf-8"))
        self.wfile.write(bytes(f"<p>{name} is {age} years old.</p>" , "utf-8"))

if __name__ == "__main__":        
    server = HTTPServer((HOST, PORT), MyServer)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    server.server_close()