# Agent MCP Template  
  
This repository contains a generic Python template for an AgentKit Model Context Protocol (MCP) server. The server uses FastAPI to expose a tool that calls an unauthenticated weather API (Open Meteo) and returns a simple forecast for a given latitude and longitude.  
  
## Structure  
- `server.py` – FastAPI application implementing a `get_forecast` endpoint for AgentKit. It fetches current and hourly temperature data from the Open Meteo API.  
- `requirements.txt` – Python dependencies.  
- `.github/workflows/deploy.yaml` – Placeholder workflow for deployment. You will need to configure your own AWS credentials and hosting details.  
  
## Usage  
1. Install dependencies: `pip install -r requirements.txt`.  
2. Run the server locally: `uvicorn server:app --host 0.0.0.0 --port 8000`.  
3. Deploy to your own hosting platform (for example AWS Lambda or EC2).  
4. Register the endpoint in AgentKit’s Connector Registry.  
  
## Notes  
- The weather API used here (Open Meteo) does not require an API key.  
- For production use you should secure the MCP endpoint with a bearer token and handle error cases.

Trigger deployment
