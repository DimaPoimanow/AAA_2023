import unittest
from count_vectorizer import CountVectorizer


class Test_CountVectorizer(unittest.TestCase):
    def setUp(self):
        """Initialize class for future testing"""
        self.count_vectorizer = CountVectorizer()

    def test_case_1(self):
        data = [
            "Crock Pot Pasta Never boil pasta again",
            "Pasta Pomodoro Fresh ingredients Parmesan to taste",
        ]
        count_matrix = self.count_vectorizer.fit_transform(data)
        true_matrix = [
            [1, 1, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1],
        ]
        assert count_matrix == true_matrix, "Wrong answer"
        assert isinstance(count_matrix, type(true_matrix))
        feature_names = self.count_vectorizer.get_feature_names()
        true_feature_names = [
            "crock",
            "pot",
            "pasta",
            "never",
            "boil",
            "again",
            "pomodoro",
            "fresh",
            "ingredients",
            "parmesan",
            "to",
            "taste",
        ]
        assert feature_names == true_feature_names, "Wrong feature names"
        assert isinstance(feature_names, type(true_feature_names))

    def test_case_2(self):
        data = [
            "x " * 10 + "x",
            "y " * 10 + "y",
            "z " * 10 + "z",
        ]
        count_matrix = self.count_vectorizer.fit_transform(data)
        true_matrix = [
            [11, 0, 0],
            [0, 11, 0],
            [0, 0, 11],
        ]
        assert count_matrix == true_matrix, "Wrong answer"
        assert isinstance(count_matrix, type(true_matrix))
        feature_names = self.count_vectorizer.get_feature_names()
        true_feature_names = ["x", "y", "z"]
        assert feature_names == true_feature_names, "Wrong feature names"
        assert isinstance(feature_names, type(true_feature_names))


if __name__ == "__main__":
    unittest.main()
