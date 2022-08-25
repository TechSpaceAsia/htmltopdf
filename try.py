import requests
import fire
from pathlib import Path

def main(input: str='./demo.html', output: str='./output.pdf'):
  content = Path(input).read_text()
  response = requests.post(
    'http://localhost:9000/generate',
    json={
      "html": content
    }
  )

  with open(output, 'wb') as f:
    f.write(response.content)

if __name__ == '__main__':
  fire.Fire(main)