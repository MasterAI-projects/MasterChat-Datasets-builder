# MasterChat-Datasets-Builder

A lightweight dataset builder for AI projects. MasterChat-Datasets Builder allows downloading, filtering, and converting large code datasets into optimized formats like `.parquet`. Designed for research, fine-tuning, and startups aiming to scale AI models with efficient, clean data pipelines.

---

## 🚀 Features
- 📥 Download datasets directly from Hugging Face.  
- 🔍 Automatic filtering (length check, comments, TODO removal, import detection).  
- 🧩 Tokenization with Hugging Face tokenizers.  
- 💾 Save data in `.parquet`, `.jsonl`, `.arrow`, or raw `.py` formats.  
- ⚡ Lightweight and fast — perfect for startups or researchers.  

---

## 📦 Installation
```bash
pip install datasets transformers pyarrow