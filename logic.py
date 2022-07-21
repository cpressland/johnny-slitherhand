import random


def move_logic(body, height, width):
    options = ["up", "down", "left", "right"]
    head = body[0]
    torso = body[1:]
    for body_chunk in torso:
        try:
            if body_chunk["x"] == head["x"] - 1:
                options.remove("left")
            elif body_chunk["x"] == head["x"] + 1:
                options.remove("right")
            elif body_chunk["y"] == head["y"] - 1:
                options.remove("down")
            elif body_chunk["y"] == head["y"] + 1:
                options.remove("up")
        except ValueError:
            continue
    try:
        if head["y"] <= 1:
            options.remove("down")
        elif head["y"] >= height - 1:
            options.remove("up")
        elif head["x"] <= 1:
            options.remove("left")
        elif head["x"] >= width - 1:
            options.remove("right")
    except ValueError:
        pass
    return random.choice(options)
