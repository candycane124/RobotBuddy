# Robot Buddy
A GPS Buddy Prototype for SE 101.

## Overview
The GPS Buddy is an automated robot that physically leads its users to their desired destination around campus using an optimized route through a breadth-first search sorting algorithm. Our prototype goal was to make a self-driving Raspberry Pi robot that follows a path on a predetermined grid that emulates the campus.

## HARDWARE
Build Process:
- Assembled the robot parts: secured the motors, the power bank, battery holder, and the ball caster onto the chassis
- Soldered wires: starting with the motors, two wires were soldered onto each of their two ends; next, the motors were connected to the motor control board and the battery holder was connected to the motor control board.
- Connected Raspberry Pi Zero W: the GPIO ports of the Raspberry Pi Zero W were connected to the motor controller board and a micro USB to micro HDMI wire connected the Raspberry Pi to the power bank.

The robot’s three wheels -- two of which are powered by motors -- allow for the GPS Buddy to turn in place, move forward, and move backward, depending on the input provided to each motor.

<img width="500" alt="GPS_buddy" src="https://github.com/candycane124/GridBot/assets/93748376/439a307e-4768-42c8-af16-21a0429bcd5f">
<img width="500" alt="GPS_build" src="https://github.com/candycane124/GridBot/assets/93748376/e966c73b-eb33-4051-b138-cb677e5dfe0a">

## SOFTWARE
A microSD card with Raspberry Pi OS was placed in the Raspberry Pi Zero W and connected to the wifi server after its MAC address was whitelisted. Then, we were able to SSH or connect through a VNC to operate the RPi remotely using its IP address. Additionally, we also designed a program that visualizes the robot’s movement and pathfinding on a grid using Python’s Turtle library. 

<img width="500" alt="GPS_turtle" src="https://github.com/candycane124/GridBot/assets/93748376/12d81472-4465-4230-b1e7-e0a892d76c78">

Specifically, for the robot to calculate the shortest path toward its target destination, we implemented a breadth-first search algorithm through the BFS_robot() function and a predetermined grid to imitate the school’s campus using a 2D array. The user can input starting coordinates and the coordinates of its desired destination as many times in a row as they desire through the console.

## Team
Angela Huang, Jahnavi Malhotra, Laavanya Thiagalingam, Gloria Wang, Alexia Himelfarb
