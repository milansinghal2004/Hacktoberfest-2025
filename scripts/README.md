# Factorial Calculator

A Python implementation of factorial calculation with comprehensive unit testing.

## Description

This project provides a simple yet robust factorial calculator that computes the factorial of non-negative integers. The implementation includes comprehensive error handling and validation to ensure reliable operation.

## Features

- Calculates factorial for non-negative integers
- Comprehensive error handling for invalid inputs
- Extensive unit test coverage
- Performance benchmarking capabilities
- Well-documented code with docstrings

## Installation

No external dependencies are required for the basic functionality. The project uses only Python standard library modules.

### For Testing (Optional)

If you want to use pytest instead of unittest:

```bash
pip install pytest
```

For test coverage analysis:

```bash
pip install coverage
```

## Usage

### Basic Usage

```python
from factorial_calculator import factorial

# Calculate factorial of 5
result = factorial(5)
print(result)  # Output: 120

# Calculate factorial of 0
result = factorial(0)
print(result)  # Output: 1
```

### Running the Script Directly

```bash
python factorial_calculator.py
```

This will run example calculations and demonstrate the functionality.

## Running Tests

The project includes comprehensive unit tests to ensure code quality and functionality.

### Using unittest (Python standard library)

Run all tests:

```bash
python -m unittest test_factorial_calculator.py
```

Run tests with verbose output:

```bash
python -m unittest test_factorial_calculator.py -v
```

Run a specific test class:

```bash
python -m unittest test_factorial_calculator.TestFactorialCalculator
```

Run a specific test method:

```bash
python -m unittest test_factorial_calculator.TestFactorialCalculator.test_factorial_basic_cases
```

### Using pytest (if installed)

Run all tests:

```bash
pytest test_factorial_calculator.py
```

Run tests with verbose output:

```bash
pytest test_factorial_calculator.py -v
```

Run tests and show coverage:

```bash
pytest test_factorial_calculator.py --cov=factorial_calculator
```

### Running Tests Directly

You can also run the test file directly for additional options:

```bash
python test_factorial_calculator.py
```

With verbose output:

```bash
python test_factorial_calculator.py --verbose
```

With performance benchmarks:

```bash
python test_factorial_calculator.py --benchmark
```

Show test coverage information:

```bash
python test_factorial_calculator.py --coverage
```

## Test Coverage

The test suite provides comprehensive coverage including:

### Functional Tests
- Basic factorial calculations (0! through 15!)
- Edge cases (0 and 1)
- Large number calculations
- Mathematical property validation

### Error Handling Tests
- Negative number inputs (ValueError)
- Non-integer inputs (TypeError)
- Special cases with boolean inputs

### Integration Tests
- Module import functionality
- Function signature validation
- Documentation completeness

### Performance Tests
- Execution time validation
- Large number handling
- Performance benchmarking

## Test Structure

```
test_factorial_calculator.py
├── TestFactorialCalculator
│   ├── test_factorial_basic_cases
│   ├── test_factorial_larger_numbers
│   ├── test_factorial_zero
│   ├── test_factorial_one
│   ├── test_factorial_negative_numbers
│   ├── test_factorial_non_integer_inputs
│   ├── test_factorial_boolean_inputs
│   ├── test_factorial_return_type
│   ├── test_factorial_mathematical_properties
│   ├── test_factorial_consistency
│   ├── test_factorial_edge_case_large_number
│   └── test_factorial_performance_reasonable
└── TestFactorialCalculatorIntegration
    ├── test_module_import
    ├── test_function_docstring
    └── test_function_signature
```

## Continuous Integration

To integrate these tests into a CI/CD pipeline, add the following to your workflow:

### GitHub Actions Example

```yaml
name: Run Tests

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: [3.7, 3.8, 3.9, 3.10, 3.11]

    steps:
    - uses: actions/checkout@v2
    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: ${{ matrix.python-version }}
    
    - name: Run tests
      run: |
        cd scripts
        python -m unittest test_factorial_calculator.py -v
```

## Code Quality

The code follows Python best practices:

- PEP 8 style guidelines
- Comprehensive docstrings
- Type hints where appropriate
- Proper error handling
- Extensive test coverage

## Contributing

When contributing to this project:

1. Ensure all existing tests pass
2. Add tests for any new functionality
3. Update documentation as needed
4. Follow existing code style conventions

### Running All Quality Checks

```bash
# Run tests
python -m unittest test_factorial_calculator.py

# Check test coverage (if coverage is installed)
coverage run -m unittest test_factorial_calculator.py
coverage report -m

# Run performance benchmarks
python test_factorial_calculator.py --benchmark
```

## Error Handling

The factorial function includes robust error handling:

- **TypeError**: Raised when input is not an integer
- **ValueError**: Raised when input is a negative number

Example error handling:

```python
try:
    result = factorial(-5)
except ValueError as e:
    print(f"Error: {e}")  # Error: Factorial is not defined for negative numbers

try:
    result = factorial(3.5)
except TypeError as e:
    print(f"Error: {e}")  # Error: Input must be an integer
```

## Performance Notes

The current implementation uses an iterative approach with O(n) time complexity. For applications requiring frequent factorial calculations, consider implementing memoization for improved performance with repeated calculations.

## License

This project is part of the Hacktoberfest 2025 contribution and follows the repository's license terms.

## Support

For issues or questions regarding the factorial calculator or its tests:

1. Check existing test cases for expected behavior
2. Run the test suite to identify specific issues
3. Review error messages for debugging information
4. Refer to function docstrings for usage guidance