cmake_minimum_required(VERSION 3.8)
project(turtle_msgs)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# Encontre as dependências
find_package(ament_cmake REQUIRED)
find_package(rosidl_default_generators REQUIRED)

# Gere interfaces de mensagens e serviços
rosidl_generate_interfaces(${PROJECT_NAME}
  "msg/Turtle.msg"
  "msg/TurtleArray.msg"
)

ament_export_dependencies(rosidl_default_runtime)
ament_package()

