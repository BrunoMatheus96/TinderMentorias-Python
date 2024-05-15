import uvicorn
import os

if __name__ == "__main__":
    PORT = os.getenv("PORT")

    if not PORT:
        PORT = 5000

    PORT = int(PORT)

    uvicorn.run('main:app', host="0.0.0.0", port=PORT, reload=True)
