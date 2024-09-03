from artifaq.artifaq import Artifaq
from artifaq.logger import Logger

app = Artifaq()

@app.get("/")
async def root():
    return {"message": "Hello World"}

Logger().error("This is an error message")