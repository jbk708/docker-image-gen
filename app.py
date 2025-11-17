#!/usr/bin/env python3
"""
Simple demo application for Docker image generation.
"""

from http.server import HTTPServer, BaseHTTPRequestHandler
import os
import json
from datetime import datetime

class DemoHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            
            response = {
                "message": "Docker Image Generation Demo",
                "timestamp": datetime.utcnow().isoformat(),
                "image": os.environ.get("IMAGE_NAME", "docker-image-gen"),
                "version": os.environ.get("VERSION", "latest")
            }
            
            self.wfile.write(json.dumps(response, indent=2).encode())
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'Not Found')
    
    def log_message(self, format, *args):
        # Suppress default logging
        pass

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8000))
    server = HTTPServer(('0.0.0.0', port), DemoHandler)
    print(f"Server running on http://0.0.0.0:{port}")
    server.serve_forever()

