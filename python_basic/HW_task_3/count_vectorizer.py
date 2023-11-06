from typing import List


class CountVectorizer:
    """
    Convert a collection of text documents to a matrix of token counts.
    """

    def __init__(self):
        self.feature_names = []

    def fit_transform(self, documents: List[str]) -> List[List[int]]:
        """
        Learn the vocabulary dictionary and return document-term matrix.

        Parameters
        ----------
        documents : list
            A list of documents with length n_samples.

        Returns
        -------
        X : array of shape (n_samples, n_features)
            Document-term matrix.
        """
        # Fit from documents
        self.feature_names = []
        for document in documents:
            words = document.lower().split(" ")
            for word in words:
                if word not in self.feature_names:
                    self.feature_names.append(word)

        # Transform documents
        X = []
        for document in documents:
            words = document.lower().split(" ")
            transformed_document = [0 for _ in range(len(self.feature_names))]
            for word in words:
                word_idx = self.feature_names.index(word)
                transformed_document[word_idx] += 1
            X.append(transformed_document)
        return X

    def get_feature_names(self) -> List[str]:
        """Get output feature names for transformation."""
        return self.feature_names
