import uuid
import random
from dataclasses import dataclass

@dataclass(frozen=True) # Immutable attributes
class GeneticCode:
    sequence: str

class Organism:
    def __init__(self, name):
        self.name = name
        self._id = uuid.uuid4()

    def __hash__(self): # Hashable objects
        return hash(self._id)

class Fungi(Organism):
    def __init__(self, name, strain, **kwargs):
        super().__init__(name)
        self.strain = strain
        self.nutrients = kwargs.get("initial_nutrients", 100) # Mutable
        random_sequence = "".join(random.choices("ATCG", k=10))
        self.dna = GeneticCode(random_sequence)
        self.network = [] # Composition: List of connected nodes

    def __add__(self, other): # Magic Method: Merging colonies
        if isinstance(other, Fungi):
            # Calculate combined nutrients
            combined_nutrients = self.nutrients + other.nutrients
            
            # Create new hybrid with combined nutrient pool
            return Fungi(
                f"{self.name}-{other.name}", 
                self.strain, 
                initial_nutrients=combined_nutrients
            )
        raise TypeError("Can only merge a Fungi with another Fungi object.")
        
    def __repr__(self):
        return f"Fungi(species={self.name}, health={self.nutrients})"

class Tree(Organism):
    def __init__(self, species):
        super().__init__(species)
        self.symbionts = [] # Composition