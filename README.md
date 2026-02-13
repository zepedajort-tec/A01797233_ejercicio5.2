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

<img width="1230" height="378" alt="Captura de pantalla 2026-02-13 a la(s) 16 24 29" src="https://github.com/user-attachments/assets/49174991-c7f5-4f76-9174-b7b2780efeab" />

## Running the Program


```bash
    make run
```

<img width="606" height="156" alt="Captura de pantalla 2026-02-13 a la(s) 16 25 08" src="https://github.com/user-attachments/assets/03970a98-d44d-4961-a2d5-2d0b98a61d3c" />

Results will be displayed on screen and saved into:

```
    output/SalesResults.txt
```

<img width="261" height="452" alt="Captura de pantalla 2026-02-13 a la(s) 16 21 31" src="https://github.com/user-attachments/assets/6c0af068-ca27-469c-b82c-2918b88efcf6" />

Following image displays SalesResults.txt output after running ```make run```

<img width="327" height="153" alt="Captura de pantalla 2026-02-13 a la(s) 16 22 10" src="https://github.com/user-attachments/assets/2bce571c-7a8f-4c58-bb5f-830e30bbd795" />

## Running Unit Tests

```bash
    make test
```

<img width="1303" height="314" alt="Captura de pantalla 2026-02-13 a la(s) 16 25 49" src="https://github.com/user-attachments/assets/1f4ba126-75b2-4ab9-8c92-58c80a1f0160" />

## Static Code Analysis

### Flake
```bash
    make flake
```
<img width="564" height="69" alt="Captura de pantalla 2026-02-13 a la(s) 16 27 02" src="https://github.com/user-attachments/assets/59636f7a-7547-4870-a358-f7f76305141a" />

### Pylint
```bash
    make lint
```
<img width="567" height="142" alt="Captura de pantalla 2026-02-13 a la(s) 16 27 56" src="https://github.com/user-attachments/assets/f91642b1-f060-49a0-83dd-2723102ebc81" />

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
<img width="1304" height="421" alt="Captura de pantalla 2026-02-13 a la(s) 16 28 39" src="https://github.com/user-attachments/assets/f59f635f-2ca1-42a4-b550-1a9754848701" />

## Test Coverage
```bash
    pytest -v
```

## PR workflows

At this time we have 4 workflows

    - pr-title check: it verify Pull Rquest format (feat, fix, chore, etc)
    - pylint check: it verify pylint code changes in src/ data/ and tests/ directories
    - flake check: it verify flake8 code changes in src/ data/ and tests/ directories
    - unit_test check: it verify all unit test in tests/ directory

<img width="921" height="436" alt="Captura de pantalla 2026-02-13 a la(s) 0 36 24" src="https://github.com/user-attachments/assets/aa370911-84f3-4d5c-95e0-bf3b4d06e95a" />

