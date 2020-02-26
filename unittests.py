import unittest

from similarity import image_similiarity_score, main


class TestSum(unittest.TestCase):
    def test_similarity_score(self):
        """
        Test similarity score
        """
        image1 = '/Users/ravi.he/Downloads/red-dahlia-flower-60597.jpg'
        image2 = '/Users/ravi.he/Downloads/red-dahlia-flower-60597.png'
        self.assertEqual(image_similiarity_score(image1, image2), 0)

    def test_not_correct_image_file_exception(self):
        image1 = '/Users/ravi.he/Downloads/atlassian_interview.txt'
        image2 = '/Users/ravi.he/Downloads/red-dahlia-flower-60597.png'
        # self.assertRaises(image_similiarity_score(image1, image2), FileNotFoundError)
        with self.assertRaises(IOError): image_similiarity_score(image1, image2)

    def test_file_not_found_exception(self):
        image1 = '/Users/ravi.he/Downloads/atlassian_interview.tx'
        image2 = '/Users/ravi.he/Downloads/red-dahlia-flower-60597.png'
        # self.assertRaises(image_similiarity_score(image1, image2), FileNotFoundError)
        with self.assertRaises(FileNotFoundError): image_similiarity_score(image1, image2)


if __name__ == '__main__':
    unittest.main()