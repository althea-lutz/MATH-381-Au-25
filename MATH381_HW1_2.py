from ortools.linear_solver import pywraplp

# Construct the LP solver. We will use GLOP, a simplex method solver.
solver = pywraplp.Solver.CreateSolver("GLOP")

# Create the variables c1, c2, w1, w2
w1 = solver.NumVar(0, solver.infinity(), "w1")
a1 = solver.NumVar(0, solver.infinity(), "a1")
w2 = solver.NumVar(0, solver.infinity(), "w2")
a2 = solver.NumVar(0, solver.infinity(), "a2")

# Create the constraints
solver.Add(0.2*w1 - 0.8*a1 >= 0)
solver.Add(-0.6*w2 + 0.4*a2 >= 0)
solver.Add(w1 + w2 <= 1000)
solver.Add(a1 + a2 <= 800)

# Set the objective
solver.Maximize(w1 + 1.1*a1 + 0.8*w2 + 0.9*a2)

# Solve
status = solver.Solve()
val = solver.Objective().Value() # optimal value

# Print solution
if status == pywraplp.Solver.OPTIMAL:
    print(f"Optimal value = {val:0.2f}")
    print(f"w1 = {w1.solution_value():0.2f}")
    print(f"a1 = {a1.solution_value():0.2f}")
    print(f"w2 = {w2.solution_value():0.2f}")
    print(f"a2 = {a2.solution_value():0.2f}")
else:
    print("The problem does not have an optimal solution.")


