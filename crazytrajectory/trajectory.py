import zmq
from threading import Thread
from scipy import interpolate
from numpy import linspace

COPTER_ID = 1
LZ_ID = 2
ABOUT_TRHESHOLD = 0.1
HEIGHT = 0.5
SET_POINTS = 10


class CrazyTrajectory(Thread):

    def __init__(self):
        Thread.__init__(self)

        self.context = context = zmq.Context()
        self.camera_con = context.socket(zmq.PULL)
        self.camera_con.connect('tcp://127.0.0.1:7777')

        self.controller_con = context.socket(zmq.PUSH)
        self.controller_con.bind('tcp://*:5124')
        self.copter_pos = None
        self.lz_pos = None

    def run(self):
        while not self.copter_pos or not self.lz_pos:
            data = self.camera_con.recv_json()
            if 'id' not in data:
                print('Data is missing "id": %s' % data)
            elif data['id'] == COPTER_ID:
                self.copter_pos = data
            elif data['id'] == LZ_ID:
                self.lz_pos = data
            else:
                print('Invalid id')

        curve = self._generate_trajectory_curve()
        self.next_pos = next(curve)

        while not self._is_at_lz():
            data = self.camera_con.recv_json()
            if data['id'] == COPTER_ID:
                self.copter_pos = data
            else:
                continue
            if self._is_at_pos(self.copter_pos, self.next_pos):
                self.next_pos = next(curve, self.lz_pos)
                self.controller_con.send_json({'set-points': self.next_pos})

        print('Trajectory completed!')

    def _generate_trajectory_curve(self):
        """
        Calculates a curve between the current position and the target.
        """
        start = self.copter_pos
        end = self.lz_pos
        mid = {'x': (start['x'] + end['x'])/2,
               'y': (start['y'] + end['y'])/2,
               'z': max(start['z'], end['z']) + HEIGHT}

        x = [start['x'], mid['x'], end['x']]
        y = [start['y'], mid['y'], end['y']]
        z = [start['z'], mid['z'], end['z']]

        (tck, u) = interpolate.splprep([x, y, z], k=2)
        t = linspace(0, 1, SET_POINTS)
        points = interpolate.splev(t, tck)

        for i in range(SET_POINTS):
            x = points[0][i]
            y = points[1][i]
            z = points[2][i]
            yield {'x': x, 'y': y, 'z': z}

    def _aboutEquals(self, a, b):
        return abs(a - b) < ABOUT_TRHESHOLD

    def _is_at_pos(self, p1, p2):
        return (self._aboutEquals(p1['x'], p2['x']) and
                self._aboutEquals(p1['y'], p2['y']) and
                self._aboutEquals(p1['z'], p2['z']))

    def _is_at_lz(self):
        return self._is_at_pos(self.copter_pos, self.lz_pos)

    def stop(self):
        self.running = False
