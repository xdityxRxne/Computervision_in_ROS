#!/usr/bin/env python

from __future__ import print_function
import roslib
import sys
import rospy
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

def main(args):

  bridge = CvBridge()
  try:

    rospy.init_node("tennis_ball_publisher") # creating node

    img_pub = rospy.Publisher("tennis_ball_image",Image)# image publisher

    vid_feed = cv2.VideoCapture("/home/aditya/catkin_ws/src/ros_essentials_cpp/src/topic03_perception/video/tennis-ball-video.mp4")

    rate = rospy.Rate(30)

    while True:

        ret, frame = vid_feed.read()

        img_2_msg = bridge.cv2_to_imgmsg(frame, "bgr8")

        img_pub.publish(img_2_msg)

        rate.sleep()
        if cv2.waitKey(1) & 0xFF == ord('q'):
           break
    vid_feed.release()
  except CvBridgeError as e:
     print(e)

if __name__ == '__main__':
    try:
       main(sys.argv)
    except KeyboardInterrupt:
       print("Shutting down")