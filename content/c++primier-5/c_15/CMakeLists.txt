FILE(GLOB SRCS *.cc)

foreach (SRC ${SRCS})
    get_filename_component(NAME ${SRC} NAME_WLE)
    add_executable(c15_${NAME} ${SRC})
endforeach (CHARTER)