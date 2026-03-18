import pulp

def optimise_staff(demand: int, max_staff: int, cost_per_staff: float = 1.0):
    model = pulp.LpProblem("Staff_Optimisation", pulp.LpMinimize)
    staff = pulp.LpVariable("staff", lowBound=0, upBound=max_staff, cat="Integer")

    model += cost_per_staff * staff
    model += staff >= demand

    model.solve(pulp.PULP_CBC_CMD(msg=False))
    return int(staff.value())
