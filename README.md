Data Science & AI Prep

A structured learning repository to strengthen my foundations in Python, data analytics, mathematics, decision science, machine learning, and deep learning.

The goal is not just to work through individual topics, but to build a strong understanding of the concepts behind modern Data Science & AI and to apply them through code.

The learning process combines theoretical understanding with practical exercises, real-world datasets, and progressively more complex projects.

⸻

Learning Path

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

The repository grows together with my progress. New folders and topics are added as I reach them instead of creating the entire structure in advance.

⸻

Repository Structure

The repository is organized into seven main chapters.

data-science-prep/
│
├── 01-python/
│
├── 02-data-toolkit/
│   ├── 01-numpy/
│   ├── 02-pandas/
│   ├── 03-data-cleaning/
│   ├── 04-data-aggregation/
│   ├── 05-data-merging/
│   ├── 06-data-visualization/
│   └── 07-apis-web-scraping/
│
├── 03-maths/                  (planned)
├── 04-decision-science/       (planned)
├── 05-machine-learning/      (planned)
├── 06-deep-learning/          (planned)
├── 07-projects/               (planned)
│
├── .gitignore
├── README.md
├── PROGRESS.md
└── requirements.txt

Folders for future chapters are created progressively as the learning path advances.

⸻

01 — Python Fundamentals

Status: Completed — 100%

Build a solid Python foundation before moving into the Data Science stack.

The objective is to understand how Python works, develop programming logic, and write structured, reusable code.

Learning Modules

Module	Topic	Status
01.01	Python Basics	Completed
01.02	Control Flow	Completed
01.03	Functions	Completed
01.04	Data Structures	Completed
01.05	Modules	Completed
01.06	Object-Oriented Programming	Completed
01.07	Error Handling	Completed
01.08	Professional Python	Completed

01.01 Python Basics

* Variables and objects
* Data types
* Object identity
* References
* Mutable vs. immutable objects
* Copying objects
* Operators
* Basic input/output

01.02 Control Flow

* Boolean logic
* Comparisons
* if / elif / else
* for loops
* while loops
* break and continue
* Iteration patterns

01.03 Functions

* Defining functions
* Parameters and arguments
* Return values
* Scope
* Default parameters
* *args and **kwargs
* Lambda functions
* Writing reusable functions

01.04 Data Structures

* Lists
* Tuples
* Dictionaries
* Sets
* Nested data structures
* Indexing and slicing
* List / dictionary comprehensions
* Choosing appropriate data structures

01.05 Modules

* Imports
* Python standard library
* Creating own modules
* Packages
* Organizing Python code
* Environments and dependencies

01.06 Object-Oriented Programming

* Classes and objects
* Attributes
* Methods
* Constructors
* Instance vs. class attributes
* Inheritance
* Composition

01.07 Error Handling

* Reading tracebacks
* Exceptions
* try / except
* else / finally
* Raising exceptions
* Debugging

01.08 Professional Python

* Clean code
* Naming and structure
* Type hints
* Docstrings
* Testing
* Debugging
* Refactoring
* Git workflow

Learning Outcome

After completing Chapter 01, I can:

* Write Python programs using functions, loops, and data structures.
* Understand how Python handles objects and references.
* Organize code into reusable components.
* Identify and debug common programming errors.
* Work with Python environments and external libraries.
* Use Git and GitHub to manage my learning projects.

⸻

02 — Data Toolkit

Status: In Progress — 70% Completed

Move from general Python programming toward working with real-world data.

The focus is on practical data analysis, transforming raw data into meaningful information, and developing the skills required for business analytics, operations analytics, and machine learning.

Seven of ten learning modules have been completed.

The current focus is transitioning from practical data collection and analysis toward statistical reasoning and inference.

Repository Structure

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
├── 03-data-cleaning/
│   └── data_cleaning.ipynb
│
├── 04-data-aggregation/
│   └── business_kpis.ipynb
│
├── 05-data-merging/
│   └── data_merging.ipynb
│
├── 06-data-visualization/
│   └── data_visualization.ipynb
│
└── 07-apis-web-scraping/
    └── apis_web_scraping.ipynb

Learning Modules

