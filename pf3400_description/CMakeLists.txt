cmake_minimum_required(VERSION 3.5)
project(pf3400_description)

find_package(ament_cmake REQUIRED)

ament_package()

install(DIRECTORY meshes urdf srv 
    DESTINATION share/${PROJECT_NAME})
