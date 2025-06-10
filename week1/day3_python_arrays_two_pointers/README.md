# 🌀 Day 3 – Python Arrays & Two Pointers Challenges

---

## ⚔️ Challenge 6 – Two Sum II (LeetCode)

**🔗 Source:** [Two Sum II – LeetCode](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)

### 🧠 Problem Statement:
Given a sorted array of integers `numbers` and an integer `target`, return the 1-based indices of the two numbers such that they add up to `target`.

### 🚀 Solution Strategy:
- Use the two-pointer technique: start with one pointer at the beginning and one at the end.
- Move pointers inward based on the sum compared to the target.
- Return indices as soon as the pair is found.

### 📌 Key Concepts:
- Two-pointer technique for sorted arrays
- Efficient O(n) search for pairs
- 1-based index output

---

## ⚔️ Challenge 7 – Valid Palindrome (LeetCode)

**🔗 Source:** [Valid Palindrome – LeetCode](https://leetcode.com/problems/valid-palindrome/)

### 🧠 Problem Statement:
Check if a string is a palindrome, ignoring non-alphanumeric characters and case.

### 🚀 Solution Strategy:
- Clean the string by removing non-alphanumeric characters and converting to lowercase.
- Use two pointers to compare characters from both ends.
- Return True if all pairs match, False otherwise.

### 📌 Key Concepts:
- String cleaning and normalization
- Two-pointer palindrome check
- Handling edge cases (empty string, punctuation)

---

## ⚔️ Challenge 8 – Container With Most Water (LeetCode)

**🔗 Source:** [Container With Most Water – LeetCode](https://leetcode.com/problems/container-with-most-water/)

### 🧠 Problem Statement:
Given an array `height` where each element represents the height of a vertical line on the x-axis, find the maximum area of water a container can store using any two lines.

### 🚀 Solution Strategy:
- Use two pointers, one at the start and one at the end of the array.
- Calculate the area between the two lines and update the maximum area found.
- Move the pointer pointing to the shorter line inward to try to find a larger area.
- Continue until the pointers meet.

### 📌 Key Concepts:
- Two-pointer technique for maximizing area
- Greedy approach for optimal solution
- Efficient O(n) time complexity

---

## 📊 Summary of Learnings – Day 3

| Language | Concept         | Key Skills Practiced                |
|----------|-----------------|-------------------------------------|
| Python   | Arrays, Strings | Two-pointer technique, string ops   |
| Python   | Algorithms      | Efficient search, palindrome logic  |

- Practiced the two-pointer approach for array and string problems.
- Learned to efficiently solve problems with sorted data.
- Reinforced string manipulation and validation techniques.

---

## 🧪 How to Run

```bash
# Run Challenge 6 – Two Sum II
python3 challenge6.py

# Run Challenge 7 – Valid Palindrome
python3 challenge7.py

# Run Challenge 8 – Container With Most Water
python3 challenge8.py
```
