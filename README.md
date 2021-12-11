# Xingyu's Interactive Device Design Lab Hub (Cornell Tech Fall 2021)

for [Interactive Device Design](https://github.com/FAR-Lab/Developing-and-Designing-Interactive-Devices/)

Please place links here to the README.md's for each of your labs here:

[Lab 1. Staging Interaction](Lab%201/)

[Lab 2. Interactive Prototyping: The Clock of Pi](Lab%202/)

[Lab 3. Chatterboxes](Lab%203/)

[Lab 4. Ph-UI!!!](Lab%204/)

[Lab 5. Observant Systems](Lab%205/)

[Lab 6. Little Interactions Everywhere](Lab%206/)

[Final Project](https://github.com/FAR-Lab/Developing-and-Designing-Interactive-Devices/blob/2021Fall/FinalProject.md)<!--[](Final%20Project/)-->

# Final Project

Using the tools and techniques you learned in this class, design, prototype and test an interactive device.

Project plan - November 22

Peer feedback on Project plans: November 24

Functional check-off - November 30 & December 2

Final Project Presentations - December 7

Write-up and documentation due - December 13

## Objective

The goal of this final project is for you to have a fully functioning and well-designed interactive device of your own design.
 
## Description
Your project is to design and build an interactive device to suit a specific application of your choosing, and test the interaction with people. 
## Deliverables

1. Project plan: Big idea, timeline, parts needed, fall-back plan.

2. Functioning project: The finished project should be a device, system, interface, etc. that people can interact with.

3. Documentation of design process
4. Archive of all code, design patterns, etc. used in the final design. (As with labs, the standard should be that the documentation would allow you to recreate your project if you woke up with amnesia.)
5. Video of someone using your project
6. Reflections on process (What have you learned or wish you knew at the start?)

7. Group work distribution questionnaire

## Change of Design

It is fine to change your project goals, but please resubmit the project plan for the new design when you do that.


## Teams

You can and are not required to work in teams. Be clear in documentation who contributed what. The total project contributions should reflect the number of people on the project.

## Examples

[Here is a list of good final projects from previous classes.](https://github.com/FAR-Lab/Developing-and-Designing-Interactive-Devices/wiki/Previous-Final-Projects)
This version of the class is very different, but it may be useful to see these.

## Final Design

![3d_printing](https://user-images.githubusercontent.com/14202464/145690801-21210ecf-cd0e-4859-8a46-73a895f59f05.png)

After experimenting with the transistor setup and not getting a lot of success with it, we spent some time rethinking how we could control the pumps via the raspberry using parts we already have access to. 

We knew that the micro servo motors we have could provide accurate but small range movement with its arms, so we decided to test the approach of connecting the wiring of the pumps by physically moving the connection with the help of a servo motor, basically using the servo motor as a controllable relay switch. 

Our small scale test with one motor and pump actually worked out quite well, so we settled on this approach and built our final wiring design.

### Actual Wiring

![3d_printing](https://user-images.githubusercontent.com/14202464/145690855-4bbb4827-2e37-4a5c-a734-6a6e81011fc4.jpg)

### Pumping Mechanism

<img src="https://user-images.githubusercontent.com/14202464/145690871-1eda0a2e-07bc-428e-bc37-e36305ee69c5.jpg" width="400">

We used a breadboard to wire our 3 pumps in parallel to a 12V battery pack. The pumps would draw liquids and dispense them easily using lengths of silicone pipes. There is a small height difference between the liquid container and the dispensing head, but after testing out the setup we found out that this did not affect the pumping rate.

### Control Mechanism

<img src="https://user-images.githubusercontent.com/14202464/145690930-fef09438-ddb9-476e-b42c-a1745b0a3a0a.jpg" width="400">

This is a closeup of the servo motor setup we used to control the pump. To limit the movement of the motor, we drilled small holes onto the backboard and used thin wires to secure the servo motors. When the raspberry pi sends a signal to the servo controller, the servo connected will move by a small amount (between 40 to 60 degrees depending on our tuning) to connect the pump wiring and activate it.

### 3-D Printing vs. Lego Prototype

| **3-D Printing Design** | **Lego Prototype** |
| --- | --- |
| <img src="https://user-images.githubusercontent.com/14202464/145690961-791d9b4a-84c7-42af-a009-64eeffcd4cdf.PNG" width="400"> | <img src="https://user-images.githubusercontent.com/14202464/145690951-34d8164d-0055-4c9c-a78d-940dba04f2f2.jpg" width="400"> |

An interesting tradeoff we made was to replace our designed 3-D printed dispenser parts with lego prototypes since the 3-D printers were fully occupied. The lego parts provided a similar design flexibility while being easily assembled and saved us a lot of time.
