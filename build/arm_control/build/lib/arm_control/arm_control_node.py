import rclpy
from rclpy import Node
from sensor_msgs import Joy

class ArmControl(Node):
    
    def __init__(self):
        super().__init__("armControl_node")
        self.subcription = self.create_subscription(msg_type=Joy,topic="joystick_node",qos_profile=10,callback = self.armControlCallback)

    def armControlCallback(self,data):
        self.get_logger.info('Buttons and axes recieved')
        self.buttonArray = data.buttons
        self.axesArray = data.axes

    def getButtonArray(self):
        return self.buttonArray

    def getAxesArray(self):
        return self.axesArray

def main(args=None):
    rclpy.init(args=args)

    armControlNode = ArmControl()

    rclpy.spin(armControlNode)
    armControlNode.destroy_node()
    rclpy.shutdown()

