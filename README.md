# 🐙 GitHub Activity CLI

A command-line tool to view recent GitHub activity of any public user.  
Built using only Python standard libraries — no external dependencies.

> 📌 Project inspired by [roadmap.sh](https://roadmap.sh/projects/github-user-activity)

---

## 🔍 What It Does

- 🧑‍💻 Takes a GitHub username as input
- 📡 Fetches recent public activity from the GitHub Events API
- 📄 Displays meaningful actions:
  - Pushed commits
  - Opened/closed issues
  - Starred repositories
  - Forked repos
  - And more!

---

## 🚀 How to Use

```bash
python main.py <github_username>
```

### 🧪 Example:

```bash
python main.py kamranahmedse
```

### ✅ Sample Output

```
Output:
- Pushed 3 commits to kamranahmedse/developer-roadmap
- Opened an issue in kamranahmedse/developer-roadmap
- Starred kamranahmedse/developer-roadmap
- Forked kamranahmedse/developer-roadmap
```

---

## ⚠️ Error Handling

This CLI handles:

- `400`: Bad request
- `401`: Unauthorized access
- `403`: Rate limit exceeded
- `404`: User not found
- `429`: Too many requests
- `500 / 503`: Server issues
- Network problems
- Invalid JSON response

---

## 🧠 Skills Practiced

- Fetching from public APIs using `urllib.request`
- Handling `HTTPError` and `URLError`
- JSON decoding and safe parsing
- Using command-line arguments (`sys.argv`)
- `match-case` logic to simplify branching
- Formatting and displaying structured output

---

## 👤 Author

**Jurabek**  
High school student and aspiring **AI Chatbot Developer**.  
Building real-world Python projects as part of the [roadmap.sh](https://roadmap.sh/python) learning path.

