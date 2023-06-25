from typing import Callable

from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse, Response
from starlette.middleware.base import BaseHTTPMiddleware


class MaintenanceModeMiddleware(BaseHTTPMiddleware):
    """
    Middleware for enabling maintenance mode in a fastapi application.
    """

    def __init__(self, app: FastAPI, is_maintenance_mode=False):
        super().__init__(app)
        self.is_maintenance_mode = is_maintenance_mode

    async def dispatch(self, request: Request, call_next: Callable) -> Response:
        """Intercept the incoming requests

        Args:
            request (Request): incoming request
            call_next (Callable): next route

        Returns:
            Response: client response
        """
        if self.is_maintenance_mode:
            return JSONResponse(
                content={
                    "detail": "Service is temporarily unavailable due to maintenance"
                },
                status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            )
        response = await call_next(request)
        return response
