# 📦 Understanding Stack Behavior in Direct Recursion

This README explains how the **call stack** behaves when performing **direct recursion** in Python or any similar programming language.

---

## 🔁 What is Direct Recursion?

**Direct recursion** occurs when a function calls itself directly to solve a smaller part of the problem.

### Python Example:
```python
def countdown(n):
    if n == 0:
        print("Done!")
        return
    print(n)
    countdown(n - 1)
