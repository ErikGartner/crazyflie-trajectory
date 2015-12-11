import unittest
import zmq

from crazytrajectory.trajectory import CrazyTrajectory


class TestCrazyTrajectory(unittest.TestCase):

    def setUp(self):
        context = zmq.Context()
        self.mock_camera = context.socket(zmq.PUSH)
        self.mock_controller = context.socket(zmq.PULL)
        self.mock_camera.connect('tcp://127.0.0.1:7777')
        self.mock_controller.connect('tcp://127.0.0.1:5124')
        self.trajectory = CrazyTrajectory()

    def tearDown(self):
        self.mock_camera.close()
        self.mock_controller.close()

    def testAboutEquals(self):
        self.assertTrue(self.trajectory._aboutEquals(0, 0))
        self.assertTrue(self.trajectory._aboutEquals(0, 0.09))
        self.assertFalse(self.trajectory._aboutEquals(0, 0.1))

    def testIsAtPos(self):
        p1 = {'x': 0, 'y': 1, 'z': 2}
        p2 = {'x': -0.09, 'y': 1.09, 'z': 2.09}
        p3 = {'x': 0, 'y': 1, 'z': 3}
        self.assertTrue(self.trajectory._is_at_pos(p1, p2))
        self.assertFalse(self.trajectory._is_at_pos(p1, p3))

    def testGenerateTrajectory(self):
        self.trajectory.copter_pos = {'x': 0, 'y': 0, 'z': 0}
        self.trajectory.lz_pos = {'x': 1, 'y': 10, 'z': 0}

        curve = self.trajectory._generate_trajectory_curve()
        step = next(curve)

        # test start point
        actual_step = self.trajectory.copter_pos
        self.assertDictEqual(actual_step, step, 'Incorrect trajectory step')
        for i in range(4):
            step = next(curve)

        # test mid point
        actual_step = {'x': 0.5, 'y': 5, 'z': 0.5}
        self.assertAlmostEqual(actual_step['x'], step['x'], delta=0.2)
        self.assertAlmostEqual(actual_step['y'], step['y'], delta=1)
        self.assertAlmostEqual(actual_step['z'], step['z'], delta=0.2)

        for i in range(5):
            step = next(curve)

        # test end point
        actual_step = self.trajectory.lz_pos
        self.assertDictEqual(actual_step, step, 'Incorrect trajectory step')

    def testRun(self):
        """
        self.trajectory.start()

        copter = {'id': COPTER_ID, 'x': 0, 'y': 0, 'z': 0}
        lz = {'id': LZ_ID, 'x': 1, 'y': 10, 'z': 0}

        self.mock_camera.send_json(copter)
        self.mock_camera.send_json(lz)

        step = self.mock_controller.recv_json()
        self.assertDictEqual(copter, step, 'Incorrect trajectory step')
        """
