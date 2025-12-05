# Combined script for Homework 2 (StackOverflow) and Homework 3 (Titanic)
import pandas as pd
import numpy as np

# -----------------------------
# Homework 2: StackOverflow QA
# -----------------------------
df = pd.read_csv('task\\stackoverflow_qa.csv')

# make a working copy and parse dates
df2 = df.copy()
df2['creationdate'] = pd.to_datetime(df2['creationdate'], errors='coerce')

# 1. Find all questions that were created before 2014
before_2014 = df2[df2['creationdate'] < pd.Timestamp('2014-01-01')]
print("1) Questions created before 2014:", before_2014.shape[0])
print(before_2014.head(), '\n')

# 2. Find all questions with a score more than 50
score_gt_50 = df2[df2['score'] > 50]
print("2) Questions with score > 50:", score_gt_50.shape[0])
print(score_gt_50.head(), '\n')

# 3. Find all questions with a score between 50 and 100 (inclusive boundaries: change if you want exclusive)
score_50_100 = df2[(df2['score'] >= 50) & (df2['score'] <= 100)]
print("3) Questions with score between 50 and 100:", score_50_100.shape[0])
print(score_50_100.head(), '\n')

# 4. Find all questions answered by Scott Boston
# handle NaN safely:
answered_by_scott = df2[df2['ans_name'].fillna('').str.strip().eq('Scott Boston')]
print("4) Questions answered by Scott Boston:", answered_by_scott.shape[0])
print(answered_by_scott.head(), '\n')

# 5. Find all questions answered by the following 5 users
# Replace the list below with the actual five usernames you want to search for.
users_to_find = ['UserA', 'UserB', 'UserC', 'UserD', 'UserE']
answered_by_users = df2[df2['ans_name'].fillna('').isin(users_to_find)]
print(f"5) Questions answered by users {users_to_find}:", answered_by_users.shape[0])
print(answered_by_users.head(), '\n')

# 6. Find all questions that were created between March 2014 and October 2014,
#    answered by Unutbu and have score less than 5.
start = '2014-03-01'
end   = '2014-10-31'  # inclusive
mask_date = (df2['creationdate'] >= pd.Timestamp(start)) & (df2['creationdate'] <= pd.Timestamp(end))
mask_answered_unutbu = df2['ans_name'].fillna('').str.strip().eq('Unutbu')
mask_score_lt_5 = df2['score'] < 5
q6 = df2[mask_date & mask_answered_unutbu & mask_score_lt_5]
print("6) Questions Mar-Oct 2014 answered by Unutbu with score < 5:", q6.shape[0])
print(q6.head(), '\n')

# 7. Find all questions that have score between 5 and 10 OR have viewcount > 10,000
mask_score_5_10 = (df2['score'] >= 5) & (df2['score'] <= 10)
mask_view_gt_10000 = df2['viewcount'] > 10000
q7 = df2[mask_score_5_10 | mask_view_gt_10000]
print("7) Questions with score 5-10 OR viewcount > 10,000:", q7.shape[0])
print(q7.head(), '\n')

# 8. Find all questions that are NOT answered by Scott Boston
# This includes rows where ans_name is NaN (they are obviously not answered by Scott Boston).
not_answered_by_scott = df2[~df2['ans_name'].fillna('').str.strip().eq('Scott Boston')]
print("8) Questions NOT answered by Scott Boston:", not_answered_by_scott.shape[0])
print(not_answered_by_scott.head(), '\n')

# Optional: if you want to save results to csv files:
# before_2014.to_csv('before_2014.csv', index=False)
# answered_by_scott.to_csv('answered_by_scott.csv', index=False)
# etc.

# -----------------------------
# Homework 3: Titanic dataset
# -----------------------------
titanic_df = pd.read_csv("task\\titanic.csv")
td = titanic_df.copy()

# Clean column names for convenience (optional)
td.columns = [c.strip() for c in td.columns]

# Some helper: ensure numeric types for Age, Fare, SibSp, Parch, PassengerId
td['Age'] = pd.to_numeric(td['Age'], errors='coerce')
td['Fare'] = pd.to_numeric(td['Fare'], errors='coerce')
td['SibSp'] = pd.to_numeric(td['SibSp'], errors='coerce')
td['Parch'] = pd.to_numeric(td['Parch'], errors='coerce')
td['PassengerId'] = pd.to_numeric(td['PassengerId'], errors='coerce')

# NOTE: Many public Titanic files encode Survived as 0 =
