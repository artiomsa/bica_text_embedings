from sentence_transformers import SentenceTransformer
from pydantic import BaseModel
from fastapi import FastAPI
import numpy as np

app = FastAPI()

model = SentenceTransformer('all-MiniLM-L6-v2')

class inp_sentence(BaseModel):
    sent: str


@app.get("/")
async def root():
    return {"message": "Hello!"}


@app.post('/sentence')
def get_embeding(inp_sentence: inp_sentence):

    embedding = model.encode(inp_sentence.sent)
    embedding = ';'.join(list(map(str,list(embedding))))
    return {'embeding':embedding}
