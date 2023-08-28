import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription

from launch import LaunchDescription
from ament_index_python.packages import get_package_share_directory
from launch_ros.actions import Node


def generate_launch_description():
    pkg_path = get_package_share_directory("urdf_robot")

    urdf = os.path.join(pkg_path, "urdf", "robot.urdf")

    with open(urdf, "r") as infp:
        robot_desc = infp.read()

    return LaunchDescription(
        [
            Node(
                package="robot_state_publisher",
                executable="robot_state_publisher",
                name="robot_state_publisher",
                output="both",
                parameters=[
                    {"use_sim_time": True},
                    {"robot_description": robot_desc},
                ],
            ),
            Node(
                package="joint_state_publisher_gui",
                executable="joint_state_publisher_gui",
            ),
        ]
    )
