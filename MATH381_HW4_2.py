from ortools.linear_solver import pywraplp

# Create a GLOP integer program solver
solver = pywraplp.Solver.CreateSolver("GLOP")

# Variables

x_1 = solver.NumVar(0.000001, 1, "x_1")
x_2 = solver.NumVar(0.000001, 1, "x_2")
x_3 = solver.NumVar(0.000001, 1, "x_3")
z_prime = solver.NumVar(-solver.infinity(), solver.infinity(), "z_prime")

# Objective function
solver.Maximize(z_prime)

# Constraints
solver.Add(x_1 + x_2 + x_3 == 1)
solver.Add(z_prime <= 0.25*x_1 - 0.5*x_2 - 0.5*x_3)
solver.Add(z_prime <= -0.5*x_1 + 0.25*x_2 - 0.5*x_3)

# Solve
status = solver.Solve()
val = solver.Objective().Value() # optimal value

# Print solution
if status == pywraplp.Solver.OPTIMAL:
    print(f"Optimal value = {val:0.2f}")
    print(f"x_1 = {x_1.solution_value():0.2f}")
    print(f"x_2 = {x_2.solution_value():0.2f}")
    print(f"x_3 = {x_3.solution_value():0.2f}")
else:
    print("The problem does not have an optimal solution.")

