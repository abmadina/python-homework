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

# NOTE: Many public Titanic files encode Survived as 0 = did not survive, 1 = survived.
# If your file uses opposite encoding, invert the comparisons below.
# We'll assume Survived == 1 => survived.
#
# 1. Select Female Passengers in Class 1 with Ages between 20 and 30:
mask_female = td['Sex'].str.lower() == 'female'
mask_class1 = td['Pclass'] == 1
mask_age_20_30 = (td['Age'] >= 20) & (td['Age'] <= 30)
female_class1_20_30 = td[mask_female & mask_class1 & mask_age_20_30]
print("T1) Female Passengers in Class 1 with ages 20-30:", female_class1_20_30.shape[0])
print(female_class1_20_30.head(), '\n')

# 2. Filter Passengers Who Paid More than $100:
paid_over_100 = td[td['Fare'] > 100]
print("T2) Passengers who paid > $100:", paid_over_100.shape[0])
print(paid_over_100.head(), '\n')

# 3. Select Passengers Who Survived and Were Alone:
# Alone: SibSp == 0 and Parch == 0
survived_and_alone = td[(td['Survived'] == 1) & (td['SibSp'] == 0) & (td['Parch'] == 0)]
print("T3) Survived and traveling alone:", survived_and_alone.shape[0])
print(survived_and_alone.head(), '\n')

# 4. Filter Passengers Embarked from 'C' and Paid More Than $50:
embarked_c_paid_gt_50 = td[(td['Embarked'].fillna('') == 'C') & (td['Fare'] > 50)]
print("T4) Embarked from C and paid > $50:", embarked_c_paid_gt_50.shape[0])
print(embarked_c_paid_gt_50.head(), '\n')

# 5. Select Passengers with Siblings or Spouses AND Parents or Children:
both_sibsp_parch = td[(td['SibSp'] > 0) & (td['Parch'] > 0)]
print("T5) Passengers with both SibSp>0 and Parch>0:", both_sibsp_parch.shape[0])
print(both_sibsp_parch.head(), '\n')

# 6. Filter Passengers Aged 15 or Younger Who Didn't Survive:
# "Didn't survive" -> Survived == 0 (assuming standard encoding)
kids_didnt_survive = td[(td['Age'] <= 15) & (td['Survived'] == 0)]
print("T6) Age <=15 and did not survive:", kids_didnt_survive.shape[0])
print(kids_didnt_survive.head(), '\n')

# 7. Select Passengers with Cabins and Fare Greater Than $200:
has_cabin_and_fare_gt_200 = td[td['Cabin'].notna() & (td['Fare'] > 200)]
print("T7) Passengers with cabin and fare > $200:", has_cabin_and_fare_gt_200.shape[0])
print(has_cabin_and_fare_gt_200.head(), '\n')

# 8. Filter Passengers with Odd-Numbered Passenger IDs:
odd_passengerid = td[td['PassengerId'] % 2 == 1]
print("T8) Odd PassengerId count:", odd_passengerid.shape[0])
print(odd_passengerid.head(), '\n')

# 9. Select Passengers with Unique Ticket Numbers:
# Identify tickets that occur only once and keep those rows
ticket_counts = td['Ticket'].value_counts(dropna=False)
unique_ticket_mask = td['Ticket'].isin(ticket_counts[ticket_counts == 1].index)
unique_ticket_passengers = td[unique_ticket_mask]
print("T9) Passengers with unique ticket numbers:", unique_ticket_passengers.shape[0])
print(unique_ticket_passengers.head(), '\n')

# 10. Filter Passengers with 'Miss' in Their Name and Were in Class 1:
# also restrict to female (you requested "female passengers having 'Miss' in their name")
miss_class1_female = td[
    td['Name'].fillna('').str.contains('Miss', case=True, na=False) &
    (td['Pclass'] == 1) &
    (td['Sex'].str.lower() == 'female')
]
print("T10) Female 'Miss' in name and Pclass==1:", miss_class1_female.shape[0])
print(miss_class1_female.head(), '\n')

# Optionally save results:
# female_class1_20_30.to_csv('t1_female_class1_20_30.csv', index=False)
# survived_and_alone.to_csv('t3_survived_and_alone.csv', index=False)
