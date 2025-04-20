# Leveraging AI for Programming

## Prompt Engineering
Craft clear, specific, and goal-oriented prompts to get useful responses from AI.

### Keys to Good Prompts
- **Specific**: Focus on one task at a time
- **Context**: Include what the code should do or what you've tried
- **Clear Request**: Ask for a function, example, explanation, etc.

### Example Task
Write a function that identifies the highest CO₂ reading.

- **Weak**: `"How do I find the highest value in my data?"`
- **Strong**: `"Can you write a Python function that takes a dictionary of CO₂ sensor readings (with timestamps as keys) and returns the timestamp with the highest value?"`

## Chunking Your Questions

Break a large task into small, focused parts. This helps:
- Get focused responses
- Understand each step
- Mimic how programming happens in practice

## Debugging with AI

AI can help you:
- Spot the issue
- Explain the error
- Suggest a fix
- Teach you why it failed

### Use Cases
- You got an error or traceback
- The code runs, but gives unexpected results
- You’re unsure how to fix it

### Prompt Examples
- “What does `TypeError: unsupported operand type` mean?”
- “Why is my average function returning `None`?”
- “Can you rewrite this loop so it doesn’t crash with an empty list?”

## Comments and Documentation

Clear documentation helps **other humans** and **AI tools** understand your code.

### Tools
- **Comments**: Inline `#` explanations for logic, assumptions, etc.
- **Docstrings**: Describe function purpose, parameters, returns, errors
- **README**: Explain what your script/project does, dependencies, how to run it

## Repetitive Structures

Use AI to scaffold the boring parts of common projects.

### Common Use Cases
- **Web Apps**: Flask or Streamlit apps scaffolded from one prompt
- **API Wrappers**: Turn REST calls into clean Python functions
- **Python Packages**: Full `setup.py`, module structure, and CLI logic

## When Not to Trust AI

AI is helpful — but it’s not perfect. Watch out for:

### 🏗️ Domain Knowledge
- AI is a generalist — you are the expert
- _Ex: Glue-in-pizza incident where ChatGPT suggested adding glue to dough to hold toppings_

### 🧠 Hallucinations
- AI makes up facts, methods, or citations with confidence
- _Ex: Lawyer submitted a legal brief with fake cases invented by ChatGPT_

### 📅 Out-of-Date Info
- AI may use deprecated libraries or give old advice
- _Ex: Recommends outdated Python syntax or tools no longer in use_

> **You are still the engineer** — always verify code, test edge cases, and understand what you're using.
