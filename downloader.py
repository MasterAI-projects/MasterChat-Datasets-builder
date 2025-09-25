
from datasets import load_dataset

def download_and_filter_dataset(dataset_link="bigcode/the-stack-v2", data_dir="data/Python"):
    """
    Downloads a Hugging Face dataset and filters it.

    Args:
        dataset_link (str): The dataset repository on Hugging Face (default: bigcode/the-stack-v2).
        data_dir (str): The language directory inside the dataset (default: Python).

    Returns:
        datasets.Dataset: The filtered dataset.
    """
    dataset = load_dataset(dataset_link, data_dir=data_dir, split="train")

    def filter_data(example):
        content = example.get("content", "")

        # 1. Keep files with content length < 2000 characters
        if len(content) >= 2000:
            return False

        # 2. Keep files that contain the string "import"
        if "import" not in content:
            return False

        # 3. Ignore files that are only comments
        lines = content.strip().splitlines()
        if lines and all(line.strip().startswith("#") or not line.strip() for line in lines):
            return False

        # 4. Ignore files that contain the string "TODO"
        if "TODO" in content:
            return False

        return True

    filtered_dataset = dataset.filter(filter_data)
    return filtered_dataset


if __name__ == "__main__":
    filtered_dataset = download_and_filter_dataset()
    print(f"Filtered dataset size: {filtered_dataset.num_rows}")
    print(filtered_dataset[0])