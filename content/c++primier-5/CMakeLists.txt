cmake_minimum_required(VERSION 3.2)
project(Cpp-Primer-5th)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11")

include_directories(include)

FILE(GLOB CHARTERS c_*)

foreach (CHARTER ${CHARTERS})
    message(${CHARTER})
    add_subdirectory(${CHARTER})
endforeach (CHARTER)