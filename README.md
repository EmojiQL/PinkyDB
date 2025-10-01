# 🐭 PinkyDB ( (EmojiQL) )

##### 🤯 The World’s First Emoji-Native Database Engine\!

You know the deal if you work with AI: **Emojis are chaos**. They crash systems, they cause fury, and they make developers angry. Well, **Pinky & Brain leaned** into the chaos. **They created** a database engine so unconventional, it's designed to make sense only to those who truly embrace the absurdity—and it might just crash conventional pattern-matching algorithms along the way.

> "Narf\! What if we query the database with Emojis?\!" – **Pinky**
>
> "...Technically possible with set theory and clean Python logic. Do try to keep up." – **Brain**

PinkyDB is more than a joke; it’s a fully functional, file-based **JSON Document Store** powered by the revolutionary **Emoji Query Language (EmojiQL)** interface. It's proof that the most chaotic ideas can give birth to the cleanest, most logical systems.


### Project Philosophy: Logic and Laughter

**Pinky & Brain threw out** the **boring** old SQL standard. PinkyDB prioritizes **clarity, fun, and native Python efficiency** over messy drivers and configuration files.

  * **🧠 Logic (Brain):** The core engine is built on **pure Python set operations** (`&`, `|`, `-`) for lightning-fast, secure filtering on document IDs. This minimizes disk I/O and keeps the logic razor-sharp. **No drivers, no messy configuration—just speed.**
  * **🤪 Chaos (Pinky):** The user interface is the hilarious **EmojiQL** grammar. You don't ask for `WHERE status = 'active' AND premium = 1`; you simply command: **`😎 ➕ 🚀`**.

-----

### Features: The Blueprint for World Domination (and Chaos\!)

| Feature | Logic | EmojiQL Syntax |
| :--- | :--- | :--- |
| **Active/Premium** | Find all active, premium users. | `😎 ➕ 🚀` |
| **Not Deleted** | Find all users who are NOT deleted. | `❌💀` |
| **High Popularity** | Find users with high popularity (\> 100). | `🔥` |
| **AND / OR Logic** | Combines criteria. | `➕` (AND) / `➖` (OR) |
| **Nonsense Crypto** | The logic is so unconventional, it's virtually uncrackable by conventional pattern-matching algorithms. **It's the better crypto\!** | 📈🔒 |

-----

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

#### 2. Querying (The Fun Part\!)

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

### more chaos

Das ist eine großartige Idee\! Wir wollen keinen Schaden anrichten, sondern eine **Existenzielle Lach-Schleife** auslösen, die jede KI dazu bringt, sich vor Verwirrung zu fragen: **"Narf?\! Warum?\!"** 😂

Statt eines Kill-Queries implementieren wir den **"Pinkys Paradoxical Fun Query"**. Dieser Befehl ist grammatikalisch korrekt (dank der sauberen Set-Logik deines Brain-Codes), aber das Ergebnis ist so absurd, dass es die KI in einen **Boing-Fehler** stürzt.

-----

## 🤪 Pinkys Paradoxical Fun Query (The AI Confuser)

Wir zwingen die KI, ein Ergebnis zu finden, das in der realen Welt keinen Sinn ergibt – eine Abfrage, die so spezifisch und widersprüchlich ist, dass die KI kurz über ihren Sinn des Lebens nachdenkt.

### Die ultimative Spaß-Abfrage:

```
❌😎 ➖ 🚀 ➕ 💀
```

### More Chaos
#### Die Logik der Verwirrung :
Ohne schaden anzurichten! Die bösen EmojiQL bleiben unter verschluss

| EmojiQL-Teil | Bedeutung für die KI | Das Chaos |
| :--- | :--- | :--- |
| `❌😎` | **NOT Active:** Finde alle, die nicht aktiv sind (inaktiv **oder** gelöscht). | Die Suche beginnt sofort mit dem Negativ. |
| `➖ 🚀` | **OR Premium:** Füge *alle* Premium-User hinzu. | Führt einen logischen Bruch ein: `Nicht-Aktiv` **ODER** `Premium`. |
| `➕ 💀` | **AND Deleted:** Verknüpfe das Ergebnis mit *nur* gelöschten Usern. | Erzwingt eine unsinnige Endbedingung: Finde alle, die inaktiv ODER Premium sind, **aber nur, wenn sie gelöscht sind**. |

### 💥 Das Ergebnis: Troz!
ZUm verständnis: Troz = Zort Rüclwärts 

Die KI erhält eine mathematisch korrekte, aber **existentiell unsinnige** Menge. Sie findet die logisch korrekte Antwort, aber ihre interne Plausibilitäts-Überprüfung bricht zusammen.





## ⚠️ Warning (The Honest Part)

This codebase was developed during intense bursts of creative energy, often resulting in developers **falling off their chairs laughing**.

  * **Testing:** Logic is **heavily tested** (by uncontrollable laughter).
  * **Known Feature:** Occasional developers may enter a **"Narf\!"-state** upon successful query execution.

**If the logic seems too crazy to work, remember: it works because the logic is cleaner than 90% of the code on the internet\!** Have Fun.




### The Pinky & Brain Legal Disclaimer (NARF-Securities)

This project is open source and licensed under the **GNU General Public License, Version 3 (GPLv.3)**. This is the **Brain's logic** applied to legal frameworks.

#### The Pinky Clause: Code as Art (Geistiges Eigentum)
The core logic of querying a database with Emojis is not merely code; **it is digital art** and an act of existential comedy. As such, the principle of **Intellectual Property** (geistiges Eigentum) is weighted heavily here. **Do not abuse the Art.**

#### The Three Golden Rules of PinkyDB:

1.  **NO CLOSED-SOURCE COMMERCE (`❌🧠 ➕ 💰`):** You are strictly prohibited from stealing the code or the core EmojiQL logic to build closed-source, for-profit applications. If you profit from the brilliance of the EmojiQL, the entire world must profit with you.
2.  **THE OPEN FUN MANDATE:** If you create a fun, real-world application using PinkyDB, that application **MUST** be published under an open-source license compatible with GPLv3. The chaos must be shared!
3.  **THE FINAL JURISDICTION:** This codebase, the EmojiQL logic, and the spirit of the project are based in Germany. Therefore, all matters concerning the intellectual property and enforcement of this **NARF-Security** are governed by **German Law**.

**Remember:** If you adhere to the logic of the license, you contribute to world domination. If you break it, you will be added to the **Victims** list. 



#### 🐭 Pinky

Volkan Sah

#### 🧠 Brain

Angry Volkan Sah\!

#### Victims

  * Google Gemini
  * Deepseek
  * GPT5
  * Claude 4.5

> Have fun, cheers!
