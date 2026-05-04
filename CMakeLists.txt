cmake_minimum_required(VERSION 3.10)

project(ScaleAtoN-Crypto-Mapper)

find_package(CCUDA REQUIRED)

set(CMAKE_CUDA_STANDARD 14)
set(CMAKE_CUDA_ARCH_BIN "70;75;80;86")

include_directories(include)

set(SOURCES
    src/main.cu
    src/kangaroo_kernel.cu
    src/ec_math.cu
)

add_executable(ScaleAtoN-Crypto-Mapper ${SOURCES})
