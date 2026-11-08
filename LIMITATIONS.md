### Project Limitations

### Current Limitations

This project demonstrates how QAOA can be applied to a simplified warehouse robot pathfinding problem. However, there are several limitations to the current implementation.

### Problem Size

The current system generates a small number of candidate routes for each warehouse scenario. This keeps the optimization problem manageable but does not represent the complexity of a full-scale warehouse environment.

### Classical and Quantum Performance

The classical A* algorithm currently finds routes significantly faster than the QAOA simulator. In our testing, A* completed pathfinding in approximately 1 millisecond, while the simulator's QAOA optimization averaged approximately 0.95 seconds.

These results do not demonstrate a quantum advantage. The two algorithms also perform different tasks: A* generates candidate routes, while QAOA selects among those routes.

### Quantum Hardware Limitations

The IBM Quantum hardware experiments used a fixed QAOA parameter value of 0.5 rather than optimizing the circuit parameters on the hardware.

Hardware measurements produced bitstrings that did not always satisfy the one-route selection constraint. The current hardware implementation does not encode this constraint directly into the cost operator. Instead, it filters measurement results after execution and selects the lowest-energy outcome among those that select exactly one route.

This means the hardware circuit does not directly solve the constrained route-selection problem as intended. Improving constraint encoding is an important area for future development.

### Simplified Warehouse Environment

The warehouse is represented as a two-dimensional grid. The current implementation does not fully model real-world factors such as robot traffic, dynamic obstacles, varying payload weights, or communication between multiple robots.

### Future Improvements

Several improvements could make the system more representative of real-world warehouse operations.

Constraint Encoding: Improve the quantum cost Hamiltonian so the one-route selection constraint is encoded directly into the QAOA circuit rather than relying only on filtering measurement results.

Parameter Optimization: Experiment with optimizing QAOA parameters for IBM Quantum hardware instead of using fixed values.

Larger Problems: Test the system with more candidate routes, larger warehouse grids, and additional obstacles.

Multi-Robot Coordination: Expand the optimization problem to account for multiple robots navigating the warehouse simultaneously.

Energy Modeling: Improve the energy model by incorporating additional factors such as robot payload, acceleration, and movement conditions.

Performance Comparison: Conduct more controlled experiments comparing classical and quantum approaches using the same optimization problem and evaluation criteria.

### Conclusion

The project demonstrates a working exploration of QAOA applied to warehouse route selection using both a local simulator and IBM Quantum hardware.

The current results show that quantum hardware can execute the optimization circuits, but the implementation still has limitations in constraint handling, parameter selection, and problem size. Further development is needed before this approach could be considered practical for real-world warehouse pathfinding.

The project does not claim a quantum advantage over classical algorithms. Instead, it explores the potential and current limitations of applying quantum optimization to an industrial robotics problem.