import random

previous_move = ""


def move_logic():
    global previous_move
    options = ["up", "down", "left", "right"]
    if previous_move:
        options.remove(previous_move)
    move = random.choice(options)
    previous_move = move
    return move
