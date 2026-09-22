cmake_minimum_required(VERSION 4.2)
project(lab1 CXX)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

if(MSVC)
    add_compile_options($<$<CONFIG:Release>:/O2>)
    add_compile_options($<$<CONFIG:Release>:/W3>)
else()
    add_compile_options($<$<CONFIG:Release>:-O2>)
endif()

add_executable(lab1 matrix_mul.cpp)