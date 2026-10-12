import sqlite3
import pandas as pd

conn = sqlite3.connect("titanic_clean.db")

query = "SELECT isalone, ROUND(AVG(survived), 2) AS rate, COUNT(*) AS n FROM passengers GROUP BY isalone"
print(pd.read_sql(query, conn))


print("Next query")

query = """
SELECT pclass, isalone, ROUND(AVG(survived), 2) AS rate, COUNT(*) AS n
FROM passengers
GROUP BY pclass, isalone
"""
print(pd.read_sql(query, conn))

conn.close()