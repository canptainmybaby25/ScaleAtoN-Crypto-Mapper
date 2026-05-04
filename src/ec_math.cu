#include <stdio.h>
#include <stdint.h>

// Field parameters
const uint64_t p = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F;

// Modular addition
__device__ uint64_t mod_add(uint64_t a, uint64_t b, uint64_t p) {
    return (a + b) % p;
}

// Modular multiplication
__device__ uint64_t mod_mul(uint64_t a, uint64_t b, uint64_t p) {
    return (a * b) % p;
}

// Extended Euclidean Algorithm for modular inversion
__device__ uint64_t mod_inv(uint64_t a, uint64_t p) {
    uint64_t m0 = p, t, q;
    uint64_t x0 = 0, x1 = 1;

    if (p == 1) return 0;

    while (a > 1) {
        // q is quotient
        q = a / p;
        t = p;

        // p is remainder now, process same as Euclid's algorithm
        p = a % p, a = t;
        t = x0;

        x0 = x1 - q * x0;
        x1 = t;
    }

    // Make x1 positive
    if (x1 < 0) x1 += m0;

    return x1;
}

// Point doubling operation
__device__ void point_double(uint64_t& x, uint64_t& y) {
    uint64_t slope = (3 * mod_mul(x, x, p)) * mod_inv(2 * y, p) % p;
    uint64_t x3 = (mod_mul(slope, slope, p) - 2 * x + p) % p;
    uint64_t y3 = (mod_mul(slope, (x - x3 + p) % p, p) - y + p) % p;

    x = x3;
    y = y3;
}

// Example usage
__global__ void example() {
    uint64_t x = 0; // Replace with actual values
    uint64_t y = 0; // Replace with actual values

    point_double(x, y);
    printf("Doubled point: (%llu, %llu)\n", x, y);
}