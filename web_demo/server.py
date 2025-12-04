#!/usr/bin/env python3
"""
Simple HTTP server for the GPU side-channel attack demo.

This server serves the HTML files needed to demonstrate the attack.
Run this script and open http://localhost:8000/attacker.html in your browser.
"""

import http.server
import socketserver
import os
import sys
from pathlib import Path

DEFAULT_PORT = 8000

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Add CORS headers to allow cross-origin requests if needed
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        super().end_headers()

    def log_message(self, format, *args):
        # Customize logging
        print(f"[{self.log_date_time_string()}] {format % args}")

def find_available_port(start_port=DEFAULT_PORT, max_attempts=10):
    """Try to find an available port starting from start_port."""
    for i in range(max_attempts):
        port = start_port + i
        try:
            with socketserver.TCPServer(("", port), None) as test_server:
                test_server.server_close()
                return port
        except OSError:
            continue
    return None

def main():
    # Change to the web_demo directory
    demo_dir = Path(__file__).parent
    os.chdir(demo_dir)
    
    Handler = MyHTTPRequestHandler
    
    # Try to find an available port
    port = find_available_port()
    if port is None:
        print("=" * 60)
        print("ERROR: Could not find an available port")
        print("=" * 60)
        print("\nPlease close other servers or specify a port manually.")
        print("You can also kill the process using port 8000:")
        print("  lsof -ti:8000 | xargs kill")
        sys.exit(1)
    
    if port != DEFAULT_PORT:
        print(f"⚠️  Port {DEFAULT_PORT} is in use, using port {port} instead")
    
    try:
        with socketserver.TCPServer(("", port), Handler) as httpd:
            print("=" * 60)
            print("GPU Side-Channel Attack Demo Server")
            print("=" * 60)
            print(f"\nServer running at http://localhost:{port}/")
            print("\nOpen these URLs in your browser:")
            print(f"  Attacker:  http://localhost:{port}/attacker.html")
            print(f"  Victim:    http://localhost:{port}/victim.html")
            print("\nPress Ctrl+C to stop the server")
            print("=" * 60)
            
            try:
                httpd.serve_forever()
            except KeyboardInterrupt:
                print("\n\nServer stopped.")
    except OSError as e:
        print("=" * 60)
        print("ERROR: Could not start server")
        print("=" * 60)
        print(f"\nError: {e}")
        print("\nIf port is in use, you can:")
        print("  1. Close the other server")
        print("  2. Kill the process: lsof -ti:8000 | xargs kill")
        print("  3. Use a different port by modifying DEFAULT_PORT in server.py")
        sys.exit(1)

if __name__ == "__main__":
    main()
