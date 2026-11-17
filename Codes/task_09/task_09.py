
import numpy as np

print("TASK 09: EIGENVALUES AND EIGENVECTORS")

# PART 1: Original computer network
# Node order: A, B, C, D
# 1 = connection exists, 0 = no connection

A = np.array([
    [0., 1., 1., 0.],
    [1., 0., 1., 1.],
    [1., 1., 0., 1.],
    [0., 1., 1., 0.]
])

nodes = ["A", "B", "C", "D"]

# PART 2: Calculate eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(A)

# Find the dominant eigenvalue
index = np.argmax(np.real(eigenvalues))

dominant_value = np.real(eigenvalues[index])
dominant_vector = np.abs(np.real(eigenvectors[:, index]))

# Normalize the eigenvector to get importance scores
centrality = dominant_vector / dominant_vector.sum()

print("\n--- ORIGINAL COMPUTER NETWORK ---")
print("Adjacency matrix:")
print(A)

print("\nAll eigenvalues:")
print(np.round(eigenvalues, 4))

print("\nDominant eigenvalue:")
print(round(dominant_value, 4))

print("\nEigenvector-based node importance:")

for node, score in zip(nodes, centrality):
    print(f"Node {node}: {score:.4f}")

# PART 3: Verify the eigenvector calculation
v = np.real(eigenvectors[:, index])

verification_error = np.linalg.norm(
    A @ v - dominant_value * v
)

print("\nVerification error:", verification_error)

# PART 4: Modify one input
# Remove the connection between nodes B and D

modified_A = A.copy()
modified_A[1, 3] = 0
modified_A[3, 1] = 0

modified_values, modified_vectors = np.linalg.eig(modified_A)

modified_index = np.argmax(np.real(modified_values))

modified_dominant = np.real(
    modified_values[modified_index]
)

modified_vector = np.abs(
    np.real(modified_vectors[:, modified_index])
)

modified_centrality = (
    modified_vector / modified_vector.sum()
)

print("\n--- MODIFIED NETWORK ---")
print("Modified adjacency matrix:")
print(modified_A)

print("\nNew node importance scores:")

for node, score in zip(nodes, modified_centrality):
    print(f"Node {node}: {score:.4f}")

# PART 5: New real-world application
# Model a campus emergency communication network.
# Nodes: Security, Administration, Library, Laboratory, Clinic

campus_nodes = [
    "Security",
    "Administration",
    "Library",
    "Laboratory",
    "Clinic"
]

campus_A = np.array([
    [0., 1., 1., 1., 1.],
    [1., 0., 1., 0., 1.],
    [1., 1., 0., 1., 0.],
    [1., 0., 1., 0., 1.],
    [1., 1., 0., 1., 0.]
])

campus_values, campus_vectors = np.linalg.eig(campus_A)

campus_index = np.argmax(np.real(campus_values))

campus_dominant = np.real(
    campus_values[campus_index]
)

campus_vector = np.abs(
    np.real(campus_vectors[:, campus_index])
)

campus_scores = campus_vector / campus_vector.sum()

print("\n--- CAMPUS COMMUNICATION NETWORK ---")
print("Dominant eigenvalue:", round(campus_dominant, 4))

print("\nDepartment importance scores:")

for department, score in zip(campus_nodes, campus_scores):
    print(f"{department}: {score:.4f}")

print("\nTask 09 completed successfully.")
