import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# ----------------- parameters -----------------
N = 100                     # number of boids (index 0 is the leader)
WIDTH, HEIGHT = 1200, 1000    # world size
MAX_SPEED = 4.0
MAX_FORCE = 0.05
PERCEPTION_RADIUS = 50.0
SEPARATION_RADIUS = 20.0

W_ALIGN = 10.0
W_COHESION = 10.0           # now used as the "seek the leader" weight
W_SEPARATION = 1.0

DT = 1.0
SEED = 1

# ----- NEW: leader parameters -----
LEADER_IDX = 0               # which boid in the array is the leader
WANDER_STRENGTH = 0.03       # how sharply the leader turns while wandering

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
    dpos = pos[:, None, :] - pos[None, :, :]             # shape (N, N, 2)
    dist = np.linalg.norm(dpos, axis=2)                 # shape (N, N)

    neigh_mask = dist < PERCEPTION_RADIUS
    sep_mask = dist < SEPARATION_RADIUS

    align = np.zeros_like(vel)
    cohesion = np.zeros_like(vel)      # repurposed: "seek the leader" vector
    separation = np.zeros_like(vel)

    for i in range(N):
        if i == LEADER_IDX:
            continue  # the leader doesn't flock — handled separately below

        # alignment: still only with OTHER FOLLOWERS, leader excluded
        neighbors = neigh_mask[i].copy()
        neighbors[i] = False
        neighbors[LEADER_IDX] = False
        if np.any(neighbors):
            avg_vel = vel[neighbors].mean(axis=0)
            align[i] = avg_vel - vel[i]

        # ----- NEW: cohesion is replaced by "always seek the leader" -----
        # no neighbor-mask/distance check here on purpose — every follower
        # steers toward the leader regardless of how far away it is.
        desired = pos[LEADER_IDX] - pos[i]
        cohesion[i] = desired - vel[i]

        # separation: still only from OTHER FOLLOWERS, leader excluded
        # (so followers aren't pushed away from the thing they're seeking)
        close = sep_mask[i].copy()
        close[i] = False
        close[LEADER_IDX] = False
        if np.any(close):
            rep = dpos[i, close]
            rep_norms = np.linalg.norm(rep, axis=1)
            rep_norms[rep_norms == 0] = 1e-8
            rep_dir = rep / rep_norms[:, None]
            sep_vec = rep_dir.sum(axis=0)
            separation[i] = -sep_vec

    accel = (W_ALIGN * align) + (W_COHESION * cohesion) + (W_SEPARATION * separation)

    # ----- NEW: leader ignores all flocking rules and just wanders -----
    leader_turn = rng.normal(0.0, 1.0, size=2) * WANDER_STRENGTH
    accel[LEADER_IDX] = leader_turn

    accel = limit_rows(accel, MAX_FORCE)

    vel = vel + accel * DT
    vel = limit_rows(vel, MAX_SPEED)
    pos = pos + vel * DT

    pos[:, 0] = np.mod(pos[:, 0], WIDTH)
    pos[:, 1] = np.mod(pos[:, 1], HEIGHT)

    return pos, vel

# ----------------- visualization -----------------
fig, ax = plt.subplots(figsize=(8, 6))
ax.set_xlim(0, WIDTH)
ax.set_ylim(0, HEIGHT)

# ----- NEW: draw the leader separately so it stands out -----
follower_idx = np.arange(N) != LEADER_IDX

scat_followers = ax.scatter(pos[follower_idx, 0], pos[follower_idx, 1],
                             s=30, color='k')
scat_leader = ax.scatter(pos[LEADER_IDX, 0], pos[LEADER_IDX, 1],
                          s=100, color='red', marker='*', zorder=5)

quiv = ax.quiver(pos[:, 0], pos[:, 1], vel[:, 0], vel[:, 1],
                 angles='xy', scale_units='xy', scale=1.5, width=0.004)

def update(frame):
    global pos, vel
    pos, vel = step(pos, vel)
    scat_followers.set_offsets(pos[follower_idx])
    scat_leader.set_offsets(pos[LEADER_IDX])
    quiv.set_offsets(pos)
    quiv.set_UVC(vel[:, 0], vel[:, 1])
    return scat_followers, scat_leader, quiv

anim = FuncAnimation(fig, update, frames=2000, interval=30, blit=False)
plt.title("Boids with a Leader (followers seek the leader, not each other's centroid)")
plt.show()