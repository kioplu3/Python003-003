#!/usr/bin/env python
# coding=utf-8


import os
import numpy as np
import pandas as pd

pwd = os.path.dirname(os.path.realpath(__file__))
book = os.path.join(pwd, 'book_utf8.csv')
df = pd.read_csv(book)


# 1. select * From data;
print(df)

# 2. select * From data Limit 10;
print(df.head(10))

# 3. SELECT id FROM data;  //id 是 data 表的特定一列
df.columns = ['star', 'vote', 'shorts']
print(df['star'])

# 4. 4. SELECT COUNT(id) FROM data;
print(df['star'].count())

# 5.SELECT * FROM data WHERE id<1000 AND age>30;
print(df.query('vote > 4 & star == "还行"'))

# 6. SELECT id,COUNT(DISTINCT order_id) FROM table1 GROUP BY id;
df2 = df.drop_duplicates(['vote', 'star'])
print(df2.groupby('star').vote.size())


# SELECT * FROM table1 t1 INNER JOIN table2 t2 ON t1.id = t2.id;

df3 = pd.DataFrame({'a': np.random.randint(10, size=4)})
print(df3)
df4 = pd.DataFrame({'a': np.random.randint(
    10, size=100), 'b': np.random.randn(100)})
print(df4)

print(pd.merge(df3, df4, on='a'))


# 8. SELECT * FROM table1 UNION SELECT * FROM table2;
df5 = pd.DataFrame({'a': np.random.randint(100,
                                           10000, size=100), 'b': np.random.randn(100)})
print(pd.concat([df4, df5]))

# 9. DELETE FROM table1 WHERE id=10;

df9 = df.loc[df['star'] != "较差"]
print(df9)

# 10. ALTER TABLE table1 DROP COLUMN column_name;
print(df9.drop('star', axis=1))
