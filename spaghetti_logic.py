"""Data processing module with clean code principles."""

from typing import List

# Configuration constants
TAX_RATE = 1.15
LOG_FILE = "log.txt"


def calculate_tax_adjusted_value(value: float, tax_rate: float = TAX_RATE) -> float:
    """Calculate tax-adjusted value for a given amount.
    
    Args:
        value: Original value to adjust.
        tax_rate: Tax multiplication rate (default: 1.15).
        
    Returns:
        Tax-adjusted value as float.
    """
    return value * tax_rate


def format_result_message(value: float) -> str:
    """Format value as readable message.
    
    Args:
        value: Value to format.
        
    Returns:
        Formatted string message.
    """
    return f"Total: {value:.2f}"


def log_results(results: List[float], filename: str = LOG_FILE) -> None:
    """Write processing results to log file.
    
    Args:
        results: List of processed values.
        filename: Target log file path.
        
    Raises:
        IOError: If file write operation fails.
    """
    try:
        with open(filename, "a") as log_file:
            log_file.write(str(results) + "\n")
    except IOError as error:
        print(f"Error writing to log file: {error}")
        raise


def process_data(data: List[float]) -> List[float]:
    """Process data by applying tax adjustment and logging results.
    
    This function orchestrates the data processing workflow:
    1. Applies tax adjustment to each value
    2. Displays formatted results
    3. Logs results to file
    
    Args:
        data: List of numeric values to process.
        
    Returns:
        List of tax-adjusted values.
        
    Raises:
        ValueError: If input data is empty.
    """
    if not data:
        raise ValueError("Input data cannot be empty")
    
    processed_results = []
    
    for original_value in data:
        adjusted_value = calculate_tax_adjusted_value(original_value)
        message = format_result_message(adjusted_value)
        print(message)
        processed_results.append(adjusted_value)
    
    log_results(processed_results)
    return processed_results
