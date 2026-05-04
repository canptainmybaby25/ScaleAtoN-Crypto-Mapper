#!/bin/bash

# Build the CUDA project using CMake

# Set the build directory
BUILD_DIR="build"

# Create build directory if it doesn't exist
if [ ! -d "$BUILD_DIR" ]; then
    mkdir "$BUILD_DIR"
fi

# Navigate to the build directory
cd "$BUILD_DIR"

# Define CUDA architectures to compile for
CUDA_ARCHS=("30" "35" "50" "52" "60" "61" "70" "75" "80")

# Generate the build system with CMake
cmake .. -DCMAKE_CUDA_ARCH_BIN="${CUDA_ARCHS[*]}"

# Compile the project
make