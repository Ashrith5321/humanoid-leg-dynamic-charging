#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

class MoveLegNode(Node):
    def __init__(self):
        super().__init__('move_leg')
        self.get_logger().info("Move leg node started.")

def main(args=None):
    rclpy.init(args=args)
    node = MoveLegNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
