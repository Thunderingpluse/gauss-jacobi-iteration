import numpy as np

def gauss_jacobi(A, B, tol=0.001, max_iter=100):
    n, x = len(B), np.zeros(len(B))
    print("\nStarting Gauss Jacobi")
    
    if not np.all(np.abs(np.diag(A)) >= (np.sum(np.abs(A), axis=1) - np.abs(np.diag(A)))):
        print("Matrix is not diagonally dominant")

    for k in range(max_iter):
        x_new = np.array([(B[i] - (np.dot(A[i, :i], x[:i]) + np.dot(A[i, i+1:], x[i+1:]))) / A[i, i] for i in range(n)])
        error = np.max(np.abs(x_new - x))
        print(f"Iteration {k+1}: [{', '.join(f'{v:8.3f}' for v in x_new)}]")
        
        if error < tol:
            print(f"\nConverged in {k+1} iterations")
            return x_new
        x = x_new
    print("\nNot converge")
    return x

def main():
    try:
        print("Gauss Jacobi Iterative Method")
        n = int(input("Size of matrix (N): "))
        print(f"Enter the elements of {n}x{n} matrix A: ")
        A = np.array([list(map(float, input(f"Row {i+1}: ").split())) for i in range(n)])
        print(f"Enter the {n} elements of vector B:")
        B = np.array(list(map(float, input().split())))
        
        sol = gauss_jacobi(A, B)
        print("\nFinal Solution:")
        for i, val in enumerate(sol): print(f"x{i+1} = {val:.3f}")
    except Exception as e: print(f"Error: {e}")

if __name__ == "__main__": main()
