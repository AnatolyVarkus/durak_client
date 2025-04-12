import json

async def send_state(websocket, state):
    # print(f"Sent: ", {"type": "state", "state": state})
    await websocket.send(json.dumps({"type": "state", "state": state}))

async def send_attack(websocket, attack):
    # print(f"Sent: ", {"type": "attack", "move": attack})
    await websocket.send(json.dumps({"type": "attack", "move": attack}))

async def send_defence(websocket, defence):
    # print(f"Sent: ", {"type": "defend", "move": defence})
    await websocket.send(json.dumps({"type": "defend", "move": defence}))

async def send_wtv(websocket, wtv):
    # print(f"Sent: ", wtv)
    await websocket.send(json.dumps(wtv))

async def send_wait(websocket):
    # print(f"Sent: ", {"type": "wait"})
    await websocket.send(json.dumps({"type": "wait"}))
