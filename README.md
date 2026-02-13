# Programming Exercise 5.2 – Compute Sales

## Description

This project implements a Python program that calculates the total sales cost based on:

- A product price catalogue (JSON file)
- A sales record file (JSON file)

The program validates input data, handles errors gracefully, performs static code analysis, and includes unit testing to ensure software quality.

---

## Objectives

- Apply static and dynamic testing techniques
- Implement defensive programming
- Follow PEP-8 coding standards
- Use static analysis tools
- Automate testing and validation tasks

---

## Project Structure
```
A01797233_ejercicio5.2/
│
├── .github/
│ └── workflows
│       └── flake.yml
│       └── pr-title.yml
│       └── pylint.yml
│       └── unit_test.yml
│
├── src/
│ └── compute_sales.py
│
├── tests/
│ └── test_compute_sales.py
│
├── data/
│ ├── priceCatalogue.json
│ ├── salesRecord.json
│ ├── priceCatalogue_with_errors.json
│ └── salesRecord_with_errors.json
│
├── output/
├── Salesresults.txt
│
├── requirements.txt
├── Makefile
├── README.md
```


---

## Requirements

- Python 3.10+
- pip
- Virtual environment recommended

---

## Install dependencies

```bash
    make install
```

## Running the Program


```bash
    make run
```

Results will be displayed on screen and saved into:

```
    output/SalesResults.txt
```

## Running Unit Tests

```bash
    make test
```

## Static Code Analysis

### Flake
```bash
    make flake
```
### Pylint
```bash
    make pylint
```

## Execute All Quality Checks
```bash
    make check
```

This command runs:
```
    Flake8
    Pylint
    Unit tests
```

## Test Coverage
```bash
    pytest -v
```
