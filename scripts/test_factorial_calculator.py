#!/usr/bin/env python3
"""
Unit tests for factorial_calculator.py

This module contains comprehensive unit tests for the factorial function,
including tests for normal operation, edge cases, and error conditions.

Test Categories:
- Basic functionality tests
- Edge case tests
- Error handling tests
- Performance tests
- Input validation tests

Usage:
    python -m unittest test_factorial_calculator.py
    python -m pytest test_factorial_calculator.py (if pytest is installed)
"""

import unittest
import sys
import os

# Add the current directory to the Python path to import factorial_calculator
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from factorial_calculator import factorial


class TestFactorialCalculator(unittest.TestCase):
    """Test cases for the factorial function."""

    def setUp(self):
        """Set up test fixtures before each test method."""
        pass

    def tearDown(self):
        """Clean up after each test method."""
        pass

    def test_factorial_basic_cases(self):
        """Test factorial calculation for basic valid inputs."""
        test_cases = [
            (0, 1),     # 0! = 1 (mathematical definition)
            (1, 1),     # 1! = 1
            (2, 2),     # 2! = 2
            (3, 6),     # 3! = 6
            (4, 24),    # 4! = 24
            (5, 120),   # 5! = 120
            (6, 720),   # 6! = 720
            (7, 5040),  # 7! = 5040
        ]
        
        for input_value, expected_result in test_cases:
            with self.subTest(input_value=input_value):
                actual_result = factorial(input_value)
                self.assertEqual(
                    actual_result, 
                    expected_result,
                    f"factorial({input_value}) should return {expected_result}, got {actual_result}"
                )

    def test_factorial_larger_numbers(self):
        """Test factorial calculation for larger valid inputs."""
        test_cases = [
            (8, 40320),
            (9, 362880),
            (10, 3628800),
            (12, 479001600),
            (15, 1307674368000),
        ]
        
        for input_value, expected_result in test_cases:
            with self.subTest(input_value=input_value):
                actual_result = factorial(input_value)
                self.assertEqual(
                    actual_result, 
                    expected_result,
                    f"factorial({input_value}) should return {expected_result}, got {actual_result}"
                )

    def test_factorial_zero(self):
        """Test that factorial of 0 returns 1 (mathematical definition)."""
        result = factorial(0)
        self.assertEqual(result, 1, "factorial(0) should return 1")

    def test_factorial_one(self):
        """Test that factorial of 1 returns 1."""
        result = factorial(1)
        self.assertEqual(result, 1, "factorial(1) should return 1")

    def test_factorial_negative_numbers(self):
        """Test that factorial raises ValueError for negative inputs."""
        negative_test_cases = [-1, -5, -10, -100]
        
        for negative_input in negative_test_cases:
            with self.subTest(negative_input=negative_input):
                with self.assertRaises(ValueError) as context:
                    factorial(negative_input)
                
                error_message = str(context.exception)
                self.assertIn(
                    "Factorial is not defined for negative numbers", 
                    error_message,
                    f"ValueError message should mention negative numbers for input {negative_input}"
                )

    def test_factorial_non_integer_inputs(self):
        """Test that factorial raises TypeError for non-integer inputs."""
        non_integer_test_cases = [
            3.5,      # float
            "5",      # string
            [5],      # list
            None,     # None type
            complex(5, 0),  # complex number
        ]
        
        for invalid_input in non_integer_test_cases:
            with self.subTest(invalid_input=invalid_input):
                with self.assertRaises(TypeError) as context:
                    factorial(invalid_input)
                
                error_message = str(context.exception)
                self.assertIn(
                    "Input must be an integer", 
                    error_message,
                    f"TypeError message should mention integer requirement for input {invalid_input}"
                )

    def test_factorial_boolean_inputs(self):
        """Test factorial with boolean inputs (special case since bool is subclass of int)."""
        # In Python, bool is a subclass of int, so True=1 and False=0
        self.assertEqual(factorial(True), 1, "factorial(True) should return 1")
        self.assertEqual(factorial(False), 1, "factorial(False) should return 1")

    def test_factorial_return_type(self):
        """Test that factorial always returns an integer."""
        test_inputs = [0, 1, 2, 3, 4, 5, 10]
        
        for input_value in test_inputs:
            with self.subTest(input_value=input_value):
                result = factorial(input_value)
                self.assertIsInstance(
                    result, 
                    int, 
                    f"factorial({input_value}) should return an integer, got {type(result)}"
                )

    def test_factorial_mathematical_properties(self):
        """Test mathematical properties of factorial function."""
        # Test that n! = n * (n-1)! for various values
        test_values = [2, 3, 4, 5, 6, 7, 8, 9, 10]
        
        for n in test_values:
            with self.subTest(n=n):
                factorial_n = factorial(n)
                factorial_n_minus_1 = factorial(n - 1)
                expected = n * factorial_n_minus_1
                
                self.assertEqual(
                    factorial_n, 
                    expected,
                    f"factorial({n}) should equal {n} * factorial({n-1})"
                )

    def test_factorial_consistency(self):
        """Test that multiple calls with same input return same result."""
        test_values = [0, 1, 5, 10]
        
        for value in test_values:
            with self.subTest(value=value):
                result1 = factorial(value)
                result2 = factorial(value)
                result3 = factorial(value)
                
                self.assertEqual(result1, result2, f"Multiple calls to factorial({value}) should return same result")
                self.assertEqual(result2, result3, f"Multiple calls to factorial({value}) should return same result")

    def test_factorial_edge_case_large_number(self):
        """Test factorial with reasonably large number to check for overflow handling."""
        # Test with 20! which is still manageable in Python
        result = factorial(20)
        expected = 2432902008176640000
        self.assertEqual(result, expected, "factorial(20) should handle large numbers correctly")

    def test_factorial_performance_reasonable(self):
        """Test that factorial completes in reasonable time for moderate inputs."""
        import time
        
        start_time = time.time()
        result = factorial(100)  # 100! is a large but reasonable test
        end_time = time.time()
        
        execution_time = end_time - start_time
        
        # Should complete within 1 second for factorial(100)
        self.assertLess(
            execution_time, 
            1.0, 
            f"factorial(100) should complete within 1 second, took {execution_time:.4f} seconds"
        )
        
        # Verify result is correct type and positive
        self.assertIsInstance(result, int, "factorial(100) should return an integer")
        self.assertGreater(result, 0, "factorial(100) should return a positive number")


