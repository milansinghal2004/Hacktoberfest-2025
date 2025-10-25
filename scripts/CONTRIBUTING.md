# Contributing Guidelines

Thank you for your interest in contributing to the Factorial Calculator project!

## Development Setup

1. Clone the repository
2. Navigate to the scripts directory
3. No additional dependencies required for basic functionality

## Running Tests

Before submitting any changes, ensure all tests pass:

### Quick Test Run
```bash
python3 -m unittest test_factorial_calculator.py
```

### Comprehensive Testing
```bash
python3 run_tests.py --all
```

## Test Requirements

All contributions must:

1. **Pass existing tests**: All current tests must continue to pass
2. **Add new tests**: New functionality requires corresponding test cases
3. **Maintain coverage**: Aim for comprehensive test coverage
4. **Follow patterns**: Use existing test patterns and naming conventions

## Test Categories

When adding tests, consider these categories:

- **Basic functionality**: Core feature testing
- **Edge cases**: Boundary conditions (0, 1, large numbers)
- **Error handling**: Invalid inputs and error conditions
- **Performance**: Execution time and efficiency
- **Integration**: Module and function integration

## Code Quality Standards

### Testing Best Practices

1. **Descriptive test names**: Use clear, descriptive test method names
2. **Good documentation**: Include docstrings for test methods
3. **Isolated tests**: Each test should be independent
4. **Assertion messages**: Provide clear failure messages
5. **Use subtests**: For parameterized testing with multiple inputs

### Example Test Structure

```python
def test_function_name_scenario(self):
    """Test that function behaves correctly under specific scenario."""
    # Arrange
    input_value = 5
    expected_result = 120
    
    # Act
    actual_result = factorial(input_value)
    
    # Assert
    self.assertEqual(
        actual_result, 
        expected_result,
        f"factorial({input_value}) should return {expected_result}"
    )
```

## Submitting Changes

1. **Fork the repository**
2. **Create a feature branch**
3. **Make your changes**
4. **Add/update tests**
5. **Run full test suite**
6. **Submit pull request**

### Pull Request Checklist

- [ ] All existing tests pass
- [ ] New tests added for new functionality
- [ ] Code follows existing style conventions
- [ ] Documentation updated if necessary
- [ ] Test coverage maintained or improved

## Common Testing Scenarios

### Adding New Functionality

When adding new features:

1. Write tests first (TDD approach recommended)
2. Implement the feature
3. Ensure all tests pass
4. Add edge case tests
5. Add error handling tests

### Bug Fixes

When fixing bugs:

1. Write a test that reproduces the bug
2. Verify the test fails with current code
3. Fix the bug
4. Verify the test now passes
5. Ensure no regression in other tests

## Testing Tools

### Built-in Tools
- `unittest`: Python standard library testing framework
- `python3 -m unittest`: Command-line test runner

### Optional Tools
- `pytest`: Enhanced testing framework
- `coverage`: Test coverage analysis
- `pytest-cov`: Coverage plugin for pytest

### Installation of Optional Tools
```bash
pip install -r requirements-test.txt
```

## Performance Testing

For performance-related changes:

1. Run baseline benchmarks before changes
2. Implement changes
3. Run benchmarks again
4. Document performance impact
5. Ensure no significant performance regression

```bash
python3 test_factorial_calculator.py --benchmark
```

## Troubleshooting Tests

### Common Issues

1. **Import errors**: Ensure you're in the correct directory
2. **Path issues**: Use absolute imports when necessary
3. **Python version**: Ensure Python 3.6+ is being used

### Getting Help

If you encounter issues with testing:

1. Check test output for specific error messages
2. Verify your Python environment
3. Ensure all dependencies are available
4. Review existing test examples
5. Check the README.md for detailed testing instructions

## Code Review Process

All contributions go through code review:

1. **Automated testing**: GitHub Actions runs tests automatically
2. **Manual review**: Maintainers review code quality and test coverage
3. **Feedback incorporation**: Address review comments
4. **Final approval**: Merge after all checks pass

## Recognition

Contributors who significantly improve test coverage or add valuable test cases will be recognized in the project documentation.

Thank you for helping make this project more robust and reliable through comprehensive testing!