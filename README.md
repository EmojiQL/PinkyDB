# 🐭 PinkyDB ((EmojiQL)
#### The first Emoji-Native Database Engine in the world!

> "Narf! What if we query the database with Emojis?!" – Pinky
>
> "...Technically possible with set theory and clean Python logic." – Brain

PinkyDB is not just a joke; it's a fully functional, file-based **JSON Document Store** with a revolutionary **Emoji Query Language (EmojiQL)** interface. It proves that the most secure and logical systems can emerge from the silliest ideas.

## 🎯 Project Philosophy: Problem Solving over Solutions

Why Emojis? Because traditional database query languages are **boring** and prone to human error. PinkyDB prioritizes **clarity, fun, and native efficiency**.

  * **Logic (Brain):** The core engine uses native Python set operations (`&`, `|`, `-`) for fast, secure filtering on document IDs, minimizing disk I/O. **No SQL, no drivers, no messy configuration.**
  * **Chaos (Pinky):** Your user interface will be built entirely on the intuitive (and hilarious) **EmojiQL** grammar. You don't ask for `WHERE status = 'active' AND premium = 1`; you ask for **`😎 ➕ 🚀`**.

-----

## 🔑 Features: The Secret to World Domination

| Feature | Logic | EmojiQL Syntax |
| :--- | :--- | :--- |
| **Active/Premium** | Find all active, premium users. | `😎 ➕ 🚀` |
| **Not Deleted** | Find all users who are NOT deleted. | `❌💀` |
| **High Popularity** | Find users with high popularity (\> 100). | `🔥` |
| **AND / OR Logic** | Combines criteria. | `➕` (AND) / `➖` (OR) |
| **Nonsense Crypto** | The logic is so unconventional, it's virtually uncrackable by conventional pattern-matching algorithms. **It's the better crypto\!** | 📈🔒 |

-----

## 🛠️ How to Use PinkyDB

The engine is written in pure Python and uses a **JSON Lines (`.jsonl`)** format for data storage, making it inherently portable and simple.

### 1. **Setup**

The engine automatically creates the `./pinkydb_engine` directory to store your data.

```python
from pinkydb_engine import create_table, insert, select, schema

# Define the table schema (maps Emojis to real field names)
create_table("users", schema) 

# Insert data (using regular field names)
insert("users", {"name": "Brain", "status": "active", "premium": 1, "popularity": 150})
insert("users", {"name": "Pinky", "status": "active", "premium": 0, "popularity": 95})
```

### 2. **Querying (The Fun Part\!)**

Querying is done entirely via the **Emoji Query Language (EmojiQL)**.

```python
# Query 1: Active AND Premium
# SQL equivalent: WHERE status = 'active' AND premium = 1
results = select("users", "😎 ➕ 🚀")
print("Results for '😎 ➕ 🚀':", results)

# Query 2: NOT Deleted AND High Popularity
# SQL equivalent: WHERE NOT status = 'deleted' AND popularity > 100
results = select("users", "❌💀 ➕ 🔥")
print("Results for '❌💀 ➕ 🔥':", results)
```

-----

## ⚠️ Warning (The Honest Part)

This codebase was developed during intense bursts of creative energy, often resulting in developers **falling off their chairs laughing**.

  * **Testing:** Logic is **heavily tested** (by uncontrollable laughter).
  * **Known Feature:** Occasional developers may enter a **"Narf!"-state** upon successful query execution.

**If the logic seems too crazy to work, remember: it works because the logic is cleaner than 90% of the code on the internet!** Have Fun

#### Pinky

