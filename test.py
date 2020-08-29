import unittest
from converter import *

class TestOutputCorrect(unittest.TestCase):
    """
    Test that the returned list comp expression is in fact a correct conversion of the original loop.
    """

    def test_basic(self):
        """
        example_result = []
        for val in example_list:
            example_result.append(val + 2)
        """
        expected_result = 'example_result = [val + 2 for val in example_list]'
        actual_result = loop_to_list_comp('example_result = []\nfor val in example_list:\nexample_result.append(val + 2)'
                                          '\nif keyword in post]')

        self.assertEqual(expected_result, actual_result)


    def test_handles_single_if(self):
        """
        relevant_post_index = []
        for keyword in keywords:
            for post in posts:
                if keyword in post:
                    relevant_post_index.append(post)
        """
        expected_result = 'relevant_post_index = [post for keyword in keywords if len(keyword) > 2 for post in posts ' \
                          'if keyword in post]'
        actual_result = loop_to_list_comp('relevant_post_index = []\nfor keyword in keywords: if len(keyword) > 2: '
                                          'for post in posts:\nif keyword in post:\nrelevant_post_index.append(post)')

        self.assertEqual(expected_result, actual_result)


    def test_handles_list_at_top(self):
        """
        numbers = [1, 2, 3, 4, 5]
        doubled_nums = []
        for n in numbers:
            doubled_nums.append(n * 2)
        """
        expected_result = 'doubled_nums = [n * 2 for n in numbers]'
        actual_result = loop_to_list_comp('numbers = [1, 2, 3, 4, 5]\ndoubled_nums = []\nfor n in numbers:\n'
                                          'doubled_nums.append(n * 2)')

        self.assertEqual(expected_result, actual_result)


    def test_handles_multiple_fors(self):
        """
        relevant_post_index = []
        for keyword in keywords:
            for post in posts:
                if keyword in post:
                    relevant_post_index.append(post)
        """
        expected_result = 'relevant_post_index = [post for keyword in keywords for post in posts if keyword in post]'
        actual_result = loop_to_list_comp('relevant_post_index = []\nfor keyword in keywords:\nfor post in posts:\n'
                                          'if keyword in post:\nrelevant_post_index.append(post)')

        self.assertEqual(expected_result, actual_result)


    def test_handles_multiple_fors_and_ifs(self):
        """
        relevant_post_index = []
        for keyword in keywords:
            if len(keyword) > 2:
                for post in posts:
                    if keyword in post:
                        relevant_post_index.append(post)
        """
        expected_result = 'relevant_post_index = [post for keyword in keywords if len(keyword) > 2 for post in ' \
                          'posts if keyword in post]'
        actual_result = loop_to_list_comp('relevant_post_index = []\nfor keyword in keywords:\nif len(keyword) > '
                                          '2:\nfor post in posts:\nif keyword in post:\n'
                                          'relevant_post_index.append(post)')

        self.assertEqual(expected_result, actual_result)


    def test_handles_multiple_lists_fors_ifs(self):
        """
        a = []
        b = []
        c = []
        for keyword in keywords:
            if len(keyword) > 2:
                a.append(posts)
                for p in posts:
                    b.append(p)
                    if keyword in posts:
                        c.append(keyword)
        """
        expected_result = 'a, b, c = [posts for keyword in keywords if len(keyword) > 2], ' \
                          '[p for keyword in keywords if len(keyword) > 2 for p in posts], ' \
                          '[keyword for keyword in keywords if len(keyword) > 2 for p in posts if keyword in posts]'
        actual_result = loop_to_list_comp('a = []\nb = []\nc = []\nfor keyword in keywords:\nif len(keyword) > 2:\na.append(posts)\n'
                                          'for p in posts:\nb.append(p)\nif keyword in posts:\nc.append(keyword)')
        self.assertEqual(expected_result, actual_result)

if __name__ == '__main__':
    unittest.main()




