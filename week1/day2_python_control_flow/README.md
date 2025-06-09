# 🚦 Day 2 – Python Control Flow Challenges

---

## ⚔️ Challenge 3 – Contains Duplicate (LeetCode)

**🔗 Source:** [Contains Duplicate – LeetCode](https://leetcode.com/problems/contains-duplicate/)

### 🧠 Problem Statement:
Given an array of integers `nums`, determine if any value appears at least twice in the array.

### 🚀 Solution Strategy:
- Use a set to track seen numbers.
- If a number is already in the set, return True (duplicate found).
- Otherwise, add the number to the set and continue.
- If no duplicates are found, return False.

### 📌 Key Concepts:
- Sets for fast membership checking
- Looping and early exit

---

## ⚔️ Challenge 4 – Valid Anagram (LeetCode)

**🔗 Source:** [Valid Anagram – LeetCode](https://leetcode.com/problems/valid-anagram/)

### 🧠 Problem Statement:
Given two strings `s` and `t`, determine if `t` is an anagram of `s` (i.e., both strings contain the same characters with the same frequency).

### 🚀 Solution Strategy:
- Use a dictionary to count character frequencies in `s`.
- Decrement counts while iterating through `t`.
- If a character is missing or count goes negative, return False.
- If all counts are zero at the end, return True.

### 📌 Key Concepts:
- Dictionaries for frequency counting
- String iteration and comparison
- Early exit for efficiency

---

## 📊 Summary of Learnings – Day 2

| Language | Concept           | Key Skills Practiced                |
|----------|-------------------|-------------------------------------|
| Python   | Sets, Dictionaries| Membership test, frequency counting |
| Python   | Control Flow      | Loops, conditionals, early return   |

- Practiced using sets and dictionaries for efficient lookups.
- Reinforced control flow with loops and conditionals.
- Learned to solve common interview problems with clean, efficient code.

---

## 🧪 How to Run

```bash
# Run Challenge 3 – Contains Duplicate
python3 challenge3.py

# Run Challenge 4 – Valid Anagram
python3 challenge4.py
```
