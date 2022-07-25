import random


def move_logic(body, height, width):
    options = ["up", "down", "left", "right"]
    head = body[0]
    torso = body[1:]
    for body_chunk in torso:
        try:
            if body_chunk["x"] == head["x"] - 1:
                options.remove("left")
                print("Cannibalism: Removed Left")
            elif body_chunk["x"] == head["x"] + 1:
                options.remove("right")
                print("Cannibalism: Removed Right")
            elif body_chunk["y"] == head["y"] - 1:
                options.remove("down")
                print("Cannibalism: Removed Down")
            elif body_chunk["y"] == head["y"] + 1:
                options.remove("up")
                print("Cannibalism: Removed Up")
        except ValueError:
            continue
    return random.choice(options)
