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

import os
from os import environ, pathsep

from ament_index_python.packages import get_package_prefix, get_package_share_directory
from launch import LaunchDescription
from launch.actions import (
    DeclareLaunchArgument,
    IncludeLaunchDescription,
    SetEnvironmentVariable,
)
from launch.conditions import IfCondition
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration

from launch_pal.include_utils import include_launch_py_description
from launch_pal.robot_arguments import CommonArgs


def get_model_paths(packages_names):
    model_paths = ""
    for package_name in packages_names:
        if model_paths != "":
            model_paths += pathsep

        package_path = get_package_prefix(package_name)
        model_path = os.path.join(package_path, "share")

        model_paths += model_path

    if 'GAZEBO_MODEL_PATH' in environ:
        model_paths += pathsep + environ['GAZEBO_MODEL_PATH']

    return model_paths


def get_resource_paths(packages_names):
    resource_paths = ""
    for package_name in packages_names:
        if resource_paths != "":
            resource_paths += pathsep

        package_path = get_package_prefix(package_name)
        resource_paths += package_path

    return resource_paths


def generate_launch_description():

    world_name: DeclareLaunchArgument = DeclareLaunchArgument(
        name='world_name',
        default_value='empty',
        description="Specify world name, will be converted to full path.")
    fixed_base_arg = DeclareLaunchArgument(
        "fixed_base", default_value="False", description="Fix the robot in the air."
    )
    enable_crane_arg = DeclareLaunchArgument(
        "enable_crane", default_value="False", description="Enable crane"
    )
    head_type_arg = DeclareLaunchArgument(
        "head_type", default_value="default", description="Head type"
    )
    disable_gazebo_camera_arg = DeclareLaunchArgument(
        "disable_gazebo_camera",
        default_value="False",
        description="Enable/Disable camera in simulation",
    )
    default_configuration_type_arg = DeclareLaunchArgument(
        "default_configuration_type",
        default_value="zeros",
        description="configuration of the robot",
    )
    robot_model_arg = DeclareLaunchArgument(
        "robot_model", default_value="full_v2", description="Robot model"
    )

    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            [
                os.path.join(
                    get_package_share_directory("pal_gazebo_worlds"), "launch"
                ),
                "/pal_gazebo.launch.py",
            ]
        ),
    )

    talos_spawn = include_launch_py_description(
        "talos_gazebo", ["launch", "talos_spawn.launch.py"],
        launch_arguments={
            'x': LaunchConfiguration('x'),
            'y': LaunchConfiguration('y'),
            'z': LaunchConfiguration('z'),
            'roll': LaunchConfiguration('roll'),
            'pitch': LaunchConfiguration('pitch'),
            'yaw': LaunchConfiguration('yaw'),
        }.items()
    )

    talos_bringup = include_launch_py_description(
        "talos_bringup", ["launch", "talos_bringup.launch.py"],
        launch_arguments={
            'fixed_base': LaunchConfiguration('fixed_base'),
            'sim_time': 'true',
            'enable_crane': LaunchConfiguration('enable_crane'),
            'head_type': LaunchConfiguration('head_type'),
            'disable_gazebo_camera': LaunchConfiguration('disable_gazebo_camera'),
            'default_configuration_type': LaunchConfiguration('default_configuration_type'),
        }.items()
    )

    # Default controller
    default_controller_launch = include_launch_py_description(
        "talos_controller_configuration",
        ["launch", "default_controllers.launch.py"])

    move_group = include_launch_py_description(
        "talos_moveit_config",
        ["launch", "move_group.launch.py"],
        launch_arguments={'use_sim_time': 'true'}.items(),
        condition=IfCondition(LaunchConfiguration("moveit")),
    )
    packages = ['talos_description']

    model_path = get_model_paths(packages)
    resource_path = get_resource_paths(packages)

    if "GAZEBO_MODEL_PATH" in environ:
        model_path += pathsep + environ["GAZEBO_MODEL_PATH"]

    if "GAZEBO_RESOURCE_PATH" in environ:
        resource_path += pathsep + environ["GAZEBO_RESOURCE_PATH"]

    # Create the launch description and populate
    ld = LaunchDescription()

    # Reuse arguments from launch_pal
    x = CommonArgs.x
    y = CommonArgs.y
    z = DeclareLaunchArgument(
        name="z",
        description="Z pose of the robot",
        default_value="1.1")
    roll = CommonArgs.roll
    pitch = CommonArgs.pitch
    yaw = CommonArgs.yaw
    moveit = CommonArgs.moveit

    ld.add_action(x)
    ld.add_action(y)
    ld.add_action(z)
    ld.add_action(roll)
    ld.add_action(pitch)
    ld.add_action(yaw)
    ld.add_action(world_name)
    ld.add_action(moveit)

    # Add the above actions to the launch description
    ld.add_action(SetEnvironmentVariable(
        "GAZEBO_MODEL_PATH", model_path))

    ld.add_action(fixed_base_arg)
    ld.add_action(enable_crane_arg)
    ld.add_action(head_type_arg)
    ld.add_action(disable_gazebo_camera_arg)
    ld.add_action(default_configuration_type_arg)
    ld.add_action(default_controller_launch)
    ld.add_action(robot_model_arg)

    ld.add_action(gazebo)
    ld.add_action(talos_spawn)
    ld.add_action(talos_bringup)

    ld.add_action(move_group)

    return ld
