
import numpy as np

print("TASK 05: MATRIX ALGEBRA AND MATRIX OPERATIONS")

# PART 1: Original square coordinates
points = np.array([
    [0.0, 0.0],
    [1.0, 0.0],
    [1.0, 1.0],
    [0.0, 1.0]
])

print("\n--- Original Coordinates ---")
print(points)

# PART 2: Create a rotation matrix
angle = np.deg2rad(45)

rotation = np.array([
    [np.cos(angle), -np.sin(angle)],
    [np.sin(angle),  np.cos(angle)]
])

# PART 3: Create a scaling matrix
scale = np.array([
    [2.0, 0.0],
    [0.0, 1.5]
])

# PART 4: Combine rotation and scaling
transformation = rotation @ scale

# Transform all four points
transformed_points = points @ transformation.T

print("\n--- Rotation Matrix ---")
print(rotation)

print("\n--- Scaling Matrix ---")
print(scale)

print("\n--- Combined Transformation Matrix ---")
print(transformation)

print("\n--- Transformed Coordinates ---")
print(np.round(transformed_points, 4))

# PART 5: Matrix operations
determinant = np.linalg.det(transformation)

print("\n--- Matrix Operations ---")
print("Determinant:", round(determinant, 4))

# Check whether the transformation is invertible
if not np.isclose(determinant, 0):
    inverse = np.linalg.inv(transformation)
    print("Inverse Matrix:")
    print(np.round(inverse, 4))

# PART 6: Modify the rotation angle
modified_angle = np.deg2rad(90)

modified_rotation = np.array([
    [np.cos(modified_angle), -np.sin(modified_angle)],
    [np.sin(modified_angle),  np.cos(modified_angle)]
])

modified_transformation = modified_rotation @ scale

modified_points = points @ modified_transformation.T

print("\n--- Modified Experiment: 90 Degree Rotation ---")
print(np.round(modified_points, 4))

# PART 7: Related real-world application
# Transform a rectangular room layout.
room_points = np.array([
    [0.0, 0.0],
    [4.0, 0.0],
    [4.0, 2.0],
    [0.0, 2.0]
])

room_angle = np.deg2rad(30)

room_rotation = np.array([
    [np.cos(room_angle), -np.sin(room_angle)],
    [np.sin(room_angle),  np.cos(room_angle)]
])

room_scale = np.array([
    [1.5, 0.0],
    [0.0, 1.5]
])

room_transformation = room_rotation @ room_scale
new_room_points = room_points @ room_transformation.T

print("\n--- Real-World Application: Room Layout ---")
print("Original room coordinates:")
print(room_points)

print("Transformed room coordinates:")
print(np.round(new_room_points, 4))
