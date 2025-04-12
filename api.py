import asyncio
import websockets
import json
from main import main_function

SERVER_URL = "ws://93.183.90.171:8000/ws"
PLAYER_ID = "123456789"
GAME_TYPE = 1  # или 0

async def websocket_client():
    async with websockets.connect(SERVER_URL) as websocket:
        init_data = {
            "player_id": PLAYER_ID,
            "game_type": GAME_TYPE
        }
        await websocket.send(json.dumps(init_data))

        while True:
            data = json.loads(await websocket.recv())
            # print(f"\nReceived: {json.dumps(data, indent=2)}")  # дата с сервера, можете раскомментить

            asyncio.create_task(main_function(websocket, data, PLAYER_ID))


asyncio.run(websocket_client())
