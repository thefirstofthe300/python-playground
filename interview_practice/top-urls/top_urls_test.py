import top_urls
import unittest

class TestTopUrls(unittest.TestCase):

  def testGetHostname(self):
    tests = [
      ("https://test.youtube.com/hello-world/wazzup", "test.youtube.com"),
      ("https://play.google.com/music", "play.google.com"),
      ("ftp://google.com", "google.com"),
      ("http://danielseymour.info", "danielseymour.info")
    ]
    for test in tests:
      self.assertEqual(top_urls.GetHostname(test[0]), test[1])

  def testGetHostnameCountsForUrls(self):
    tests = [
        (
          ["ftp://maloy.com", "https://www.google.com", "http://google.com"],
          {"google.com": 1, "www.google.com": 1, "maloy.com": 1}
        ),
        (
          ["ftp://maloy.com", "https://www.google.com", "http://google.com", "http://youtube.com", "https://youtube.com/hello-world/testing"],
          {"youtube.com": 2, "google.com": 1, "www.google.com": 1, "maloy.com": 1}
        ),
        (
          ["ftp://maloy.com", "https://www.google.com", "http://google.com", "http://youtube.com", "https://youtube.com/hello-world/testing"],
          {"youtube.com": 2, "google.com": 1, "www.google.com": 1, "maloy.com": 1}
        ),
        (
          ["ftp://maloy.com", "https://www.google.com", "http://google.com", "http://youtube.com", "https://youtube.com/hello-world/testing"],
          {"youtube.com": 2, "google.com": 1, "www.google.com": 1, "maloy.com": 1}
        )
      ]

    for test in tests:
      self.assertTrue(top_urls.GetHostnameCountsForUrls(test[0]) == test[1])

  def testGetTopHostnames(self):
    tests = [
      (
        {"google.com": 10, "hello.world": 2, "daniel.com": 4, "youtube.com": 5, "play.google.com": 8, "thecw.com": 4, "justdoit.com": 8, "testing.com": 1, "gotcha.test": 11, "goner.com": 9, "just.done": 15},
        {"google.com": 10, "hello.world": 2, "daniel.com": 4, "youtube.com": 5, "play.google.com": 8, "thecw.com": 4, "justdoit.com": 8, "gotcha.test": 11, "goner.com": 9, "just.done": 15}
      )
    ]

    for test in tests:
      self.assertEqual(top_urls.GetTopHostnames(test[0]), test[1])

if __name__ == "__main__":
  unittest.main()