from http.server import BaseHTTPRequestHandler
import json
import os
from upstash_redis import Redis

redis = Redis(url=os.environ.get("UPSTASH_REDIS_REST_URL"), 
              token=os.environ.get("UPSTASH_REDIS_REST_TOKEN"))

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        
        data = redis.lrange("mensagens", 0, -1)
        messages = [json.loads(m) for m in data]
        
        self.wfile.write(json.dumps(messages).encode('utf-8'))

    def do_PUT(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        
        try:
            payload = json.loads(post_data.decode('utf-8'))
            
            redis.rpush("mensagens", json.dumps(payload))
            
            self.send_response(201)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({"status": "salvo no redis"}).encode('utf-8'))
        except Exception as e:
            self.send_response(400)
            self.end_headers()
            self.wfile.write(str(e).encode('utf-8'))