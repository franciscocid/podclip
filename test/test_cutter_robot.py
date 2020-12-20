from unittest import TestCase, mock
from podclip.robots import CutterRobot
from podclip.robot import RobotState
from os.path import join
import logging

class TestCutterRobot(TestCase):

  def setUp(self):
    logging.basicConfig(level=logging.INFO, format='%(message)s')

  def test_subclip_called_with_right_parameters(self):
    prev_state = RobotState(
      video_path=join('test', 'resources', 'videos', 'a deriva 6 - arthur petry.mp4'),
      clip_start=0,
      clip_end=10,
      clip_path=join('test', 'resources', 'videos', 'clip0.mp4'),
    )
    with mock.patch('podclip.robots.cutter_robot.ffmpeg_extract_subclip') as m:
      state = CutterRobot().run(prev_state)
      m.assert_called_once_with(prev_state.video_path, 0, 10, targetname=prev_state.clip_path)