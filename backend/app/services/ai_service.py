import anthropic
import json
import pandas as pd

client = anthropic.Anthropic()


def analyze_structure(df: pd.DataFrame) -> dict:
    json_data = df.to_json(orient="records")
    prompt = f"""You are a data analysis expert. Analyze the following JSON data extracted from an Excel sheet and identify its tabular structure.

Your task:
1. Identify the real column headers (they may not be in the first row)
2. Identify any rows to skip at the beginning (titles, empty rows, metadata)
3. Identify how many rows to skip at the end (totals, summaries, footers)

Data:
{json_data}

Respond ONLY with a valid JSON object following this exact structure:
{{
    "headers": ["column1", "column2", "column3"],
    "skip_rows": [0, 1],
    "skip_footer": 1
}}

Rules:
- "headers" must be a list of strings with the real column names in order
- "skip_rows" must be a list of row indices to skip at the beginning (empty list if none)
- "skip_footer" must be an integer with the number of rows to skip at the end (0 if none)
- Do not include any explanation, markdown, or text outside the JSON
- If you cannot determine the structure, respond with an empty headers list"""

    try:
        response = client.messages.create(
            model="claude-sonnet-4-5",
            max_tokens=1000,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        raw_text = response.content[0].text
        print("RAW RESPONSE:", repr(raw_text))
        clean_text = raw_text.strip()
        if clean_text.startswith("```"):
            clean_text = clean_text.split("```")[1]
            if clean_text.startswith("json"):
                clean_text = clean_text[4:]
        clean_text = clean_text.strip()
        result = json.loads(clean_text)
        return result
    except Exception as e:
        print("ERROR:", str(e))
        raise Exception(f"AI analysis failed: {str(e)}")