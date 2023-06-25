from fastapi import FastAPI

from .middleware import MaintenanceModeMiddleware

app = FastAPI()
app.add_middleware(MaintenanceModeMiddleware, is_maintenance_mode=True)


@app.get("/")
async def root():
    return {"status": "Ok"}
