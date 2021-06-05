import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16
import numpy as np


class CalculatorNode(Node):
    def __init__(self):
        super().__init__("Calculator")
        self.create_subscription(Int16, "countup", self.cb_sub, 10)
        self.publisher_ = self.create_publisher(Int16, "even", 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.cb_pub)
        self.n = 0

    def cb_sub(self, msg):
        self.get_logger().info("Listen: %d" % msg.data)
        self.n = msg.data

    def cb_pub(self):
        msg = Int16()
        msg.data = self.cal(self.n)
        self.publisher_.publish(msg)

    def cal(self, n):
        return int(np.multiply(n, 2))


def main(args=None):
    rclpy.init(args=args)
    calculator_node = CalculatorNode()
    rclpy.spin(calculator_node)
    calculator_node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
