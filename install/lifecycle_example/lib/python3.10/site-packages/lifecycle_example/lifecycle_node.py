#!/usr/bin/env python3
import rclpy
from rclpy.lifecycle import LifecycleNode, LifecycleState, TransitionCallbackReturn
from example_interfaces.msg import Int64

class MyNode(LifecycleNode):
    def __init__(self):
        super().__init__("my_node")
        self.get_logger().info("IN constructor")
        self.pub = None
        self.timer = None

    def on_configure(self, state: LifecycleState):
        self.get_logger().info("IN on_configure")
        self.pub = self.create_lifecycle_publisher(Int64, "number", 10)
        self.timer = self.create_timer(1.0, self.publish_number)
        self.timer.cancel()
        return TransitionCallbackReturn.SUCCESS 
    
    def on_cleanup(self, state: LifecycleState):
        self.get_logger().info("IN on_cleanup")
        self.destroy_lifecycle_publisher(self.pub)
        self.destroy_timer(self.timer)
        return TransitionCallbackReturn.SUCCESS
        
    def on_activate(self, state: LifecycleState):
        self.get_logger().info("IN on_activate")
        self.timer.reset()
        return super().on_activate(state)
    
    def on_deactivate(self, state: LifecycleState):
        self.get_logger().info("IN on_deactivate")
        self.timer.cancel()
        return super().on_deactivate(state)
    
    def on_shutdown(self, state: LifecycleState):
        self.get_logger().info("IN on_shutdown")
        self.destroy_lifecycle_publisher(self.pub)
        self.destroy_timer(self.timer)
        return TransitionCallbackReturn.SUCCESS

    def publish_number(self):
        msg = Int64()
        msg.data = 5
        self.get_logger().info("Publish number")
        self.pub.publish(msg)
        

def main(args=None):
    rclpy.init(args=args)
    node = MyNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__=="__main__":
    main()