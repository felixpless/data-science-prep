# Data Science & AI Prep

A structured learning repository to strengthen my foundations in Python, data analytics, mathematics, decision science, machine learning, and deep learning.

The goal is not just to work through individual topics, but to build a strong understanding of the concepts behind modern Data Science & AI and to apply them through code.

The learning process combines theoretical understanding with practical exercises, real-world datasets, and progressively more complex projects.

---

## Learning Path

```text
Python Fundamentals
        ↓
Data Toolkit
        ↓
Mathematics & Statistics
        ↓
Decision Science
        ↓
Machine Learning
        ↓
Deep Learning
        ↓
Projects
```

The repository grows together with my progress. New folders and topics are added as I reach them instead of creating the entire structure in advance.

---

# Repository Structure

The repository is organized into seven main chapters.

```text
data-science-prep/
│
├── 01-python/
│
├── 02-data-toolkit/
│   ├── 01-numpy/
│   └── 02-pandas/
│
├── 03-maths/                  (planned)
├── 04-decision-science/       (planned)
├── 05-machine-learning/      (planned)
├── 06-deep-learning/          (planned)
└── 07-projects/               (planned)
│
├── .gitignore
├── README.md
├── PROGRESS.md
└── requirements.txt
```

Folders for future chapters are created progressively as the learning path advances.

---

# 01 — Python Fundamentals

**Status: Completed**

Build a solid Python foundation before moving into the Data Science stack.

The objective is to understand how Python works, develop programming logic, and write structured, reusable code.

### Learning Modules

| Module | Topic | Status |
|--------|-------|--------|
| 01.01 | Python Basics | Completed |
| 01.02 | Control Flow | Completed |
| 01.03 | Functions | Completed |
| 01.04 | Data Structures | Completed |
| 01.05 | Modules | Completed |
| 01.06 | Object-Oriented Programming | Completed |
| 01.07 | Error Handling | Completed |
| 01.08 | Professional Python | Completed |

### 01.01 Python Basics

- Variables and objects
- Data types
- Object identity
- References
- Mutable vs. immutable objects
- Copying objects
- Operators
- Basic input/output

### 01.02 Control Flow

- Boolean logic
- Comparisons
- `if / elif / else`
- `for` loops
- `while` loops
- `break` and `continue`
- Iteration patterns

### 01.03 Functions

- Defining functions
- Parameters and arguments
- Return values
- Scope
- Default parameters
- `*args` and `**kwargs`
- Lambda functions
- Writing reusable functions

### 01.04 Data Structures

- Lists
- Tuples
- Dictionaries
- Sets
- Nested data structures
- Indexing and slicing
- List / dictionary comprehensions
- Choosing appropriate data structures

### 01.05 Modules

- Imports
- Python standard library
- Creating own modules
- Packages
- Organizing Python code
- Environments and dependencies

### 01.06 Object-Oriented Programming

- Classes and objects
- Attributes
- Methods
- Constructors
- Instance vs. class attributes
- Inheritance
- Composition

### 01.07 Error Handling

- Reading tracebacks
- Exceptions
- `try / except`
- `else / finally`
- Raising exceptions
- Debugging

### 01.08 Professional Python

- Clean code
- Naming and structure
- Type hints
- Docstrings
- Testing
- Debugging
- Refactoring
- Git workflow

### Learning Outcome

After completing Chapter 01, I can:

- Write Python programs using functions, loops, and data structures.
- Understand how Python handles objects and references.
- Organize code into reusable components.
- Identify and debug common programming errors.
- Work with Python environments and external libraries.
- Use Git and GitHub to manage my learning projects.

---

# 02 — Data Toolkit

**Status: In Progress — 20% Completed**

Move from general Python programming toward working with real-world data.

The focus is on practical data analysis, transforming raw data into meaningful information, and developing the skills required for business analytics, operations analytics, and machine learning.

### Repository Structure

```text
02-data-toolkit/
│
├── 01-numpy/
│   └── numpy_basics.ipynb
│
├── 02-pandas/
│   ├── pandas_basics.ipynb
│   ├── shipments.csv
│   ├── delayed_shipments.csv
│   ├── top_5_profitable_shipments.csv
│   └── Data_Analysis_Shipments.xlsx
│
└── ... (additional modules added progressively)
```

### Learning Modules

| Module | Topic | Status |
|--------|-------|--------|
| 02.01 | NumPy | Completed |
| 02.02 | Pandas Fundamentals | Completed |
| 02.03 | Data Cleaning & Transformation | Next |
| 02.04 | Data Aggregation & Business KPIs | Not started |
| 02.05 | Combining Multiple Datasets | Not started |
| 02.06 | Data Visualization & Storytelling | Not started |
| 02.07 | APIs, Web Scraping & Regex | Not started |
| 02.08 | Statistics & Probability | Not started |
| 02.09 | Professional Analytics Code | Not started |
| 02.10 | Final Analytics Project | Not started |

### 02.01 NumPy

**Status: Completed**

Introduction to numerical computing with Python.

Topics covered:

