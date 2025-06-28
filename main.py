import sys
import json
import urllib.request
from urllib.error import HTTPError
from urllib.error import URLError


if len(sys.argv) != 2:
    print("Usage: python main.py \"github_username\"")
    sys.exit(1)

username = sys.argv[1]
url = f"https://api.github.com/users/{username}/events"

headers = {
    "User-Agent": "Python-GitHub-CLI/1.0"
}

req = urllib.request.Request(url, headers=headers)

try:
    with urllib.request.urlopen(req) as response:
        events = json.loads(response.read())

        if not events:
            print(f"No public activity found for {username}.")
            sys.exit(0)

        print("\nOutput:")
        for event in events:
            repo = event.get("repo", {}).get("name", "Unknown Repo")
            payload = event.get("payload", {})

            match event.get("type"):
                case "PushEvent":
                    commits = payload.get("commits", [])
                    count = len(commits)
                    print(f"- Pushed {count} commit{'s' if count != 1 else ''} to {repo}")
                case "IssuesEvent":
                    action = payload.get("action", "did something")
                    print(f"- {action.capitalize()} an issue in {repo}")
                case "WatchEvent":
                    print(f"- Starred {repo}")
                case "ForkEvent":
                    print(f"- Forked {repo}")
                case _:
                    print(f"- {event.get("type")} in {repo}")
        print("\n")

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
