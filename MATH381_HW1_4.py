from ortools.linear_solver import pywraplp

# Construct the LP solver. We will use GLOP, a simplex method solver.
solver = pywraplp.Solver.CreateSolver("GLOP")

# Create the variables c1, c2, w1, w2
f0 = solver.NumVar(0, solver.infinity(), "f0")
l3 = solver.NumVar(0, solver.infinity(), "l3")
l4 = solver.NumVar(0, solver.infinity(), "l4")
p0 = solver.NumVar(0, solver.infinity(), "p0")
p1 = solver.NumVar(0, solver.infinity(), "p1")
p2 = solver.NumVar(0, solver.infinity(), "p2")
p3 = solver.NumVar(0, solver.infinity(), "p3")
p4 = solver.NumVar(0, solver.infinity(), "p4")
p5 = solver.NumVar(0, solver.infinity(), "p5")

# Create the constraints
solver.Add(f0 + p0 >= 4)
solver.Add(f0 +p0 + p1 >= 3)
solver.Add(f0 + p0 + p1 + p2 >= 4)
solver.Add(f0 + p1 + p2 + p3 - l3 >= 6)
solver.Add(f0 + p2 + p3 + p4 - l4 >= 5)
solver.Add(f0 + p3 + p4 + p5 >= 6)
solver.Add(f0 + p4 + p5 >= 8)
solver.Add(f0 + p5 >= 8)
solver.Add(p0 + p1 + p2 + p3 + p4 + p5 <= 5)
solver.Add(f0 == l3 + l4)

# Set the objective
solver.Minimize(72*f0 + 15*p0 + 15*p1 + 15*p2 + 15*p3 + 15*p4 + 15*p5)

# Solve
status = solver.Solve()
val = solver.Objective().Value() # optimal value

# Print solution
if status == pywraplp.Solver.OPTIMAL:
    print(f"Optimal value = {val:0.2f}")
    print(f"f0 = {f0.solution_value():0.2f}")
    print(f"l3 = {l3.solution_value():0.2f}")
    print(f"l4 = {l4.solution_value():0.2f}")
    print(f"p0 = {p0.solution_value():0.2f}")
    print(f"p1 = {p1.solution_value():0.2f}")
    print(f"p2 = {p2.solution_value():0.2f}")
    print(f"p3 = {p3.solution_value():0.2f}")
    print(f"p4 = {p4.solution_value():0.2f}")
    print(f"p5 = {p5.solution_value():0.2f}")
else:
    print("The problem does not have an optimal solution.")

