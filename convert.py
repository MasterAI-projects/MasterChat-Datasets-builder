import os
import pyarrow.parquet as pq
import pyarrow as pa

def save_raw_py_files(dataset, output_dir="output/raw_py"):
    """
    Saves the filtered dataset content into raw .py files.
    """
    os.makedirs(output_dir, exist_ok=True)
    for i, example in enumerate(dataset):
        file_path = os.path.join(output_dir, f"file_{i:06d}.py")
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(example.get("content", ""))
    print(f"Saved {len(dataset)} raw .py files to {output_dir}")


def save_tokenized_parquet(dataset, output_path="output/tokenized_data.parquet"):
    """
    Saves the tokenized dataset into a compressed Parquet file.
    """
    output_dir = os.path.dirname(output_path)
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)

    table = pa.Table.from_pandas(dataset.to_pandas())
    pq.write_table(table, output_path, compression="snappy")
    print(f"Saved tokenized data to {output_path}")