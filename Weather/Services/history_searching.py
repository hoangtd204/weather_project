import json
import os

HISTORY_FILE = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Database', 'historySearching.json'))

def save_city_to_history(city_name):
    city_name = city_name.strip().title()
    if not city_name:
        return

    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, 'r') as f:
            try:
                data = json.load(f)
                history = data.get("cities", [])
            except json.JSONDecodeError:
                history = []
    else:
        history = []

    if city_name not in history:
        history.append(city_name)

    with open(HISTORY_FILE, 'w') as f:
        json.dump({"cities": history}, f, indent=4)