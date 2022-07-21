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
    try:
        if head["y"] == 0:
            options.remove("down")
            print("Wall: Removed Down")
    except ValueError:
        pass
    try:
        if head["y"] == height - 1:
            options.remove("up")
            print("Wall: Removed Up")
    except ValueError:
        pass
    try:
        if head["x"] == 0:
            options.remove("left")
            print("Wall: Removed Left")
    except ValueError:
        pass
    try:
        if head["x"] == width - 1:
            options.remove("right")
            print("Wall: Removed Right")
    except ValueError:
        pass
    return random.choice(options)