Module	Topic	Status
02.01	NumPy	Completed
02.02	Pandas Fundamentals	Completed
02.03	Data Cleaning & Transformation	Completed
02.04	Data Aggregation & Business KPIs	Completed
02.05	Combining Multiple Datasets	Completed
02.06	Data Visualization & Storytelling	Completed
02.07	APIs, Web Scraping & Regex	Completed
02.08	Statistics & Probability	Next
02.09	Professional Analytics Code	Not Started
02.10	Final Analytics Project	Not Started

⸻

02.01 NumPy

Status: Completed

Introduction to numerical computing with Python.

Topics Covered

* NumPy arrays
* Array creation
* Dimensions and shapes
* Indexing and slicing
* Vectorized operations
* Broadcasting
* Numerical calculations
* Working with multidimensional arrays

Learning Outcome

Understand how NumPy enables efficient numerical operations and why vectorized computations are important for data science.

⸻

02.02 Pandas Fundamentals

Status: Completed

Introduction to data manipulation and analysis using Pandas.

Practical exercises are based on a logistics shipment dataset containing shipment information, customers, cities, delivery times, revenue, and delivery status.

Topics Covered

* Pandas Series and DataFrames
* Importing CSV files
* Exploring datasets with head(), info(), and describe()
* Understanding rows, columns, and DataFrame shapes
* Selecting data with loc and iloc
* Filtering with Boolean conditions
* Sorting and ranking observations
* Creating calculated columns
* Working with dates and timestamps
* Calculating revenue, operating costs, and profit
* Calculating individual and overall profit margins
* Exporting analysis results to CSV files

Practical Exercise: Logistics Shipment Analysis

Dataset: shipments.csv

Business questions included:

1. How many shipments are recorded?
2. What is the total revenue?
3. What is the average delivery time?
4. How many shipments were delayed?
5. Which delayed shipment generated the highest profit?
6. Which shipments generated more than €1,000 in profit?
7. What is the overall profit margin?
8. How can delayed shipments be exported for further analysis?

Learning Outcome

Use Pandas to explore structured datasets, manipulate observations, calculate business metrics, and answer practical analytical questions.

⸻

02.03 Data Cleaning & Transformation

Status: Completed

Learn how to prepare real-world datasets for reliable analysis.

Real-world data is often incomplete, inconsistent, or incorrectly formatted. Before performing analysis, these issues must be identified and handled systematically.

Topics Covered

* Identifying missing values
* Handling incomplete observations
* Detecting duplicate records
* Removing duplicates using appropriate identifiers
* Correcting inconsistent data types
* Standardizing categorical values
* Cleaning text columns
* Converting numerical variables
* Preserving original datasets
* Validating data quality after transformations

Practical Exercise: Shipment Data Cleaning

Worked with a logistics dataset containing common data-quality problems.

The cleaning workflow included:

1. Preserving the original dataset.
2. Identifying duplicate shipment IDs.
3. Standardizing customer names.
4. Standardizing shipment statuses.
5. Converting revenue values into numerical data.
6. Handling missing delivery times using the median.
7. Preserving unknown financial values instead of inventing replacements.
8. Verifying the cleaned dataset.

The objective was to produce a cleaned DataFrame while maintaining data integrity.

Learning Outcome

Build reproducible data-cleaning workflows, identify common data-quality problems, and make appropriate cleaning decisions without introducing unsupported assumptions.

⸻

02.04 Data Aggregation & Business KPIs

Status: Completed

Learn how to transform individual observations into meaningful business performance indicators.

Topics Covered

* Grouping observations using groupby()
* Aggregation functions
* Group-level statistics
* Revenue analysis
* Profitability analysis
* Operational performance metrics
* Customer-level analysis
* KPI calculations
* Comparing performance across categories

Practical Exercise: Logistics Business KPIs

Analyzed shipment data to derive operational and financial insights.

The exercises focused on understanding how individual shipment records can be aggregated to evaluate customer performance, operational efficiency, and profitability.

Learning Outcome

Transform transactional data into meaningful business metrics and use aggregation techniques to identify patterns, compare performance, and support operational decisions.

⸻

