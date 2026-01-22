# Variable Naming in Python

## Question

Which of the following is an invalid variable name and why?

1. BASICSALARY
2. \_basic
3. basic-hra
4. #MEAN
5. group.
6. 422
7. pop in 2020
8. over
9. timemindovermatter
10. SINGLE
11. hELLO
12. queue.
13. team'svictory
14. Plot # 3
15. 2015_DDay

---

## Python Variable Naming Rules

A valid Python variable name must:

1. Start with a **letter (a–z, A–Z)** or an **underscore `_`**
2. Contain only **letters, digits, and underscores**
3. **Not contain spaces or special characters** (`- . # '`)
4. **Not start with a digit**
5. **Not be a Python keyword**

---

## Analysis of Given Variable Names

| Variable Name        | Valid / Invalid | Reason                     |
| -------------------- | --------------- | -------------------------- |
| `BASICSALARY`        | ✅ Valid        | Contains only letters      |
| `_basic`             | ✅ Valid        | Starts with underscore     |
| `basic-hra`          | ❌ Invalid      | Hyphen `-` not allowed     |
| `#MEAN`              | ❌ Invalid      | `#` is used for comments   |
| `group.`             | ❌ Invalid      | Dot `.` not allowed        |
| `422`                | ❌ Invalid      | Cannot start with a digit  |
| `pop in 2020`        | ❌ Invalid      | Contains spaces            |
| `over`               | ✅ Valid        | Letters only               |
| `timemindovermatter` | ✅ Valid        | Letters only               |
| `SINGLE`             | ✅ Valid        | Uppercase letters allowed  |
| `hELLO`              | ✅ Valid        | Mixed case allowed         |
| `queue.`             | ❌ Invalid      | Dot `.` not allowed        |
| `team'svictory`      | ❌ Invalid      | Apostrophe `'` not allowed |
| `Plot # 3`           | ❌ Invalid      | Contains space and `#`     |
| `2015_DDay`          | ❌ Invalid      | Starts with a digit        |

---

**Invalid variable names are:**

basic-hra
#MEAN
group.
422
pop in 2020
queue.
team'svictory
Plot # 3
2015_DDay

**Reason:**  
They violate Python variable naming rules by using special characters, spaces, or starting with digits.

---

## Key Takeaways

- ✔ Allowed characters: `a–z`, `A–Z`, `0–9`, `_`
- ❌ Disallowed: spaces, `-`, `.`, `#`, `'`
- ❌ Variables cannot start with numbers

---

## Example of Valid Variable Names

```python
basic_salary = 25000
_total_marks = 450
year2025 = 2025

```
