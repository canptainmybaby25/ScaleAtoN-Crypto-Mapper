// Configuration parameters for BitCRACKQ Kangaroo algorithm

#ifndef CONFIG_H
#define CONFIG_H

// Tunable parameters
const int WINDOW_LENGTH = 10000;  // Length of the window
const int QMAP_BITS = 27;          // Number of bits in qmap
const int DP_THRESHOLD = 5000;      // DP threshold
const int NEAR_COLLISION_BITS = 20; // Near-collision bits
const int JUMP_TABLE_SIZE = 1024;   // Size of the jump table
const int FOOTPRINT_BITS = 30;       // Footprint bits

// GPU parameters
const int GPU_MAX_THREADS = 256;     // Maximum threads per block
const int GPU_SHARED_MEMORY = 49152; // Shared memory per block (in bytes)

// Event buffer size
const int EVENT_BUFFER_SIZE = 1024;   // Size of the event buffer

// Search range parameters
const int SEARCH_RANGE_START = 0;     // Start of search range
const int SEARCH_RANGE_END = 100000;  // End of search range

#endif // CONFIG_H
