# Cardboard Robot Wars

Similar to the competition created by [Columbia Gadget Works](http://www.columbiagadgetworks.org/wiki/index.php/Combat_Robots), this competition involves putting robots made out of cardboard head to head to find a victor.

## Instructions on Setting up a Working Cardboard Warrior
* Connect RaspberryPi via USB to a computer via the micro-USB port masked "USB"
  * follow instructions on the following link to set up raspberry pi: https://www.youtube.com/watch?v=xj3MPmJhAPU&vl=en-GB [1]
  * see the wpa_supplicant.conf file in the "Installation Files" directory of this repository for an example of something that works. Don't forget to change the network name and password. This should be the same on all of the Pi's.

* Loading & Running Software
  * use CyberDuck or other SFTP protocol (via cli or gui) to transfer the following files onto the pi:
    * cardboardFighter.py -> from Software directory
    * gpiotest.py -> from rpi-giotest-master (https://github.com/kgbplus/gpiotest [2]) -> this file is for manually debugging and watching the gpio pin outputs
  * N.B.: It's easy to just place all the files in the home directory so you can run things quickly
  * ssh into the rpi:
    * via WiFi: putty -> pi@192.168.xx.xx (you'll need to find the IP address - use nmap to help for this)
    * locally:  putty -> pi@raspberrypi.local
    * password = "raspberry"
  * to debug run the following command in shell first:
    * sudo python gpiotest.py
  * to play type:
    * python cardboardFighter.py
  
## Stuff to do
* Build robot
  * Build cardboard robot chassis
  * Build motor control board electronics
    * Follow instructions on: https://www.instructables.com/id/Controlling-a-Raspberry-Pi-RC-Car-With-a-Keyboard/ [3]
    * N.B.: BCM Pin numbering used (see: https://pinout.xyz/pinout/servo_pwm_pi_zero [4]). 
    * N.B.: Control Pins are different to instructables. Set to:
      * LED1 = 5
      * LED2 = 6
      * weaponPin = 18
      * mot1in1 = 22    -> input 1 to motor 1 at BCM Pin 22
      * mot1in2 = 23    -> input 2 to motor 1 at BCM Pin 23
      * mot2in1 = 24    -> input 1 to motor 2 at BCM Pin 24
      * mot2in2 = 25    -> input 2 to motor 2 at BCM Pin 25
* Test 
  * test cardboardFighter.py with physical electronics (already tested with GPIOTEST.PY pin monitor)
* Prep for comp
  * create skeleton code that allows them to fill in blanks from cardboardFighter.py
  * Design a competition arena (and create a cool name for it)
  * Create a set of competition and build rules
* If time exists implement a circular buffer for input handling and fill on interrupt to make things more responsive
* run comp

## Notes for future improvement
* Polling is bad - do things in an interrupt driven manner. It wasn't done this time as an artefact of previous examples from instructable example (see ref [3]).
* Get XBOX controllers working
* Rebase this to Arduino to get rid of asynchronies in PWM signals - or do this with an rPi with a manually created PWM so that processing time is synchronous with clock (python's GPIO libraries have inbuilt inconsistencies due to no-op implementations so your 80% duty cycle may not be exactly 80%).
