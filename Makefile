# Variables
PIP=pip3
PYTHON = python3
SRC = src
TESTS = tests

# Install dependencies
install:
	pip install -r requirements.txt

# Run compute sales
run:
	make clean
	$(PYTHON) src/compute_sales.py data/priceCatalogue.json data/salesRecord.json

# Execute unit tests
test:
	pytest -v

# Run flake8
flake:
	flake8 $(SRC) $(TESTS)

# Run pylint
lint:
	pylint $(SRC) $(TESTS)

# Execute all checks
check: flake lint test

# Clean temp files
clean:
	find . -type d -name "__pycache__" -exec rm -r {} +
	find . -type f -name "*.pyc" -delete
	rm -f output/SalesResults.txt