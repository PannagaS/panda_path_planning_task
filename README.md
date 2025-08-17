# Obstacle-Aware Motion Planning for a Panda Arm 

## Objective
This repository contains a ROS2 package for obstacle aware path planning for the Franka Emika Panda robot, using ROS2, Rviz2, Isaac Sim (4.5) and MoveIt2 for experiments. 


### Note: The primary tasks remain the same (as mentioned in the `main` branch). This branch integrates IsaacSim with the existing ROS2 + MoveIt2 + Rviz2 pipeline.  

## Project Prerequisites
This project requires ROS 2-humble, Moveit2, and Isaac Sim to perform all tasks. 
- Install [Isaac Sim 4.5](https://docs.isaacsim.omniverse.nvidia.com/4.5.0/installation/download.html)
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

Navigate to `isaac_panda` workspace inside project directory and exectute the following: 
```
cd panda_path_planning_task/isaac_panda
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
ros2 launch perception_pipeline perception_pipeline_demo.launch.py
```


### *Follow the motion planning instructions for setting up the `Motion Planning` tab in RViz as described in `main` branch*
 
## Running the Isaac Sim part
Open IsaacSim and import `moveit_perception_panda.usd`. This usd contains ActionGraph and everything else pre-configured. Once everything is loaded, click `play`.

####  Plan a random valid motion and execute on `RViz` side, and you should see the arm mimic the motion in `Isaac Sim`.



## Result (Isaac Sim + MoveIt + ROS 2)
The following visual shows a Panda arm planning a path while there are obstacles around it in RViz.


<p align="center">
    <img src="assets/Screencastfrom08-11-2025100428PM-ezgif.com-video-to-gif-converter.gif" alt="GIF"/>
</p>

<!-- 
#### You can also watch the video by by clicking here - [demo 1](https://youtu.be/Kpos1U_8N2A), [demo 2](https://youtu.be/51J_CLuVIU4) -->



The following visual demonstrates successful integration of IsaacSim with ROS2 and MoveIt2. 


<p align="center">
    <img src="assets/Screencastfrom08-15-2025104716AM-ezgif.com-video-to-gif-converter.gif" alt="GIF"/>
</p>

<p align="center">
    <img src="assets/Screencastfrom08-16-2025101124PM-ezgif.com-speed.gif" alt="GIF"/>
</p>




