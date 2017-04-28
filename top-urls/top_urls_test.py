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
        )
      ]

    for test in tests:
      self.assertTrue(top_urls.GetHostnameCountsForUrls(test[0]) == test[1])


if __name__ == "__main__":
  unittest.main()