from ortools.linear_solver import pywraplp

# Create a SAT integer program solver
solver = pywraplp.Solver.CreateSolver("SAT")

m = 8

# x[i] = 1 if guard is assigned to room i, 0 otherwise
x = [solver.IntVar(0, 1, "x" + str(i)) for i in range(m)]

# Objective function
solver.Minimize(solver.Sum(x[i] for i in range(m)))

# Constraints
solver.Add(x[0] + x[1] + x[5] >= 1)
solver.Add(x[0] + x[1] + x[2] + x[3] >= 1)
solver.Add(x[1] + x[2] + x[3] + x[5] + x[6] >= 1)
solver.Add(x[1] + x[2] + x[3] + x[4] >= 1)
solver.Add(x[3] + x[4] + x[6] + x[7] >= 1)
solver.Add(x[0] + x[2] + x[5] +x[6] >= 1)
solver.Add(x[2] + x[4] + x[5] + x[6] + x[7] >= 1)
solver.Add(x[4] + x[6] + x[7] >= 1)

# Solve
status = solver.Solve()

if status == pywraplp.Solver.OPTIMAL:
    rooms = [i + 1 for i in range(m) if x[i].solution_value() == 1]
else:
    rooms = []

print(rooms)

