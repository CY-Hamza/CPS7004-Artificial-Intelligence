class MapColoringCSP:
    def __init__(self, variables, domains, constraints):
        """
        Initialize the CSP problem with:
        - variables: list of regions to color
        - domains: dictionary of possible colors for each region
        - constraints: list of tuples representing adjacent regions that can't share colors
        """
        self.variables = variables
        self.domains = domains
        self.constraints = constraints
        self.assignment = {}

    def is_consistent(self, variable, value):
        """Check if assigning a value to a variable violates any constraints"""
        for (var1, var2) in self.constraints:
            # If the constraint involves our variable and the other variable is assigned
            if var1 == variable and var2 in self.assignment:
                if self.assignment[var2] == value:
                    return False
            elif var2 == variable and var1 in self.assignment:
                if self.assignment[var1] == value:
                    return False
        return True

    def backtracking_search(self):
        
        return self.backtrack(self.assignment)

    def backtrack(self, assignment):
        """Recursive backtracking algorithm"""
        if len(assignment) == len(self.variables):
            return assignment  # Solution found

        # Select unassigned variable (simple selection - first unassigned)
        var = next(v for v in self.variables if v not in assignment)
        
        for value in self.domains[var]:
            if self.is_consistent(var, value):
                assignment[var] = value
                result = self.backtrack(assignment)
                if result is not None:
                    return result
                del assignment[var]  # Backtrack
        return None  # No solution found

def solve_map_coloring():
    """Solve the specific map coloring problem with regions A, B, C and colors Red, Blue"""
    # Problem definition
    variables = ['A', 'B', 'C']
    domains = {
        'A': ['Red', 'Blue'],
        'B': ['Red', 'Blue'],
        'C': ['Red', 'Blue']
    }
    constraints = [('A', 'B'), ('B', 'C'), ('A', 'C')]  # All regions are adjacent
    
    # Solve the problem
    csp = MapColoringCSP(variables, domains, constraints)
    solution = csp.backtracking_search()
    
    # Output the solution
    if solution:
        print("Valid coloring found:")
        for region, color in sorted(solution.items()):
            print(f"{region}: {color}")
    else:
        print("No valid coloring exists for this configuration.")

if __name__ == "__main__":
    solve_map_coloring()