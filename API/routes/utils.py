from fastapi import status, HTTPException


def getResponse(done: bool, errorMessage: str):
    if not done:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=errorMessage)
    return {"status_code": status.HTTP_200_OK}


async def riseHttpExceptionIfNotFound(result, message: str):
    if result is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=message)