02.05 Combining Multiple Datasets

Status: Completed

Learn how to combine information from multiple sources using Pandas.

In real-world analytics, relevant information is frequently distributed across several datasets. Understanding how to combine these datasets correctly is essential.

Topics Covered

* Merging DataFrames
* Understanding join keys
* Inner joins
* Left joins
* Right joins
* Outer joins
* Concatenation
* Handling missing matches
* Validating merged datasets
* Understanding how join operations affect the resulting data

Practical Exercise: Combining Logistics Datasets

Combined related datasets to create a more comprehensive analytical view.

The exercises focused on identifying appropriate join keys, understanding differences between join types, and validating the resulting DataFrames.

Learning Outcome

Combine multiple datasets accurately and understand how different join operations affect the completeness and structure of analytical results.

⸻

02.06 Data Visualization & Storytelling

Status: Completed

Learn how to explore datasets visually and communicate analytical findings effectively.

The focus is not only on creating charts, but also on selecting appropriate visualizations and translating data into meaningful business insights.

Topics Covered

* Exploratory Data Analysis
* Matplotlib
* Seaborn
* Bar charts
* Histograms
* Scatter plots
* Regression visualizations
* Correlation analysis
* Distribution analysis
* Creating multi-chart dashboards
* Communicating findings to management

Practical Exercise: Logistics Management Dashboard

Developed a four-panel analytical dashboard using Python.

The dashboard combined several perspectives on operational and financial performance.

Visualizations included:

* Customer revenue comparison
* Shipment volume analysis
* Delivery-time distribution
* Relationships between numerical variables

The exercise emphasized selecting meaningful visualizations, interpreting results, and presenting information clearly.

Learning Outcome

Create analytical visualizations, identify patterns and relationships in data, and communicate results through structured dashboards.

⸻

02.07 APIs, Web Scraping & Regular Expressions

Status: Completed

Learn how to retrieve external data using APIs, extract information from websites, and transform unstructured information into structured datasets.

Learning Modules

Submodule	Topic	Status
02.07.01	Understanding APIs & HTTP Requests	Completed
02.07.02	API Query Parameters & Filtering	Completed
02.07.03	API Error Handling & Reliability	Completed
02.07.04	Combining Multiple API Endpoints	Completed
02.07.05	API Pagination	Completed
02.07.06	Web Scraping with BeautifulSoup	Completed
02.07.07	Extracting Structured Data from HTML	Completed
02.07.08	Regular Expressions	Completed
02.07.09	Web Data Collection Mini-Project	Completed

APIs & HTTP Requests

* Understanding REST APIs
* Sending HTTP requests using requests
* Working with JSON responses
* Converting JSON into Pandas DataFrames
* Query parameters
* Filtering API responses
* HTTP status codes
* Error handling
* Request timeouts
* Retry mechanisms
* Exponential backoff
* Combining multiple API endpoints
* API pagination

Web Scraping

* Understanding HTML structure
* Parsing HTML using BeautifulSoup
* Finding HTML elements
* Extracting text and attributes
* Extracting multiple records
* Creating structured datasets
* Handling pagination
* Converting extracted data into Pandas DataFrames

Regular Expressions

* Pattern matching
* Extracting numerical information
* Capturing groups
* Matching structured identifiers
* re.findall()
* re.search()
* re.sub()
* Cleaning and standardizing text using Regex

Practical Project: Bookstore Web Scraper

Website: Books to Scrape

Developed a Python web scraper that automatically retrieves product information from a multi-page online bookstore demonstration website.

Project Objectives

1. Retrieve HTML content using Python.
2. Extract structured product information.
3. Navigate automatically through multiple catalogue pages.
4. Combine all extracted records into one DataFrame.
5. Clean numerical values.
6. Validate the resulting dataset.

Extracted Information

Column	Description
Book Title	Product title
Price	Book price in GBP
Available	Availability status
Rating	Product rating category

Project Results

* Scraped 50 catalogue pages
* Collected 1,000 book records
* Extracted four product attributes
* Converted prices into numerical values
* Verified missing values
* Investigated duplicate book titles
* Analyzed rating distributions
* Verified availability information

Data Quality Findings

