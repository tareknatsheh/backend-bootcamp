from fastapi import HTTPException

def handle_errors(fn):
    def wrapper(*args, **kwargs):
        try:
            return fn(*args, **kwargs)
        except HTTPException as http_error:
            raise http_error
        except Exception as error:
            print(error)
            raise HTTPException(status_code=500, detail="Internal server error. Check logs for more info")
    return wrapper