import types
import unittest

class TestLibrary(unittest.TestCase):

  def test_imports(self):
    try:
      import cv2
      import librosa
      import matplotlib
      import numpy
      import scipy
    except ImportError as e:
      self.fail(e)

  def test_opencv(self):
    try:
      import cv2
      self.assertTrue(type(cv2.SIFT) == types.BuiltinFunctionType)
    except AttributeError as e:
      self.fail(e)
    except ImportError as e:
      self.fail(e)

  def test_load_video(self):
    try:
      import numpy as np

      from datasets import CS4065_Dataset
      from cvtools import VideoReader

      video_file_path = CS4065_Dataset.get_testcases_data()['video']

      video_reader = VideoReader()
      video_reader.open(video_file_path)

      number_of_frames = video_reader.get_number_of_frames()
      video_width = video_reader.get_width()
      video_height = video_reader.get_height()

      self.assertTrue(video_reader.is_opened())
      self.assertTrue(video_width > 0)
      self.assertTrue(video_height > 0)
      self.assertTrue(number_of_frames > 0)
      self.assertTrue(video_reader.get_frame_rate() > 0)

      read_frames = 0
      for frame in video_reader.get_frames():
        frame_shape = np.shape(frame)
        self.assertEqual(read_frames, video_reader.get_current_frame_index())
        self.assertEqual(len(frame_shape), 3)
        self.assertEqual(frame_shape[0], video_height)
        self.assertEqual(frame_shape[1], video_width)
        read_frames += 1
      self.assertEqual(read_frames, number_of_frames)
    except ImportError as e:
      self.fail(e)
    except IOError as e:
      self.fail(e)

  def test_load_audio(self):
    try:
      from datasets import CS4065_Dataset
      audio_file_path = CS4065_Dataset.get_testcases_data()['audio']
      # TODO(alessio): check properties (e.g., stream length).
      raise NotImplementedError()
    except ImportError as e:
      self.fail(e)

  def test_load_image(self):
    try:
      import cv2
      import numpy as np
      from datasets import CS4065_Dataset
      image_file_path = CS4065_Dataset.get_testcases_data()['image']
      image = cv2.imread(image_file_path)
      self.assertTrue((512, 512, 3) == np.shape(image))
    except ImportError as e:
      self.fail(e)

if __name__ == "__main__":
  unittest.main()
