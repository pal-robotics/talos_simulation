# Copyright (c) 2024 PAL Robotics S.L. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from launch_pal.robot_arguments import CommonArgs


def generate_launch_description():

    robot_model = DeclareLaunchArgument(
        "robot_model", default_value="full_v2", description="Gazebo model name"
    )
    talos_entity = Node(
        package="gazebo_ros",
        executable="spawn_entity.py",
        arguments=[
            "-topic",
            "robot_description",
            "-entity", LaunchConfiguration("robot_model"),
            "-x", LaunchConfiguration('x'),
            "-y", LaunchConfiguration('y'),
            "-z", LaunchConfiguration('z'),
            "-R", LaunchConfiguration('roll'),
            "-P", LaunchConfiguration('pitch'),
            "-Y", LaunchConfiguration('yaw'),
        ],
        output="screen",
    )

    # @TODO: head_type node image_proc
    # @TODO: load PID gains? used in gazebo_ros_control fork
    # @TODO: load talos_pal_hardware_gazebo

    # Create the launch description and populate
    ld = LaunchDescription()

    ld.add_action(robot_model)
    ld.add_action(CommonArgs.x)
    ld.add_action(CommonArgs.y)
    ld.add_action(CommonArgs.z)
    ld.add_action(CommonArgs.roll)
    ld.add_action(CommonArgs.pitch)
    ld.add_action(CommonArgs.yaw)
    ld.add_action(talos_entity)

    return ld
