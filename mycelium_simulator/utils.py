import copy

def distribute_nutrients(amount, *targets): # *args
    """Docstring: Distributes energy across multiple organism nodes."""
    share = amount / len(targets)
    for target in targets:
        target.nutrients += share

def reproduce(organism, mode="asexual"):
    if mode == "asexual":
        return copy.copy(organism) # Shallow copy
    else:
        return copy.deepcopy(organism) # Deep copy

def calculate_spread(node_depth): # Recursion
    if node_depth <= 0:
        return 1
    return 2 * calculate_spread(node_depth - 1)

class SporeGenerator: # Iterables / Generators
    def __init__(self, count):
        self.count = count

    def __iter__(self):
        for i in range(self.count):
            yield f"Spore_{i}"