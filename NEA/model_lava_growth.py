import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# -----------------------------
# Parameters
# -----------------------------
N = 40
dt = 0.05
steps = 250

rupture_time = 40
mhetase_delay = 30

# -----------------------------
# Fields
# -----------------------------
PET = np.ones((N, N, N))
PETase = np.zeros((N, N, N))
MHETase = np.zeros((N, N, N))

# -----------------------------
# Vesicle positions
# -----------------------------
mid = N // 2
vesicles = []
radius = 1.5

for x in range(6, N, 7):
    for y in range(6, N, 7):
        vesicles.append((x, y, mid))

# -----------------------------
# Plot setup
# -----------------------------
fig = plt.figure(figsize=(7, 7))
ax = fig.add_subplot(projection="3d")

ax.set_xlim(0, N)
ax.set_ylim(0, N)
ax.set_zlim(0, N)

# LOCK CAMERA (important)
ax.view_init(elev=25, azim=45)

# -----------------------------
# Sphere generator
# -----------------------------
def draw_sphere(cx, cy, cz, r, color, alpha):
    u = np.linspace(0, 2*np.pi, 12)
    v = np.linspace(0, np.pi, 12)
    x = cx + r * np.outer(np.cos(u), np.sin(v))
    y = cy + r * np.outer(np.sin(u), np.sin(v))
    z = cz + r * np.outer(np.ones_like(u), np.cos(v))
    ax.plot_surface(x, y, z, color=color, alpha=alpha, linewidth=0)

# -----------------------------
# Animation update
# -----------------------------
def update(frame):
    global PET

    ax.cla()
    ax.set_xlim(0, N)
    ax.set_ylim(0, N)
    ax.set_zlim(0, N)
    ax.view_init(elev=25, azim=45)

    # Rupture event
    if frame >= rupture_time:
        for x, y, z in vesicles:
            PETase[x, y, z] = 1.0

    # Simple PET decay where enzyme present
    PET -= 0.02 * PETase
    PET = np.clip(PET, 0, 1)

    # --- Draw PET degradation ---
    xs, ys, zs = np.where(PET < 0.8)
    ax.scatter(xs, ys, zs, c='red', s=4, alpha=0.4)

    # --- Draw vesicles ---
    for x, y, z in vesicles:
        if frame < rupture_time:
            draw_sphere(x, y, z, radius, "cyan", 0.35)
        else:
            draw_sphere(x, y, z, radius, "gray", 0.15)

    ax.set_title(f"UV-Triggered Vesicle Rupture – t = {frame}")

ani = FuncAnimation(fig, update, frames=steps, interval=60)
plt.show()
