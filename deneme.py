def swap_integers(a, b):
    # Swap the values without using return
    a, b = b, a
    
    # Print the swapped values (optional)
    print("After swapping: a =", a, ", b =", b)

# Example usage:
x = 5
y = 10

print("Before swapping: x =", x, ", y =", y)
swap_integers(x, y)