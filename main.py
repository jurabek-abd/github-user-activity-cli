import os
import sys
import time
import json
import urllib.request
from urllib.error import HTTPError
from urllib.error import URLError

if len(sys.argv) < 2:
    print("Usage: python main.py \"github_username\"")
    sys.exit(1)

username = sys.argv[1]
filter_event_type = sys.argv[2] if len(sys.argv) > 2 else None
url = f"https://api.github.com/users/{username}/events"
cache_file = f".cache_{username}.json"

headers = {
    "User-Agent": "Python-GitHub-CLI/1.0"
}

req = urllib.request.Request(url, headers=headers)

# Validate Cache
def is_cache_valid(file_path, ttl=600):
    # Check if cache file exists
    if not os.path.exists(file_path):
        return False
    with open(file_path, 'r', encoding="utf-8") as f:
        try:
            cached = json.load(f)
            # Calculate how much time passed since data was cached
            age = time.time() - cached["timestamp"]
            return age < ttl
        except (json.JSONDecodeError, KeyError):
            return False

def display_data(display_events):
    print("\nOutput:")

    from collections import defaultdict
    summary = defaultdict(lambda: {"count": 0, "commits": 0, "actions": []})

    filtered_events = [e for e in events if e.get("type") == filter_event_type] if filter_event_type else events

    for event in filtered_events:
        event_type = event.get("type")
        repo = event.get("repo", {}).get("name", "Unknown Page")
        payload = event.get("payload", {})

        key = (event_type, repo)
        summary[key]["count"] += 1

        # if event_type == "PushEvent":
            # summary["key"]["commits"] +=

    print("\n")

if is_cache_valid(cache_file):
    with open(cache_file, "r", encoding="utf-8") as f:
        events = json.load(f)["data"]
        print("\n(Loaded from cache)")
        display_data(events)
else:
    try:
        with urllib.request.urlopen(req) as response:
            events = json.loads(response.read())

            if not events:
                print(f"No public activity found for {username}.")
                sys.exit(0)

            print("\n(Fetched from GitHub API)")

            with open(cache_file, 'w', encoding="utf-8") as f:
                json.dump({
                    "timestamp": time.time(),
                    "data": events
                }, f)

            display_data(events)

    except HTTPError as error:
        match error.code:
            case 400:
                print("Bad request (400): Something's wrong with the URL or parameters.")
            case 401:
                print("Unauthorized (401): You need to authenticate.")
            case 403:
                print("Forbidden (403): Access denied or rate limit exceeded.")
            case 404:
                print(f"User not found: {username}")
            case 429:
                print("Rate limit exceeded (429): Please wait and try again later.")
            case 500:
                print("Server error (500): Try again later.")
            case 503:
                print("GitHub service unavailable (503): Try again soon.")
            case _:
                print("Unknown Error: Try again later.")
        sys.exit(1)
    except URLError as error:
        print(f"Network Error: {error.reason}")
        sys.exit(1)
    except json.JSONDecodeError:
        print("Failed to parse response from GitHub.")
        sys.exit(1)
