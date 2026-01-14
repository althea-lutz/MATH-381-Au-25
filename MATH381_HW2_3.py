from ortools.linear_solver import pywraplp

# Create a SAT integer program solver
solver = pywraplp.Solver.CreateSolver("SAT")

m = 11
n = 7

# x[i] = 1 if guard is assigned to room i, 0 otherwise
x = [solver.IntVar(0, 1, "x" + str(i)) for i in range(m)]
y = [solver.IntVar(0, 1, "y" + str(j)) for j in range(n)]

# Objective function
solver.Maximize(43*y[0] +29*y[1] + 42*y[2] + 21*y[3] + 56*y[4] + 18*y[5] + 71*y[6])

# Constraints
solver.Add(x[0] + x[1] + x[2] + x[3] + x[4] + x[5] + x[6] + x[7] + x[8] + x[9] + x[10] == 2)
solver.Add(y[0] + y[1] - 2*x[0] <= 1)
solver.Add(y[0] + y[2] - 2*x[1] <= 1)
solver.Add(y[1] + y[2] - 2*x[2] <= 1)
solver.Add(y[1] + y[3] - 2*x[3] <= 1)
solver.Add(y[1] + y[4] - 2*x[4] <= 1)
solver.Add(y[2] + y[3] - 2*x[5] <= 1)
solver.Add(y[3] + y[4] - 2*x[6] <= 1)
solver.Add(y[3] + y[5] - 2*x[7] <= 1)
solver.Add(y[3] + y[6] - 2*x[8] <= 1)
solver.Add(y[4] + y[5] - 2*x[9] <= 1)
solver.Add(y[5] + y[6] - 2*x[10] <= 1)

# Solve
status = solver.Solve()

if status == pywraplp.Solver.OPTIMAL:
    assignments = [i + 1 for i in range(m) if x[i].solution_value() == 1]
else:
    assignments = []

print(assignments)

