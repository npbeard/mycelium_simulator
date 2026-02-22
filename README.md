Mycelium Simulator

Version: 2.0.1 

A Python-based simulation engine designed to model the growth and nutrient distribution of fungal networks (mycelium) based on environmental variables. The simulator integrates real-world weather data to influence biological reproduction and colony merging.

## Key Features
Real-time Environment Integration: Uses the Open-Meteo API to fetch current humidity levels at specific coordinates (defaulting to Manaus, Brazil) to trigger growth cycles.


Biological Logic: Implements fungal behaviors such as asexual reproduction (shallow/deep copies), spore generation, and nutrient sharing across nodes.

Colony Merging: Supports "magic method" operations to merge two separate fungi objects into a single hybrid colony with a combined nutrient pool.


Complexity Modeling: Uses recursive algorithms to calculate theoretical branching complexity and potential network spread.

## Installation
This project uses hatchling as a build backend. Ensure you have the dependencies installed:

pip install requests
## Usage
Run the simulation from the root directory using the main.py entry point. You can specify the fungus species and the depth of the simulation.

uv run python -m mycelium_simulator.main --species "Fly Agaric" --depth 5 --lat -3.1 --lon -60.0
### Arguments

--species: The name of the fungi species (Default: Amanita).


--depth: The initial branching depth/spore count for the simulation (Default: 3).

## Project Structure

main.py: The primary execution script and simulation loop.

organisms.py: Defines the Fungi and Tree classes using Object-Oriented principles like inheritance and dataclasses.

environment.py: Handles API requests for weather data and includes a @weather_check decorator for logging.

utils.py: Contains helper functions for recursion, nutrient distribution, and spore iteration.

## Simulation Output
Upon completion, the simulator generates a data/logs.txt file containing:

The final health/nutrient status of every node in the network.

Details of any hybrid colonies created during the run.

The total biomass of the entire mycelial network.