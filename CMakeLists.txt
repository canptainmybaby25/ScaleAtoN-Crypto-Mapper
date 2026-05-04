# CMakeLists.txt for BitCRACKQ Kangaroo CUDA project

cmake_minimum_required(VERSION 3.10)

# Set project name and version
project(BitCRACKQ VERSION 1.0)

# Find CUDA
find_package(CUDA REQUIRED)

# Specify the source files
set(SOURCES
    main.cu
    # Add other source files here
)

# Include directories
include_directories(${CUDA_INCLUDE_DIRS})

# Define executable
cuda_add_executable(BitCRACKQ ${SOURCES})

# Set additional options if needed
set_target_properties(BitCRACKQ PROPERTIES CUDA_SEPARABLE_COMPILATION ON)

# Link any required libraries here
