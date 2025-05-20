import json
import os

def parse_incidents():
    """
    Reads and parses the sample incident log file from the data folder.
    """
    file_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'sample_incidents.json')
    try:
        with open(file_path, 'r') as f:
            incidents = json.load(f)
    except Exception as e:
        incidents = []
    return incidents

if __name__ == '__main__':
    incidents = parse_incidents()
    import json
    print(json.dumps(incidents, indent=2))
