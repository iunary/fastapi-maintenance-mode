from fastapi import status
from fastapi.testclient import TestClient

from fastapi_maintenance_mode import MaintenanceModeMiddleware
from fastapi_maintenance_mode.main import app


def test_maintenance_mode():
    # enable the maintenance mode
    app.add_middleware(MaintenanceModeMiddleware, is_maintenance_mode=True)
    client = TestClient(app)

    response = client.get("/")
    assert response.status_code == status.HTTP_503_SERVICE_UNAVAILABLE

    # remove the maintenance mode middleware
    app.user_middleware.clear()
    app.middleware_stack = app.build_middleware_stack()
    response = client.get("/")
    assert response.status_code == status.HTTP_200_OK
