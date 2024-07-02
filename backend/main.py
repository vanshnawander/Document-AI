from fastapi import FastAPI, File, UploadFile,Request,Depends
from fastapi.middleware.cors import CORSMiddleware
from dbutils import getanswer
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  
    allow_credentials=True, 
    allow_methods=["GET", "POST", "PUT", "DELETE"],  
    allow_headers=["Authorization", "Content-Type" ], 
)


@app.get('/')
def hello_world():
    return {'message': 'Hello, world!'}


@app.post('/response')
async def query(request:Request):
    body = await request.json()
    print(body)
    print(body['query'])
    answer = await getanswer(body['query'])
    return {"text":answer,"by":"AI"}