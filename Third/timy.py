#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import String
from beginner_tutorials.msg import TIMEPU
from datetime import datetime


def timy():
    pub = rospy.Publisher('timy', TIMEPU, queue_size=10)
    rospy.init_node('timy', anonymous=True)
    rate = rospy.Rate(1) # 10hz
    timo_msg = TIMEPU()
    while not rospy.is_shutdown():
	now = datetime.now()
   	timo_msg.hour = now.hour
	timo_msg.minute = now.minute
	timo_msg.second = now.second
        timo_msg.whole_time = now.strftime('%H: %M: %S')


	rospy.loginfo("-------")        
	rospy.loginfo("HOUR : %d",timo_msg.hour)
        rospy.loginfo("MINUTE : %d",timo_msg.minute)
        rospy.loginfo("SECOND : %d",timo_msg.second)
        rospy.loginfo("WHOLE_TIME : %s",timo_msg.whole_time)

        pub.publish(timo_msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        timy()
    except rospy.ROSInterruptException:
        pass
