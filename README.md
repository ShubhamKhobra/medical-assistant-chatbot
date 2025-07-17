# 💊 Medical Information Assistant Chatbot

A conversational chatbot that provides **drug safety summaries**, **usage instructions**, and even **medication suggestions** for common conditions. It combines **real-time FDA data** with the power of **LLaMA 3 (via Together.ai)** to give clear, friendly medical insights — all without requiring OpenAI's paid API.

---

## ✨ Features

- ✅ **Live FDA data** using the [OpenFDA API](https://open.fda.gov/)
- 🧠 **LLM-powered summaries** with [LLaMA 3](https://www.together.ai/models/nim-llama-3-1-8b-instruct) via Together.ai
- 💬 Ask about **drug safety, usage, and effects**
- 🔁 Ask **what medicine to take** for common problems (e.g., “What should I take for a headache?”)
- 🖥️ Built using Python + Streamlit for a clean UI

---

## 🛠️ Tech Stack

| Tool           | Purpose                                 |
|----------------|-----------------------------------------|
| **Python**     | Backend logic                           |
| **Streamlit**  | Web-based chatbot UI                    |
| **OpenFDA API**| Fetch drug label data from FDA          |
| **LLaMA 3**    | Free LLM API from Together.ai           |

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/ShubhamKhobra/medical-assistant-chatbot.git
cd medical-assistant-chatbot
