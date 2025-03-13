# Pets_Name_Generator

## Overview

This is a **Streamlit** web application that generates creative pet names based on the selected animal type and its color. The app uses **LangChain** and **Ollama's LLaMA 3.2** model to suggest unique and cool names.

## Features

- User-friendly **Streamlit UI**.
- Select from various pet types (Dog, Cat, Bird, etc.).
- Enter your pet's color for personalized name suggestions.
- Uses **Ollama LLaMA 3.2** to generate five creative pet names.
- Instant results with a simple button click.

## Installation

### Prerequisites

Ensure you have the following installed:

- Python (>=3.8)
- Streamlit
- LangChain
- Ollama

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/pet-name-generator.git
   cd pet-name-generator
   ```
2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On macOS/Linux
   venv\Scripts\activate     # On Windows
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Ensure **Ollama LLaMA 3.2** model is installed:
   ```bash
   ollama pull llama3.2
   ```

## Running the App

Start the Streamlit app by running:

```bash
streamlit run app.py
```

## Usage

1. Select your pet type from the sidebar.
2. Enter your pet's color.
3. Click the "Generate Names" button.
4. View the five suggested names displayed on the screen.

## Dependencies

- **Streamlit**: For the UI
- **LangChain**: For prompt templating
- **Ollama**: For local LLaMA model inference

## Example Output

For a **Golden Dog**, the app might generate:

```
1. Blaze
2. Sunny
3. Goldie
4. Rusty
5. Nugget
```

## Contributing

Feel free to open issues or submit pull requests for improvements.

## Contact
kalpanil22kanbarkar@gmail.com

## License

This project is licensed under the MIT License.
