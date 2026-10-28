# 🐍 Python Core, OOP & Software Engineering Portfolio

[![Python Version](https://img.shields.io/badge/Python-3.8%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![NumPy](https://img.shields.io/badge/Library-NumPy-013243.svg?logo=numpy&logoColor=white)](https://numpy.org/)
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
- **Scientific & Numerical Computing**: High-performance multi-dimensional arrays (`ndarray`), matrix initialization routines, scalar & multi-axis broadcasting, feature scaling for ML pipelines, vectorized conditional selection (`np.where`), missing value imputation (`np.isnan`, `np.nan_to_num`), multi-axis sorting (`np.sort`, `np.argsort`), and linear algebra routines (`np.linalg`: matrix multiplication `@`/`np.dot`, dot products, determinants, matrix inverses, identity matrices, and linear system solvers) with NumPy.
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

### 3. 📊 Data Structures & Numerical Computing (NumPy & Arrays)

| File / Program | Core Concepts | Functionality & Key Mechanics | Time / Space Complexity |
| :--- | :--- | :--- | :--- |
| [`array.py`](array.py) | Dynamic List Operations | Implements mutable sequence operations: indexing, item replacement, `append()`, `insert()`, `pop()`, and `len()`. | Append: $O(1)$ amortized<br>Insert/Delete: $O(n)$<br>Access: $O(1)$ |
| [`importarray.py`](importarray.py) | Memory-Efficient Homogeneous Arrays | Uses Python's native `array` module with type code `'i'` (signed integers) for dense memory allocation. | Memory efficiency vs heterogeneous Python lists; C-style memory buffers. |
| [`traversalARRAY.py`](traversalARRAY.py) | Iteration & Traversal | Iterates over arrays using indexed `range(len(arr))` loops. | Traversal: $O(n)$ time, $O(1)$ auxiliary space. |
| [`searching.py`](searching.py) | Linear Search Algorithm | Scans an array sequentially for a target key with an early `break` and Python's unique `for-else` block. | Worst: $O(n)$<br>Best: $O(1)$<br>Demonstrates clean loop termination. |
| [`numpyarraycreation.py`](numpyarraycreation.py) | NumPy Multi-Dimensional Arrays (`ndarray`), Matrix Generation, Array Metadata | Generates 1D/2D arrays, pre-filled matrices (`zeros`, `ones`, `full`, `identity/eye`), numerical ranges (`arange`, `linspace`), and introspects core attributes (`ndim`, `shape`, `size`, `dtype`). | Contiguous C-memory block<br>Shape/Strides: $O(1)$<br>Vectorized SIMD readiness |
| [`numpyrupee.py`](numpyrupee.py) | 1D & 2D Indexing, Positive/Negative Offsets, Range Slicing & Strided Reversals | Demonstrates 1D element access, negative indexing (`arr[-1]`), step slicing (`arr[::-1]`), and 2D coordinate indexing `[row, col]` on currency and score matrices. | Direct Offset: $O(1)$<br>Slicing/Reversal: $O(1)$ memory view |
| [`housenumpy.py`](housenumpy.py) | 2D Column Slicing, Boolean Masking & Conditional Row Filtering | Analyzes multi-feature tabular housing data (Area, Bedrooms, Age), extracts column slices (`[:, 0]`, `[:, 1]`), and performs vectorized conditional filtering (`houses[houses[:, 0] > 1000]`). | Column Slice: $O(1)$ view<br>Mask Evaluation: $O(N)$ vectorized SIMD filter |
| [`indexingslicingnumpy.py`](indexingslicingnumpy.py) | 2D Multi-Axis Indexing, Submatrix Extraction & Row/Column Slicing | Demonstrates 2D coordinate indexing `[row, col]`, whole row selections `[i]` vs `[[i]]`, whole column slicing (`[:, 1]`, `[:, 0]`), and submatrix block extraction (`[1:3, 1:3]`). | Coordinate / Slice Access: $O(1)$ memory view<br>Submatrix Extraction: $O(1)$ view |
| [`numpytemp.py`](numpytemp.py) | 2D Dataset Introspection & Vectorized Scalar Broadcasting | Instantiates a 2D temperature array, introspects dimensions/shape/datatype (`ndim`, `shape`, `size`, `dtype`), and applies arithmetic scalar broadcasting (`temperatures + 5`) across all elements without loops. | Introspection: $O(1)$ property lookup<br>Broadcasting: $O(N)$ vectorized SIMD calculation |
| [`temperaturenumpy.py`](temperaturenumpy.py) | Statistical Reductions & Descriptive Aggregations | Evaluates 1D sensor/weather readings using NumPy reduction routines: arithmetic mean (`np.mean`), maximum (`np.max`), and minimum (`np.min`). | Aggregation: $O(N)$ single-pass C-speed reduction<br>Aux Space: $O(1)$ |
| [`reshapingnumpy.py`](reshapingnumpy.py) | Shape Transformation, Flattening (`flatten` vs `ravel`) & Matrix Transpose | Reshapes continuous range vectors (`1D -> 3x4`), compares deep memory copy (`.flatten()`) vs zero-copy view (`.ravel()`), and performs 2D matrix transposition (`.T`). | Reshape/Transpose/Ravel: $O(1)$ view stride manipulation<br>Flatten: $O(N)$ contiguous copy |
| [`joiningarray_numpy.py`](joiningarray_numpy.py) | Multi-Axis Array Concatenation & Stacking | Merges multiple 2D matrices along specific geometric axes using `np.concatenate()`: axis 0 (vertical stack) and axis 1 (horizontal stack). | Concatenation: $O(N \times M)$ memory allocation & contiguous buffer copy |
| [`Arithmeticnumpy.py`](Arithmeticnumpy.py) | Vectorized Element-Wise Arithmetic & Exponentiation | Computes element-wise vector operations (`+`, `-`, `*`, `/`, `**`) between matching-dimension 1D arrays without loops. | Vectorized SIMD: $O(N)$<br>Output Space: $O(N)$ |
| [`broadcastingnumpy.py`](broadcastingnumpy.py) | Scalar-to-Array Broadcasting | Adds a scalar value (`10`) across a 1D vector; demonstrates NumPy automatically expanding scalar dimensions with zero memory duplication. | Vectorized SIMD: $O(N)$<br>Virtual Dimension: $O(1)$ |
| [`newrow_numpy.py`](newrow_numpy.py) | Multi-Dimensional Row Broadcasting | Broadcasts a 1D row array of shape `(3,)` across a 3x3 matrix of shape `(3, 3)` along axis 0. | Vectorized: $O(N \times M)$<br>Zero-copy view expansion: $O(1)$ |
| [`newcolumn_numpy.py`](newcolumn_numpy.py) | Multi-Dimensional Column Broadcasting | Broadcasts a 2D column vector of shape `(2, 1)` across a 2D matrix of shape `(2, 3)` along axis 1. | Vectorized: $O(N \times M)$<br>Zero-copy view expansion: $O(1)$ |
| [`scaling_numpy.py`](scaling_numpy.py) | Feature Scaling & Data Normalization for ML | Performs vectorized decimal/range scaling (`marks / 100`) on tabular matrix data to normalize features into the $[0, 1]$ interval. | Normalization: $O(N \times M)$<br>Space: $O(N \times M)$ |
| [`vectorizationcondn_numpy.py`](vectorizationcondn_numpy.py) | Vectorized Conditional Selection (`np.where`) | Performs scalar curve addition (`marks + 5`), boolean evaluation (`>= 40`), and ternary conditional replacement via `np.where()` without iteration. | Vectorized Selection: $O(N)$<br>Space: $O(N)$ |
| [`Random_numpy.py`](Random_numpy.py) | Pseudorandom Sampling & Matrix Generation | Generates discrete uniform random integers (`np.random.randint`) for simulated events/matrices and continuous uniform floats (`np.random.rand`). | Sampling: $O(N)$ PRNG generation<br>Space: $O(N)$ |
| [`datacleaning_numpy.py`](datacleaning_numpy.py) | Missing Value Handling (`NaN`), Imputation & Boolean Filtering | Detects missing values with `np.isnan()`, imputes missing entries using `np.nan_to_num()` with mean statistic `np.nanmean()`, and filters low thresholds with boolean indexing. | Detection & Imputation: $O(N)$<br>Filtering: $O(N)$ |
| [`sorting_numpy.py`](sorting_numpy.py) | 1D/2D Array Sorting, Indirect Index Sorting (`np.argsort`) & Axis-Wise Ordering | Sorts 1D arrays ascending and descending (`[::-1]`), retrieves index permutations using `np.argsort()`, and sorts 2D matrices independently across rows (`axis=1`) and columns (`axis=0`). | 1D Sort: $O(N \log N)$ (Introsort/QuickSort)<br>2D Multi-Axis: $O(M \times N \log N)$ |
| [`IdentityMatrix_numpy.py`](IdentityMatrix_numpy.py) | Identity Matrix Generation (`np.eye`) | Generates a 3x3 identity matrix with ones on the main diagonal and zeros elsewhere using `np.eye(3)`. | Matrix Properties: $I \cdot A = A$<br>Space: $O(N^2)$<br>Time: $O(N^2)$ initialization |
| [`LinearEQN_numpy.py`](LinearEQN_numpy.py) | Solving Systems of Linear Equations (`np.linalg.solve`) | Solves simultaneous linear equations ($Ax = B$) for unknown variable vectors using exact matrix decomposition algorithms. | Solve Complexity: $O(N^3)$ (LU decomposition)<br>Exact numerical solver vs manual matrix inversion |
| [`determinant_numpy.py`](determinant_numpy.py) | Matrix Determinant Calculation (`np.linalg.det`) | Computes scalar matrix determinant $\det(A)$ of a 2x2 matrix to test matrix singularity and invertible conditions. | Determinant: $O(N^3)$ (via LU factorization)<br>Singularity test: $\det(A) \neq 0$ |
| [`dotproductofvectors_numpy.py`](dotproductofvectors_numpy.py) | Vector Dot Product (`np.dot`) | Calculates the algebraic inner product $\mathbf{x} \cdot \mathbf{y} = \sum x_i y_i$ between two 1D vectors with SIMD acceleration. | Time: $O(N)$ vectorized SIMD<br>Space: $O(1)$ scalar result |
| [`inverse_numpy.py`](inverse_numpy.py) | Matrix Inversion (`np.linalg.inv`) | Computes the multiplicative matrix inverse $A^{-1}$ such that $A \cdot A^{-1} = I$ for non-singular square matrices. | Inversion: $O(N^3)$ Gaussian/LU decomposition<br>Conditioning & numerical stability |
| [`matrixmul_numpy.py`](matrixmul_numpy.py) | Matrix Multiplication (`@` Operator & `np.dot`) | Performs true matrix-matrix multiplication between 2D matrices using both Python 3.5+ `@` operator and `np.dot()`. | Matrix Product: $O(N^3)$ (optimized BLAS/GEMM routines)<br>Dimensional compatibility ($M \times K$ with $K \times N$) |

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
python numpyarraycreation.py
python numpyrupee.py
python housenumpy.py
python indexingslicingnumpy.py
python joiningarray_numpy.py
python reshapingnumpy.py
python numpytemp.py
python temperaturenumpy.py
python Arithmeticnumpy.py
python broadcastingnumpy.py
python newrow_numpy.py
python newcolumn_numpy.py
python scaling_numpy.py
python vectorizationcondn_numpy.py
python Random_numpy.py
python datacleaning_numpy.py
python sorting_numpy.py
python IdentityMatrix_numpy.py
python LinearEQN_numpy.py
python determinant_numpy.py
python dotproductofvectors_numpy.py
python inverse_numpy.py
python matrixmul_numpy.py
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
<summary><b>3. What is the difference between a Python List, the native Array module, and a NumPy Array?</b></summary>
<ul>
  <li><b>Python List:</b> Heterogeneous collection storing pointers/references to objects in scattered memory locations. Offers flexibility at the cost of high memory overhead and pointer dereferencing latency.</li>
  <li><b>Native Array (<code>array.array</code>):</b> Homogeneous 1D collection storing contiguous C-type primitive values. Greatly reduces memory footprint compared to lists, but lacks multi-dimensional support and vectorized linear algebra operations.</li>
  <li><b>NumPy Array (<code>numpy.ndarray</code>):</b> High-performance, N-dimensional homogeneous array stored in contiguous C/Fortran memory blocks. Supports vectorized operations (SIMD acceleration), broadcasting, fast matrix slicing, and $O(1)$ stride manipulations without copying data.</li>
</ul>
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

<details>
<summary><b>7. Why does NumPy use attributes like <code>.ndim</code>, <code>.shape</code>, <code>.size</code>, and <code>.dtype</code> instead of methods?</b></summary>
In NumPy, array metadata (dimensionality, shape tuple, element count, and data type) are stored directly inside the C-level <code>PyArrayObject</code> struct header. Accessing them is an instantaneous $O(1)$ property lookup that does not require recomputing dimensions or iterating through elements.
</details>

<details>
<summary><b>8. What is the fundamental difference between NumPy array slicing and Python list slicing?</b></summary>
When slicing a standard Python list (e.g. <code>my_list[1:4]</code>), Python allocates a <b>new list object and shallow-copies</b> pointers, costing $O(k)$ time and memory. In contrast, NumPy slicing (e.g. <code>rupee[1:4]</code> or <code>houses[:, 0]</code>) returns a <b>view</b> of the existing data buffer with modified strides and byte offsets. Creating a view is an instantaneous $O(1)$ operation that avoids memory allocation and data duplication.
</details>

<details>
<summary><b>9. How does boolean masking / conditional filtering work in NumPy (e.g. <code>houses[houses[:, 0] > 1000]</code>)?</b></summary>
The relational condition (<code>houses[:, 0] > 1000</code>) evaluates element-wise across the selected column slice using SIMD vectorization at C-speed, producing an array of boolean flags (<code>[False, True, False, True]</code>). When passed back into the array indexer, NumPy selects only rows where the corresponding flag is <code>True</code>, eliminating slow Python-level <code>for</code> loops and <code>if</code> conditions.
</details>

<details>
<summary><b>10. What is the fundamental difference between NumPy's <code>flatten()</code> and <code>ravel()</code>?</b></summary>
Both methods return a 1D representation of a multi-dimensional array. However, <code>ravel()</code> returns a <b>view</b> (reference) of the original array whenever possible without allocating new memory, so changes to the raveled array modify the original array. In contrast, <code>flatten()</code> always allocates fresh memory and returns an independent <b>deep copy</b>.
</details>

<details>
<summary><b>11. How does the <code>axis</code> parameter determine array concatenation in <code>np.concatenate()</code>?</b></summary>
In multi-dimensional arrays, <code>axis</code> specifies the direction of operation: <code>axis=0</code> concatenates along rows (vertical stacking, increasing row count), whereas <code>axis=1</code> concatenates along columns (horizontal stacking, increasing column count). In NumPy, dimensions along all axes other than the concatenation axis must match identically.
</details>

<details>
<summary><b>12. What are the rules of NumPy Broadcasting, and how does it prevent memory duplication?</b></summary>
NumPy compares array shapes element-wise starting from trailing (rightmost) dimensions. Two dimensions are compatible when:
<ol>
  <li>They are equal, or</li>
  <li>One of them is <code>1</code> (or missing).</li>
</ol>
If a dimension is <code>1</code>, NumPy treats the array as if it were stretched along that axis by setting the stride for that axis to <code>0</code>. This means the same memory buffer is reused without allocating extra RAM, allowing operations between e.g. a <code>(2, 3)</code> matrix and a <code>(2, 1)</code> column vector at peak SIMD efficiency.
</details>

<details>
<summary><b>13. How does <code>np.where(condition, x, y)</code> work as a vectorized ternary operator?</b></summary>
<code>np.where(condition, x, y)</code> is the vectorized equivalent of Python's ternary <code>x if condition else y</code>. The condition is evaluated element-wise across the array at C speed; for each element where the condition is <code>True</code>, the value from <code>x</code> is selected; otherwise, the value from <code>y</code> is selected. It avoids Python bytecode loop overhead and returns a newly formatted array in $O(N)$ time.
</details>

<details>
<summary><b>14. Why is feature scaling (e.g. <code>marks / 100</code>) important in machine learning data pipelines?</b></summary>
Raw real-world numerical features often span disparate ranges (e.g. salaries in tens of thousands vs ages under 100). Feature scaling (normalizing values to a bounded range such as $[0, 1]$ or standard normal distribution with mean 0 and variance 1) prevents high-magnitude features from dominating distance metrics (Euclidean distance) and accelerates gradient descent convergence during model training.
</details>

<details>
<summary><b>15. How does NumPy handle random number generation, and what is the difference between <code>randint()</code> and <code>rand()</code>?</b></summary>
NumPy generates pseudorandom numbers using fast BitGenerators (such as PCG64). <code>np.random.randint(low, high, size)</code> produces discrete integers from the half-open interval $[low, high)$, suitable for discrete event simulations like dice rolls and matrix generation. In contrast, <code>np.random.rand(d0, d1, ...)</code> generates continuous floating-point numbers uniformly distributed over $[0, 1)$. For reproducible experiments, passing a seed fixes the deterministic pseudorandom sequence.
</details>

<details>
<summary><b>16. How does NumPy handle missing data (<code>NaN</code>), and why should we use <code>np.nanmean()</code> instead of <code>np.mean()</code>?</b></summary>
<code>np.nan</code> represents missing or undefined numerical data under IEEE 754 floating-point standards. Standard arithmetic reductions (such as <code>np.mean()</code> or <code>np.sum()</code>) propagate <code>NaN</code>, returning <code>nan</code> if any missing values exist. NumPy provides NaN-safe alternatives like <code>np.nanmean()</code>, <code>np.nansum()</code>, and <code>np.nanstd()</code> that ignore missing entries during computation. To clean arrays, <code>np.nan_to_num(arr, nan=replacement_value)</code> imputes missing values with statistical measures (e.g. mean) cleanly without altering array shapes.
</details>

<details>
<summary><b>17. What is the difference between <code>np.sort()</code> and <code>np.argsort()</code>, and how does the <code>axis</code> parameter govern 2D sorting?</b></summary>
<code>np.sort()</code> returns a sorted copy of array elements, whereas <code>np.argsort()</code> returns an array of integer indices representing the permutation that would sort the array. This index mapping is essential for sorting related parallel datasets or ranking elements. For 2D matrices, <code>axis=1</code> sorts each row independently along the horizontal direction, while <code>axis=0</code> sorts each column independently along the vertical direction.
</details>

<details>
<summary><b>18. What is the difference between element-wise multiplication (<code>*</code>) and matrix multiplication (<code>@</code> or <code>np.dot()</code>) in NumPy?</b></summary>
The asterisk operator (<code>A * B</code>) performs element-by-element Hadamard multiplication, requiring matching shapes or broadcasting compatibility. In contrast, <code>A @ B</code> (Python 3.5+ infix operator) or <code>np.dot(A, B)</code> performs true linear algebraic matrix dot product (multiplying rows of $A$ by columns of $B$), requiring the inner dimensions to align ($M \times K$ with $K \times N$, yielding an $M \times N$ matrix).
</details>

<details>
<summary><b>19. How does <code>np.linalg.solve()</code> solve linear systems ($Ax = B$), and why is it preferred over <code>np.linalg.inv(A) @ B</code>?</b></summary>
Mathematically, $x = A^{-1}B$. However, computing an explicit matrix inverse with <code>np.linalg.inv()</code> is computationally expensive ($O(N^3)$), prone to floating-point rounding errors, and catastrophic on ill-conditioned matrices. Instead, <code>np.linalg.solve(A, B)</code> invokes LAPACK <code>gesv</code> routines using LU/Cholesky decomposition with partial pivoting, which is significantly faster, uses less memory, and guarantees superior numerical stability.
</details>

<details>
<summary><b>20. What is an identity matrix (<code>np.eye</code>), and why is the determinant (<code>np.linalg.det</code>) critical before matrix inversion?</b></summary>
An identity matrix $I$ generated by <code>np.eye(N)</code> is a square matrix whose main diagonal entries are $1$ and off-diagonal entries are $0$, acting as the multiplicative identity ($A \cdot I = I \cdot A = A$). The determinant $\det(A)$ represents the volume scaling factor of the linear transformation. If $\det(A) = 0$, the matrix is <b>singular</b> (non-invertible) because its rows/columns are linearly dependent, causing <code>np.linalg.inv()</code> to raise a <code>LinAlgError</code>.
</details>

---

## 👩‍💻 Author

**Riya**
- GitHub: [@Riya18code](https://github.com/Riya18code)
- Focus: Software Development, Python, Object-Oriented Architecture