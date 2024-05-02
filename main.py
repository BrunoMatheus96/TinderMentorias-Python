from fastapi import FastAPI

app = FastAPI()


@app.get("/ola-mundo")
def read_root():
    return {
        "mensagem": "Olá, as configurações iniciais deram certo!"
    }