from ortools.linear_solver import pywraplp

# Create a SCIP integer program solver
solver = pywraplp.Solver.CreateSolver("SAT")

m = 14

# x[i] = 1 if course i is added to schedule, 0 otherwise
x = [solver.IntVar(0, 1, "x" + str(i)) for i in range(m)]

# Objective function
solver.Maximize(solver.Sum(x[i] for i in range(m)))

# Constraints
solver.Add(x[0] + x[3]<= 1)
solver.Add(x[1]+x[4]+x[6]<=1)
solver.Add(x[7] + x[13] <= 1)
solver.Add(x[2] + x[9] + x[10] <= 1)
solver.Add(x[5] + x[8] + x[12] <= 1)
solver.Add(x[1] - x[0] <= 0)
solver.Add(x[3] - x[2] <= 0)
solver.Add(x[7] - x[6] <= 0)
solver.Add(x[0] + x[1] + x[4] >= 1)
solver.Add(x[6] + x[7] + x[8] + x[12] >= 1)
solver.Add(x[7] + x[11] + x[13] <= 1)

# Solve
status = solver.Solve()

if status == pywraplp.Solver.OPTIMAL:
    courses = [i + 1 for i in range(m) if x[i].solution_value() == 1]
else:
    courses = []

print(courses)