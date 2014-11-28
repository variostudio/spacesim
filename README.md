spacesim
========
The Solar system simulator.
PyGame 1.9.2 module is required

This version methos Kutta-Runge is added. Also automation asteroid generation is done. See the configuration asteroids.ini for details
The STEPS parameter in main.py is added for speedup the simulation

Command line is:
python3.3 main.py -f <configuratio>.ini

or 

python3.3 main.py -h

NOTE: you can choose precision of simulation by editing T value in flyobj.py

Keys used:
    q or ESC    = Exit
    p or SPACE  = Pause
    arrows = move view
