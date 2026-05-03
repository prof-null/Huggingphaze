> ⚡ Fully automated AI notebook generation via GitHub Actions

# Huggingphaze

A modular, cloud-native AI chatbot builder designed for non-technical users.

---

## 🚀 What This Project Does

Huggingphaze automatically:

- Generates AI chatbot notebooks
- Uses secure API integration (no exposed keys)
- Supports structured inputs (CSV, JSON, YAML)
- Runs entirely in the cloud via GitHub Actions

---

## ⚙️ How It Works

1. You push code to GitHub  
2. GitHub Actions runs the pipeline  
3. A Jupyter Notebook is generated automatically  
4. You can open and run it online  

---

## 📓 Open the Generated Notebook

Click below to open in a cloud notebook environment:

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/YOUR_USERNAME/huggingphaze/blob/main/notebooks/huggingphaze_notebook.ipynb)

> Replace `YOUR_USERNAME` with your GitHub username.

---

## 🔐 Security

API keys are handled using GitHub Secrets:

- `OPENROUTER_API_KEY`
- `HUGGINGFACE_API_KEY`

They are never stored in code or notebooks.

---

## 📁 Project Structure

huggingphaze/
│
├── .github/workflows/ci.yml
├── generate_notebook.py
├── requirements.txt
│
├── notebooks/
│ └── huggingphaze_notebook.ipynb




---

## 🧪 How to Trigger Notebook Generation

1. Edit any file in GitHub  
2. Commit the change  
3. Go to the **Actions tab**  
4. Wait for the workflow to finish  

Your notebook will appear in `/notebooks/`.

---

## 🧠 Vision

This project aims to:

- Bridge technical and non-technical AI users  
- Enable low-resource AI workflows  
- Provide a modular, container-friendly pipeline  

---

## ⚡ Future Features

- CSV → chatbot training  
- Multi-model routing (via APIs)  
- Statistical optimization layers  
- UI-based chatbot builder  

---

## 📌 Notes

- Notebooks are viewable in GitHub  
- Execution requires Colab or Codespaces