The collected dataset contained:

* 1,000 records
* 4 columns
* No missing values
* One duplicated title
* Five rating categories
* All products marked as available

The duplicated title appeared in two records with different prices but identical ratings.

Both records were preserved because identical titles alone were insufficient to establish that they represented the same product.

Learning Outcome

Develop Python workflows that retrieve external data, handle HTTP requests reliably, extract information from HTML, transform unstructured information into Pandas DataFrames, and validate the resulting datasets.

⸻

02.08 Statistics & Probability

Status: Next

Develop statistical reasoning skills and learn how to interpret data beyond descriptive summaries.

Planned Topics

* Descriptive statistics
* Statistical distributions
* Probability fundamentals
* Random variables
* Expected values
* Variance and standard deviation
* Sampling
* Central Limit Theorem
* Statistical inference
* Confidence intervals
* Hypothesis testing
* p-values
* Correlation vs. causation
* A/B testing

Learning Objective

Understand how statistical methods can be used to quantify uncertainty, evaluate evidence, and support data-driven decisions.

⸻

02.09 Professional Analytics Code

Status: Not Started

Learn how to structure analytical code for readability, maintainability, and reproducibility.

Planned Topics

* Structuring analytical projects
* Writing reusable analysis functions
* Clean and readable Pandas code
* Error handling
* Reproducibility
* Testing analytical workflows
* Documentation
* Refactoring analytical code

Learning Objective

Develop professional coding practices for building reliable and maintainable data-analysis workflows.

⸻

02.10 Final Analytics Project

Status: Not Started

Apply the skills developed throughout Chapter 02 to a complete analytical problem.

Planned Project Workflow

1. Define analytical questions.
2. Import a real-world dataset.
3. Assess data quality.
4. Clean and transform the data.
5. Perform exploratory analysis.
6. Calculate relevant business KPIs.
7. Visualize results.
8. Apply appropriate statistical methods.
9. Interpret findings.
10. Communicate recommendations.

Learning Objective

Demonstrate the ability to independently execute an end-to-end data-analysis project.

⸻

03 — Mathematics & Statistics

Status: Not Started

Develop the mathematical intuition required to understand optimization and machine learning.

Planned Repository Structure

03-maths/
│
├── linear-algebra/
├── calculus/
├── probability/
└── statistics/

Linear Algebra

* Vectors
* Matrices
* Matrix operations
* Linear transformations
* Systems of equations
* Eigenvalues and eigenvectors

Calculus

* Functions
* Derivatives
* Partial derivatives
* Gradients
* Optimization intuition

Probability

* Random variables
* Probability distributions
* Conditional probability
* Expectation and variance
* Bayes’ theorem

Statistics

* Descriptive statistics
* Sampling
* Estimation
* Confidence intervals
* Hypothesis testing
* Correlation
* Regression foundations

⸻

04 — Decision Science

Status: Not Started

Use mathematical models and algorithms to make optimal decisions.

Planned Repository Structure

04-decision-science/
│
├── optimization/
├── linear-programming/
├── integer-programming/
├── stochastic-models/
└── operations-research/

Planned Topics

* Mathematical optimization
* Objective functions and constraints
* Linear Programming
* Integer Programming
* Modeling decision problems
* Network problems
* Scheduling and allocation
* Stochastic models
* Optimization with Python
* Operations Research applications

The focus is on translating real-world business and operational problems into mathematical models that can support better decisions.

⸻

05 — Machine Learning

Status: Not Started

Understand both how machine-learning algorithms work and how to apply them correctly.

Planned Repository Structure

05-machine-learning/
│
├── supervised-learning/
├── unsupervised-learning/
├── model-evaluation/
├── feature-engineering/
└── pipelines/

Supervised Learning

* Linear Regression
* Logistic Regression
* Decision Trees
* Random Forests
* Gradient Boosting
* k-Nearest Neighbors
* Support Vector Machines

Unsupervised Learning

* Clustering
* K-Means
* Dimensionality reduction
* PCA

Model Evaluation

* Train / validation / test split
* Cross-validation
* Regression metrics
* Classification metrics
* Bias and variance
* Overfitting and underfitting

