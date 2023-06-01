import sqlite3 as sq

def new(args):
    with sq.connect("notes.db") as con:
        cur = con.cursor()
        cur.execute(f'SELECT * FROM types WHERE type = "{args["type"]}"')
        # print(cur)
        f = 1
        for item in cur:
            f = 0
        if f:
            cur.execute(f"""INSERT INTO types (type) VALUES('{args["type"]}')""")

        cur.execute(f'INSERT INTO notes (note, date, done) VALUES("{args["note"]}", "{args["date"]}", 0)')
        # INSERT INTO users (name, old, score) VALUES('Igor', 22, 1000)

def get_any_notes(date, category):
    if category == 'all':
        return get_notes(date)
    else:
        return get_notes_with_category(date, category)

def get_notes(date):
    # print(date)
    with sq.connect("notes.db") as con:
        cur = con.cursor()
        # print(date)
        cur.execute(f'SELECT * FROM notes WHERE date LIKE "{date}"')
        # print("qq", *cur)
        res = []
        # print(list(cur))
        for item in cur:
            res.append(item[1])
        return res

def get_notes_with_category(date, category):
    with sq.connect("notes.db") as con:
        cur = con.cursor()
        type_id = cur.execute(f'SELECT * FROM types WHERE type = "{category}"')
        type_id = list(type_id)
        type_id = type_id[0][0]
        cur.execute(f'SELECT * FROM notes WHERE date LIKE "{date}" AND type_id = "{type_id}"')
        res = []
        for item in cur:
            res.append(item[1])
        return res

def get_category():
    with sq.connect("notes.db") as con:
        cur = con.cursor()
        # print(date)
        cur.execute(f'SELECT type FROM types')
        # print("qq", *cur)
        res = []
        for item in cur:
            print(item)
            res.append(item[0])
        return res




with sq.connect("notes.db") as con:
    cur = con.cursor()

    # cur.execute("DROP TABLE IF EXISTS notes")
    # cur.execute("PRAGMA foreign_keys = ON;")
    cur.execute("""CREATE TABLE IF NOT EXISTS notes (
    id INTEGER  NOT NULL  PRIMARY KEY AUTOINCREMENT,
    note TEXT NOT NULL,
    date TEXT NOT NULL,
    done INTEGER NOT NULL DEFAULT 0,
    type_id INTEGER,
    FOREIGN KEY(type_id) REFERENCES types(id)
    )
    """)

    # cur.execute("DROP TABLE IF EXISTS types")
    cur.execute("""CREATE TABLE IF NOT EXISTS types (
    id INTEGER  NOT NULL  PRIMARY KEY AUTOINCREMENT,
    type TEXT NOT NULL
    )
    """)
    