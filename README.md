# ⭐ Product Review Sentiment & Summary Analyzer

A Generative AI application that analyzes product reviews using a Large Language Model (LLM). The application determines the sentiment of a review, assigns a sentiment score, extracts key points, and generates a concise summary while strictly using only the information provided in the review.

---

## 📌 Problem Statement

Customer reviews contain valuable insights about products, but they are often unstructured and difficult to analyze manually. Businesses need an automated solution to understand customer feedback efficiently.

This application analyzes product reviews and provides:

- Sentiment Classification
- Sentiment Score
- Key Point Extraction
- Review Summary

without adding external knowledge or assumptions.

---

## 🎯 Objective

Develop a Generative AI application that:

- Classifies review sentiment.
- Assigns a sentiment score.
- Extracts important key points.
- Generates a concise summary.
- Returns structured output using a Pydantic model.

---

## 🚀 Features

- ✅ Positive, Negative, Neutral & Mixed sentiment detection
- ✅ Sentiment score generation
- ✅ Key point extraction
- ✅ Concise review summarization
- ✅ Structured output using Pydantic
- ✅ Streamlit user interface
- ✅ Prompt Engineering using LangChain
- ✅ Groq LLM Integration

---

## 🛠️ Technologies Used

- Python
- Streamlit
- LangChain
- Groq LLM
- Prompt Engineering
- Pydantic
- python-dotenv

---

## 📂 Project Structure

```
Product Review Sentiment/
│
├── app.py               # Streamlit UI
├── llm.py               # LLM Configuration
├── prompt.py            # Prompt Template
├── parser.py            # Pydantic Output Schema
├── main.py              # Testing Script
├── requirements.txt
├── .gitignore
├── README.md
└── .env
```

---

## 🏗️ Architecture

```
User Review
      │
      ▼
Prompt Template
      │
      ▼
Groq LLM
      │
      ▼
Pydantic Output Parser
      │
      ▼
Structured JSON Output
      │
      ▼
Streamlit Interface
```

---

## 📥 Input Example

```
The phone looks good but battery drains quickly.
```

---

## 📤 Output Example

```json
{
  "sentiment": "Mixed",
  "sentiment_score": 0.6,
  "key_points": [
    "Good design",
    "Poor battery life"
  ],
  "summary": "The phone has a good design but the battery drains quickly."
}
```

---

## 🧪 Test Cases

### Positive Review

```
Amazing camera quality and excellent battery life.
```

### Negative Review

```
The battery drains quickly and performance is slow.
```

### Mixed Review

```
The phone looks premium but the battery drains quickly.
```

### Neutral Review

```
The phone has 128GB storage and a 6.5-inch display.
```

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/Shivathamme/product-review-sentiment-analyzer.git
```

Move into the project folder

```bash
cd product-review-sentiment-analyzer
```

Create a virtual environment

```bash
python -m venv .venv
```

Activate the virtual environment

Windows

```bash
.venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the project directory.

```
groq_class=YOUR_GROQ_API_KEY
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

or

```bash
python -m streamlit run app.py
```

---

## 📈 Future Enhancements

- Multi-language review support
- Aspect-based sentiment analysis
- Review analytics dashboard
- Batch review processing
- Export results to CSV/PDF
- Product-wise sentiment visualization

