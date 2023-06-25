# FastAPI Maintenance Mode Middleware

FastAPI Maintenance Mode Middleware is a Python package that provides middleware for enabling maintenance mode in FastAPI applications. When maintenance mode is enabled, all incoming requests will receive a 503 Service Unavailable response indicating that the service is temporarily unavailable due to maintenance.

## Installation

You can install the package using `pip`:

```shell
pip install fastapi-maintenance-mode
```

## Example

```python
from fastapi import FastAPI
from fastapi_maintenance_mode import MaintenanceModeMiddleware

app = FastAPI()
app.add_middleware(MaintenanceModeMiddleware, is_maintenance_mode=True)


@app.get("/")
async def root():
    return {"status": "Ok"}

```