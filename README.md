# pa_ros2_pf3400
This is documentation for the custom ROS2 package put together by IndustrialNext for the PF3400 robot. \
This package uses original ROS1 code and allows it to be installed as ROS2 package.

## Install:
In order to install this package only into your workspace do all the required steps shown below.

Create workspace:
```
mkdir -p ~/pf3400_ws/src
```

Place code inside the `/src` folder:
```
git clone git@github.com:industrialnext/tcs-ros-rviz.git -b industrialnext
```

Source your ROS2 distro (skip if .bashrc does this by default):
```
source /opt/ros/<distro name>/setup.bash
```

Resolve dependecies:
```
rosdep install --ignore-src --from-paths src -y -r
```

Install package:
```
colcon build --symlink-install
```

## Run package:
Open your workspace;
```
cd ~/pf3400_ws
```

Source installed package:
```
source ./install/setup.bash
```

Run demo (as of Feb 12, 2024 it is not working, needs to be updated to ROS2 code):
ros2 launch pf3400_motion_control_example bridge.launch ip:="192.168.0.1"
