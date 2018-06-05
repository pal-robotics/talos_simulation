cmake_minimum_required(VERSION 2.8.3)
project(talos_gazebo)

find_package(catkin REQUIRED)

catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES talos_gazebo
#  CATKIN_DEPENDS other_catkin_pkg
#  DEPENDS system_lib
)

foreach(dir launch)
    install(DIRECTORY ${dir}/
        DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/${dir})
endforeach(dir)
