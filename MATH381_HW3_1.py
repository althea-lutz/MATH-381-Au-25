from ortools.linear_solver import pywraplp

# Create a GLOP integer program solver
solver = pywraplp.Solver.CreateSolver("GLOP")

# Variables
x_NY_Chicago = solver.NumVar(0, solver.infinity(), "x_NY_Chicago")
x_NY_Memphis = solver.NumVar(0, solver.infinity(), "x_NY_Memphis")
x_Chicago_Denver = solver.NumVar(0, solver.infinity(), "x_Chicago_Denver")
x_Chicago_Dallas = solver.NumVar(0, solver.infinity(), "x_Chicago_Dallas")
x_Memphis_Denver = solver.NumVar(0, solver.infinity(), "x_Memphis_Denver")
x_Memphis_Dallas = solver.NumVar(0, solver.infinity(), "x_Memphis_Dallas")
x_Denver_LA = solver.NumVar(0, solver.infinity(), "x_Denver_LA")
x_Dallas_LA = solver.NumVar(0, solver.infinity(), "x_Dallas_LA")

# Objective function
solver.Maximize(x_NY_Chicago + x_NY_Memphis)

# Constraints
solver.Add(0 <= x_NY_Chicago <= 500)
solver.Add(0 <= x_NY_Memphis <= 400)
solver.Add(0 <= x_Chicago_Denver <= 300)
solver.Add(0 <= x_Chicago_Dallas <= 250)
solver.Add(0 <= x_Memphis_Denver <= 200)
solver.Add(0 <= x_Memphis_Dallas <= 150)
solver.Add(0 <= x_Denver_LA <= 400)
solver.Add(0 <= x_Dallas_LA <= 350)
solver.Add(x_NY_Chicago == x_Chicago_Denver + x_Chicago_Dallas)
solver.Add(x_NY_Memphis == x_Memphis_Dallas + x_Memphis_Denver)
solver.Add(x_Chicago_Denver + x_Memphis_Denver == x_Denver_LA)
solver.Add(x_Chicago_Dallas + x_Memphis_Dallas == x_Dallas_LA)

# Solve
status = solver.Solve()

status = solver.Solve()
val = solver.Objective().Value() # optimal value

# Print solution
if status == pywraplp.Solver.OPTIMAL:
    print(f"Optimal value = {val:0.2f}")
    print(f"x_NY_Chicago = {x_NY_Chicago.solution_value():0.2f}")
    print(f"x_NY_Memphis = {x_NY_Memphis.solution_value():0.2f}")
    print(f"x_Chicago_Denver = {x_Chicago_Denver.solution_value():0.2f}")
    print(f"x_Chicago_Dallas = {x_Chicago_Dallas.solution_value():0.2f}")
    print(f"x_Memphis_Denver = {x_Memphis_Denver.solution_value():0.2f}")
    print(f"x_Memphis_Dallas = {x_Memphis_Dallas.solution_value():0.2f}")
    print(f"x_Denver_LA = {x_Denver_LA.solution_value():0.2f}")
    print(f"x_Dallas_LA = {x_Dallas_LA.solution_value():0.2f}")
else:
    print("The problem does not have an optimal solution.")


