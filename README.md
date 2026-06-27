# ⭐ Product Review Sentiment & Summary Analyzer

A **Generative AI** application that analyzes product reviews using a **Large Language Model (LLM)**. The application determines the sentiment of a review, assigns a sentiment score, extracts key points, and generates a concise summary while strictly using only the information provided in the review.

---

## 🚀 Live Demo

**🌐 Streamlit App:**
https://appuct-review-sentiment-analyzer-dzq7ptl42pxctwa2jyb4nf.streamlit.app/

---

## 📌 Problem Statement

Customer reviews provide valuable insights into product quality and customer satisfaction. However, manually analyzing thousands of reviews is time-consuming and inefficient.

This project automates review analysis by:

* Detecting review sentiment
* Assigning a sentiment score
* Extracting important key points
* Generating a concise summary

while ensuring that **no external information or assumptions** are added.

---

## 🎯 Objective

Develop a Generative AI application that can:

* Analyze customer product reviews
* Classify sentiment as Positive, Negative, Neutral, or Mixed
* Generate a sentiment score
* Extract meaningful key points
* Produce a concise summary
* Return structured output using a Pydantic schema

---

## ✨ Features

* ✅ Positive, Negative, Neutral & Mixed Sentiment Detection
* ✅ Sentiment Score Generation
* ✅ Key Point Extraction
* ✅ Automatic Review Summarization
* ✅ Structured Output using Pydantic
* ✅ Prompt Engineering with LangChain
* ✅ Groq LLM Integration
* ✅ Interactive Streamlit Web Application

---

## 🛠️ Technologies Used

* Python
* Streamlit
* LangChain
* Groq LLM
* Prompt Engineering
* Pydantic
* python-dotenv

---

## 📂 Project Structure

```
Product Review Sentiment/
│
├── app.py               # Streamlit User Interface
├── main.py              # Application Entry Point
├── llm.py               # LLM Configuration
├── prompt.py            # Prompt Template
├── parser.py            # Pydantic Output Schema
├── requirements.txt
├── README.md
├── .gitignore
└── .env
```

---

## 🏗️ System Architecture

```
                 User Review
                      │
                      ▼
            Prompt Template (LangChain)
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
             Streamlit Web App
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

## 🧪 Sample Test Cases

### ✅ Positive Review

```
Amazing camera quality and excellent battery life.
```

---

### ❌ Negative Review

```
The battery drains quickly and performance is slow.
```

---

### ⚖️ Mixed Review

```
The phone looks premium but the battery drains quickly.
```

---

### ➖ Neutral Review

```
The phone has a 128GB storage capacity and a 6.5-inch display.
```

---

## ⚙️ Installation

### Clone the Repository

```bash
git clone https://github.com/Shivathamme/product-review-sentiment-analyzer.git
```

### Navigate to the Project Directory

```bash
cd product-review-sentiment-analyzer
```

### Create a Virtual Environment

```bash
python -m venv .venv
```

### Activate Virtual Environment

**Windows**

```bash
.venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root.

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

## 📸 Application Screenshots

### Home Page

*Add a screenshot here after deployment.*

```
images/home.png
```

### Analysis Result

*Add a screenshot here after testing.*

```
images/output.png
```

---

## 📈 Future Enhancements

* Multi-language Review Support
* Aspect-Based Sentiment Analysis
* Product Comparison Dashboard
* Batch Review Processing
* Export Results to CSV/PDF
* Sentiment Trend Visualization
* Review Analytics Dashboard


