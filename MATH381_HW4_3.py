from ortools.linear_solver import pywraplp

# Create a GLOP integer program solver
solver = pywraplp.Solver.CreateSolver("GLOP")

# Variables

y_S = solver.NumVar(0, 1, "y_S")
y_P = solver.NumVar(0, 1, "y_P")
z = solver.NumVar(-solver.infinity(), solver.infinity(), "z")

# Objective function
solver.Minimize(z)

# Constraints
solver.Add(y_S + y_P == 1)
solver.Add(z >= -y_P + y_S)
solver.Add(z >= -y_S)

# Solve
status = solver.Solve()
val = solver.Objective().Value() # optimal value

# Print solution
if status == pywraplp.Solver.OPTIMAL:
    print(f"Optimal value = {val:0.2f}")
    print(f"y_S = {y_S.solution_value():0.2f}")
    print(f"y_P = {y_P.solution_value():0.2f}")
else:
    print("The problem does not have an optimal solution.")


