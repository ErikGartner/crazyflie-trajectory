# crazyflie-trajectory
*Trajectory generation using for the Crazyflie*

It connects to the crazyflie AR solution using zmq to get postion and issue set-point commands.

## Usage
```python3 main.py```

## Installation
Below is the Mac guide.

1. Install python3: ```brew install python3```
2. Install libzmq: ```brew install libzmq```
3. Install dependencies using pip: ```python3 setup.py --develop```

## Tests
Unit tests exists in *test/*. Run them using *nose* using the command:
```nosetest```
in the root directory.
