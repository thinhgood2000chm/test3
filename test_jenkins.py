from fastapi import FastAPI
app = FastAPI(

)
@app.post("/detection")
def test():
    return {"test": "hahaha11111111ffffff"}

