import http
from logging import Handler
import socketserver

PUERTO = 9515
Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PUERTO), Handler) as httpd:
    print("[!] > Server Abierto en el puerto:", PUERTO)
    httpd.serve_forever()
