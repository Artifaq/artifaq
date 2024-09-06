from artifaq.main import artifaq

app = artifaq()

@app.get("/")
async def root():
    return {"message": "Hello World"}
