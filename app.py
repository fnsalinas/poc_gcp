
from typing import Dict, List, Tuple, Any
from fastapi import FastAPI

from src.dbextract.postgresql import extract_postgres


app = FastAPI()


@app.get("/process_id={process_id}")
def read_root(process_id: int):
    response: Dict[str, Any] = extract_postgres(
        process_id=process_id,
        bucket_name="poc-gcp-381517.appspot.com",
        folderpath="config"
    )
    return response


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)