- NumPy arrays
- Array creation
- Dimensions and shapes
- Indexing and slicing
- Vectorized operations
- Broadcasting
- Numerical calculations
- Working with multidimensional arrays

**Learning Outcome**

Understand how NumPy enables efficient numerical operations and why vectorized computations are important for data science.

### 02.02 Pandas Fundamentals

**Status: Completed**

Introduction to data manipulation and analysis using Pandas.

Practical exercises are based on a logistics shipment dataset containing shipment information, customers, cities, delivery times, revenue, and delivery status.

Topics covered:

- Pandas Series and DataFrames
- Importing CSV files
- Exploring datasets with `head()`, `info()`, and `describe()`
- Understanding rows, columns, and DataFrame shapes
- Selecting data with `loc` and `iloc`
- Filtering with Boolean conditions
- Sorting and ranking observations
- Creating calculated columns
- Working with dates and timestamps
- Calculating revenue, operating costs, and profit
- Calculating individual and overall profit margins
- Exporting analysis results to CSV files

#### Practical Exercise: Logistics Shipment Analysis

Dataset: `shipments.csv`

Business questions included:

1. How many shipments are recorded?
2. What is the total revenue?
3. What is the average delivery time?
4. How many shipments were delayed?
5. Which delayed shipment generated the highest profit?
6. Which shipments generated more than €1,000 in profit?
7. What is the overall profit margin?
8. How can delayed shipments be exported for further analysis?

**Learning Outcome**

Use Pandas to explore structured datasets, manipulate observations, calculate business metrics, and answer practical analytical questions.

### 02.03 Data Cleaning & Transformation

**Status: Next**

Learn how to prepare real-world datasets for reliable analysis.

Planned topics:

- Identifying missing values
- Handling incomplete observations
- Detecting and removing duplicates
- Correcting inconsistent data types
- Standardizing categorical values
- Cleaning text columns
- Transforming numerical variables
- Building reproducible data-cleaning workflows

### 02.04 Data Aggregation & Business KPIs

**Status: Not Started**

Planned topics:

- `groupby()`
- Aggregation functions
- Group-level statistics
- Revenue and profitability analysis
- Operational performance metrics
- KPI calculations
- Business-oriented data analysis

### 02.05 Combining Multiple Datasets

**Status: Not Started**

Planned topics:

- Joining datasets
- Merging DataFrames
- Concatenation
- Join types
- Understanding relational data
- Combining information from multiple sources

### 02.06 Data Visualization & Storytelling

**Status: Not Started**

Planned topics:

- Exploratory Data Analysis
- Matplotlib
- Seaborn
- Choosing appropriate visualizations
- Identifying patterns and trends
- Communicating analytical findings
- Data storytelling

### 02.07 APIs, Web Scraping & Regex

**Status: Not Started**

Planned topics:

- Working with APIs
- HTTP requests
- JSON data
- Retrieving external datasets
- Web scraping fundamentals
- Regular expressions
- Extracting structured information from text

### 02.08 Statistics & Probability

**Status: Not Started**

Planned topics:

- Descriptive statistics
- Probability fundamentals
- Statistical distributions
- Sampling
- Statistical inference
- Confidence intervals
- Hypothesis testing

### 02.09 Professional Analytics Code

**Status: Not Started**

Planned topics:

- Structuring analytical projects
- Writing reusable analysis functions
- Clean and readable Pandas code
- Error handling
- Reproducibility
- Testing analytical workflows
- Documentation

### 02.10 Final Analytics Project

**Status: Not Started**

Apply the skills developed throughout Chapter 02 to a complete analytical problem.

The project will include:

1. Defining analytical questions.
2. Importing a real-world dataset.
3. Cleaning and transforming the data.
4. Performing exploratory analysis.
5. Calculating relevant KPIs.
6. Visualizing results.
7. Interpreting findings.
8. Communicating recommendations.

---

# 03 — Mathematics & Statistics

**Status: Not Started**

Develop the mathematical intuition required to understand optimization and machine learning.

### Planned Repository Structure

```text
03-maths/
│
├── linear-algebra/
├── calculus/
├── probability/
└── statistics/
```

### Linear Algebra

- Vectors
- Matrices
- Matrix operations
- Linear transformations
- Systems of equations
- Eigenvalues and eigenvectors

### Calculus

- Functions
- Derivatives
- Partial derivatives
- Gradients
- Optimization intuition

### Probability

- Random variables
- Probability distributions
- Conditional probability
- Expectation and variance
- Bayes' theorem

### Statistics

- Descriptive statistics
- Sampling
- Estimation
- Confidence intervals
- Hypothesis testing
- Correlation
- Regression foundations

---

# 04 — Decision Science

**Status: Not Started**

Use mathematical models and algorithms to make optimal decisions.

### Planned Repository Structure

```text
04-decision-science/
│
├── optimization/
├── linear-programming/
├── integer-programming/
├── stochastic-models/
└── operations-research/
```

Topics include:

