from fastapi import FastAPI

app = FastAPI(title="API de Documentos", version="0.1.0")

@app.get("/health")
def verificar_status():
    return {"status": "ativo", "servico": "api-documentos"}