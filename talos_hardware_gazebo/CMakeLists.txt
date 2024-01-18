cmake_minimum_required(VERSION 3.5)
project(talos_hardware_gazebo)

find_package(ament_cmake_auto REQUIRED)  # pal_hardware_gazebo)

ament_auto_find_build_dependencies()

ament_auto_package(INSTALL_TO_SHARE)

