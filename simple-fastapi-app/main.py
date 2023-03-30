from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def index():
    return {
        "message": "selamat datang"
    }

@app.get('/about')
async def about():
    return {
        "message": "selamat datang about"
    }

@app.get('/contact')
async def contact():
    return {
        "message": "selamat datang contact"
    }