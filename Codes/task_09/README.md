# Task 09: Eigenvalues and Eigenvectors

## 1. Objective

To understand eigenvalues and eigenvectors and use Python to determine the structural importance of nodes in a network.

## 2. Mathematical Concept

An eigenvector is a non-zero vector whose direction remains unchanged when a matrix transformation is applied.

The relationship is represented by:

Av = λv

Where A is a square matrix, v is an eigenvector and λ is its eigenvalue.

The dominant eigenvector can be normalized to calculate relative node-importance scores.

## 3. Original Problem

A small computer network contains four nodes labelled A, B, C and D. The objective is to identify the most influential nodes based on their connection patterns.

## 4. Input Values

The adjacency matrix is:

[[0, 1, 1, 0],
 [1, 0, 1, 1],
 [1, 1, 0, 1],
 [0, 1, 1, 0]]

A value of 1 represents an existing connection, while 0 represents no connection.

## 5. Mathematical Operations

The program uses:

- `np.linalg.eig()` to calculate eigenvalues and eigenvectors.
- `np.argmax()` to identify the dominant eigenvalue index.
- Eigenvector normalization to calculate node-importance scores.
- Matrix multiplication to verify the eigenvector relationship.

## 6. Original Results

The dominant eigenvalue is approximately 2.5616.

The normalized importance scores are:

- Node A: 0.2192
- Node B: 0.2808
- Node C: 0.2808
- Node D: 0.2192

Nodes B and C have the highest structural importance.

## 7. Modified Experiment

The connection between nodes B and D was removed by changing the corresponding entries in the adjacency matrix.

This changed the network structure and produced a new distribution of eigenvector-based importance scores.

## 8. Related Real-World Application

A campus emergency communication network was modelled using five departments: Security, Administration, Library, Laboratory and Clinic.

The same eigenvalue and eigenvector method was used to estimate the structural importance of each department based on its connections.

## 9. Assumptions

- The network is undirected.
- Connections are represented using binary values.
- All connections have equal weight.
- The adjacency matrix represents the network structure accurately.
- The dominant eigenvector is used as a relative importance measure.

## 10. Conclusion

Eigenvalues and eigenvectors can help identify structurally influential nodes in networks. This technique has applications in network analysis, Google PageRank concepts, vibration analysis and principal component analysis.