from sentence_transformers import SentenceTransformer


class SentenceModel:

    def __init__(self):

        print("Sentence Transformer yükleniyor...")

        self.model = SentenceTransformer(
            "sentence-transformers/all-MiniLM-L6-v2"
        )

        print("Sentence Transformer hazır.")