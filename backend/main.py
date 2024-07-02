from fastapi import FastAPI, File, UploadFile,Request,Depends
from fastapi.middleware.cors import CORSMiddleware
import sqlite3,json
from dotenv import load_dotenv
from openai import OpenAI
load_dotenv()


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  
    allow_credentials=True, 
    allow_methods=["GET", "POST", "PUT", "DELETE"],  
    allow_headers=["Authorization", "Content-Type" ], 
)



client = OpenAI()
conn = sqlite3.connect('data.db')
cursor = conn.cursor()



@app.get('/')
def hello_world():
    return {'message': 'Hello, world!'}




@app.post('/response')
async def query(request:Request):
    body = await request.json()
    print(body)
    print(body['query'])

    SYSTEM_PROMPT = '''Below are the table schema 
CREATE TABLE IF NOT EXISTS political_bonds (
    Sr_No INTEGER,
    Date_of_Encashment TEXT,
    Name_of_the_Political_Party TEXT,
    Account_no_of_Political_Party TEXT,
    Prefix TEXT,
    Bond_Number INTEGER,
    Denominations INTEGER,
    Pay_Branch_Code TEXT,
    Pay_Teller INTEGER
);

CREATE TABLE IF NOT EXISTS bonds (
    Sr_No INTEGER,
    Reference_No_URN TEXT,
    Journal_Date TEXT,
    Date_of_Purchase TEXT,
    Date_of_Expiry TEXT,
    Name_of_the_Purchaser TEXT,
    Prefix TEXT,
    Bond_Number INTEGER,
    Denominations INTEGER,
    Issue_Branch_Code INTEGER,
    Issue_Teller INTEGER,
    Status TEXT
);

you are a sqlite3 query writer, given a question by user you output only sqlite3 queries based on given schemas, give output in json format'''
    completion = client.chat.completions.create(model="gpt-4o",
    messages=[
    {"role": "system", "content": SYSTEM_PROMPT},
    {"role": "user", "content":body['query']},
  ],
  response_format= { "type": "json_object" }
)

    x=completion.choices[0].message.content

    query = json.loads(x)
    sql_query = query['query']
    print(sql_query)
    cursor.execute(sql_query)
    answer= cursor.fetchone()[0]
    if(answer ==None ):
        answer = ""
    return {"text":answer,"by":"AI"}