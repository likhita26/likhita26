import cvxpy as cp

# Create two scalar optimization variables.
x = cp.Variable()
y = cp.Variable()

# Create two constraints.
constraints = [x+y==2]

# Form objective.
obj = cp.Minimize((0.5*((x+y)**2) +0.5*((x)**2) +0.5*((y)**2))*6)

# Form and solve problem.
prob = cp.Problem(obj, constraints)
prob.solve()  # Returns the optimal value.
print("status:", prob.status)
print("optimal value", prob.value)
