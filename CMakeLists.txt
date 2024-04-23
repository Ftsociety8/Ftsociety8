cmake_minimum_required(VERSION 3.27)
project(Python)

set(CMAKE_CXX_STANDARD 17)

add_executable(Python main.cpp
        minesweeper.cpp
)
