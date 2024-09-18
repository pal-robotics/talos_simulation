^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Changelog for package talos_gazebo
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

2.0.0 (2024-09-18)
------------------
* Merge branch 'ros2-migration' into 'humble-devel'
  Ros2 migration
  See merge request robots/talos_simulation!18
* added default controllers to talos_gazebo launch
* reuse the launch args from launch_pal CommonArgs for talos_gazebo
* reuse the launch args from launch_pal CommonArgs
* Add robot model type as argument
* Remove metapkg. Create single package talos_gazebo
* Add the initial pose as arguments of the launch file.
* launch automatically the simulation
* add launch folder
* simulation with positions controllers
* fix version and delete depend from metapkg
* delete talos_cc_gazebo - talos_cc of the main pkg will be used
* migration talos_hardware_gazebo
* migration to ROS2 CMakeLists and package.xml - hardware_gazebo
* migration to ROS2 CMakeLists and package.xml - gazebo
* migration to ROS2 CMakeLists and package.xml - controller_conf
* migration to ROS2 CMakeLists and package.xml - metapkg
* Contributors: Adrià Roig, Maximilien Naveau, Sai Kishor Kothakota, ileniaperrella

0.2.3 (2022-04-20)
------------------
* Merge branch 'eye_hand_test_fix' into 'erbium-devel'
  added enable_crane argument to the launch file
  See merge request robots/talos_simulation!16
* added enable_crane argument to the launch file
* Contributors: Sai Kishor Kothakota, saikishor

0.2.2 (2020-11-13)
------------------
* Merge branch 'lidar_head' into 'erbium-devel'
  use image_proc only in case of default head_type
  See merge request robots/talos_simulation!15
* use image_proc only in case of default head_type
* Contributors: Sai Kishor Kothakota, victor

0.2.1 (2020-07-21)
------------------
* Merge branch 'talos_6' into 'erbium-devel'
  Set simulation arg to true for the bringup
  See merge request robots/talos_simulation!14
* Set simulation arg to true for the bringup
* Contributors: Adria Roig, sergi

0.2.0 (2020-01-10)
------------------
* Merge branch 'disable_gazebo_camera' into 'erbium-devel'
  added option to disable the gazebo camera plugin in simulation
  See merge request robots/talos_simulation!13
* added option to disable the gazebo camera plugin in simulation
* Change license to LGPL-3.0
* Contributors: Sai Kishor Kothakota, Victor Lopez

0.1.8 (2018-08-03)
------------------

0.1.7 (2018-08-02)
------------------

0.1.6 (2018-07-12)
------------------
* Merge branch 'as_extra_model_loading' into 'erbium-devel'
  Avoid multiple model loading, split sensor config files.
  See merge request robots/talos_simulation!9
* Avoid multiple model loading, split sensor config files.
* Contributors: alexandersherikov

0.1.5 (2018-07-11)
------------------
* Merge branch 'hardware_config' into 'erbium-devel'
  added hardware config for no arms
  See merge request robots/talos_simulation!7
* added hardware config for no arms
* Contributors: Hilario Tome

0.1.4 (2018-06-22)
------------------
* Add recording and extra_gazebo_args parameters
* Contributors: Victor Lopez

0.1.3 (2018-06-15)
------------------

0.1.2 (2018-06-15)
------------------

0.1.1 (2018-06-06)
------------------
* Add image_proc dependency
* Merge branch 'talos-gazebo-worlds' into 'erbium-devel'
  Use pal_gazebo_worlds
  See merge request robots/talos_simulation!4
* Use pal_gazebo_worlds
* Contributors: Hilario Tome, Victor Lopez

0.1.0 (2018-04-12)
------------------
* deleted changelogs
* 0.0.16
* updated changelogs
* deleted changelogs
* 0.0.15
* updated changelog
* fixed simulation launch
* Merge branch 'camera-fixes' into 'erbium-devel'
  Add image_proc nodes to emulate the real robot topics
  See merge request robots/talos_simulation!3
* Add image_proc nodes to emulate the real robot topics
* Add new models of stairs and a new world with stairs
* Contributors: Adrià Roig, Hilario Tome, Victor Lopez

0.0.14 (2016-11-15 23:11)
-------------------------
* Updated changelog
* Contributors: Hilario Tome

0.0.13 (2016-11-15 22:32)
-------------------------
* Updated changelog
* Added depends
* Merge branch 'dubnium-devel' of gitlab:robots/talos_simulation into dubnium-devel
* Contributors: Hilario Tome

0.0.12 (2016-11-15 13:21)
-------------------------
* Add changelog
* Removed no used models and worlds
* Contributors: Luca

0.0.11 (2016-11-14)
-------------------
* Update changelog
* Contributors: Victor Lopez

0.0.10 (2016-11-12)
-------------------
* Update changelog
* Contributors: Victor Lopez

0.0.9 (2016-11-11 11:47)
------------------------
* Add changelog
* Contributors: Luca

0.0.8 (2016-11-11 10:28)
------------------------
* Updated changelog
* Contributors: Hilario Tome

0.0.7 (2016-11-10 18:19)
------------------------
* Updated changelog
* Contributors: Hilario Tome

0.0.6 (2016-11-10 12:07)
------------------------
* Updated changelog
* Merge branch 'dubnium-devel' of gitlab:robots/talos_simulation into dubnium-devel
* Merge branch 'dubnium-devel' of gitlab:robots/talos_simulation into dubnium-devel
* modified talos bringu
* Modified bringup
* Contributors: Hilario Tome, Hillario Tome, Luca

0.0.5 (2016-10-31)
------------------
* Updated changelog
* Fixed pid gain names forgripper
* Contributors: Hilario Tome

0.0.4 (2016-10-14)
------------------
* Updated changelog
* Contributors: Hilario Tome

0.0.3 (2016-10-13 19:34)
------------------------
* Updated changelog
* Fixed install rule talos gazebo
* Contributors: Hilario Tome

0.0.2 (2016-10-13 19:05)
------------------------
* Updated changelog
* Changed talos world physics to match reem-c, added depends to talos gazebo
* Contributors: Hilario Tome

0.0.1 (2016-10-12)
------------------
* Added changelog
* added depends
* Clean up
* Changed empty world simulation params
* Added vrc worlds
* Merge branch 'master' of gitlab:robots/talos_simulation
* Added talos small office, seems to run much faster than empty world
* Fix initial pose to not bump up into the air
* Finished renaming
* Renamed tor to talos
* Contributors: Hilario Tome, Sam Pfeiffer
