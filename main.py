from datetime import datetime
from pytz import timezone

from fastapi import FastAPI

app = FastAPI()

# Define Nepal time zone
nepal_tz = timezone('Asia/Kathmandu')


@app.get("/nepal_time/")
async def get_nepal_time():
  """
  Get current time in Nepal with date.
  """
  now_nepal = datetime.now(nepal_tz)
  return {
      "time": now_nepal.strftime("%H:%M:%S"),
      "date": now_nepal.strftime("%Y-%m-%d")
  }


if __name__ == "__main__":
  import uvicorn
  uvicorn.run("main:app", reload=True)
