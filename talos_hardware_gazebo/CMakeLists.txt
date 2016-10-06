cmake_minimum_required(VERSION 2.8.3)
project(talos_hardware_gazebo)

find_package(catkin REQUIRED COMPONENTS pal_hardware_gazebo)

catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES talos_hardware_gazebo
#  CATKIN_DEPENDS other_catkin_pkg
#  DEPENDS system_lib
)

install(DIRECTORY config/
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/config)

