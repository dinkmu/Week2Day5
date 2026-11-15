# Healthy Breakfast Ideas with LangChain

A small Python assignment that uses LangChain's `ChatOpenAI` to ask an OpenAI chat model for exactly five healthy breakfast ideas.

## Project Structure

```text
breakfast/
├── breakfast.py
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

> Create your own `.env` locally from `.env.example`. Never commit your real `.env` file or API key to GitHub.

## Setup

### Windows PowerShell

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
Copy-Item .env.example .env
```

### macOS / Linux

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

Edit `.env` and replace the placeholder with your OpenAI API key:

```env
OPENAI_API_KEY=your-openai-api-key-here
```

## Run

```bash
python breakfast.py
```

The program prints only the generated text because `llm.invoke()` returns a LangChain message object and the script uses:

```python
reply = llm.invoke(prompt)
print(reply.content)
```

instead of:

```python
print(reply)
```

## Expected Format

```text
1. Breakfast idea
2. Breakfast idea
3. Breakfast idea
4. Breakfast idea
5. Breakfast idea
```

The exact ideas can vary between runs.

## Run It Twice

```bash
python breakfast.py
python breakfast.py
```

Compare both responses. This project uses `temperature=0.7`, so the model can produce different ideas or ordering between runs.

For more consistent model output, change:

```python
temperature=0.7
```

to:

```python
temperature=0
```

A lower temperature reduces randomness, but applications requiring exactly identical output should not rely on temperature alone.

## What Does "Healthy" Mean Here?

The prompt defines healthy breakfasts as including:

- A high-fiber carbohydrate
- A protein source
- Fruit or vegetables
- Limited heavily processed foods and excessive added sugar

This makes the request more specific than simply asking the model for "healthy breakfasts."

## Submission

Take a screenshot of the terminal after running:

```bash
python breakfast.py
```

The screenshot should show exactly five numbered breakfast ideas. Do not expose your OpenAI API key in the screenshot.
