# 🐙 GitHub Activity CLI

A command-line tool to view recent GitHub activity of any public user — with optional event filtering and caching support.  
Built using **only Python standard libraries**, no external dependencies.

> 📌 Project inspired by [roadmap.sh](https://roadmap.sh/projects/github-user-activity)

---

## 🔍 What It Does

- 🧑‍💻 Takes a GitHub username as input
- 🧩 (Optional) Filter events by type (e.g., `PushEvent`, `IssuesEvent`, etc.)
- 📡 Fetches recent public activity from the GitHub Events API
- 💾 Caches results for 10 minutes to reduce API calls
- 📄 Displays meaningful activity summaries:
  - Number of commits pushed
  - Issues opened or closed
  - Starred or forked repositories
  - And other events

---

## 🚀 How to Use

```bash
python main.py <github_username> [event_type]
```

### 🧪 Examples

```bash
# All activity
python main.py kamranahmedse

# Only push events
python main.py kamranahmedse PushEvent
```

---

## ✅ Sample Output

### From API:

```text
(Fetched from GitHub API)

Output:
- Pushed 3 commits to kamranahmedse/developer-roadmap
- Opened 1 issue in kamranahmedse/developer-roadmap
- Starred kamranahmedse/developer-roadmap (2 times)
```

### From Cache:

```text
(Loaded from cache)

Output:
- Pushed 2 commits to kamranahmedse/dev-notes
```

---

## ⚠️ Error Handling

The script handles various scenarios:

- `400` : Bad request
- `401` : Unauthorized access
- `403` : Rate limit exceeded
- `404` : User not found
- `429` : Too many requests
- `500` / `503` : Server issues
- Network issues
- Malformed or empty API response

---

## 🧠 Skills Practiced

- Fetching data from APIs using `urllib.request`
- Handling errors (`HTTPError`, `URLError`)
- JSON parsing and cache validation
- Using `sys.argv` for CLI input
- Writing clean `match-case` logic
- Grouping and summarizing data
- Implementing basic caching for performance

---

## 👤 Author

**Jurabek**  
High school student learning Python and backend development.  
Focused on real-world projects with a goal of becoming a freelance AI chatbot developer.

---
