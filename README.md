# 🐍 Python Core, OOP & Software Engineering Portfolio

[![Python Version](https://img.shields.io/badge/Python-3.8%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code Style: Clean](https://img.shields.io/badge/Code%20Style-PEP%208-brightgreen.svg)](https://peps.python.org/pep-0008/)
[![Placement Ready](https://img.shields.io/badge/Focus-Placement%20%26%20Interviews-orange.svg)]()

> A structured, interview-oriented repository showcasing foundational Python programming, Object-Oriented Analysis & Design (OOAD), Data Structures, algorithmic problem solving, and modular application development.

---

## 📌 Executive Summary

This repository serves as a technical portfolio curated for campus placements, technical interviews, and software development engineering (SDE) evaluations. It demonstrates competencies in:
- **Clean Architecture & PEP 8 Standards**: Readable, structured, and maintainable code.
- **Robust Error Handling**: Production-ready exception handling and edge-case mitigation.
- **Object-Oriented Design (OOD)**: Full mastery of the four pillars of OOP (Encapsulation, Abstraction, Inheritance, Polymorphism).
- **File I/O & Persistent Storage**: Reading, writing, and appending structured data to persistent storage files.
- **Algorithmic Fundamentals**: Array manipulations, recursion, search routines, and time-complexity awareness.
- **Package Modularity**: Real-world application breakdown using layered packages.

---

## 🗂️ Complete Program Catalog (Placement Reference)

Every program in this repository is cataloged below with its key technical concepts, functionality, and interview relevance.

---

### 1. 🧱 Core Fundamentals & String Manipulation

| File / Program | Core Concepts | Functionality & Key Mechanics | Interview Relevance |
| :--- | :--- | :--- | :--- |
| [`hello.py`](hello.py) | Console I/O, Basic Syntax | Prints greetings; demonstrates initial Python runtime execution. | Python interpreter basics, script execution flow. |
| [`userinput.py`](userinput.py) | Type Casting, Arithmetic Operations | Accepts interactive numbers, performs type casting (`int()`), computes sum, difference, and average. | Type safety, `input()` returning `str`, arithmetic operator precedence. |
| [`fstring.py`](fstring.py) | String Formatting, Float Precision | Formats numeric values into strings with custom decimal precision (`{price :2f}`). | PEP 498 formatted string literals vs `.format()` and `%`. |
| [`stringoperations.py`](stringoperations.py) | Negative Indexing, Slicing, Step Slicing | Explores string slicing `[start:stop:step]`, negative indexes, string concatenation, and case conversions. | Slicing internals, immutability of Python strings, memory allocation. |
| [`stringmethod.py`](stringmethod.py) | Built-in String Validation & Transformation | Tests identifier validity (`isidentifier()`), title casing (`title()`), capitalization, whitespace splitting, and word replacement. | String validation algorithms, parsing techniques, string methods efficiency. |
| [`finder.py`](finder.py) | Character Iteration, Membership Testing, String Filtering | Traverses user input string to count vowels (`in "aeiou"`) and consonants using `.isalpha()`. | Character-by-character parsing, membership lookup efficiency, separating alphanumeric data. |

---

### 2. ⚡ Functions, Arguments & Functional Programming

| File / Program | Core Concepts | Functionality & Key Mechanics | Interview Relevance |
| :--- | :--- | :--- | :--- |
| [`calculator.py`](calculator.py) | Modular Functions, Return Values | Implements multiplication logic designed for import across other modules. | DRY principle, module exports, clean function contracts. |
| [`positionalargv.py`](positionalargv.py) | Positional Arguments | Demonstrates positional argument mapping and how order impacts parameter values. | Function signatures, parameter binding order, argument errors. |
| [`keywordargument.py`](keywordargument.py) | Keyword (Named) Arguments | Illustrates named argument binding regardless of parameter order (`name=...`, `roll=...`). | Default values, `*args`, `**kwargs`, flexible API design. |
| [`lambda.py`](lambda.py) | Anonymous Functions, First-Class Functions | Compact single-expression inline function `lambda a, b: a + b`. | Functional programming in Python, higher-order functions (`map`, `filter`, `sorted`). |
| [`listcomp.py`](listcomp.py) | List Comprehensions, Conditional Filtering | Generates squares up to 20 and filters even numbers using concise syntax `[x for x in list if condition]`. | Pythonic idioms, bytecode performance compared to standard `for` loops. |
| [`recursion.py`](recursion.py) | Recursion, Call Stack, Base Case | Calculates mathematical factorial $n!$ via recursive breakdown with an explicit termination base case (`n == 0`). | Call stack limits, `RecursionError`, recursion vs iterative performance. |
| [`exception.py`](exception.py) | Robust Error Handling, Exception Hierarchy | Handles `ZeroDivisionError`, `TypeError`, `ValueError`, and generic `Exception` across 5 test suites. | Fault-tolerant programming, exception propagation, enterprise error handling. |

---

### 3. 📊 Data Structures & Algorithms

| File / Program | Core Concepts | Functionality & Key Mechanics | Time / Space Complexity |
| :--- | :--- | :--- | :--- |
| [`array.py`](array.py) | Dynamic List Operations | Implements mutable sequence operations: indexing, item replacement, `append()`, `insert()`, `pop()`, and `len()`. | Append: $O(1)$ amortized<br>Insert/Delete: $O(n)$<br>Access: $O(1)$ |
| [`importarray.py`](importarray.py) | Memory-Efficient Homogeneous Arrays | Uses Python's native `array` module with type code `'i'` (signed integers) for dense memory allocation. | Memory efficiency vs heterogeneous Python lists; C-style memory buffers. |
| [`traversalARRAY.py`](traversalARRAY.py) | Iteration & Traversal | Iterates over arrays using indexed `range(len(arr))` loops. | Traversal: $O(n)$ time, $O(1)$ auxiliary space. |
| [`searching.py`](searching.py) | Linear Search Algorithm | Scans an array sequentially for a target key with an early `break` and Python's unique `for-else` block. | Worst: $O(n)$<br>Best: $O(1)$<br>Demonstrates clean loop termination. |

---

### 4. 🏛️ Object-Oriented Programming (OOP) Architecture

| File / Program | OOP Pillar / Concept | Implementation & Design Details | Placement & Interview Insights |
| :--- | :--- | :--- | :--- |
| [`constructor.py`](constructor.py) | Class Instantiation & `self` | Demonstrates the `__init__` constructor and instance attribute binding. | Role of `self`, instance vs class variables, object lifecycle. |
| [`class with using function.py`](class with using function.py) | Instance Methods & State Encapsulation | Defines a `student` entity with state (`name`, `age`, `marks`) and display behaviors. | Designing domain entities and behavioral methods. |
| [`classemployee.py`](classemployee.py) | Class-Level Attributes vs Instance Attributes | Demonstrates shared class variables and overriding attribute values per instance. | Memory allocation of class vs instance namespaces (`__dict__`). |
| [`class_cal.py`](class_cal.py) | Modeling Mathematical Logic | Object-oriented area calculation for geometric rectangles. | High cohesion and clear separation of state and computation. |
| [`employee.py`](employee.py) | Access Modifiers (Public, Protected, Private) | Implements public `name`, protected `_salary`, and private `__password` attributes. | Name mangling mechanism (`_ClassName__var`), convention vs enforcement. |
| [`datahiding.py`](datahiding.py) | Data Hiding & Information Hiding | Hides student marks behind private variables accessible only via verified getters. | Defensive programming, securing internal object states. |
| [`inheritance.py`](inheritance.py) | Single Inheritance | Child class inherits physical traits and behaviors from parent class. | Code reusability, `is-a` relationship, class hierarchies. |
| [`animal.py`](animal.py) | Hierarchical Inheritance & Method Re-use | Base `Animal` class with derived `dog` class invoking inherited `info()` and custom `sound()`. | Constructor chaining, superclass delegation, specialization. |
| [`polymorphhism.py`](polymorphhism.py) | Polymorphism & Duck Typing | Defines distinct classes (`dog`, `cat`) providing identical method interfaces (`sound()`). | "If it walks like a duck..." — dynamic method resolution in Python. |
| [`method_overriding.py`](method_overriding.py) | Dynamic Method Dispatch | Derived class `ant` overrides `like()` method defined in base class `insects`. | Runtime polymorphism, virtual tables, customizing inherited logic. |
| [`Moverloading.py`](Moverloading.py) | Variable-Length Arguments (`*args`) | Implements Pythonic method overloading via variable arguments (`*number`) for arbitrary inputs. | Why Python does not support compile-time overloading by default. |
| [`abstractclass.py`](abstractclass.py) | Abstraction & Interfaces (`abc.ABC`) | Enforces an interface contract using `@abstractmethod` on base class `Animal`. | Contract-driven design, preventing direct instantiation of incomplete classes. |

---

### 5. 🚀 Modular Projects & System Architecture

| Project / Entrypoint | Architecture Type | Key Modules | Technical Description |
| :--- | :--- | :--- | :--- |
| [`miniproject.py`](miniproject.py) | **Console Enterprise CRUD App** | `Employee`, `search_employee()`, `main()` | Full-featured Employee Management System with interactive menu, validation, record mutation, search, and deletion. |
| [`diary.py`](diary.py) | **Persistent CLI Journal (File I/O)** | `PersonalDiary`, `write_entry()`, `view_entries()`, `run()` | Object-oriented personal journaling CLI utilizing Python file handling (`open()`, append mode `"a"`, read mode `"r"`) for persistent storage. |
| [`ai_pro/main.py`](ai_pro/main.py) | **Layered Python Package** | [`cleaner.py`](ai_pro/app/cleaner.py)<br>[`analyzer.py`](ai_pro/app/analyzer.py)<br>[`__init__.py`](ai_pro/app/__init__.py) | Production-style package structure demonstrating clean separation between string sanitization and metric analysis. |
| [`MYPRO/main.py`](MYPRO/main.py) | **Modular Utility Service** | [`analyze.py`](MYPRO/analyze.py) | Decoupled utility package demonstrating relative module imports and regex-like whitespace normalization. |
| [`main.py`](main.py) | **Integration Runner** | [`calculator.py`](calculator.py) | Demonstrates cross-file module imports and functional composition. |

---

## 🏆 Featured Capstone Project: Employee Management System

The [Employee Management System](miniproject.py) is a complete Object-Oriented console application designed to handle organizational workforce data cleanly and securely.

```
                  ┌────────────────────────┐
                  │      Console Menu      │
                  │   (CLI User Interface)  │
                  └───────────┬────────────┘
                              │
             ┌────────────────┴────────────────┐
             ▼                                 ▼
   ┌───────────────────┐             ┌───────────────────┐
   │  Employee Model   │             │   CRUD Handlers   │
   ├───────────────────┤             ├───────────────────┤
   │ - emp_id (str)    │             │ + Add Employee    │
   │ - name (str)      │ ◄───────────┤ + Display Records │
   │ - department (str)│             │ + Search by ID    │
   │ - salary (float)  │             │ + Update Salary   │
   │ + display()       │             │ + Delete Record   │
   │ + update_salary() │             └───────────────────┘
   └───────────────────┘
```

### Key Highlights for Interviewers:
1. **Input Validation**: Rejects empty strings, validates numeric inputs with `try-except ValueError`, and blocks negative salaries.
2. **Data Integrity**: Checks for duplicate employee IDs before insertion.
3. **Encapsulation**: State mutations (e.g. salary changes) occur through dedicated object methods (`update_salary()`).

---

## 💻 How to Clone & Run

### 1. Clone the Repository
```bash
git clone https://github.com/Riya18code/Python_Code.git
cd Python_Code
```

### 2. Run the Capstone Project
```bash
python miniproject.py
```

### 3. Run the Modular Package
```bash
python ai_pro/main.py
```

### 4. Run Any Practice Script
```bash
python exception.py
python abstractclass.py
python recursion.py
python finder.py
python diary.py
```

---

## 💡 Placement & Interview FAQs (Quick Revision)

<details>
<summary><b>1. How does Python enforce private variables in OOP?</b></summary>
Python uses <i>name mangling</i> for attributes prefixed with double underscores (e.g., <code>__password</code> becomes <code>_Employee__password</code>). It does not strictly prohibit access at the hardware level, but protects variables from unintentional overrides in subclasses.
</details>

<details>
<summary><b>2. Why doesn't Python support traditional method overloading?</b></summary>
Because Python is dynamically typed and interprets functions by name in the local namespace. Later definitions overwrite previous ones. Overloading behavior is achieved using default arguments, <code>*args</code>, or the <code>functools.singledispatch</code> decorator.
</details>

<details>
<summary><b>3. What is the difference between a Python List and an Array?</b></summary>
Python <b>lists</b> are heterogeneous (can hold elements of varying types) and store references to objects. Python <b>arrays</b> (from the <code>array</code> module) are homogeneous and store primitive data types contiguously in memory, offering significant memory savings.
</details>

<details>
<summary><b>4. How does the <code>for-else</code> construct in <code>searching.py</code> work?</b></summary>
The <code>else</code> block in a Python loop executes <i>only</i> if the loop terminates normally without encountering a <code>break</code> statement. This eliminates the need for manual boolean flag variables.
</details>

<details>
<summary><b>5. How does Python handle file persistence with append mode (<code>"a"</code>) vs write mode (<code>"w"</code>)?</b></summary>
Write mode (<code>"w"</code>) overwrites and truncates the file if it exists, creating a fresh file. Append mode (<code>"a"</code>) seeks to the end of the file and appends new content without deleting existing data. Both modes create the file if it doesn't already exist.
</details>

<details>
<summary><b>6. What is the time complexity of character membership testing (<code>ch in "aeiou"</code>) in Python?</b></summary>
Checking membership in a small fixed-size string like <code>"aeiou"</code> takes $O(1)$ constant time ($k=5$ comparisons). For large collections, converting to a <code>set</code> yields true $O(1)$ hash table lookups versus $O(n)$ linear scans on long sequences.
</details>

---

## 👩‍💻 Author

**Riya**
- GitHub: [@Riya18code](https://github.com/Riya18code)
- Focus: Software Development, Python, Object-Oriented Architecture