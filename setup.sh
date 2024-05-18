#Build
echo Please, confirm you are in the directory 'Turtle_Killer_Project'
cd Turtle_Killer_Project
colcon build 
source install/setup.bash
echo "source ~/Turtle_Killer_Project/install/setup.bash" >> ~/.bashrc
