# Intercom-Network

This is a repository for an intercom network built for my school.
The goal for this project, was to build a small box to place in each class room within my school, to allow faculty to broadcast messages with ease. 

This system utilises over 30 raspberry pi's acting as hosts and slaves.

System overview
  - One Pi acts as the host, running a LAMP web server and a mysql server. 
		The web sever hosts the password protected admin page. 
		On this page faculy can:
		- Broadcast pre-recorded audio messages, 
		- Enable/Disable a indicator light which informs students if they can go outside for break (Weather dependig) this light is automatically controlled by
			an external pi with humidity sensor however this is a overwrite for it
		- Initate a school lockdown, this plays a siren sound, and alerts all students to enter lowdown prodecure
		

	- The rest of the pi's act as slaves.
add more text later
