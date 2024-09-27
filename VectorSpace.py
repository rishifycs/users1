from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def get_user_input():
    # Get the number of documents
    num_docs = int(input("Enter the number of documents: "))
    
    # Collect the documents
    documents = []
    for i in range(num_docs):
        doc = input(f"Enter document {i + 1}: ")
        documents.append(doc)
    
    # Get the query
    query = input("Enter the query: ")
    
    return documents, query

def main():
    # Get user input
    documents, query = get_user_input()

    # Check if we have documents and a query
    if not documents or not query:
        print("Documents or query cannot be empty.")
        return

    # Transform Data
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(documents + [query])
    
    # Separate the query vector from the documents' vectors
    doc_vectors = tfidf_matrix[:-1]  # All but the last
    query_vector = tfidf_matrix[-1]  # The last one
    
    # Compute Similarity
    cosine_similarities = cosine_similarity(query_vector, doc_vectors).flatten()
    
    # Rank Documents
    document_scores = list(enumerate(cosine_similarities))
    document_scores.sort(key=lambda x: x[1], reverse=True)
    
    # Print the rankings and scores
    print("\nDocument Rankings and Scores:")
    for rank, (index, score) in enumerate(document_scores, start=1):
        print(f"Rank {rank}: Document {index + 1} (Score: {score:.4f})")

if __name__ == "__main__":
    main()
