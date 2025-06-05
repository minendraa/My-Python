# ### Brief Intro to Operator Overloading
# Magic methods also allow you to define how standard operators (`+`, `-`, `*`, `/`, `==`, `<`, `>`, etc.) work with your custom objects.
# This is called **operator overloading**.

# Example: Using `__add__(self, other)` to overload the `+` operator.
# Other common operator magic methods include:
# `__sub__(self, other)` for `-`
# `__mul__(self, other)` for `*`
# `__lt__(self, other)` for `<`
# `__gt__(self, other)` for `>`

class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

    # Overload the + operator for Vector2D objects
    def __add__(self, other):
        # Check if the 'other' object is also a Vector2D (good practice)
        if isinstance(other, Vector2D):
            # Return a *new* Vector2D object representing the sum
            new_x = self.x + other.x
            new_y = self.y + other.y
            return Vector2D(new_x, new_y)
        else:
            # Indicate that addition with this type is not supported
            return NotImplemented # Special value
    
    def __sub__(self,other):
        if isinstance(other,Vector2D):
            new_x = self.x - other.x
            new_y = self.y - other.y
            return Vector2D(new_x,new_y)
        
        else:
            return NotImplemented
        
    def __mul__(self,other):
        if isinstance(other,Vector2D):
            new_x = self.x * other.x
            new_y = self.y * other.y
            return Vector2D(new_x,new_y)
        
        else:
            return NotImplemented
        
    def __lt__(self, other):
        if isinstance(other, Vector2D):
            return (self.x, self.y) < (other.x, other.y)
        else:
            return NotImplemented
        
    def __gt__(self, other):
        if isinstance(other, Vector2D):
            return (self.x, self.y) > (other.x, other.y)
        else:
            return NotImplemented
    

    # Example: Overload == operator
    def __eq__(self, other):
        if isinstance(other, Vector2D):
            return self.x == other.x and self.y == other.y
        return False

# Create some vectors
v1 = Vector2D(1, 2)
v2 = Vector2D(3, 4)
v3 = Vector2D(4, 6)
v4 = Vector2D(1, 2)

print(v1)

print(f"v1 = {v1}")
print(f"v2 = {v2}")

# Use the overloaded + operator
v_sum = v1 + v2
print(f"v1 + v2 = {v_sum}")
print(f"Is v_sum a Vector2D? {isinstance(v_sum, Vector2D)}")

v_sub = v1 - v2
print(f"v1 - v2 = {v_sub}")
print(f"Is v_sub a Vector2D? {isinstance(v_sub, Vector2D)}")

v_mul = v1 * v2
print(f"v1 * v2 = {v_mul}")
print(f"Is v_mul a Vector2D? {isinstance(v_mul, Vector2D)}")

print("-----Less than/ Greater than-----")
print(v1<v2)
print(v1>v2)

# Use the overloaded == operator
print(f"Does v1 == v2? {v1 == v2}")
print(f"Does v1 == v4? {v1 == v4}") # Should be True because of __eq__
print(f"Does v_sum == v3? {v_sum == v3}") # Should be True