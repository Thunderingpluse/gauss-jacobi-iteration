# Gauss-Jacobi Iteration Method

## Aim
To solve a system of $N \times N$ linear equations iteratively using the Gauss-Jacobi method.

## Theory
The Gauss-Jacobi method is an iterative algorithm for determining the solutions of a strictly diagonally dominant system of linear equations. 
Given a system $Ax = b$, the equation for each variable $x_i$ at iteration $k+1$ is updated using values of $x$ from the previous iteration $k$:

$$x_i^{(k+1)} = \frac{1}{A_{i,i}} \left( b_i - \sum_{j \neq i} A_{i,j} x_j^{(k)} \right)$$

### Convergence Condition
The method is guaranteed to converge if the matrix $A$ is **strictly diagonally dominant**, meaning:
$$|A_{i,i}| > \sum_{j \neq i} |A_{i,j}| \quad \forall i$$
The script automatically checks for diagonal dominance and prints a warning if the matrix does not meet this condition.

## File Structure
- `Gauss Jacobi.py` - Core iterative solver with diagonal dominance checking and convergence logs.
- `output.txt` - Sample run logs detailing iterative convergence steps.

## How to Run
Ensure you have Python 3 and NumPy installed:
```bash
pip install numpy
python "Gauss Jacobi.py"
```

### Input Format
- Enter the size of matrix $N$ (e.g., `3`).
- Enter the $N \times N$ coefficient matrix $A$ row-by-row.
- Enter the $N$ constants of vector $B$ space-separated.
