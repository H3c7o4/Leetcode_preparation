#!/usr/bin/env python3
"""
Table: Person

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| email       | varchar |
+-------------+---------+
id is the primary key (column with unique values) for this table.
Each row of this table contains an email. The emails will not contain uppercase letters.
"""
import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    duplicate_emails = person[person.duplicated('email', keep=False)]['email'].drop_duplicates()
    result = pd.DataFrame({'Email': duplicate_emails})
    return result
