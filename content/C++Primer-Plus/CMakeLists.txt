cmake_minimum_required(VERSION 3.2)
project(Cpp-Primer-Plus)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11")

FILE(GLOB SRCS */*.cpp)

foreach (SRC ${SRCS})
    get_filename_component(NAME ${SRC} NAME_WLE)
    cmake_path(GET SRC PARENT_PATH FOLDER)
    get_filename_component(NAME_PRE ${FOLDER} NAME_WLE)
    string(REPLACE " " "_" NAME_PRE ${NAME_PRE})
    add_executable(${NAME_PRE}_${NAME} ${SRC})
endforeach ()