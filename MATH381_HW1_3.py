from ortools.linear_solver import pywraplp

# Construct the LP solver. We will use GLOP, a simplex method solver.
solver = pywraplp.Solver.CreateSolver("GLOP")

# Create the variables
f1 = solver.NumVar(0, solver.infinity(), "f1")
df1 = solver.NumVar(0, solver.infinity(), "df1")
f2 = solver.NumVar(0, solver.infinity(), "f2")
df2 = solver.NumVar(0, solver.infinity(), "df2")
w1 = solver.NumVar(0, solver.infinity(), "w1")
a1 = solver.NumVar(0, solver.infinity(), "a1")
w2 = solver.NumVar(0, solver.infinity(), "w2")
a2 = solver.NumVar(0, solver.infinity(), "a2")

# Create the constraints
solver.Add(f1 + df1 == w1 + a1)
solver.Add(f2 + df2 == w2 + a2)
solver.Add(df1 - f1 >= 300)
solver.Add(df2 - f2 >= 300)
solver.Add(0.2*w1 - 0.8*a1 >= 0)
solver.Add(-0.6*w2 + 0.4*a2 >= 0)
solver.Add(w1 + w2 <= 1000)
solver.Add(a1 + a2 <= 800)

# Set the objective
solver.Maximize(1.5*f1 + 1.25*df1 + 1.3*f2 + df2 - 0.5*w1 - 0.5*w2 - 0.4*a1 - 0.4*a1)

# Solve
status = solver.Solve()
val = solver.Objective().Value() # optimal value

# Print solution
if status == pywraplp.Solver.OPTIMAL:
    print(f"Optimal value = {val:0.2f}")
    print(f"f1 = {f1.solution_value():0.2f}")
    print(f"df1 = {df1.solution_value():0.2f}")
    print(f"f2 = {f2.solution_value():0.2f}")
    print(f"df2 = {df2.solution_value():0.2f}")
    print(f"w1 = {w1.solution_value():0.2f}")
    print(f"a1 = {a1.solution_value():0.2f}")
    print(f"w2 = {w2.solution_value():0.2f}")
    print(f"a2 = {a2.solution_value():0.2f}")
else:
    print("The problem does not have an optimal solution.")


