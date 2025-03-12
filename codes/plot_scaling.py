import matplotlib.pyplot as plt
import numpy as np

# Data
processes = np.array([2, 4, 8, 16])
time_taken = np.array([1.7658, 1.0472, 0.5291, 0.4192])

# Ideal linear scaling (normalized to 2-process time)
ideal_time = time_taken[0] * (processes[0] / processes)

# Plot
plt.figure(figsize=(8, 5))
plt.plot(processes, time_taken, marker='o', linestyle='-', color='b', label='Execution Time')
plt.plot(processes, ideal_time, marker='s', linestyle='--', color='r', label='Ideal Linear Scaling')

# Labels and title
plt.xlabel('Number of Processes')
plt.ylabel('Time Taken (seconds)')
plt.title('Scaling Performance')
plt.xticks(processes)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()

# Show plot
plt.savefig('./scalability.pdf')
