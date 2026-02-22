import argparse
from pathlib import Path
from mycelium_simulator.organisms import Fungi
from mycelium_simulator.environment import World
from mycelium_simulator.utils import SporeGenerator
from mycelium_simulator.utils import reproduce, distribute_nutrients
from mycelium_simulator.utils import calculate_spread

SIMULATION_VERSION = "2.0.1"

def run_simulation(species_name, initial_depth, latitude, longitude):
    # Latitude: -3.1, Longitude: -60.0 (Manaus, Brazil)
    world = World(lat=latitude, lon=longitude)
    mycelium = Fungi(species_name, "Standard")
    
    # Paths
    log_path = Path("data/logs.txt")
    log_path.parent.mkdir(exist_ok=True)

    print(f"Starting {species_name} growth...")

    # Calculate theoretical complexity using recursion 
    total_potential_tips = calculate_spread(initial_depth)
    print(f"Theoretical Branching Complexity: {total_potential_tips} potential tips.")

    # Create unique nodes using shallow copies
    nodes = [reproduce(mycelium, mode="asexual") for _ in range(3)]

    # Initialize the generator for a set number of potential spores
    spores = SporeGenerator(count=initial_depth) 
    
    for i, spore_id in enumerate(spores):
        humidity = world.get_humidity()
        
        if humidity > 50:
            # Feed the existing network
            distribute_nutrients(50, *nodes)
            
            # Generate a new node from a spore
            new_node = reproduce(mycelium, mode="asexual")
            new_node.name = f"{species_name}_{spore_id}"
            nodes.append(new_node)
            
            print(f"Cycle {i}: Humidity {humidity}%. Fed {len(nodes)-1} nodes and germinated {spore_id}.")
        
    # Write to file
    with open(log_path, "w") as f:
        f.write(f"Simulation of {species_name} completed.\n")
        f.write("Final Network Status:\n")
        for node in nodes:
            f.write(f"- {repr(node)}\n")
        
        total_biomass = sum(node.nutrients for node in nodes)

        if len(nodes) >= 2:
            colony_c = nodes[0] + nodes[1]
            # Write the hybrid to the file as well
            f.write(f"\nHybrid Colony Created: {repr(colony_c)}\n")
            print(f"Merged Colony Created: {colony_c.name}")

        f.write(f"\nTotal Network Biomass: {total_biomass} units")

def main():
    parser = argparse.ArgumentParser(description="Mycelium Simulator")
    parser.add_argument("--species", default="Amanita")
    parser.add_argument("--depth", type=int, default=3)
    parser.add_argument("--lat", type=float, default=-3.1, help="Latitude for weather data")
    parser.add_argument("--lon", type=float, default=-60.0, help="Longitude for weather data")
    args = parser.parse_args()
    
    run_simulation(args.species, args.depth, args.lat, args.lon)

if __name__ == "__main__":
    main()