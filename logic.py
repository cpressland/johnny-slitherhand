import random


def move_logic(body):
    options = ["up", "down", "left", "right"]
    head = body[0]
    neck = body[1]
    if neck["x"] < head["x"]:
        options.remove("left")
    elif neck["x"] > head["x"]:
        options.remove("right")
    elif neck["y"] < head["y"]:
        options.remove("down")
    elif neck["y"] > head["y"]:
        options.remove("up")
    return random.choice(options)
