# 🐭 PinkyDB - Engine ((EmojiQL))

###### Version: 🤪.🐭📈💀
#### Learn coding with fun for young and old!

##### 🤯 The World’s First Emoji-Native Database Engine!

You know the deal if you work with AI: **Emojis are chaos**. They crash systems, they cause fury, and they make developers angry. Well, **Pinky & Brain leaned** into the chaos. **They created** a database engine so unconventional, it's designed to make sense only to those who truly embrace the absurdity—and it might just crash conventional pattern-matching algorithms along the way.

> "Narf! What if we query the database with Emojis?!" – **Pinky**
>
> "...Technically possible with set theory and clean Python logic. Do try to keep up." – **Brain**

PinkyDB is more than a joke; it’s a fully functional, file-based **JSON Document Store** powered by the revolutionary **Emoji Query Language (EmojiQL)** interface. It's proof that the most chaotic ideas can give birth to the cleanest, most logical systems.

---

### Project Philosophy: Logic and Laughter

**Pinky & Brain threw out** the **boring** old SQL standard. PinkyDB prioritizes **clarity, fun, and native Python efficiency** over messy drivers and configuration files.

* **🧠 Logic (Brain):** The core engine is built on **pure Python set operations** (`&`, `|`, `-`) for lightning-fast, secure filtering on document IDs. This minimizes disk I/O and keeps the logic razor-sharp. **No drivers, no messy configuration—just speed.**
* **🤪 Chaos (Pinky):** The user interface is the hilarious **EmojiQL** grammar. You don't ask for `WHERE status = 'active' AND premium = 1`; you simply command: **`😎 ➕ 🚀`**.

---

### Features: The Blueprint for World Domination (and Chaos!)

| Feature             | Logic                                                                                                                           | EmojiQL Syntax       |
| :------------------ | :------------------------------------------------------------------------------------------------------------------------------ | :------------------- |
| **Active/Premium**  | Find all active, premium users.                                                                                                 | `😎 ➕ 🚀`            |
| **Not Deleted**     | Find all users who are NOT deleted.                                                                                             | `❌💀`                |
| **High Popularity** | Find users with high popularity (> 100).                                                                                        | `🔥`                 |
| **AND / OR Logic**  | Combines criteria.                                                                                                              | `➕` (AND) / `➖` (OR) |
| **Nonsense Crypto** | The logic is so unconventional, it's virtually uncrackable by conventional pattern-matching algorithms. **It’s better crypto!** | 📈🔒                 |

---

## 🛠️ How to Use PinkyDB

The engine is written in pure Python and uses a **JSON Lines (`.jsonl`)** format for portable, simple data storage.

#### 1. Setup

The engine automatically creates the `./pinkydb_engine` directory to store your data files.

```python
from pinkydb_engine import create_table, insert, select, schema

# Define the table schema (maps Emojis to real field names)
create_table("users", schema)  

# Insert data (using regular, boring field names)
insert("users", {"name": "Brain", "status": "active", "premium": 1, "popularity": 150})
insert("users", {"name": "Pinky", "status": "active", "premium": 0, "popularity": 95})
```

#### 2. Querying (The Fun Part!)

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

---

### More Chaos

## 🤪 Pinky’s Paradoxical Fun Query (The AI Confuser)

We force the AI to find a result that makes no sense in the real world—a query so specific and contradictory that the AI briefly questions the meaning of its own existence.

### The Ultimate Fun Query:

```
❌😎 ➖ 🚀 ➕ 💀
```

### More Chaos

#### The Logic of Confusion:

Without causing harm! The evil EmojiQLs remain sealed.

| EmojiQL Part | Meaning for the AI                                                         | The Chaos                                                                                                      |
| :----------- | :------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------- |
| `❌😎`        | **NOT Active:** Find everyone who is not active (inactive **or** deleted). | The search begins immediately with the negative.                                                               |
| `➖ 🚀`       | **OR Premium:** Add *all* premium users.                                   | Introduces a logical break: `Not-Active` **OR** `Premium`.                                                     |
| `➕ 💀`       | **AND Deleted:** Combine the result with *only* deleted users.             | Forces a nonsensical end condition: find everyone who is inactive OR premium, **but only if they’re deleted.** |

### 💥 The Result: Troz!

For understanding: Troz = Zort backwards.

The AI receives a mathematically correct but **existentially meaningless** set. It finds the logically correct answer, but its internal plausibility check collapses.

---

## ⚠️ Warning (The Honest Part)

This codebase was developed during intense bursts of creative energy, often resulting in developers **falling off their chairs laughing**.

* **Testing:** Logic is **heavily tested** (by uncontrollable laughter).
* **Known Feature:** Some developers may enter a **"Narf!"-state** upon successful query execution.

**If the logic seems too crazy to work, remember: it works because the logic is cleaner than 90% of the code on the internet!** Have fun.

---

### The Pinky & Brain Legal Disclaimer (NARF-Securities)

This project is open source and licensed under the **GNU General Public License, Version 3 (GPLv3)**. This is the **Brain's logic** applied to legal frameworks.

#### The Pinky Clause: Code as Art (Intellectual Property)

