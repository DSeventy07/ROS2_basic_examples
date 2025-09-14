import os
from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():
    ld = LaunchDescription()

    config = os.path.join(
        get_package_share_directory("my_robot_bringup"),
        "config",
        "params.yaml"
    )

    my_node = Node(
        package="py_package_example",
        executable="py_node",
        name="py_test",
        namespace="ns1",
        parameters=[config]
    )


    """
    talker_node = Node(
        package="demo_nodes_cpp",
        executable="talker",
        name="my_talker_cpp",
        remappings= [
            ("chatter", "my_chatter")
        ],
        parameters=[
            {"param_name": "value"},
            {"param_2": 19}
        ]
    )
    listener_node = Node(
        package="demo_nodes_py",
        executable="listener",
        remappings=[
            ("chatter", "my_chatter")
        ]
    )

    ld.add_action(talker_node)
    ld.add_action(listener_node)
    """

    ld.add_action(my_node)
    return ld

