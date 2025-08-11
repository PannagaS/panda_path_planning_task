from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare
from launch.substitutions import PathJoinSubstitution


def generate_launch_description():
    panda_demo_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            PathJoinSubstitution([
                FindPackageShare('moveit_resources_panda_moveit_config'),
                'launch', 'demo.launch.py'
            ])
        )
    )
    demo_node = Node(
        package='panda_path_planning',
        executable='planning_scene_demo',
        output='screen'
    )

    obstacle_node = Node(
        package='panda_path_planning',
        executable='obstacle_publisher',
        output='screen'
    )


    return LaunchDescription([panda_demo_launch, demo_node, obstacle_node])
