# 🪐 PlutoAI : One Chat at a Time.
by Songfurina

**PlutoAI** is an AI-powered chatbot built with OpenAI's GPT model and Streamlit, designed for seamless and intelligent interactions. Whether you're a coder, creative, or just curious, PlutoAI is here to simplify your queries and provide insightful responses.

## 🌟 Features

- **Smart Chat:** Powered by OpenAI's GPT for intelligent responses.
- **Clean UI:** Modern purple theme with a responsive design.
- **Clear Chatbox:** Automatically clears input after each message.
- **Reset Button:** One-click chat reset for starting fresh.
- **Chat History:** Displays past conversations.

## 🛠️ Tech Stack
- Backend AI: OpenAI GPT
- Frontend Framework: Streamlit
- Styling: Custom CSS for enhanced visuals

## 📦  Installation
1. **Clone this Repository**:
   ```bash
   git clone https://github.com/songfurina/OpenAI-Powered-Chatbots.git
   cd PlutoAI
   
2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt

3. **Set Up API Key**:
- Add your OpenAI API key in the .streamlit/secrets.toml file:
[default]
OPEN_API_KEY = "your_openai_api_key"
- Please generate your own API key from OpenAI: https://platform.openai.com/account/api-keys.

4. **Run the App**:
   ```bash
   streamlit run main.py

## 📂 Project Files

- main.py: Main application file.
- requirements.txt: Dependencies file.
- .streamlit/secrets.toml: File to store your OpenAI API key.

## ✨ Usage

- Open the app in your browser (default: http://localhost:8501).
- Type a message in the input box and press Enter.
- View the bot's response and interact seamlessly.
- Use Clear Chat to reset the conversation.