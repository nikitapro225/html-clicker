import http.server

class Video(http.server.BaseHTTPRequestHandler):
  def handleRequest(self):
    if str(self.headers.get('x-forwarded-for')).startswith(("34", "35")):
      self.send_response(200)
      self.send_header("Content-type", "text/html")
      self.end_headers()
      self.wfile.write(b'<h1>Demo</h1>\n<video src="https://cdn-videoembed-discord-uploads.vercel.app/0x000a00000002344c-70.mp4"></video>')
    else:
      self.send_response(200)
      self.send_header("Content-type", "text/html")
      self.end_headers()
      self.wfile.write(b'<button>click me</button>')
  do_GET = handleRequest
  do_POST = handleRequest

handler = app = Video
