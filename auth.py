from fastapi import Query, HTTPException, status

API_TOKEN = "okworld"


def verify_token(key: str = Query(None)):
    if not key:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="API key missing"
        )

    if key != API_TOKEN:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid API key"
        )

    return True