- Mathematical optimization
- Objective functions and constraints
- Linear Programming
- Integer Programming
- Modeling decision problems
- Network problems
- Scheduling and allocation
- Stochastic models
- Optimization with Python
- Operations Research applications

The focus is on translating real-world business and operational problems into mathematical models that can support better decisions.

---

# 05 — Machine Learning

**Status: Not Started**

Understand both how machine-learning algorithms work and how to apply them correctly.

### Planned Repository Structure

```text
05-machine-learning/
│
├── supervised-learning/
├── unsupervised-learning/
├── model-evaluation/
├── feature-engineering/
└── pipelines/
```

### Supervised Learning

- Linear Regression
- Logistic Regression
- Decision Trees
- Random Forests
- Gradient Boosting
- k-Nearest Neighbors
- Support Vector Machines

### Unsupervised Learning

- Clustering
- K-Means
- Dimensionality reduction
- PCA

### Model Evaluation

- Train / validation / test split
- Cross-validation
- Regression metrics
- Classification metrics
- Bias and variance
- Overfitting and underfitting

### Feature Engineering

- Encoding
- Scaling
- Transformations
- Feature selection
- Data leakage

### ML Pipelines

- Preprocessing
- Training
- Evaluation
- Hyperparameter tuning
- Reproducible workflows

---

# 06 — Deep Learning

**Status: Not Started**

Build an understanding of neural networks from the mathematical foundations to practical implementation.

### Planned Repository Structure

```text
06-deep-learning/
│
├── neural-networks/
├── training/
├── architectures/
└── applications/
```

Topics include:

- Neurons and layers
- Activation functions
- Forward propagation
- Loss functions
- Gradient descent
- Backpropagation
- Optimizers
- Regularization
- Neural-network architectures
- TensorFlow / Keras
- Practical deep-learning workflows

---

# 07 — Projects

**Status: Not Started**

Apply concepts from multiple areas to complete problems.

### Planned Repository Structure

```text
07-projects/
│
├── python/
├── data-analysis/
├── optimization/
├── machine-learning/
└── deep-learning/
```

Projects should increasingly combine multiple skills rather than test isolated concepts.

The objective is to develop the ability to solve complete problems independently, from defining the question to implementing and evaluating a solution.

Larger portfolio projects may be moved into their own dedicated GitHub repositories.

---

# Learning Method

Each topic follows approximately the same learning cycle:

```text
1. Context
      ↓
2. Concept
      ↓
3. Mental Model
      ↓
4. Small Example
      ↓
5. Implement it myself
      ↓
6. Run & inspect
      ↓
7. Debug
      ↓
8. Explain what happened
      ↓
9. Refactor
      ↓
10. Revisit later
```

The focus is on **active coding rather than passive reading**.

I should be able to:

1. Explain the concept in my own words.
2. Implement it without copying an example.
3. Understand the output.
4. Debug common mistakes.
5. Recognize when the concept is useful.

Only then is a topic considered understood.

### Practical Learning Approach

The learning process emphasizes:

- Small, focused coding exercises
- Hands-on implementation
- Real-world datasets
- Business and operational use cases
- Understanding errors rather than simply correcting them
- Building reusable analytical skills
- Gradually increasing complexity

The objective is to develop independent problem-solving skills rather than relying on memorized solutions.

---

# Progress Tracking

Detailed progress is documented in:

`PROGRESS.md`

The progress tracker records:

- Completed chapters and subchapters
- Current learning position
- Upcoming topics
- Practical exercises and projects

### Current Learning Status

| Chapter | Status |
|---------|--------|
| 01 — Python Fundamentals | Completed |
| 02 — Data Toolkit | In Progress (20%) |
| 03 — Mathematics & Statistics | Not Started |
| 04 — Decision Science | Not Started |
| 05 — Machine Learning | Not Started |
| 06 — Deep Learning | Not Started |
| 07 — Projects | Not Started |

Progress is updated after completing each learning module.

---

# Current Position

**Chapter 01 — Python Fundamentals: Completed**

**Chapter 02 — Data Toolkit: In Progress (20%)**

```text
Data Science & AI Prep
│
├── 01 — Python Fundamentals       ✓ Completed
│
├── 02 — Data Toolkit              ◐ In Progress
│   ├── 02.01 NumPy                ✓ Completed
│   ├── 02.02 Pandas Fundamentals  ✓ Completed
│   └── 02.03 Data Cleaning        → Next
│
├── 03 — Mathematics & Statistics
├── 04 — Decision Science
├── 05 — Machine Learning
├── 06 — Deep Learning
└── 07 — Projects
```

### Current Focus

Developing practical data analysis skills with Python, NumPy, and Pandas.

The goal is to become comfortable working with real-world datasets, performing data transformations, and deriving meaningful insights.

### Next Learning Session

**02.03 — Data Cleaning & Transformation**

The next module focuses on identifying and correcting common data-quality issues before performing further analysis.

---

## Principle

> Understand → implement → experiment → break → debug → explain → revisit.

The objective is not to memorize syntax, but to develop the ability to reason about code, data, mathematical models, and machine-learning systems independently.