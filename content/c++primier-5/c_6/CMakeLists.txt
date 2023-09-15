FILE(GLOB SRCS *.cc)

foreach (SRC ${SRCS})
    get_filename_component(NAME ${SRC} NAME_WLE)
    add_executable(c6_${NAME} ${SRC})
endforeach (CHARTER)