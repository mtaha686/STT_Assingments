import java.util.Scanner;

public class MatrixInversion {
    public static void main(String[] args) {
        // Initialize the input matrix A
        double[][] A = new double[2][2];
        try (Scanner scanner = new Scanner(System.in)) {
            System.out.println("Enter the elements of the 2x2 matrix A:");
            for (int i = 0; i < 2; i++) {
                for (int j = 0; j < 2; j++) {
                    A[i][j] = scanner.nextDouble();
                }
            }
        }
        // Compute the determinant of A
        double det = A[0][0] * A[1][1] - A[0][1] * A[1][0];

        // Check if A is invertible
        if (det == 0) {
            System.out.println("Error: Matrix A is not invertible.");
            return;
        }

        double[][] Ainv = new double[2][2];
        Ainv[0][0] = A[1][1] / det;
        Ainv[0][1] = -A[0][1] / det;
        Ainv[1][0] = -A[1][0] / det;
        Ainv[1][1] = A[0][0] / det;

        double[][] Aprod = new double[2][2];
        for (int i = 0; i < 2; i++) {
            for (int j = 0; j < 2; j++) {
                Aprod[i][j] = 0;
                for (int k = 0; k < 2; k++) {
                    Aprod[i][j] += A[i][k] * Ainv[k][j];
                }
            }
        }

        boolean pass = true;
        for (int i = 0; i < 2; i++) {
            for (int j = 0; j < 2; j++) {
                if (i == j && Math.abs(Aprod[i][j] - 1) > 1e-6) {
                    pass = false;
                } else if (i != j && Math.abs(Aprod[i][j]) > 1e-6) {
                    pass = false;
                }
            }
        }

        if (pass) {
            System.out.println("PASS: A*Ainv = I");
        } else {
            System.out.println("FAIL: A*Ainv != I");
        }
    }
}
