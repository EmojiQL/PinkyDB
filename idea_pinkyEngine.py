# "NARF! Was wenn wir die Datenbank mit Emojis abfragen?!"

import os
import json
from datetime import datetime
from collections import defaultdict

# ==============================
# Config / Storage
# ==============================
DB_DIR = "./pinkydb_engine"
os.makedirs(DB_DIR, exist_ok=True)

# Emoji-Regeln (mit Werten!)
emoji_rules = {
    '😎': {'field': 'status', 'value': 'active', 'op': '=='},
    '😴': {'field': 'status', 'value': 'inactive', 'op': '=='},
    '💀': {'field': 'status', 'value': 'deleted', 'op': '=='},
    '🚀': {'field': 'premium', 'value': 1, 'op': '=='},
    '🔥': {'field': 'popularity', 'value': 100, 'op': '>'}
}

# Logik-Emojis
logic_emojis = {
    '➕': 'AND',
    '➖': 'OR',
    '❌': 'NOT'
}

# Tabellen + Indexe
tables = {}
indexes = defaultdict(lambda: defaultdict(set))

# ==============================
# Helper-Funktionen
# ==============================
def table_file(table_name):
    return os.path.join(DB_DIR, f"{table_name}.jsonl")

def index_file(table_name):
    return os.path.join(DB_DIR, f"{table_name}_idx.json")

def save_indexes(table_name):
    idx_data = {k: list(v) for k, v in indexes[table_name].items()}
    with open(index_file(table_name), 'w') as f:
        json.dump(idx_data, f)

def load_indexes(table_name):
    try:
        with open(index_file(table_name)) as f:
            idx_data = json.load(f)
            indexes[table_name] = {k: set(v) for k, v in idx_data.items()}
    except FileNotFoundError:
        pass

# ==============================
# Tabellenoperationen
# ==============================
def create_table(table_name, schema):
    """
    schema = {'emoji': 'field_name', ...}
    z.B. {'😎': 'status', '🚀': 'premium'}
    """
    if os.path.exists(table_file(table_name)):
        print(f"⚠️ Tabelle {table_name} existiert schon!")
        return
    with open(table_file(table_name), "w") as f:
        pass
    tables[table_name] = schema
    print(f"✅ Tabelle {table_name} erstellt mit Schema: {schema}")

def insert(table_name, data):
    """
    data = {field_name: value, ...}
    z.B. {'status': 'active', 'premium': 1}
    """
    if table_name not in tables:
        print(f"❌ Tabelle {table_name} existiert nicht!")
        return
    
    row_id = int(datetime.now().timestamp() * 1000)
    row = {"_id": row_id}
    row.update(data)
    
    # in Datei speichern
    with open(table_file(table_name), "a") as f:
        f.write(json.dumps(row) + "\n")
    
    save_indexes(table_name)
    print(f"📥 Zeile eingefügt: {row}")

# ==============================
# Query / SELECT mit Emoji-Matching
# ==============================
def match_rule(value, rule):
    """Prüft ob value der Regel entspricht"""
    if value is None:
        return False
    
    op = rule['op']
    target = rule['value']
    
    if op == '==':
        return value == target
    elif op == '>':
        return isinstance(value, (int, float)) and value > target
    elif op == '<':
        return isinstance(value, (int, float)) and value < target
    elif op == '>=':
        return isinstance(value, (int, float)) and value >= target
    elif op == '<=':
        return isinstance(value, (int, float)) and value <= target
    return False

def select(table_name, emoji_query=None):
    if table_name not in tables:
        print(f"❌ Tabelle {table_name} existiert nicht!")
        return []
    
    load_indexes(table_name)
    schema = tables[table_name]
    
    # Keine Query = alle Rows
    if not emoji_query:
        with open(table_file(table_name)) as f:
            return [json.loads(l) for l in f]
    
    tokens = emoji_query.split()
    result_sets = []
    current_logic = None
    current_not = False
    
    for token in tokens:
        if token in logic_emojis:
            if token == '❌':
                current_not = True
                continue
            current_logic = logic_emojis[token]
            continue
        
        if token in emoji_rules:
            rule = emoji_rules[token]
            field = rule['field']
            matching_ids = set()
            
            # Finde Rows die der Regel entsprechen
            with open(table_file(table_name)) as f:
                for line in f:
                    row = json.loads(line)
                    if match_rule(row.get(field), rule):
                        matching_ids.add(row["_id"])
            
            # NOT-Operator
            if current_not:
                all_ids = set()
                with open(table_file(table_name)) as f:
                    for line in f:
                        r = json.loads(line)
                        all_ids.add(r["_id"])
                matching_ids = all_ids - matching_ids
                current_not = False
            
            result_sets.append((current_logic or "AND", matching_ids))
    
    # Kombiniere Sets
    if not result_sets:
        return []
    
    current_set = result_sets[0][1].copy()
    for logic, s in result_sets[1:]:
        if logic == "AND":
            current_set &= s
        elif logic == "OR":
            current_set |= s
    
    # Fetch Rows
    rows = []
    with open(table_file(table_name)) as f:
        for line in f:
            row = json.loads(line)
            if row["_id"] in current_set:
                rows.append(row)
    return rows

# ==============================
# DEMO
# ==============================
schema = {
    '😎': 'status',
    '😴': 'status', 
    '💀': 'status',
    '🚀': 'premium',
    '🔥': 'popularity'
}
create_table("users", schema)

# Normale Field-Namen beim Insert!
insert("users", {"status": "active", "premium": 1, "popularity": 150})
insert("users", {"status": "active", "premium": 0, "popularity": 95})
insert("users", {"status": "inactive", "premium": 1, "popularity": 120})
insert("users", {"status": "deleted", "premium": 0, "popularity": 10})

# Query mit Emojis!
res = select("users", "😎 ➕ 🚀")
print("\n🔍 Ergebnisse für '😎 ➕ 🚀' (active AND premium):")
for r in res:
    print(r)

res2 = select("users", "😎 ➖ 💀")
print("\n🔍 Ergebnisse für '😎 ➖ 💀' (active OR deleted):")
for r in res2:
    print(r)

res3 = select("users", "❌💀 ➕ 🚀")
print("\n🔍 Ergebnisse für '❌💀 ➕ 🚀' (NOT deleted AND premium):")
for r in res3:
    print(r)

res4 = select("users", "🔥")
print("\n🔍 Ergebnisse für '🔥' (popularity > 100):")
for r in res4:
    print(r)
