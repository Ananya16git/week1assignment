#!/usr/bin/env python
# coding: utf-8

# In[8]:


import sqlite3
import pandas as pd


# In[ ]:


conn = sqlite3.connect("week1_database.db")  # Creates or connects to a database.
cursor = conn.cursor()  # Create a cursor to interact with the database


# In[3]:


# table creation in week1_database
cursor.execute("""
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER,
    department TEXT
)
""")
conn.commit()  # Save changes


# In[6]:


# insert into employees table
cursor.execute("INSERT INTO employees (name, age, department) VALUES (?, ?, ?)", 
               ("Alice", 30, "HR"))
cursor.execute("INSERT INTO employees (name, age, department) VALUES (?, ?, ?)", 
               ("Bob", 25, "IT"))
conn.commit()


# In[13]:


# iterating through cursor
cursor.execute("SELECT * FROM employees")
rows = cursor.fetchall()
for row in rows:
    print(row)


# In[10]:


# Sample employee data
data = {
    "id": [5,6,7],
    "name": ["Ananya", "charan", "Gunakshi"],
    "age": [35, 36, 6],
    "department": ["HR", "IT", "Finance"]
}
# creating panda data frame
df = pd.DataFrame(data)
print(df)


# In[14]:


# saving panda data frame to in the sqllite data base
df.to_sql("employees", conn, if_exists='append', index=False)

print("Data stored in SQLite successfully!")


# In[17]:


# fetching data from sqllite
cursor.execute("select * from employees")
rows = cursor.fetchall()
for row in rows:
  print(row)


# In[ ]:




