import uvicorn as uvicorn
from mongoengine import connect
from api import app

if __name__ == '__main__':
    connect(host="mongodb://localhost:21771/admin")
    uvicorn.run(app, host="0.0.0.0", port=8000)
