# Research Crew

A Python project that uses CrewAI to create a content creation workflow with three AI agents: Content Planner, Content Writer, and Editor.

## Setup

1. **Activate the virtual environment:**
   ```bash
   source venv/bin/activate  # On macOS/Linux
   # or
   venv\Scripts\activate     # On Windows
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your OpenAI API key:**
   
   Create a `.env` file in your project directory with:
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   OPENAI_MODEL_NAME=gpt-3.5-turbo
   ```
   
   Or set it as an environment variable:
   ```bash
   export OPENAI_API_KEY=your_openai_api_key_here
   ```

## Usage

Run the script:
```bash
python research_crew.py
```

Or run it in Jupyter/IPython for better markdown display:
```bash
ipython research_crew.py
```

## How it works

The script creates three AI agents:
- **Content Planner**: Researches and plans content structure
- **Content Writer**: Writes the actual content based on the plan
- **Editor**: Reviews and refines the content

The crew works together to create a comprehensive blog post about Artificial Intelligence (or any topic you modify in the script).

## Requirements

- Python 3.8+
- OpenAI API key
- Internet connection for API calls