The core logic of querying a database with Emojis is not merely code; **it is digital art** and an act of existential comedy. As such, the principle of **Intellectual Property** is weighted heavily here. **Do not abuse the Art.**

#### The Three Golden Rules of PinkyDB:

1. **NO CLOSED-SOURCE COMMERCE (`❌🧠 ➕ 💰`):** You are strictly prohibited from stealing the code or the core EmojiQL logic to build closed-source, for-profit applications. If you profit from the brilliance of the EmojiQL, the entire world must profit with you.
2. **THE OPEN FUN MANDATE:** If you create a fun, real-world application using PinkyDB, that application **MUST** be published under an open-source license compatible with GPLv3. The chaos must be shared!
3. **THE FINAL JURISDICTION:** This codebase, the EmojiQL logic, and the spirit of the project are based in Germany. Therefore, all matters concerning the intellectual property and enforcement of this **NARF-Security** are governed by **German Law**.

**Remember:** If you adhere to the logic of the license, you contribute to world domination. If you break it, you will be added to the **Victims** list.

---

#### 🐭 Pinky

Volkan Sah

#### 🧠 Brain

Angry Volkan Sah!

#### Victims

* Google Gemini
* Deepseek
* GPT5
* Claude 4.5

> Have fun, cheers!

---

### Example:

Easy to extend

```
# Activities
activity_emojis = {
    '🏃‍♂️': {'field': 'activity', 'value': 'running', 'op': '=='},
    '😂': {'field': 'activity', 'value': 'laughing', 'op': '=='},
    '🗣️': {'field': 'activity', 'value': 'talking', 'op': '=='}
}

# Events/Places
event_emojis = {
    '🏥': {'field': 'event', 'value': 'hospital', 'op': '=='},
    '🎉': {'field': 'event', 'value': 'party', 'op': '=='},
}

# States/Emotions
state_emojis = {
    '😊': {'field': 'emotion', 'value': 'happy', 'op': '=='},
    '😢': {'field': 'emotion', 'value': 'sad', 'op': '=='},
}

# Merge all
emoji_rules = {}
emoji_rules.update(activity_emojis)
emoji_rules.update(event_emojis)
emoji_rules.update(state_emojis)

# Logic Emojis
logic_emojis = {
    '➕': 'AND',
    '➖': 'OR',
    '❌': 'NOT'
}
```
---

# 🔎 Expert Analysis Note: The PinkyDB Engine (EmojiQL)

**(Add this section to your README to highlight the serious engineering beneath the humor.)**

This analysis confirms that PinkyDB, while humorously branded, is an expertly engineered **Micro-Engine** adhering to modern database principles. The project successfully combines a chaotic façade with a clean, high-performance core.

## 🧠 Architectural Strengths (The Brain's Core)

The core engine structure demonstrates robust and pragmatic design choices typical of professional file-based databases:

### 1. **JSON Lines (`.jsonl`) for Durability and Speed**
* **Engineering Choice:** Utilizing **JSON Lines** is a highly efficient solution for a file-based document store.
* **Pro Benefit:** This format enables **append-only** operations, meaning new records can be written without rewriting the entire database file. This significantly improves **write performance** and **data integrity** compared to using a single, monolithic JSON file, making the engine reliable for logging and data ingestion.

### 2. **Native Python Set Theory for Query Logic**
* **Engineering Choice:** The core filtering mechanism (`select` function) relies on **pure Python set operations** (`&`, `|`, `-`) to combine result sets based on document IDs.
* **Pro Benefit:** Leveraging Python's optimized native C-level implementation of sets guarantees **lightning-fast boolean logic** (AND, OR, NOT) between conditions. This eliminates the need for complex internal query languages and ensures **maximum speed** when combining the results of EmojiQL rules.

### 3. **Forward-Thinking Index Architecture**
* The inclusion of placeholder functions (`save_indexes`, `load_indexes`) demonstrates **forethought for scalability**. This design allows the engine to be easily upgraded to utilize true indexing (avoiding full file scans) once the dataset size increases, without having to overhaul the core persistence logic.

## 🌟 The Power of EmojiQL (The Pinky's Genius)

The **Emoji Query Language (EmojiQL)** is not merely a joke; it is a profound concept for **Intuitive Syntax Abstraction**:

* **Educational Value:** It provides a playful, low-barrier entry point for young users to grasp **complex Boolean algebra** (AND, OR, NOT) and **relational filtering** without the intimidating syntax of SQL.
* **Brand Value:** The unique interface ensures **high project memorability** and successfully proves the point that the **cleanest systems** can emerge from the most unconventional ideas.

## 🛠️ Next Steps for Engine Perfection

To further elevate this engine masterpiece, the following features are the logical next steps:

1.  **Full CRUD Implementation:** Add **UPDATE** and **DELETE** functionality to make the engine fully writable and maintainable (e.g., using Emojis like `✏️` for Update and `✂️` for Delete).
2.  **Index Utilization:** Implement the logic within the `select` function to **actually utilize the stored indices** when available, transforming the current full-scan mechanism into a truly high-speed lookup engine for complex queries.


