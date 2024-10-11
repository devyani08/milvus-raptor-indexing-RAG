def answer_question(query, search_results):
    context = "\n".join([text for text, _, _ in search_results])
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that answers questions based on the given context."},
            {"role": "user", "content": f"Context: {context}\n\nQuestion: {query}\n\nAnswer:"}
        ]
    )
    return response.choices[0].message['content']

# Example usage
query = "What is the capital of France?"
search_results = hybrid_search(query, collection)
answer = answer_question(query, search_results)
print(f"Question: {query}")
print(f"Answer: {answer}")