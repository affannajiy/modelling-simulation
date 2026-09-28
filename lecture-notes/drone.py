
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# ----------------- parameters -----------------
N = 100                     # number of boids
WIDTH, HEIGHT = 1200, 1000    # world size
MAX_SPEED = 4.0
MAX_FORCE = 0.05
PERCEPTION_RADIUS = 50.0
SEPARATION_RADIUS = 20.0

W_ALIGN = 1.0
W_COHESION = 0.8
W_SEPARATION = 1.5

DT = 1.0
SEED = 1

# ----------------- initialization -----------------
rng = np.random.default_rng(SEED)
pos = rng.uniform([0.0, 0.0], [WIDTH, HEIGHT], size=(N, 2))
vel = rng.normal(0.0, 1.0, size=(N, 2))
speeds = np.linalg.norm(vel, axis=1, keepdims=True)
vel = vel / (speeds + 1e-8) * rng.uniform(0.5 * MAX_SPEED, MAX_SPEED, size=(N, 1))

# ----------------- helper functions -----------------
def limit_rows(v, max_val):
    """Limit the norm of each row vector in v to max_val."""
    norms = np.linalg.norm(v, axis=1)
    mask = norms > max_val
    if np.any(mask):
        v[mask] = v[mask] / norms[mask, None] * max_val
    return v

# ----------------- simulation step -----------------
def step(pos, vel):

    N = pos.shape[0]
    # pairwise displacement: vector from j -> i stored at [i,j,:]
    dpos = pos[:, None, :] - pos[None, :, :]             # shape (N, N, 2)
    dist = np.linalg.norm(dpos, axis=2)                 # shape (N, N)

    neigh_mask = dist < PERCEPTION_RADIUS
    sep_mask = dist < SEPARATION_RADIUS

    align = np.zeros_like(vel)
    cohesion = np.zeros_like(vel)
    separation = np.zeros_like(vel)

    for i in range(N):  # for every boid
        # neighbors excluding self
        neighbors = neigh_mask[i].copy()
        neighbors[i] = False
        if np.any(neighbors): # if has neighbor
    
            # alignment: steer toward average neighbor velocity
            avg_vel = vel[neighbors].mean(axis=0)            # shape (2,)
            align[i] = avg_vel - vel[i]

            # cohesion: steer toward center of mass of neighbors
            center = pos[neighbors].mean(axis=0)
            desired = center - pos[i]
            cohesion[i] = desired - vel[i]

        # separation: avoid close neighbors
        close = sep_mask[i].copy()
        close[i] = False
        if np.any(close): # if any is too close
            rep = dpos[i, close]                               # shape (k,2)
            rep_norms = np.linalg.norm(rep, axis=1)
            # avoid division by zero
            rep_norms[rep_norms == 0] = 1e-8
            rep_dir = rep / rep_norms[:, None]               # shape (k,2)
            sep_vec = rep_dir.sum(axis=0)                    # shape (2,)
            separation[i] = -sep_vec

    # combine behavior vectors with weights
    accel = (W_ALIGN * align) + (W_COHESION * cohesion) + (W_SEPARATION * separation)
    accel = limit_rows(accel, MAX_FORCE)

    # integrate
    vel = vel + accel * DT
    vel = limit_rows(vel, MAX_SPEED)
    pos = pos + vel * DT

    # wrap around edges (toroidal)
    pos[:, 0] = np.mod(pos[:, 0], WIDTH)
    pos[:, 1] = np.mod(pos[:, 1], HEIGHT)

    return pos, vel

# ----------------- visualization -----------------
fig, ax = plt.subplots(figsize=(8, 6))
ax.set_xlim(0, WIDTH)
ax.set_ylim(0, HEIGHT)
scat = ax.scatter(pos[:, 0], pos[:, 1], s=30, color='k')
quiv = ax.quiver(pos[:, 0], pos[:, 1], vel[:, 0], vel[:, 1],
                 angles='xy', scale_units='xy', scale=1.5, width=0.004)

def update(frame):
    global pos, vel
    pos, vel = step(pos, vel)
    scat.set_offsets(pos)
    quiv.set_offsets(pos)
    quiv.set_UVC(vel[:, 0], vel[:, 1])
    return scat, quiv

anim = FuncAnimation(fig, update, frames=2000, interval=30, blit=False)
plt.title("Reynolds Boids (alignment, cohesion, separation)")
plt.show()
