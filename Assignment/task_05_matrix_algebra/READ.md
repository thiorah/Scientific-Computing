# Task 05: Matrix Algebra and Matrix Operations

## 1. Objective

To understand matrix operations and apply them to coordinate transformations using Python and NumPy.

## 2. Original Problem

A computer graphics program needs to rotate and scale four coordinates representing the corners of a square.

## 3. Input Data

The square has four coordinate points:

(0,0), (1,0), (1,1), (0,1).

The original rotation angle is 45 degrees. The horizontal scaling factor is 2, while the vertical scaling factor is 1.5.

## 4. Mathematical Operations

The program creates rotation and scaling matrices and combines them through matrix multiplication.

The transformed coordinates are calculated using:

P_new = P × Tᵀ

The determinant and inverse of the transformation matrix are also calculated.

## 5. Original Results

The transformation rotates and scales the square. The determinant is approximately 3, showing that the transformation is invertible and changes the area by a factor of 3.

## 6. Modified Input

The rotation angle was increased from 45 degrees to 90 degrees.

The resulting coordinates changed because the square underwent a larger rotation.

## 7. Related Real-World Application

The program was modified to transform the coordinates of a rectangular room layout. A 30-degree rotation and a scaling factor of 1.5 were applied.

This demonstrates how matrix transformations can support floor-plan design and computer graphics.

## 8. Assumptions

- The coordinates represent points in a two-dimensional plane.
- Rotation is measured in degrees and converted to radians.
- Scaling is applied along the horizontal and vertical axes.
- The transformation uses consistent coordinate units.

## 9. Conclusion

Matrix algebra makes it possible to perform multiple mathematical operations on coordinates efficiently. NumPy provides useful functions for matrix multiplication, determinants and inverses. Changing the rotation angle demonstrated how transformation parameters affect the final coordinates.