cmake_minimum_required(VERSION 2.8.12)
project(CppMeshRenderer)

include_directories(glad)
add_definitions(-DUSE_GLAD)

add_executable(query_devices glad/egl.cpp glad/gl.cpp query_devices.cpp)
add_executable(test_device glad/egl.cpp glad/gl.cpp test_device.cpp)

target_link_libraries(query_devices dl pthread)
target_link_libraries(test_device dl pthread)