# crazyflie-trajectory
*Trajectory generation using for the Crazyflie*

[ ![Codeship Status for ErikGartner/crazyflie-trajectory](https://codeship.com/projects/7f48d0d0-8174-0133-e84e-7e8a3f8de088/status?branch=master)](https://codeship.com/projects/121231)
[![Code Climate](https://codeclimate.com/github/ErikGartner/crazyflie-trajectory/badges/gpa.svg)](https://codeclimate.com/github/ErikGartner/crazyflie-trajectory)

*A trajectory generator that connects to the CrazyFlie AR solution by Bitcraze using zmq to get postion and issue set-point commands.*

The crazytrajectory works by receiving position data from the AR detector and uses that to determine the start position of the crazyflie (carrying a marker) as well as the landing zone (another marker). It then generates a cubic spline curve between the two positions. It then sends set-points along that curve to the crazyflie-vision module that regulates and controls the actual crazyflie.

## Usage
```
./crazytrajectory.py
```

## Setup
To use the crazytrajectory you need to setup the Bitcraze control loop. A detailed guide can be found [here](https://wiki.bitcraze.io/doc:crazyflie:vision:setup?s[]=vision).

In short:

1. Setup client: https://github.com/bitcraze/crazyflie-clients-python
2. Setup controller & checkout webcam-ar branch: https://github.com/bitcraze/crazyflie-vision
3. Setup AR detector: https://github.com/AxelTLarsson/crazyflie-ar-detector
4. Setup the crazytrajectory, see installation below.
5. Print aruco markers as described in ar-detector repo.
6. Configure ZMQ ports.
7. Run all components as described in respective READMEs.

## Installation
Below is the Mac guide.

1. Install python3: ```brew install python3```
2. Install libzmq: ```brew install libzmq```
3. Install dependencies using pip: ```python3 ./setup.py develop```

## Tests
Unit tests exists in ```test/```. Run them using [nose](https://nose.readthedocs.org/en/latest/) using the command: ```python3 -m nose``` in the root directory.
