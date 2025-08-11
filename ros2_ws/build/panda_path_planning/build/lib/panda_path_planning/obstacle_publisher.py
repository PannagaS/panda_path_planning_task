import rclpy
from rclpy.node import Node
from moveit_msgs.msg import CollisionObject
from shape_msgs.msg import SolidPrimitive
from geometry_msgs.msg import Pose

class ObstaclePublisher(Node):
    def __init__(self):
        super().__init__('obstacle_publisher')
        self.publisher_ = self.create_publisher(CollisionObject, 'collision_object', 10)
        self.timer = self.create_timer(1.0, self.publish_obstacle)
        self.get_logger().info('Obstacle Publisher Node started.')

    def publish_obstacle(self):
        # Create a CollisionObject message
        collision_object = CollisionObject()
        collision_object.header.frame_id = "panda_link0"
        collision_object.id = "my_cube"
        
        # Create the cube shape
        box = SolidPrimitive()
        box.type = SolidPrimitive.BOX
        box.dimensions = [0.2, 0.2, 0.2]  # Adjust dimensions as needed
        
        # Create the cube's pose (position and orientation)
        box_pose = Pose()
        box_pose.position.x = 0.5  # Adjust position to be between start and goal
        box_pose.position.y = 0.0
        box_pose.position.z = 0.5
        box_pose.orientation.w = 1.0
        
        collision_object.primitives.append(box)
        collision_object.primitive_poses.append(box_pose)
        collision_object.operation = CollisionObject.ADD
        
        # Publish the message
        self.publisher_.publish(collision_object)
        self.get_logger().info('Published collision object: "my_cube"')
        
        # After publishing, you can destroy the timer if you only want to publish once
        # self.timer.cancel()

def main(args=None):
    rclpy.init(args=args)
    obstacle_publisher = ObstaclePublisher()
    rclpy.spin(obstacle_publisher)
    obstacle_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()