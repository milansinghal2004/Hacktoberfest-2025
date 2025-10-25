# factorial_calculator.py

# Global cache for memoization - stores previously computed factorial values
# This ensures no factorial value is calculated more than once
_factorial_cache = {0: 1, 1: 1}


def _validate_factorial_input(number):
    """
    Validates input for factorial calculation.
    
    Args:
        number: The input value to validate
        
    Raises:
        TypeError: If input is not an integer
        ValueError: If input is negative
    """
    if not isinstance(number, int):
        raise TypeError("Input must be an integer.")
    if number < 0:
        raise ValueError("Factorial is not defined for negative numbers.")


def _find_largest_cached_value(target_number):
    """
    Finds the largest cached factorial value that is <= target_number.
    This helps optimize computation by starting from the highest cached value.
    
    Args:
        target_number (int): The number we want to calculate factorial for
        
    Returns:
        int: The largest cached number <= target_number
    """
    cached_numbers = [num for num in _factorial_cache.keys() if num <= target_number]
    return max(cached_numbers) if cached_numbers else 0


def _compute_and_cache_factorials(start_value, end_value):
    """
    Computes and caches factorial values from start_value+1 to end_value.
    Uses the cached factorial of start_value as the starting point.
    
    Args:
        start_value (int): The value to start computation from (must be cached)
        end_value (int): The final value to compute factorial for
        
    Returns:
        int: The factorial of end_value
    """
    current_factorial_value = _factorial_cache[start_value]
    
    # Compute factorial incrementally and cache each intermediate result
    for current_number in range(start_value + 1, end_value + 1):
        current_factorial_value *= current_number
        _factorial_cache[current_number] = current_factorial_value
    
    return current_factorial_value


def factorial(n):
    """
    Calculates the factorial of a non-negative integer using dynamic programming.
    
    This function uses memoization to cache previously computed factorial values,
    ensuring that the factorial of any value is never calculated more than once.
    This dramatically improves performance for repeated calculations.
    
    Args:
        n (int): The non-negative integer to calculate factorial for
        
    Returns:
        int: The factorial of n (n!)
        
    Raises:
        TypeError: If n is not an integer
        ValueError: If n is negative
        
    Time Complexity: O(k) where k is the number of uncached values
    Space Complexity: O(n) for the memoization cache
    """
    # Validate input first
    _validate_factorial_input(n)
    
    # Return cached result if available - no computation needed
    if n in _factorial_cache:
        return _factorial_cache[n]
    
    # Find the largest cached value to start computation from
    largest_cached_number = _find_largest_cached_value(n)
    
    # Compute and cache factorial values from largest_cached_number+1 to n
    return _compute_and_cache_factorials(largest_cached_number, n)


def get_factorial_cache_info():
    """
    Returns information about the current state of the factorial cache.
    Useful for debugging and understanding memoization benefits.
    
    Returns:
        dict: Dictionary containing cache statistics
    """
    return {
        'total_cached_values': len(_factorial_cache),
        'cached_numbers': sorted(_factorial_cache.keys()),
        'largest_cached_number': max(_factorial_cache.keys()) if _factorial_cache else None,
        'cache_size_bytes': len(str(_factorial_cache))  # Approximate size
    }


def clear_factorial_cache():
    """
    Clears the factorial cache except for base cases (0! = 1, 1! = 1).
    Useful for testing or memory management.
    """
    global _factorial_cache
    _factorial_cache = {0: 1, 1: 1}

if __name__ == "__main__":
    print("=== Factorial Calculator with Dynamic Programming (Functions Only) ===\n")
    
    # Test basic functionality to ensure backward compatibility
    print("1. Basic functionality tests:")
    try:
        test_cases = [5, 0, 1, 10]
        expected_results = [120, 1, 1, 3628800]
        
        for number, expected in zip(test_cases, expected_results):
            calculated_result = factorial(number)
            status_symbol = "✓" if calculated_result == expected else "✗"
            print(f"   {status_symbol} factorial({number}) = {calculated_result} (expected: {expected})")
        
        print("\n2. Error handling verification:")
        # Test negative number error
        try:
            factorial(-3)
        except ValueError as error_msg:
            print(f"   ✓ Negative input properly handled: {error_msg}")
        
        # Test non-integer error  
        try:
            factorial(3.5)
        except TypeError as error_msg:
            print(f"   ✓ Non-integer input properly handled: {error_msg}")
    
    except Exception as unexpected_error:
        print(f"   ✗ Unexpected error occurred: {unexpected_error}")
    
    # Demonstrate the power of memoization
    print("\n3. Dynamic programming memoization demonstration:")
    
    # Show initial cache state
    initial_cache_info = get_factorial_cache_info()
    print(f"   Initial cache: {initial_cache_info['cached_numbers']}")
    
    # Calculate a larger factorial
    print("   Computing factorial(15)...")
    result_15 = factorial(15)
    cache_after_15 = get_factorial_cache_info()
    print(f"   Result: {result_15}")
    print(f"   Cache now contains: {len(cache_after_15['cached_numbers'])} values")
    print(f"   Cached numbers: {cache_after_15['cached_numbers']}")
    
    # Show efficiency for smaller factorial (uses cached values)
    print("\n   Computing factorial(12) (should reuse cached intermediate results)...")
    result_12 = factorial(12)
    print(f"   Result: {result_12}")
    print("   → No additional computation needed! Used cached values 0-12.")
    
    # Extend cache with larger calculation
    print("\n   Computing factorial(20) (extends from cached factorial(15))...")
    result_20 = factorial(20)
    final_cache_info = get_factorial_cache_info()
    print(f"   Result: {result_20}")
    print(f"   Final cache size: {final_cache_info['total_cached_values']} values")
    print("   → Only computed new values 16-20, reused 0-15 from cache!")
    
    # Performance comparison explanation
    print("\n4. Efficiency comparison:")
    print("   Traditional approach: Recalculates factorial from 1 each time")
    print("   Memoized approach: Calculates each factorial value only once")
    print("   → Massive performance improvement for repeated/related calculations!")
    
    # Show cache management functions
    print("\n5. Cache management demonstration:")
    print(f"   Current cache info: {get_factorial_cache_info()}")
    
    print("\n=== Refactoring Summary ===")
    print("✓ Implemented dynamic programming with function-based memoization")
    print("✓ Improved variable names and added detailed comments")
    print("✓ Broke complex logic into smaller, focused helper functions")
    print("✓ Maintained 100% backward compatibility")
    print("✓ Added cache introspection and management utilities")
    print("✓ No classes used - pure function-based approach")
