#!/bin/bash

# Proper CMake configuration
mkdir -p build
cd build
cmake ..

# Build the project with error handling
if ! make -j; then
    echo "Build failed!"
    exit 1
fi

echo "Build completed successfully!"