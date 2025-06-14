def swap_with_temp(a, b):
    temp = a
    a = b
    b = temp
    return a, b

# Example
x = 5
y = 10
x, y = swap_with_temp(x, y)
print("x:", x)  # Output: x: 10
print("y:", y)  # Output: y: 5
