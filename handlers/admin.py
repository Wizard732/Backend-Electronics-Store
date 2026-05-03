from fastapi import HTTPException, Header


def verify_admin(admin: str = Header(None)):
    if admin != "admin":
        HTTPException(status_code=400,detail="Доступ ограничен.")

