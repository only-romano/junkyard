from http.server import HTTPServer, CGIHTTPRequestHandler
from athlete import AthleteList
import glob


# Config
port = 8080
httpd = HTTPServer(('', port), CGIHTTPRequestHandler)
print(f"Starting simple_httpd on port {httpd.server_port}")
httpd.serve_forever()
