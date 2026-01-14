from ortools.linear_solver import pywraplp

# Create a SAT integer program solver
solver = pywraplp.Solver.CreateSolver("SAT")

m = 8

# x[i] = 1 if guard is assigned to room i, 0 otherwise
x = [solver.IntVar(0, 1, "x" + str(i)) for i in range(m)]


# Objective function
solver.Maximize(0)

# Constraints
solver.Add(4*x[0] + 5*x[1] + 3*x[2] + 2*x[3] + 4*x[4] + 3*x[5] + 5*x[6] + 4*x[7] >= 14)
solver.Add(4*x[0] + 5*x[1] + 3*x[2] + 2*x[3] + 4*x[4] + 3*x[5] + 5*x[6] + 4*x[7] <= 16)
solver.Add(x[0] + x[2] + x[4] + x[7] == 2)
solver.Add(x[1] + x[3] + x[5] + x[7] >= 3)
solver.Add(x[4] + x[5] >= 1)
solver.Add(x[1] + x[3] + x[4] <= 2)

# Solve
status = solver.Solve()

if status == pywraplp.Solver.OPTIMAL:
    songs = [i + 1 for i in range(m) if x[i].solution_value() == 1]
else:
    songs = []

print(songs)

