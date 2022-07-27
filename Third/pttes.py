#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import String
from beginner_tutorials.msg import Num


def pttes():
    pub = rospy.Publisher('chatter', Num, queue_size=10)
    rospy.init_node('pttes', anonymous=True)
    rate = rospy.Rate(0.0001) # 10hz
    num_msg = Num()
    while not rospy.is_shutdown():
	Num.first_name = "Lee"
	Num.last_name = "TaeHyeong"
	Num.age = 24
	Num.score = 100
	pub.publish(num_msg) 
       
	name_str = "good guy %s" % rospy.get_time()
        rospy.loginfo("-------------")
        rospy.loginfo("First_Name : %s",num_msg.first_name)
        rospy.loginfo("last_Name : %s",num_msg.last_name)
        rospy.loginfo("age : %d",num_msg.age)
        rospy.loginfo("score : %d",num_msg.score)

        pub.publish(num_msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        pttes()
    except rospy.ROSInterruptException:
        pass
