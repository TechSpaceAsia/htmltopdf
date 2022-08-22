from typing import Union
from fastapi import FastAPI
from fastapi.responses import FileResponse
import tempfile
from pydantic import BaseModel
from wkhtmltopdf import wkhtmltopdf
import os
from starlette.background import BackgroundTask

class Item(BaseModel):
  html: str

app = FastAPI()

@app.post("/generate")
async def generate_pdf(item: Item):
  input_file = tempfile.NamedTemporaryFile(
    'w', 
    delete=False, suffix='.html'
  )
  output_file = tempfile.NamedTemporaryFile(
    'w', 
    delete=False, suffix=".pdf"
  )
  input_file.write(item.html)
  input_file.close()
  # output_file.close()
  wkhtmltopdf(input_file.name, output_file.name)
  os.remove(input_file.name)
  def cleanup():
    os.remove(output_file.name)
  return FileResponse(
    output_file.name,
    background=BackgroundTask(cleanup)
  )
  


  return {"message": item.html.upper()}