import openai

openai.api_key = 'your-api-key-here'

def summarize_text(text):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that summarizes text."},
            {"role": "user", "content": f"Summarize the following text in a few sentences: {text}"}
        ]
    )
    return response.choices[0].message['content']

# Example usage
cluster_summaries = []
for cluster_id in set(cluster_assignments):
    cluster_text = " ".join([chunks[i] for i, c in enumerate(cluster_assignments) if c == cluster_id])
    summary = summarize_text(cluster_text)
    cluster_summaries.append(summary)

print(f"Created {len(cluster_summaries)} cluster summaries")