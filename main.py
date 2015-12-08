#!/usr/bin/env python3
import zmq
from threading import Thread


class CrazyTrajectory(Thread):

    def __init__(self):
        Thread.__init__(self)

        context = zmq.Context()
        self.camera_con = context.socket(zmq.PULL)
        self.camera_con.connect('tcp://127.0.0.1:7777')

        self.controller_con = context.socket(zmq.PUSH)
        self.controller_con.connect('tcp://127.0.0.1:5124')
        print(dir(self.camera_con))

    def run(self):
        while True:
            data = self.camera_con.recv_json()

    def _update_trajectory_curve():
        """
        Calculates a curve between the current position and the target.
        """
        return

    def _get_target_pos(msg):
        return {'x': 0, 'y': 0, 'y': 0}

    def _get_current_pos(msg):
        return {'x': 0, 'y': 0, 'y': 0}

    def _is_at_pos(p1, p2):
        return False

trajectory = CrazyTrajectory()
trajectory.start()
