import math


class CountVectorizer:
    def __init__(self):
        self.feature_names = []

    def fit_transform(self, corpus):
        count_matrix = []
        for text in corpus:
            for word in text.split(" "):
                word = word.lower()
                if word not in self.feature_names:
                    self.feature_names.append(word)
        for text in corpus:
            text_vector = [0 for _ in range(len(self.feature_names))]
            for word in text.split(" "):
                text_vector[self.feature_names.index(word.lower())] += 1
            count_matrix.append(text_vector)
        return count_matrix

    def get_feature_names(self):
        return self.feature_names


def tf_transform(count_matrix):
    for j in range(len(count_matrix)):
        text_sum = sum(count_matrix[j])
        for i in range(len(count_matrix[j])):
            count_matrix[j][i] /= text_sum
    return count_matrix


def idf_transform(count_matrix):
    N = len(count_matrix)
    idf_vector = [0 for _ in range(len(count_matrix[0]))]
    for i in range(len(idf_vector)):
        for j in range(N):
            idf_vector[i] += int(count_matrix[j][i] > 0)

    for i in range(len(idf_vector)):
        idf_vector[i] = round(math.log((N + 1) / (idf_vector[i] + 1)) + 1, 3)

    return idf_vector


class TfidfTransformer:
    def fit_transform(self, count_matrix):
        tf_matrix = tf_transform(count_matrix)
        idf_vector = idf_transform(count_matrix)
        for i in range(len(tf_matrix)):
            for j in range(len(tf_matrix[i])):
                tf_matrix[i][j] *= idf_vector[j]
        return tf_matrix


class TfidfVectorizer(CountVectorizer):
    def __init__(self):
        super().__init__()
        self.tfidftransformer = TfidfTransformer()

    def fit_transform(self, corpus):
        count_matrix = super().fit_transform(corpus)
        return self.tfidftransformer.fit_transform(count_matrix)
