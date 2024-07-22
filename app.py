from fastapi import FastAPI, Request
import logging

app = FastAPI()

# Set up logging to print to the console
logging.basicConfig(level=logging.INFO)


@app.post("/webhook")
async def handle_webhook(request: Request):
    # Read the JSON payload from the request
    payload = await request.json()

    # Log the received payload
    logging.info(f"Received payload: {payload}")

    # Return a success response
    return {"status": "success"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