Feature Engineering

* Encoding
* Scaling
* Transformations
* Feature selection
* Data leakage

ML Pipelines

* Preprocessing
* Training
* Evaluation
* Hyperparameter tuning
* Reproducible workflows

⸻

06 — Deep Learning

Status: Not Started

Build an understanding of neural networks from the mathematical foundations to practical implementation.

Planned Repository Structure

06-deep-learning/
│
├── neural-networks/
├── training/
├── architectures/
└── applications/

Planned Topics

* Neurons and layers
* Activation functions
* Forward propagation
* Loss functions
* Gradient descent
* Backpropagation
* Optimizers
* Regularization
* Neural-network architectures
* TensorFlow / Keras
* Practical deep-learning workflows

⸻

07 — Projects

Status: Not Started

Apply concepts from multiple areas to complete problems.

Planned Repository Structure

07-projects/
│
├── python/
├── data-analysis/
├── optimization/
├── machine-learning/
└── deep-learning/

Projects should increasingly combine multiple skills rather than test isolated concepts.

The objective is to develop the ability to solve complete problems independently, from defining the question to implementing and evaluating a solution.

Larger portfolio projects may be moved into their own dedicated GitHub repositories.

⸻

Learning Method

Each topic follows approximately the same learning cycle:

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

The focus is on active coding rather than passive reading.

I should be able to:

1. Explain the concept in my own words.
2. Implement it without copying an example.
3. Understand the output.
4. Debug common mistakes.
5. Recognize when the concept is useful.

Only then is a topic considered understood.

Practical Learning Approach

The learning process emphasizes:

* Small, focused coding exercises
* Hands-on implementation
* Real-world datasets
* Business and operational use cases
* Understanding errors rather than simply correcting them
* Building reusable analytical skills
* Gradually increasing complexity

The objective is to develop independent problem-solving skills rather than relying on memorized solutions.

⸻

Progress Tracking

Detailed progress is documented in:

PROGRESS.md

The progress tracker records:

* Completed chapters and subchapters
* Current learning position
* Upcoming topics
* Practical exercises and projects

Current Learning Status

Chapter	Status
01 — Python Fundamentals	Completed (100%)
02 — Data Toolkit	In Progress (70%)
03 — Mathematics & Statistics	Not Started
04 — Decision Science	Not Started
05 — Machine Learning	Not Started
06 — Deep Learning	Not Started
07 — Projects	Not Started

Progress is updated after completing each learning module.

⸻

Current Position

Chapter 01 — Python Fundamentals: Completed

Chapter 02 — Data Toolkit: In Progress (70%)

Data Science & AI Prep
│
├── 01 — Python Fundamentals         ✓ Completed
│
├── 02 — Data Toolkit                ◐ 70% Completed
│   ├── 02.01 NumPy                  ✓ Completed
│   ├── 02.02 Pandas Fundamentals    ✓ Completed
│   ├── 02.03 Data Cleaning          ✓ Completed
│   ├── 02.04 Business KPIs          ✓ Completed
│   ├── 02.05 Data Merging           ✓ Completed
│   ├── 02.06 Data Visualization     ✓ Completed
│   ├── 02.07 APIs & Web Scraping    ✓ Completed
│   ├── 02.08 Statistics             → Next
│   ├── 02.09 Professional Code
│   └── 02.10 Final Analytics Project
│
├── 03 — Mathematics & Statistics
├── 04 — Decision Science
├── 05 — Machine Learning
├── 06 — Deep Learning
└── 07 — Projects

Current Focus

Developing statistical reasoning skills using Python, NumPy, Pandas, and SciPy.

The next stage focuses on understanding probability distributions, sampling, statistical inference, and hypothesis testing.

The objective is to move beyond descriptive analysis toward evaluating uncertainty and making statistically informed decisions.

Next Learning Session

02.08 — Statistics & Probability

The next module focuses on understanding statistical distributions and applying probability and inference concepts to practical analytical problems.

⸻

Principle

Understand → implement → experiment → break → debug → explain → revisit.

The objective is not to memorize syntax, but to develop the ability to reason about code, data, mathematical models, and machine-learning systems independently.