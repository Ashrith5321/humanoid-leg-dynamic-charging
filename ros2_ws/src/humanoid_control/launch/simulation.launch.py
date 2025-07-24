from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package="controller_manager",
            executable="ros2_control_node",
            parameters=[
                {"robot_description": open(
                    "/home/ashed/projects/humanoid-leg-dynamic-charging/ros2_ws/src/humanoid_control/urdf/leg.urdf").read()},
                "/home/ashed/projects/humanoid-leg-dynamic-charging/ros2_ws/src/humanoid_control/config/controllers.yaml"
            ],
            output="screen"
        ),
        Node(
            package="controller_manager",
            executable="spawner",
            arguments=["joint_state_broadcaster"],
        ),
        Node(
            package="controller_manager",
            executable="spawner",
            arguments=["joint_trajectory_controller"],
        ),
    ])

