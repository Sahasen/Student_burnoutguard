import sqlite3, os

DB = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'database', 'burnout.db')
if not os.path.exists(DB):
    raise SystemExit(f'Database not found at: {DB}')

c = sqlite3.connect(DB)
print('Database file:', DB, '\n')

tables = [r[0] for r in c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%'")]
for t in tables:
    n = c.execute(f'SELECT COUNT(*) FROM {t}').fetchone()[0]
    print(f'Table {t}: {n} rows')

def show(title, sql):
    print(f'\n--- {title} ---')
    rows = c.execute(sql).fetchall()
    if not rows: print('(empty)')
    for r in rows: print(r)

show('USERS (id, username, email, created_at)', 'SELECT id, username, email, created_at FROM users')
show('PREDICTIONS (user_id, week, risk, time)', 'SELECT user_id, week_number, predicted_risk, predicted_at FROM predictions ORDER BY user_id, week_number')
if 'notification_log' in tables:
    show('EMAILS LOG (user_id, type, week, sent_at, success)', 'SELECT user_id, notif_type, week_number, sent_at, success FROM notification_log')
c.close()