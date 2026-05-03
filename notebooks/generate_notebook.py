import nbformat as nbf
from datetime import datetime

nb = nbf.v4.new_notebook()

cells = []

# Title
cells.append(nbf.v4.new_markdown_cell(f"# Huggingphaze Notebook\nGenerated: {datetime.utcnow()}"))

# Intro
cells.append(nbf.v4.new_markdown_cell("This notebook was automatically generated to help you build and test your chatbot."))

# Config cell
cells.append(nbf.v4.new_code_cell("""config = {
    "name": "SupportBot",
    "tone": "friendly",
    "platform": "web"
}
config"""))

# Sample logic
cells.append(nbf.v4.new_code_cell("""def chatbot_response(user_input):
    return f"Hello! You said: {user_input}"

chatbot_response("Test message")
"""))

# API placeholder
cells.append(nbf.v4.new_markdown_cell("## API Integration (Optional)"))

cells.append(nbf.v4.new_code_cell("""# Example placeholder for Hugging Face or OpenRouter API
# Replace with your API key

API_KEY = "YOUR_API_KEY_HERE"
"""))

nb['cells'] = cells

with open("notebooks/huggingphaze_notebook.ipynb", "w") as f:
    nbf.write(nb, f)

print("Notebook generated!")
