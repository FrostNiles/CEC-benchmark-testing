#include <WINDOWS.H>    
#include <stdio.h>
#include <math.h>
#include <malloc.h>

void cec17_test_func(double*, double*, int, int, int);

double* OShift, * M, * y, * z, * x_bound;
int ini_flag = 0, n_flag, func_flag, * SS;

int main() {
    int i, j, k, n, m, func_num;
    double* f, * x;
    FILE* fpt;
    char FileName[50];
    m = 2;
    n = 10;
    x = (double*)malloc(m * n * sizeof(double));
    f = (double*)malloc(sizeof(double) * m);

    // Check if memory allocation for x and f failed
    if (x == NULL || f == NULL) {
        fprintf(stderr, "\nError: Insufficient memory available!\n");
        free(x); // It's safe to call free on NULL
        free(f);
        return 1; // Indicate error
    }

    for (i = 0; i < 1; i++) {
        func_num = i + 1;
        sprintf_s(FileName, sizeof(FileName), ("test_data/shift_data_%d_adjusted.txt", func_num));
        //fpt = fopen(FileName, "r");
        //if (fpt == NULL) {
        //    fprintf(stderr, "\nError: Cannot open input file for reading\n");
        //    continue; // Skip this iteration if the file cannot be opened
        //}
        errno_t err;
        err = fopen_s(&fpt, FileName, "r");
        if (err != 0) {
            fprintf(stderr, "\nError: Cannot open input file for reading\n");
            continue; // or handle the error as necessary
        }
        for (k = 0; k < n; k++) {
            if (fscanf_s(fpt, "%lf", &x[k]) != 1) { // Check for read errors
                fprintf(stderr, "\nError: Failed to read data for function %d\n", func_num);
                break; // Exit the loop on read error
            }
        }

        fclose(fpt); // Make sure to close the file in each iteration

        // Initialize the rest of the x array to 0
        for (j = 0; j < n; j++) {
            x[1 * n + j] = 0.0;
        }
        
        // Call the test function with error handling for the file operations
        cec17_test_func(x, f, n, m, func_num);
        for (j = 0; j < 2; j++) {
            printf(" f%d(x[%d]) = %.10f,", func_num, j + 1, f[j]);
        }
        printf("\n");
    }

    // Free allocated resources at the end
    free(x);
    free(f);
    // Assuming y, z, M, OShift, and x_bound are allocated elsewhere
    return 0; // Indicate successful execution
}