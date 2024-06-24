import torch
from transformers import RobertaTokenizer, RobertaForMaskedLM, Trainer, TrainingArguments
from datasets import load_dataset
import os
from github import Github

# GitHub setup
github_token = "YOUR_GITHUB_TOKEN"
repo_name = "ShaliniAnandaPhD/Sea_Sifter"
file_path = "train.py"

# Initialize GitHub client
g = Github(github_token)

# Get the repository
repo = g.get_repo(repo_name)

# Get the file content
file_content = repo.get_contents(file_path).decoded_content.decode()

# Save the content to a local file
with open("local_train.py", "w") as f:
    f.write(file_content)

# Load the dataset
dataset = load_dataset("text", data_files={"train": ["local_train.py"]})

# Load tokenizer and model
tokenizer = RobertaTokenizer.from_pretrained("microsoft/codebert-base")
model = RobertaForMaskedLM.from_pretrained("microsoft/codebert-base")

# Tokenize the dataset
def tokenize_function(examples):
    return tokenizer(examples["text"], padding="max_length", truncation=True, max_length=512)

tokenized_datasets = dataset.map(tokenize_function, batched=True)

# Set up training arguments
training_args = TrainingArguments(
    output_dir="./results",
    num_train_epochs=3,
    per_device_train_batch_size=8,
    save_steps=10_000,
    save_total_limit=2,
)

# Initialize Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_datasets["train"],
)

# Start training
trainer.train()

# Save the fine-tuned model
model.save_pretrained("./fine_tuned_codebert")
tokenizer.save_pretrained("./fine_tuned_codebert")
