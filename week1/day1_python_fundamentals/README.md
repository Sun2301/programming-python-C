# 🔥 Day 1 – Programming Fundamentals Challenges

---

## ⚔️ Challenge 1 – Two Sum (LeetCode)

**🔗 Source:** [Two Sum – LeetCode](https://leetcode.com/problems/two-sum/)

### 🧠 Problem Statement:
Given an array of integers `nums` and an integer `target`, return indices of the **two numbers** such that they add up to the `target`.

### ✅ Constraints:
- Each input has **exactly one solution**.
- You may not use the same element twice.

### 🚀 Solution Strategy:
- ✅ **Brute-force (commented)** – O(n²): Check all possible pairs.
- ✅ **Optimized Hash Map** – O(n): Store complements in a dictionary while iterating.

### 📌 Key Concepts:
- Hash maps for constant-time lookups
- Enumerate for index tracking
- Clean code and fallback logic

---

## ⚡ Challenge 2 – Thor's Journey to the Light (Codingame)

**🔗 Source:** [Power of Thor – CodinGame](https://www.codingame.com/ide/puzzle/power-of-thor-episode-1)

### 🧠 Problem Statement:
Move Thor across a 40×18 grid to reach the coordinates of a light, using only directional moves (`N`, `NE`, `E`, etc.). Each turn, compute the best direction to get closer to the light.

### ✅ Constraints:
- Don’t move outside the grid
- Output only valid directions (e.g., `SW`, `N`, `E`, etc.)

### 🚀 Solution Strategy:
- Compute vertical and horizontal deltas each turn
- Append direction string accordingly (`N`, `S`, `E`, `W`)
- Adjust Thor’s current position to reflect movement

### 📌 Key Concepts:
- Greedy movement logic
- Coordinate system handling (Y axis starts from top)
- Grid bounds and directional logic

---

## 📊 Summary of Learnings – Day 1

| Language | Concept                     | Key Skills Practiced                    |
|----------|-----------------------------|-----------------------------------------|
| Python   | Arrays, Hash Maps           | Index tracking, dict lookup, I/O        |
| Python   | Control Flow, Loops         | Real-time coordinate logic, simulation  |

- Used `LeetCode` for algorithmic challenge.
- Used `CodinGame` for real-time input/output and simulation.
- Practiced translating problem constraints into clean logic.
- Reinforced understanding of directions and vector movement on 2D grids.

---

## 🧪 How to Run

```bash
# Run Challenge 1 – Two Sum
python3 challenge1.py

# Run Challenge 2 – Thor Movement
# Provide sample input as required by CodinGame format.
python3 challenge2.


---