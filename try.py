import requests
from pathlib import Path

content = Path('./demo.html').read_text()
response = requests.post(
  'http://localhost:9000/generate',
  json={
    "html": content
  }
)

with open('./output.pdf', 'wb') as f:
  f.write(response.content)