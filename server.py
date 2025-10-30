from fastapi import FastAPI
import httpx
from typing import Dict

app = FastAPI()

@app.get("/get_forecast")
async def get_forecast(lat: float, lon: float) -> Dict:
    """Fetch current weather and hourly temperature for a given latitude and longitude using Open Meteo API."""
    url = (
        f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m,weather_code,wind_speed_10m"
        f"&hourly=temperature_2m&forecast_days=1"
    )
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        response.raise_for_status()
        data = response.json()

    # Build a simplified response for MCP consumption
    current = data.get("current", {})
    hourly = data.get("hourly", {})
    result = {
        "current": current,
        "hourly": {
            "time": hourly.get("time", []),
            "temperature_2m": hourly.get("temperature_2m", []),
        },
    }
    return result
