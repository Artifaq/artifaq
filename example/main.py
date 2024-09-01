from artifaq.artifaq import Artifaq


app = Artifaq()

@app.get("/")
async def root():
    return {"message": "Hello World"}