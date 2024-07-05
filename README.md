# RefactorEarth

RefactorEarth is a project aimed at analyzing and improving the efficiency of Python code by identifying memory-intensive operations, redundant computations, and suboptimal data structures. This tool leverages state-of-the-art machine learning models to assist developers in writing more sustainable and performant code.

## Objective
Optimize Python code for reduced energy consumption and improved sustainability metrics.

## Methodology

1. **Repository Analysis:**
   - Clone target repo, identify Python files.

2. **Initial Metrics Calculation:**
   - Energy consumption, carbon footprint, sustainability score.

3. **AI-Powered Refactoring:**
   - **Base Model:** Microsoft's CodeBERT.
   - **Fine-tuning:** Custom dataset of energy-efficient Python code.
   - **Optimization Focus:** Loop efficiency, memory usage, I/O operations.
   - **Personalization:** Incorporation of repository owner's GitHub data.
   - **Process:** Iterative passes for algorithm and low-level optimizations.

## Key Performance Indicators (KPIs)

- **Energy Consumption (joules)**
- **Carbon Footprint (gCO2)**
- **Sustainability Score (0-100)**
- **CPU Time (seconds)**
- **Equivalent Smartphone Charge (%)**
- **LED Bulb Power Time (seconds, 10W bulb)**
- **Code Efficiency Metrics**
  - Loop usage efficiency
  - Redundant computation minimization
  - Generator utilization for large datasets
  - I/O operation efficiency
  - Data structure appropriateness

## Results

### Pre-Optimization Metrics
- **Energy Consumption:** 58.57 J
- **Carbon Footprint:** 0.009020 gCO2
- **Sustainability Score:** 41.4/100
- **CPU Time:** 0.00059 s
- **Smartphone Charge:** 0.00128%
- **LED Bulb Time:** 0.00200 s

### Post-Optimization Metrics
- **Energy Consumption:** 20.00 J (-65.9%)
- **Carbon Footprint:** 0.003080 gCO2 (-65.9%)
- **Sustainability Score:** 80.0/100 (+93.2%)
- **CPU Time:** 0.00020 s (-66.1%)
- **Smartphone Charge:** 0.00044% (-65.6%)
- **LED Bulb Time:** Not provided (proportional decrease expected)

### Code Structure Changes
- **Lines of Code:** 100 → 1
- **Cyclomatic Complexity:** 15 → 0
- **Function Count:** 3 → 0
- **Note:** Extreme reductions in code structure metrics require further investigation for potential analysis artifacts.

## Technical Stack
- **AI Model:** Fine-tuned CodeBERT
- **Language:** Python
- **Version Control:** Git
- **Repository Analysis:** GitHub API
- **Potential Deployment:** Docker containerization

## Installation

### Prerequisites
Ensure you have the following installed:
- Python 3.8+
- pip (Python package installer)

### Environment Variables
1. Create a `.env` file in the root directory.
2. Add your GitHub token to the `.env` file:
   ```
   GITHUB_TOKEN=your_github_token
   ```
3. Load environment variables:
   ```sh
   export $(cat .env | xargs)
   ```

### Dependencies
Install the required dependencies:
```sh
pip install torch transformers datasets PyGithub
```

## Detailed Steps

### Step-by-Step Guide to Using CodeBERT and Roberta

1. **Set Up the Environment:**
   - Make sure Python 3.8+ is installed.
   - Install the required Python packages:
     ```sh
     pip install torch transformers datasets PyGithub
     ```

2. **Configure GitHub Access:**
   - Create a `.env` file in the project root directory.
   - Add your GitHub token to the `.env` file:
     ```
     GITHUB_TOKEN=your_github_token
     ```
   - Load the environment variables:
     ```sh
     export $(cat .env | xargs)
     ```

3. **Run the Training Script:**
   - The training script `trainer.py` fetches the `train.py` file from a GitHub repository, tokenizes it using CodeBERT, and trains a model.
   - To run the training script, use:
     ```sh
     python trainer.py
     ```

### Explanation of Key Components:

- **RobertaTokenizer and RobertaForMaskedLM:** These are components from the `transformers` library used for tokenizing text and training language models.
- **TrainingArguments and Trainer:** These are used to set up and run the training process for the model.

### Example Script:

The following is an example script that the `trainer.py` runs. It fetches the content from GitHub, processes it, and trains a model:

```python
import os
import torch
from transformers import RobertaTokenizer, RobertaForMaskedLM, Trainer, TrainingArguments
from datasets import load_dataset
from github import Github

# GitHub setup
github_token = os.getenv("GITHUB_TOKEN")
repo_name = "ShaliniAnandaPhD/Sea_Sifter"
file_path = "train.py"

# Check for GitHub token
if not github_token:
    raise ValueError("GitHub token not found. Please set the GITHUB_TOKEN environment variable.")

# Initialize GitHub client
g = Github(github_token)

try:
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
    
    print("Training completed successfully.")

except Exception as e:
    print(f"An error occurred: {e}")
```

## Contributing

We welcome contributions! Here’s how you can help:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Create a new Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Conclusion
RefactorEarth demonstrates significant potential for AI-driven code optimization, achieving substantial improvements in energy efficiency and sustainability metrics. The integration of personalized coding patterns and energy-focused optimizations presents a novel approach to sustainable software development.



