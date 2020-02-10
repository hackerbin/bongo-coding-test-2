import unittest

from problem5 import User, find_transaction


class TestProblem5(unittest.TestCase):
    def setUp(self):
        print('setUp :: prepare sample input')
        self.user_1 = User('user_1')
        self.user_2 = User('user_2')
        self.user_3 = User('user_3')
        self.user_4 = User('user_4')
        self.user_5 = User('user_5')
        self.inputs = [
            {'user': self.user_1, 'amount': 50, 'share_by': [self.user_1, self.user_2, self.user_3]},
            {'user': self.user_2, 'amount': 100, 'share_by': [self.user_1, self.user_3]},
        ]
        self.inputs_1 = [
            {'user': self.user_1, 'amount': 50, 'share_by': [self.user_1]},
        ]
        self.inputs_2 = [
            {'user': self.user_2, 'amount': 50, 'share_by': [self.user_1, self.user_2, self.user_3]}
        ]

    def tearDown(self):
        print('tearDown :: clear up junks')
        del self.user_1
        del self.user_2
        del self.user_3
        del self.user_4
        del self.user_5

    def test_find_transaction(self):
        print('test_find_transaction :: assertion test')
        self.assertEqual(find_transaction(self.inputs),
                         [
                             {'from': self.user_1, 'to': self.user_2, 'amount': 33.33333333333333},
                             {'from': self.user_3, 'to': self.user_1, 'amount': 16.666666666666668},
                             {'from': self.user_3, 'to': self.user_2, 'amount': 50.0}
                         ])
        self.assertEqual(find_transaction(self.inputs_1), [])
        self.assertEqual(find_transaction(self.inputs_2),
                         [
                             {'from': self.user_1, 'to': self.user_2, 'amount': 16.666666666666668},
                             {'from': self.user_3, 'to': self.user_2, 'amount': 16.666666666666668}
                         ])
        self.assertEqual(find_transaction([]), [])
        self.assertEqual(find_transaction({}), [])

        print('test_find_transaction :: key error test')
        with self.assertRaises(KeyError):
            find_transaction(
                [
                    {'amount': 50, 'share_by': [self.user_1, self.user_2, self.user_3]}
                ]
            )

            find_transaction(
                [
                    {'user': self.user_1, 'share_by': [self.user_1, self.user_2, self.user_3]}
                ]
            )


if __name__ == '__main__':
    unittest.main()
