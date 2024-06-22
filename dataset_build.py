import datasets
import os, time, sys
from datasets import DatasetBuilder, load_dataset

dataset = load_dataset(
    "text",
    data_files={"train": [file for file in os.listdir("cs_research data")]},
)

class arxivcs_text(DatasetBuilder):
    def __init__(self):
        self.name = 'arxivcs_text'
