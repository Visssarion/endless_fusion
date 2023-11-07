import json

config = {
    "screen":
        {
            "full-screen": False,
            "x_scale": 4,
            "y_scale": 4
        }
}


def load():
    try:
        with open("config.json", "r", encoding='utf-8') as file:
            config = json.loads(file.read())
    except FileNotFoundError:
        save()


def save():
    with open("config.json", "w", encoding='utf-8') as file:
        file.write(json.dumps(config))
