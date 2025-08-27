import openai

def generate_response(user_input: str, results: dict, history: list = None) -> str:
    context = ""
    for doc, meta in zip(results['documents'][0], results['metadatas'][0]):
        context += f"Title: {meta['title']}\nSummary: {doc}\n\n"

    if not context.strip():
        return "❌ Sorry, I couldn't find any relevant book summaries."

    messages = [{"role": "system", "content": "You are a helpful book recommendation assistant."}]
    if history:
        messages.extend(history)

    messages.append({
        "role": "user",
        "content": f"{user_input}\n\nHere are book summaries:\n{context}"
    })

    response = openai.chat.completions.create(
        model="gpt-4.1-mini",
        messages=messages
    )

    return response.choices[0].message.content.strip()


def generate_response_from_db(user_input: str, db_results: dict, history: list = None) -> str:
    documents = db_results["documents"][0]
    metadatas = db_results["metadatas"][0]

    context = ""
    for doc, meta in zip(documents, metadatas):
        context += f"Title: {meta['title']}\nSummary: {doc}\n\n"

    if not context.strip():
        return "❌ No matching books found in the database."

    messages = [{"role": "system", "content": "You are a helpful AI librarian."}]
    if history:
        messages.extend(history)

    messages.append({
        "role": "user",
        "content": f"{user_input}\n\nHere are some book summaries:\n{context}"
    })

    response = openai.chat.completions.create(
        model="gpt-4.1-mini",
        messages=messages
    )

    return response.choices[0].message.content.strip()
