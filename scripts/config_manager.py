import json

config = {
    "screen":
        {
            "fullscreen": False,
            "exclusive": False,
            "scale": 4
        }
}


def load():
    global config
    try:
        with open("config.json", "r", encoding='utf-8') as file:
            config = json.loads(file.read())
    except FileNotFoundError:
        save()


def save():
    global config
    with open("config.json", "w", encoding='utf-8') as file:
        file.write(json.dumps(config))
