from transformers import AutoTokenizer

def create_tokenizer(tokenizer_name="gpt2"):
    tokenizer = AutoTokenizer.from_pretrained(tokenizer_name)
    return tokenizer

def tokenize_dataset(dataset, tokenizer):
    def tokenize_function(examples):
        return tokenizer(examples["content"], padding=True, truncation=True, max_length=512)
    return dataset.map(tokenize_function, batched=True)