class TestFactorialCalculatorIntegration(unittest.TestCase):
    """Integration tests for factorial calculator module."""

    def test_module_import(self):
        """Test that the factorial_calculator module can be imported successfully."""
        try:
            import factorial_calculator
            self.assertTrue(hasattr(factorial_calculator, 'factorial'), "Module should have factorial function")
        except ImportError as e:
            self.fail(f"Failed to import factorial_calculator module: {e}")

    def test_function_docstring(self):
        """Test that the factorial function has proper documentation."""
        self.assertIsNotNone(factorial.__doc__, "factorial function should have a docstring")
        self.assertIn("factorial", factorial.__doc__.lower(), "Docstring should mention factorial")
        self.assertIn("integer", factorial.__doc__.lower(), "Docstring should mention integer")

    def test_function_signature(self):
        """Test that the factorial function has the expected signature."""
        import inspect
        
        signature = inspect.signature(factorial)
        parameters = list(signature.parameters.keys())
        
        self.assertEqual(len(parameters), 1, "factorial function should take exactly one parameter")
        self.assertEqual(parameters[0], 'n', "factorial function parameter should be named 'n'")


def run_performance_benchmarks():
    """Run performance benchmarks for the factorial function."""
    import time
    
    print("\nPerformance Benchmarks:")
    print("-" * 50)
    
    benchmark_values = [10, 50, 100, 500, 1000]
    
    for value in benchmark_values:
        try:
            start_time = time.time()
            result = factorial(value)
            end_time = time.time()
            
            execution_time = (end_time - start_time) * 1000  # Convert to milliseconds
            result_length = len(str(result))
            
            print(f"factorial({value:4d}): {execution_time:8.3f}ms (result has {result_length} digits)")
            
        except Exception as e:
            print(f"factorial({value:4d}): ERROR - {e}")


if __name__ == '__main__':
    # Add command line argument parsing for different test modes
    import argparse
    
    parser = argparse.ArgumentParser(description='Run tests for factorial calculator')
    parser.add_argument('--verbose', '-v', action='store_true', help='Verbose output')
    parser.add_argument('--benchmark', '-b', action='store_true', help='Run performance benchmarks')
    parser.add_argument('--coverage', '-c', action='store_true', help='Show test coverage information')
    
    # Parse known args to avoid conflicts with unittest
    args, unknown = parser.parse_known_args()
    
    # Set up unittest arguments
    unittest_args = [sys.argv[0]] + unknown
    if args.verbose:
        unittest_args.append('-v')
    
    print("Running Unit Tests for Factorial Calculator")
    print("=" * 50)
    
    # Run the unit tests
    unittest.main(argv=unittest_args, exit=False, verbosity=2 if args.verbose else 1)
    
    # Run benchmarks if requested
    if args.benchmark:
        run_performance_benchmarks()
    
    # Show coverage information if requested
    if args.coverage:
        print("\nTest Coverage Summary:")
        print("-" * 50)
        print("Basic functionality: Covered")
        print("Edge cases (0, 1): Covered") 
        print("Error handling (negative, non-integer): Covered")
        print("Mathematical properties: Covered")
        print("Performance testing: Covered")
        print("Integration testing: Covered")