from launch import launch_description
from launch_ros.actions import Node


def generate_launch_description():
    ld = launch_description()

    talker_node = Node(
        package="demo_nodes.cpp",
        executable="talker"
    )
    listener_node = Node(
        package="demo_nodes.py",
        executable="listener"
    )

    ld.add_action(talker_node)
    ld.add_action(listener_node)

    return ld

