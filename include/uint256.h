#include <stdint.h>

// Structure for a 256-bit unsigned integer
typedef struct {
    uint64_t limbs[4]; // 4*64-bit fields for 256-bits
} uint256;

// Function to initialize a uint256 to zero
void uint256_init(uint256 *number) {
    for (int i = 0; i < 4; i++) {
        number->limbs[i] = 0;
    }
}

// Function to add two uint256 numbers
uint256 uint256_add(uint256 a, uint256 b) {
    uint256 result;
    __uint128_t carry = 0;
    for (int i = 0; i < 4; i++) {
        carry += (uint128_t)a.limbs[i] + b.limbs[i];
        result.limbs[i] = (uint64_t)carry;
        carry >>= 64; // propagate further carry
    }
    return result;
}

// Other arithmetic operations (subtract, multiply) can be implemented similarly.

