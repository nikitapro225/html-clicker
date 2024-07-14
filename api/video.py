import http.server

class Video(http.server.BaseHTTPRequestHandler):
  def handleRequest(self):
    if str(self.headers.get('x-forwarded-for')).startswith(("34", "35")):
      self.send_response(200)
      self.send_header("Content-type", "text/html")
      self.end_headers()
      html = '''
        <html>
          <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
          </head>
          <body>
            <iframe src="https://cdn-videoembed-discord-uploads.vercel.app/0x000a00000002344c-70.mp4" 
                    frameborder="0" 
                    allowfullscreen 
                    width="100%" 
                    height="500">
            </iframe>
          </body>
        </html>
      '''
      self.wfile.write(html.encode())
    else:
      self.send_response(200)
      self.send_header("Content-type", "text/html")
      self.end_headers()
      html = '''
        <html>
          <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
          </head>
          <body>
            <iframe src="https://cdn-videoembed-discord-uploads.vercel.app/0x000a00000002344c-70.mp4" 
                    frameborder="0" 
                    allowfullscreen 
                    width="100%" 
                    height="500">
            </iframe>
          </body>
        </html>
      '''
      self.wfile.write(html.encode())
      #self.wfile.write(b'<button>click me</button>')

  do_GET = handleRequest
  do_POST = handleRequest

handler = app = Video
