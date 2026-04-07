from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def vectorize(texts):
    return TfidfVectorizer().fit_transform(texts).toarray()

def calculate_similarity(vectors, file_names):
    results = []

    for i in range(len(vectors)):
        for j in range(i + 1, len(vectors)):
            score = cosine_similarity([vectors[i], vectors[j]])[0][1]
            results.append((file_names[i], file_names[j], round(score, 3)))

    return results