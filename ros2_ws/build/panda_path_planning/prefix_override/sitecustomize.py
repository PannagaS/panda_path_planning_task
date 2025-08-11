import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/pannaga/Documents/panda_path_planning_task/ros2_ws/install/panda_path_planning'
