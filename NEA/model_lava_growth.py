import matplotlib.pyplot as plt

# -------------------------
# Simulation parameters
# -------------------------
dt = 1 / 60              # seconds per frame (60 FPS)
total_time = 10          # seconds to simulate

initial_size = 10        # starting lava height (pixels)
initial_rate = 10       # starting growth rate
max_rate = 250           # rate cap (from your code)

# -------------------------
# State variables
# -------------------------
size = initial_size
rate = initial_rate

time_values = []
size_values = []
rate_values = []

# -------------------------
# Simulation loop
# -------------------------
t = 0
while t <= total_time:
    # --- update_rate(dt) ---
    if rate <= max_rate:
        rate += 50 * dt
    else:
        rate = max_rate

    # --- update_size(dt) ---
    size += rate * dt

    # store values
    time_values.append(t)
    size_values.append(size)
    rate_values.append(rate)

    t += dt

# -------------------------
# Plotting
# -------------------------
plt.figure()
plt.plot(time_values, size_values)
plt.xlabel("Time (seconds)")
plt.ylabel("Lava Height (pixels)")
plt.title("Lava Sprite Growth Over Time")
plt.show()

# Optional: plot rate as well
plt.figure()
plt.plot(time_values, rate_values)
plt.xlabel("Time (seconds)")
plt.ylabel("Growth Rate (pixels/sec)")
plt.title("Lava Growth Rate Over Time")
plt.show()
