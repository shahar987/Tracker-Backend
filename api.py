import uvicorn as uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from mongoengine import connect

from db import create_end_points, read_end_points
from db import create_client, read_client_by_company
from db import create_user, read_user, create_checklist, read_checklist, create_clientChecks, read_clientchecks

app = FastAPI(title='Tracker')
origins = [
    "http://localhost:3000",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# http://.../card/google


@app.on_event('startup')
def connect_to_mongo():
    connect(host="mongodb://localhost:27017/admin")


@app.get('/card/{company}')
def get_card(company: str):
    cards = read_client_by_company(company)
    if cards:
        return cards
    else:
        raise HTTPException(404, 'no such company')


@app.post('/card/{name}')
def create_card(name: str, error_num: int, ip: str, company: str) -> dict:
    card = create_client(name, error_num, ip, company)
    if card:
        return card
    else:
        raise HTTPException(404, 'card already exists')


@app.get('/endpoint/{company}')
def get_endpoint(company: str) -> dict:
    card = read_end_points(company)
    if card:
        return card
    else:
        raise HTTPException(404, 'no such endpoint')


@app.post('/endpoint/{company}')
def create_endpoint(company: str, total: int, ok: int) -> dict:
    card = create_end_points(total, ok, company)
    if card:
        return card
    else:
        raise HTTPException(404, 'endpoint already exists')


@app.get('/user/{email}')
def get_user(email: str) -> dict:  # בקשה שאמורה להחזיר מייל וסיסמא
    user = read_user(email)
    if user:
        return user
    else:
        raise HTTPException(404, 'no such user')


@app.post('/user/{email}')
def new_user(company: str, email: str, password: str) -> dict:
    user = create_user(email, password, company)
    if user:
        return user
    else:
        raise HTTPException(404, 'user already exists')


@app.get('/checklist/{number}')
def get_checklist(number: str) -> dict:
    cl = read_checklist(number)
    if cl:
        return cl
    else:
        raise HTTPException(404, 'no such checklist')


@app.post('/checklist/{number}')
def new_checklist(number: str, name: str) -> dict:
    cl = create_checklist(name, number)
    if cl:
        return cl
    else:
        raise HTTPException(404, 'checklist already exists')


@app.get('/clientCheck/{company}/{client_name}')
def get_clientcheck(company: str, client_name: str) -> dict:
    cl = read_clientchecks(company, client_name)
    if cl:
        return cl
    else:
        raise HTTPException(404, 'no such client check')


@app.post('/clientCheck/{company}/{client_name}')
def new_clientcheck(company: str, client_name: str, client_list: dict) -> dict:
    cl = create_clientChecks(company, client_name, client_list)
    if cl:
        return cl
    else:
        raise HTTPException(404, 'client check already exists')


if __name__ == '__main__':
    connect_to_mongo()
    uvicorn.run(app, host="0.0.0.0", port=8000)
