from fastapi import FastAPI
from update_signal import update_status_manually
from models import colors
from update_signal import update_status_manually, get_signal_status_by_id
import uvicorn
app=FastAPI()

@app.post("/api/v1/signals/{id}")
def set_signal_status(id: int, color: colors):
    update_status_manually(id,color)

@app.get("/api/v1/signals/{id}")
def get_signal_status(id:int):
    return get_signal_status_by_id(id)


if __name__ == "__main__":
    uvicorn.run("api_routes:app", host="127.0.0.1", port=8000, log_level="info", reload= True)

