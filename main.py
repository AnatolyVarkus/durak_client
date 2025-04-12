from ws import send_state, send_defence, send_wait, send_attack
import asyncio
from bot_script import bot_main


TOTAL_WINS = 0
TOTAL_LOSES = 0

def should_press_ready(data, player_id):
    try:
        players = [i["id"] for i in data["players"]]
        if data["players"][players.index(player_id)]["state"] == "wait":
            return True
        return False
    except KeyError:
        return False

def check_for_winner(data, player_id):
    players = [i["id"] for i in data["players"]]
    states = [i["state"] for i in data["players"]]
    if states.count("winner") == 1 and states.count("durak") == 1:
        if states[players.index(player_id)] == "winner":
            return True
        return False

async def main_function(websocket, data, player_id):
    global TOTAL_WINS, TOTAL_LOSES
    if should_press_ready(data, player_id):  # отправляет ready серверу, чтобы начать игру
        await send_state(websocket, "ready")
    else:
        try:
            if data["info"]["state"] == "play":
                pass  # основная функция
            else:
                if check_for_winner(data, player_id) is not None:  # подсчет побед/поражений. Можете удалить
                    if check_for_winner(data, player_id):
                        TOTAL_WINS += 1
                    else:
                        TOTAL_LOSES += 1
                    print(f"Total Wins: {TOTAL_WINS}\nTotal Loses: {TOTAL_LOSES}\n")
        except:
            pass  # Ненужные пакеты  

