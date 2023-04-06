from fastapi import FastAPI
import mcstatus
import dataclasses

app = FastAPI()


@app.get("/status/{server_ip}")
async def get_status(server_ip: str) -> dict:
    server = await mcstatus.JavaServer.async_lookup(server_ip)
    status = await server.async_status()
    return dataclasses.asdict(status)
