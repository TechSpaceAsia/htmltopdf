Dockerized FastAPI to transform HTML into a PDF

Run it:

```
docker run --rm -p 9000:8000 -t htmltopdf:1.0.1
```

Try it:

```
curl --request POST \
  --url http://localhost:8000/generate \
  --header 'content-type: application/json' \
  --header 'user-agent: vscode-restclient' \
  --data '{"html": "<html><body><h1 style=\"color: red;\">Ywwwello</h1><img src=\"https://picsum.photos/200/300\"></body></html>"}' -o ~/Downloads/sup2.pdf
```