from datasets import load_dataset

def download_and_filter_dataset(dataset_link="bigcode/the-stack-v2", data_dir="data/Python"):
    """
    Downloads a Hugging Face dataset and filters it.
    """
    dataset = load_dataset(dataset_link, data_dir=data_dir, split="train")

    def filter_data(example):
        content = example.get("content", "")

        if len(content) >= 2000:
            return False
        if "import" not in content:
            return False
        lines = content.strip().splitlines()
        if lines and all(line.strip().startswith("#") or not line.strip() for line in lines):
            return False
        if "TODO" in content:
            return False
        return True

    filtered_dataset = dataset.filter(filter_data)
    return filtered_dataset