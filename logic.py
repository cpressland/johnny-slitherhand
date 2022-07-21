import random


def move_logic(body):
    options = ["up", "down", "left", "right"]
    head = body[0]
    torso = body[1:]
    for body_chunk in torso:
        if body_chunk["x"] == head["x"]-1:
            options.remove("left")
        elif body_chunk["x"] == head["x"]+1:
            options.remove("right")
        elif body_chunk["y"] == head["y"]-1:
            options.remove("down")
        elif body_chunk["y"] == head["y"]+1:
            options.remove("up")
    return random.choice(options)
