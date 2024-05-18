from launch import LaunchDescription
from launch_ros.actions import Node
def generate_launch_description():
    ld = LaunchDescription()
    turtle_node = Node(
        package="turtlesim",
        executable="turtlesim_node"
    )
    turtle_spawner_node = Node(
        package="turtle_killer",
        executable="turtle_spawner",
        parameters=[
            {"spawn_frequency" : 2.0},
            {"turtle_name_prefix" : "my_turtle"}
                    ]
    )
    turtle_controller_node = Node(
        package="turtle_killer",
        executable="turtle_controller",
        parameters=[
            {"catch_closest_turtle_first_": True}
        ]
    )
    ld.add_action(turtle_node)
    ld.add_action(turtle_spawner_node)
    ld.add_action(turtle_controller_node)
    return ld