import random


def move_logic(body):
    options = ["up", "down", "left", "right"]
    head = body[0]
    torso = body[1:]
    for body_chunk in torso:
        if body_chunk["x"] == head["x"]-1:
            try:
                options.remove("left")
            except ValueError:
                pass
        elif body_chunk["x"] == head["x"]+1:
            try:
                options.remove("right")
            except ValueError:
                pass
        elif body_chunk["y"] == head["y"]-1:
            try:
                options.remove("down")
            except ValueError:
                pass
        elif body_chunk["y"] == head["y"]+1:
            try:
                options.remove("up")
            except ValueError:
                pass
    return random.choice(options)
