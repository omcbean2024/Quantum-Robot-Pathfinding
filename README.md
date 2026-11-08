# Quantum-Assisted Pathfinding for Warehouse Robots

**Florida Tech Qiskit Fallfest Hackathon 2026**

**Team:** Quantum Robot Pathfinding  
**Team Members:** Owen McBean and Ian Liu

## Project Overview

This project explores the use of quantum computing for autonomous warehouse robot pathfinding.

We compare a classical A* pathfinding algorithm with a quantum-assisted optimization approach using the Quantum Approximate Optimization Algorithm (QAOA).

Our program uses A* to generate possible routes through a simulated warehouse. QAOA then evaluates these candidate routes using calculated energy costs and selects a route to minimize the cost.

We test our implementation using a local quantum simulator and real IBM quantum hardware to examine its results, performance, and limitations.

## Project Structure

| File | Description |
|---|---|
| `warehouse.py` | Defines the simulated warehouse layout and obstacles. |
| `pathfinding.py` | Implements classical A* pathfinding and energy calculations. |
| `quantum_optimizer.py` | Implements QAOA route optimization and quantum hardware execution. |
| `visualization.py` | Displays the warehouse and robot paths. |
| `check_setup.py` | Checks the project environment and setup. |

## How It Works

### 1. Warehouse Environment

The warehouse is represented as a 12x12 grid containing open spaces, obstacles, and charging stations. Robots navigate through the grid while avoiding obstacles.

### 2. Classical Pathfinding (A*)

The classical implementation uses the A* search algorithm to find routes between a robot's starting position and destination.

The algorithm accounts for:
- Straight and diagonal movement.
- Additional energy costs for changing direction.
- Inflated obstacles to maintain clearance around obstacles.
- Temporary blocked cells to generate alternative routes.

### 3. Energy Calculation

Each candidate route is assigned an energy cost based on its movement and direction changes.

- Straight movement: 1.0 energy units.
- Diagonal movement: 1.414 energy units.
- Direction change: 0.5 additional energy units.

### 4. Quantum Optimization (QAOA)

The quantum implementation uses Qiskit and the Quantum Approximate Optimization Algorithm (QAOA).

A* first generates a baseline route and up to three alternative routes. These routes are converted into a binary optimization problem in which each route has a corresponding binary variable.

A constraint requires exactly one route to be selected. The objective is to minimize the calculated energy cost.

### 5. Quantum Hardware Testing

The project also includes an implementation that submits a QAOA circuit to a real IBM quantum computer.

The hardware circuit is transpiled for the selected backend and executed using 1,024 shots. The resulting measurement bitstrings are analyzed to identify outcomes that select exactly one route.

The current hardware implementation applies this constraint through classical filtering after measurement rather than encoding it directly into the quantum cost operator. This is an important limitation of the current implementation.

### Hardware Results

The project completed six hardware experiments across two sets of three warehouse scenarios using IBM's ibm_marrakesh processor.

Each experiment used 1,024 measurement shots. The number of binary variables varied depending on how many candidate routes were generated for each scenario.

The measurement results contained both valid and invalid route selections. Valid outcomes selected exactly one route, while invalid outcomes selected either zero or multiple routes.

The current hardware implementation filters the measurement results to identify valid outcomes. It then selects the valid outcome with the lowest calculated energy cost. This demonstrates a limitation of the current implementation, since the one-route constraint is not directly encoded into the hardware cost operator.

| Test | Run | Binary Variables | Valid Outcomes | ValidPercentage |
|---|---|---|-------------|--------|
| 1 | 1 | 1 | 67 / 1,024  | 6.54%  |
| 1 | 2 | 2 | 535 / 1,024 | 52.25% |
| 1 | 3 | 3 | 52 / 1,024  | 5.08%  |
| 2 | 1 | 4 | 360 / 1,024 | 35.16% |
| 2 | 2 | 4 | 127 / 1,024 | 12.40% |
| 2 | 3 | 3 | 71 / 1,024  | 6.93%  |

The valid percentage represents the proportion of measurement shots that selected exactly one route. These percentages describe the measured output distribution; they do not demonstrate that the hardware successfully enforced the constraint during optimization.

## Installation

Install the required Python packages:

```bash
pip install -r requirements.txt
```

## Running the Project

Launch the visual warehouse comparison:

```bash
python visualization.py
```

Run the classical pathfinding tests:

```bash
python pathfinding.py
```

Run the quantum optimization implementation:

```bash
python quantum_optimizer.py
```

## Results and Limitations

### Simulator Results

In the current simulator test, QAOA successfully selected Route 0 from the available candidate routes.

- Selected route energy: 11.828
- Average QAOA execution time: 0.9525 seconds
- Optimization status: SUCCESS

The selected route traveled from [10, 5] to [0, 5] while avoiding warehouse obstacles.

### Classical A* Results

Two robots were tested using the classical A* algorithm.

- Robot 1 execution time: 0.001204 seconds.
- Robot 2 execution time: 0.001012 seconds.
- Both routes had an energy cost of 11.828.

Both robots exceeded the available battery usage limit of 8 energy units. The battery management system identified charging stations and generated routes to them.

### Comparison

In the current test, both A* and QAOA selected routes with an energy cost of 11.828. A* completed its pathfinding in approximately 1 millisecond, while the QAOA simulator averaged approximately 0.9525 seconds.

These timings are not a controlled performance benchmark because the two approaches perform different amounts of computation.

Hardware Results

The project completed six hardware experiments across two sets of three warehouse scenarios using IBM's ibm_marrakesh processor.

Each experiment used 1,024 measurement shots. The number of binary variables varied depending on how many candidate routes were generated for each scenario.

The measurement results contained both valid and invalid route selections. This demonstrates a limitation of the current hardware implementation, which relies on classical filtering to identify valid outcomes.

This project does not demonstrate quantum advantage. The QAOA implementation operates on a small route-selection problem, and its performance is compared with a classical approach. The results are intended to explore the potential and limitations of quantum optimization for warehouse robotics.