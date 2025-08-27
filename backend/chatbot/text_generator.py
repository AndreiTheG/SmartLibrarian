import openai

def generate_response(user_input: str, results):
    context = ""
    for doc, meta in zip(results['documents'][0], results['metadatas'][0]):
        context += f"Title: {meta['title']}\nSummary: {doc}\n\n"

    if not context.strip():
        return "❌ Sorry, I couldn't find any relevant book summaries."

    prompt = f"""
You are a helpful AI librarian. ONLY recommend books from the list below.

The user asked: "{user_input}"

Here are book summaries that might help:
{context}

Based on this, recommend one or two books and explain why they are a good match.
Do not invent book titles.
"""

    completion = openai.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return completion.choices[0].message.content.strip()


def generate_response_from_db(user_input: str, db_results: list[dict]) -> str:
    context = ""
    for book in db_results:
        context += f"Title: {book['title']}\nSummary: {book['summary']}\n\n"

    if not context.strip():
        return "❌ No matching books found in the database."

    prompt = f"""
You are a helpful AI librarian.

The user asked: \"{user_input}\"

Here are some book summaries:
{context}

Please recommend one or two books and explain why.
"""

    completion = openai.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return completion.choices[0].message.content.strip()
