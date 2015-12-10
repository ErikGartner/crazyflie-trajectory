# crazyflie-trajectory
*Trajectory generation using for the Crazyflie*

[ ![Codeship Status for ErikGartner/crazyflie-trajectory](https://codeship.com/projects/7f48d0d0-8174-0133-e84e-7e8a3f8de088/status?branch=master)](https://codeship.com/projects/121231)

A trajectory generator that connects to the CrazyFlie AR solution by Bitcraze using zmq to get postion and issue set-point commands.

## Usage
```python3 ./main.py```

## Installation
Below is the Mac guide.

1. Install python3: ```brew install python3```
2. Install libzmq: ```brew install libzmq```
3. Install dependencies using pip: ```python3 ./setup.py develop```

## Tests
Unit tests exists in *test/*. Run them using *nose* using the command:
```
nosetest
```
in the root directory.
