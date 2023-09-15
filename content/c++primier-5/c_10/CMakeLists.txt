FILE(GLOB SRCS *.cc)

foreach (SRC ${SRCS})
    get_filename_component(NAME ${SRC} NAME_WLE)
    add_executable(c10_${NAME} ${SRC})
endforeach (CHARTER)