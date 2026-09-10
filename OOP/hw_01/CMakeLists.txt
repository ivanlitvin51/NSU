cmake_minimum_required(VERSION 3.15)
project(hw_01 LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

add_executable(hw_01
    main.cpp
    hypo.hpp
    hypo.cpp
    hypo_mod.hpp
    hypo_mod.cpp
)
