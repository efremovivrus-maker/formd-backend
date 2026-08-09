import os
import secrets
from typing import Optional

from fastapi import Header, HTTPException, status


def require_admin_token(
    x_admin_token: Optional[str] = Header(default=None, alias="X-Admin-Token")
) -> None:
    expected = os.getenv("ADMIN_TOKEN")

    if not expected:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="ADMIN_TOKEN is not configured on the server.",
        )

    if not x_admin_token or not secrets.compare_digest(x_admin_token, expected):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid admin token.",
        )