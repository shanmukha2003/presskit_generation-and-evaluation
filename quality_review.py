from llama_cpp import Llama  # Load LLaMA model
import json
import re

# Load LLaMA model (Update your actual model path)
llm = Llama(model_path=r"C:\Users\91630\.cache\lm-studio\models\hugging-quants\Llama-3.2-1B-Instruct-Q8_0-GGUF\llama-3.2-1b-instruct-q8_0.gguf")

def split_text(text, max_tokens=450):
    """
    Splits text into chunks that fit within the model's token limit.
    """
    words = text.split()  # Split by words
    chunks, current_chunk = [], []

    for word in words:
        current_chunk.append(word)
        if len(current_chunk) >= max_tokens:  # Check token limit
            chunks.append(" ".join(current_chunk))
            current_chunk = []

    if current_chunk:  # Add any remaining text
        chunks.append(" ".join(current_chunk))

    return chunks

def summarize_chunk(chunk):
    """
    Uses AI to summarize each chunk before final evaluation.
    """
    prompt = f"""
    Summarize the key points of the following Press Kit section:

    **Section Content:**
    {chunk}

    Provide a brief summary that captures the main points in a concise manner.
    Ensure the response is within 100 tokens and maintains key information.
    """
    response = llm(prompt, max_tokens=100)
    return response["choices"][0]["text"].strip()

def evaluate_press_kit(press_kit_draft):
    """
    Uses an AI model to evaluate the full press kit by summarizing chunks first.
    """
    if not press_kit_draft.strip():
        return "Error: No content available to evaluate."

    # Step 1: Split long press kit into smaller chunks
    chunks = split_text(press_kit_draft, max_tokens=450)

    # Step 2: Summarize each chunk to fit within context window
    summarized_content = "\n\n".join(summarize_chunk(chunk) for chunk in chunks)

    # Step 3: Evaluate full summary (now within token limit)
    prompt = f"""
    You are an expert in content evaluation. Analyze the entire Press Kit summary and provide structured feedback.

    **Press Kit Summary:**
    {summarized_content}

    **Evaluation Criteria (Score out of 10):**
    1. Content Consistency
    2. Writing Style and Tone
    3. Layout and Structure
    4. SEO Optimization

    Provide your response in **strictly valid JSON format** like this:
    {{
        "Content Consistency": 9,
        "Writing Style and Tone": 8,
        "Layout and Structure": 7,
        "SEO Optimization": 6,
        "Overall Feedback": "The draft is well-structured but needs better SEO optimization."
    }}
    """
    response = llm(prompt, max_tokens=200)
    return sanitize_json_output(response["choices"][0]["text"])

def sanitize_json_output(raw_text):
    """
    Extracts and parses the first valid JSON object from AI output.
    """
    try:
        json_match = re.search(r"\{(?:[^{}]|(?:\{[^{}]*\}))*\}", raw_text, re.DOTALL)
        if not json_match:
            raise ValueError("No valid JSON found.")

        json_str = json_match.group(0).strip()
        parsed_json = json.loads(json_str)

        return parsed_json

    except (json.JSONDecodeError, ValueError) as e:
        print("\n❌ DEBUG: Raw AI Output (Parsing Failed) ❌\n", raw_text)
        return {"Error": f"Failed to parse AI response: {str(e)}"}
