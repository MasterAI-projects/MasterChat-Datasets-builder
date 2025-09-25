from transformers import AutoTokenizer

def create_tokenizer(tokenizer_name="gpt2"):
    """
    Creates a Hugging Face tokenizer.

    Args:
        tokenizer_name (str): The tokenizer model (default: gpt2).
    """
    tokenizer = AutoTokenizer.from_pretrained(tokenizer_name)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token
    return tokenizer

def tokenize_dataset(dataset, tokenizer):
    """
    Tokenizes the dataset on the 'content' column.

    Args:
        dataset (datasets.Dataset): The dataset to tokenize.
        tokenizer: Hugging Face tokenizer.
    """
    def tokenize_function(examples):
        return tokenizer(examples["content"], padding=True, truncation=True, max_length=512)

    return dataset.map(tokenize_function, batched=True)