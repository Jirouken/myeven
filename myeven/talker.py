import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16
import numpy as np


class TalkerNode(Node):

    def __init__(self):
        super().__init__("Talker")
        self.publisher_ = self.create_publisher(Int16, "countup", 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.cb)
        self.n = 0

    def cb(self):
        msg = Int16()
        msg.data = self.n
        self.publisher_.publish(msg)
        self.n = self.n + 1


def main(args=None):
    rclpy.init(args=args)
    talker_node = TalkerNode()
    rclpy.spin(talker_node)
    talker_node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
