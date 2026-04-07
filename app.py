import os
from utils import vectorize, calculate_similarity

def read_files(folder="samples"):
    files = [f for f in os.listdir(folder) if f.endswith(".txt")]
    texts = []

    for file in files:
        with open(os.path.join(folder, file), encoding="utf-8") as f:
            texts.append(f.read())

    return files, texts


def main():
    print("🔍 Plagiarism Checker\n")

    files, texts = read_files()

    if len(files) < 2:
        print("Need at least 2 files")
        return

    vectors = vectorize(texts)
    results = calculate_similarity(vectors, files)

    print("📊 Similarity Results:\n")
    for f1, f2, score in results:
        print(f"{f1} <--> {f2} : {score * 100:.2f}%")

if __name__ == "__main__":
    main()