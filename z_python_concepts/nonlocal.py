'''

The nonlocal keyword in Python is used within a nested (inner) function to indicate that a variable is not local to the inner function but exists in the nearest enclosing scope (excluding the global scope). This allows the inner function to modify a variable that is defined in an outer (enclosing) function.

Why We Need nonlocal
When you have a nested function and you want to modify a variable that is defined in an enclosing
 (but non-global) scope, you use nonlocal to tell Python that the variable is not local to the
 nested function. Without nonlocal, Python treats the variable as local to the inner function,
 which means any assignment to that variable would create a new local variable in the inner function's scope, leaving the variable in the enclosing function unchanged.

Here's an example where nonlocal is necessary:

Without the nonlocal keyword, the code would raise an UnboundLocalError because count is referenced before assignment inside inner_function.

'''


def outer_function():
    count = 0  # A variable defined in the enclosing function

    def inner_function():
        nonlocal count  # Declare that we want to modify the 'count' from the outer scope
        count += 1

    inner_function()
    print(count)


outer_function()  # Output: 1



'''

When nonlocal is Not Needed:
1. Read-Only Access: If the inner function only needs to read the variable from the outer function, not modify it, nonlocal is not necessary.


'''


def outer_function():
    count = 0  # Variable defined in the enclosing function

    def inner_function():
        print(count)  # Only reading, no need for 'nonlocal'

    inner_function()


outer_function()  # Output: 0

'''
2. Global Scope: If the variable is defined in the global scope (i.e., outside of any function), and you want to modify it within a function,
you would use the global keyword instead of nonlocal.


'''

count = 0  # Global variable

def modify_count():
    global count  # Declare that we want to modify the global 'count'
    count += 1

modify_count()
print(count)  # Output: 1


'''
3.Local Scope Only: If the variable is both defined and used solely within the inner function, 
there is no need for nonlocal since it is purely a local variable to that function.

'''


def outer_function():
    def inner_function():
        count = 0  # Local variable to inner_function
        count += 1
        print(count)

    inner_function()


outer_function()  # Output: 1

'''
In summary, you need nonlocal when you want to modify a variable that is defined in an 
enclosing (non-global) scope, and not using it would result in creating a new local variable
 in the nested function. It is not needed when you only read the variable, modify a global variable,
  or when the variable is purely local to the nested function.

Below example of LC 547

In the provided code, the nonlocal keyword is not needed for the visited array because visited is a mutable list, 
and Python's scoping rules for mutable objects differ from those for immutable objects.

Why nonlocal Is Not Needed for visited:

Mutability of Lists: 
The visited variable is a list, which is a mutable object in Python. When you modify a mutable object (like a list) in an inner function, 
you are not changing the reference to the object; you are modifying the contents of the object itself. 
The outer function and the inner function share the same reference to the visited list, so any changes made to the list (like setting visited[current_city] = True)
 are reflected across both scopes.

Python's Scoping Rules for Mutables: 
In Python, the inner function can modify the contents of a mutable object defined in an outer scope without needing to declare it as nonlocal.
 This is because nonlocal is only required when you need to reassign a variable (i.e., change the reference that the variable points to), 
 not when you are modifying the contents of a mutable object that the variable points to.
'''


def findCircleNum_AlgoMons(self, isConnected: List[List[int]]) -> int:
    # Depth-First Search function which marks the nodes as visited
    def dfs(current_city: int):
        visited[current_city] = True  # Mark the current city as visited
        for adjacent_city, connected in enumerate(isConnected[current_city]):
            # If the adjacent city is not visited and there is a connection,
            # then continue the search from that city
            if not visited[adjacent_city] and connected:
                dfs(adjacent_city)

    # Number of cities in the given matrix
    num_cities = len(isConnected)
    # Initialize a visited list to keep track of cities that have been visited
    visited = [False] * num_cities
    # Counter for the number of provinces (disconnected components)
    province_count = 0
    # Loop over each city and perform DFS if it hasn't been visited
    for city in range(num_cities):
        if not visited[city]:  # If the city hasn't been visited yet
            dfs(city)  # Start DFS from this city
            # After finishing DFS, we have found a new province
            province_count += 1
    # Return the total number of disconnected components (provinces) in the graph
    return province_count

