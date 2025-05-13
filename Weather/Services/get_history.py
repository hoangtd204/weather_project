import os
import json

HISTORY_FILE = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Database', 'historySearching.json'))

def get_search_history():
    if not os.path.exists(HISTORY_FILE):
        return []

    try:
        with open(HISTORY_FILE, 'r') as f:
            data = json.load(f)
            return data.get("cities", [])
    except json.JSONDecodeError:
        return []
