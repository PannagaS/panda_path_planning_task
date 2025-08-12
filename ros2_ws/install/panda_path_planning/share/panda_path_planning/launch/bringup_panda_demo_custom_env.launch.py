from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare

def generate_launch_description():
    panda_config_package = FindPackageShare('moveit_resources_panda_moveit_config')
    panda_description_package = FindPackageShare('moveit_resources_panda_description')

    # Load robot description
    robot_description_content = PathJoinSubstitution([
        panda_description_package, 'urdf', 'panda.urdf.xacro'
    ])

    # Load MoveIt's planning configuration
    moveit_config = {
        'robot_description': robot_description_content,
        'planning_scene_monitor': True,
        'planning_pipelines': {
            'ompl': {
                'planning_plugin': 'ompl_interface/OMPLPlanner',
                'request_adapters': 'default_planner_request_adapters/ResolveConstraintFrames default_planner_request_adapters/AddTimeOptimalParameterization',
                'start_state_max_bounds_error': 0.1,
            },
        },
    }

    # Robot State Publisher node
    robot_state_publisher_node = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher',
        output='screen',
        parameters=[moveit_config]
    )

    # MoveGroup node
    move_group_node = Node(
        package='moveit_ros_move_group',
        executable='move_group',
        output='screen',
        parameters=[moveit_config],
        arguments=['--ros-args', '--log-level', 'info']
    )

    # Your custom RViz node with the configuration file
    rviz_config_file = PathJoinSubstitution([
        FindPackageShare('panda_path_planning'),
        'config', 'panda_demo.rviz'
    ])
    rviz_node = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        output='screen',
        arguments=['-d', rviz_config_file]
    )

    return LaunchDescription([
        robot_state_publisher_node,
        move_group_node,
        rviz_node
    ])