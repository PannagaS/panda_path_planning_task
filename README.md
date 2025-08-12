# Obstacle-Aware Motion Planning for a Panda Arm 

## Objective
This repository contains a ROS2 package for obstacle aware path planning for the Franka Emika Panda robot, using ROS2, Rviz2, and MoveIt2 for experiments.



## Tasks:
- Use a common robotic arm model (e.g., Panda or UR5e).
- Set an initial and a target pose in RViz2.
- Add a static obstacle (e.g., a cube) directly between the initial and target positions.
- Use MoveIt2 to automatically plan a collision-free path.
- Visualize the planned path and the collision object in RViz2.

## Project Structure 
The repository structure is as show below. 
```
.
├── README.md
└── ros2_ws
    ├── build/
    ├── install/
    ├── log/
    └── src
        └── panda_path_planning
            ├── launch
            │   └── bringup_panda_demo.launch.py
            ├── package.xml
            ├── panda_path_planning
            │   ├── __init__.py
            │   ├── obstacle_publisher.py
            │   └── planning_scene_demo.py
            ├── resource
            │   └── panda_path_planning
            ├── setup.cfg
            ├── setup.py
            └── test/
                
```
## Project Prerequisites
This project requires ROS 2-humble and Moveit2 to perform all tasks. 
- Install [ROS 2 humble](https://docs.ros.org/en/humble/Installation/Ubuntu-Install-Debs.html) 
- Install [Moveit 2](https://moveit.picknik.ai/humble/doc/tutorials/getting_started/getting_started.html) 
    - For sanity check after installing Moveit, run `ros2 launch moveit2_tutorials demo.launch.py rviz_config:=panda_moveit_config_demo_empty.rviz` or follow [this](https://moveit.picknik.ai/humble/doc/tutorials/quickstart_in_rviz/quickstart_in_rviz_tutorial.html) link


## How to run this project? 
### Installation instructions & setup
Clone this repository
```
git clone git@github.com:PannagaS/panda_path_planning_task.git
```

Next, we source ROS 2. Open a new terminal and execute the following
```
source /opt/ros/humble/setup.bash
```

Navigate to `ros2_ws` inside project directory and exectute the following: 
```
cd panda_path_planning_task/ros2_ws
colcon build 
```

`colcon build` ensures everything is upto code by locally building `panda_path_planning` package. 

After **successfully** building the package, execute the following to source the worksapce 
```
source /install/setup.bash
```



### Running the demo
Launch the Panda planning demo by executing the following:
```
ros2 launch panda_path_planning bringup_panda_demo.launch.py
```

This launch file launches RViz and you should see a Franka Panda arm in its 'ready' state.
In addition, it will alos load the `MotionPlanning` plugin in RViz.

To add the `MotionPlanning` panel and setup the scene for planning, 
- Click on `Add` button on Displays tab, select `MotionPlanning`
- Setup obstacles by navigating to `Scene Objects` tab
    - Set the desired box dimensions and box poses
    - *check* the boxes and when prompted to choose the link to attach to, choose `panda_link0`
- Navigate to `Context` tab
    - By default, **OMPL** planning library will be selected by Moveit2
    - Choose any *planning method* (ex. `RRTkConfigDefault`, `RRTConnectkConfigDefault`, etc.)
- Navigate to `Planning` tab
    - Choose `panda_arm` as in **Planning Group**
    - Drag the sphere attached to the tcp link of the arm to the desired pose
    - **Plan** a collision-free motion by clicking on `Plan`
    - **Execute** the planned motion after a successful plan, by clicking `Execute` 
    - Alternatively, you can also use `Plan & Execute` button
 
### A note on the robot
The current implementation fetches `panda.urdf` from `~/ws_moveit/install/moveit_resources_panda_description/share/moveit_resources_panda_description/urdf` automatically when you run the launch file as described above. This is an efficient and simpler way to leverage MoveIt's `moveit_resources_panda_description` package. 


## Result
The following video shows a Panda arm planning a path while there are obstacles around it.


<p align="center">
    <img src="assets/Screencastfrom08-11-2025100428PM-ezgif.com-video-to-gif-converter.gif" alt="GIF"/>
</p>

#### You can also watch the video by [clicking here](https://youtu.be/Kpos1U_8N2A)