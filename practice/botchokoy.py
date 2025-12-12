import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def translation(tx, ty, tz):
    T = np.eye(4)
    T[:3, 3] = [tx, ty, tz]
    return T

def scaling(sx, sy, sz):
    S = np.eye(4)
    S[0,0] = sx
    S[1,1] = sy
    S[2,2] = sz
    return S

def rotation_x(theta):
    c, s = np.cos(theta), np.sin(theta)
    R = np.eye(4)
    R[1,1], R[1,2] = c, -s
    R[2,1], R[2,2] = s, c
    return R

def rotation_y(theta):
    c, s = np.cos(theta), np.sin(theta)
    R = np.eye(4)
    R[0,0], R[0,2] = c, s
    R[2,0], R[2,2] = -s, c
    return R

def rotation_z(theta):
    c, s = np.cos(theta), np.sin(theta)
    R = np.eye(4)
    R[0,0], R[0,1] = c, -s
    R[1,0], R[1,1] = s, c
    return R

def rotation_axis_angle(axis, theta):
    axis = np.array(axis, dtype=float)
    axis = axis / np.linalg.norm(axis)
    x, y, z = axis
    c = np.cos(theta)
    s = np.sin(theta)
    C = 1 - c
    R3 = np.array([
        [x*x*C + c,   x*y*C - z*s, x*z*C + y*s],
        [y*x*C + z*s, y*y*C + c,   y*z*C - x*s],
        [z*x*C - y*s, z*y*C + x*s, z*z*C + c  ]
    ])
    R = np.eye(4)
    R[:3,:3] = R3
    return R

def apply_transform(points, transform):
    pts_h = np.hstack([points, np.ones((points.shape[0], 1))])
    transformed_h = (transform @ pts_h.T).T
    return transformed_h[:, :3]

cube_vertices = np.array([
    [-0.5, -0.5, -0.5],
    [ 0.5, -0.5, -0.5],
    [ 0.5,  0.5, -0.5],
    [-0.5,  0.5, -0.5],
    [-0.5, -0.5,  0.5],
    [ 0.5, -0.5,  0.5],
    [ 0.5,  0.5,  0.5],
    [-0.5,  0.5,  0.5],
])

edges = [
    (0,1),(1,2),(2,3),(3,0),
    (4,5),(5,6),(6,7),(7,4),
    (0,4),(1,5),(2,6),(3,7)
]

S = scaling(1.2, 0.7, 1.0)
Raxis = rotation_axis_angle([1, 1, 0], np.deg2rad(35))
Rz = rotation_z(np.deg2rad(20))
T = translation(1.5, -0.3, 0.8)

composite = T @ Rz @ Raxis @ S

transformed_vertices = apply_transform(cube_vertices, composite)

fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(111, projection='3d')
ax.set_box_aspect([1,1,1])

for a, b in edges:
    ax.plot(
        [cube_vertices[a,0], cube_vertices[b,0]],
        [cube_vertices[a,1], cube_vertices[b,1]],
        [cube_vertices[a,2], cube_vertices[b,2]]
    )

for a, b in edges:
    ax.plot(
        [transformed_vertices[a,0], transformed_vertices[b,0]],
        [transformed_vertices[a,1], transformed_vertices[b,1]],
        [transformed_vertices[a,2], transformed_vertices[b,2]]
    )

ax.set_title("3D Transformations — Original vs Transformed Cube")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")

plt.show()

print("Composite matrix:\n", np.round(composite, 4))
