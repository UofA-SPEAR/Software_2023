import rclpy
from rclpy.node import Node
from control_msgs.msg import JointJog
from geometry_msgs.msg import TwistStamped
from sensor_msgs.msg import Joy

Joy_Topic = "/joy"
Twist_Topic = "/servo_node/delta_twist_cmds"
Joint_Topic = "/servo_node/delta_joint_cmds"
EEF_Frame_ID = ""
Base_Frame_ID = ""

LEFT_STICK_X = 0
LEFT_STICK_Y = 1
LEFT_TRIGGER = 2
RIGHT_STICK_X = 3
RIGHT_STICK_Y = 4
RIGHT_TRIGGER = 5
#D_PAD_X = 6 
D_PAD_X = 14 #No Clue
#D_PAD_Y = 7
D_PAD_Y = 15 #No Clue

A = 0
B = 1
#X = 2
X = 3
#Y = 3
Y = 4
LEFT_BUMPER = 4
RIGHT_BUMPER = 5,
CHANGE_VIEW = 6,
MENU = 7,
HOME = 8,
#LEFT_STICK_CLICK = 9
LEFT_STICK_CLICK = 11
#RIGHT_STICK_CLICK = 10
RIGHT_STICK_CLICK = 12


Axis_Default = {

    LEFT_TRIGGER : 1.0,
    RIGHT_TRIGGER : 1.0,
}

class JoyToServoPub(Node):
    def __init__(self):
        super().__init__('joy_to_twist_publisher')
        #self.frame_to_publish_ = BASE_FRAME_ID

        self.twist_pub = self.create_publisher(msg_type = TwistStamped, topic = Twist_Topic, 10)
        self.joint_pub = self.create_publisher(msg_type = JointJog, topic = Joy_Topic, 10)
        self.joy_sub = self.create_subscriber(msg_type = Joy, topic = Joy_Topic, 10, callback= JoystickMsg)
        
        timer_period = 0.1

        self.timer = self.create_timer(timer_period_sec = timer_period, callback = self.JoyMain)


    def JoyMain(self):

        if(ConvertJoyToCommand()):

            self.twist_msg = TwistStamped()
            self.twist_msg.header.stamp = self.get_clock().now().to_msg()
            self.twist_msg.header.frame_id = #Fill Out


        else:
            self.joint_msg = JointJog()
            self.joint_msg.header.stamp = self.get_clock().now().to_msg()
            self.joint_msg.header.frame_id = #Fill Out



        pass

    def ConvertJoyToCommand(self):



        if(A or B or X or Y or D_PAD_X or D_PAD_Y):


            self.joint_msg.joint_names.append("FILL OUT")
            self.joint_msg.velocities.append(JoystickMsg().axes[D_PAD_X])

            self.joint_msg.joint_names.append("FILL OUT")
            self.joint_msg.velocities.append(JoystickMsg().axes[D_PAD_X])


        pass
    
    def JoystickMsg(self, msg);

        return msg