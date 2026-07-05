
def add(a: float, b: float) -> float:
    """Add two numbers a and b together

    Args:
        a (float): First number
        b (float): Second number

    Returns:
        float: The sum of the two numbers
    """

    return a + b

def multiply(a: float, b: float) -> float:
    """Multiply two numbers a and b together

    Args:
        a (float): First number
        b (float): Second number

    Returns:
        float: The product of the two numbers
    """

    return a * b

def subtract(a: float, b: float) -> float:
    """Subtract two numbers a and b

    Args:
        a (float): First number
        b (float): Second number

    Returns:
        float: The difference of the two numbers
    """

    return a - b

def divide(a: float, b: float) -> float:
    """Divide two numbers a and b

    Args:
        a (float): First number
        b (float): Second number

    Returns:
        float: The quotient of the two numbers
    """

    if b == 0:
        raise ValueError("Cannot divide by zero")
    
    return a / b 