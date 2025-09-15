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
# Quickstart
from downloader import download_and_filter_dataset
from tokenised import create_tokenizer, tokenize_dataset
from convert import save_raw_py_files, save_tokenized_parquet

# Step 1: Download + Filter
dataset = download_and_filter_dataset()

# Step 2: Tokenize
tokenizer = create_tokenizer("gpt2")
tokenized_dataset = tokenize_dataset(dataset, tokenizer)

# Step 3: Save
save_raw_py_files(dataset)
save_tokenized_parquet(tokenized_dataset)