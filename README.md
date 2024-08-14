# RefactorEarth

Welcome to **RefactorEarth**! This project is all about making Python code more efficient and sustainable. By using smart machine learning models like CodeBERT, along with tools like CodeCarbon, RefactorEarth helps identify inefficient code and suggests ways to improve it, ultimately reducing energy consumption and your carbon footprint. We're currently in the beta phase (version 0.9) and would love your feedback.

## Table of Contents

- [Overview](#overview)
- [Getting Started](#getting-started)
- [Fine-Tuning CodeBERT](#fine-tuning-codebert)
- [How It All Works Together](#how-it-all-works-together)
- [Advanced Tips & Tricks](#advanced-tips--tricks)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [API Details](#api-details)
- [FAQs](#faqs)
- [Real-World Examples](#real-world-examples)
- [What’s Next?](#whats-next)
- [Need Help?](#need-help)
- [References](#references)

## Overview

RefactorEarth is your go-to tool for making Python code leaner and greener. Modern coding practices can sometimes be wasteful, leading to unnecessary energy usage. RefactorEarth tackles this problem by analyzing your code, finding inefficiencies, and helping you fix them—all with the power of machine learning.

# RefactorEarth Project Overview

<div style="font-family: Arial, sans-serif; font-size: 14px; line-height: 1.4; max-width: 800px; margin: 0 auto;">
  <div style="background-color: #4a86e8; color: white; padding: 10px; text-align: center; font-weight: bold;">RefactorEarth</div>
  
  <table style="width: 100%; border-collapse: collapse; margin-top: 10px;">
    <tr>
      <td style="width: 33%; vertical-align: top; padding: 10px; border: 1px solid #ccc;">
        <div style="background-color: #6aa84f; color: white; padding: 5px; text-align: center; font-weight: bold;">Repository Analysis</div>
        <ul style="list-style-type: none; padding-left: 0;">
          <li>• Clone Repository</li>
          <li>• Extract Python Files</li>
          <li>• Initial Metrics Calculation</li>
        </ul>
        <div style="background-color: #cfe2f3; padding: 5px; margin-top: 10px;">
          <strong>Tools:</strong> GitHub API, CodeCarbon
        </div>
      </td>
      <td style="width: 33%; vertical-align: top; padding: 10px; border: 1px solid #ccc;">
        <div style="background-color: #e69138; color: white; padding: 5px; text-align: center; font-weight: bold;">AI-Powered Refactoring</div>
        <ul style="list-style-type: none; padding-left: 0;">
          <li>• CodeBERT Model</li>
          <li>• Fine-tuning</li>
          <li>• Optimization Engine</li>
        </ul>
        <div style="background-color: #fff2cc; padding: 5px; margin-top: 10px;">
          <strong>Output:</strong> Optimized Code
        </div>
      </td>
      <td style="width: 33%; vertical-align: top; padding: 10px; border: 1px solid #ccc;">
        <div style="background-color: #8e7cc3; color: white; padding: 5px; text-align: center; font-weight: bold;">Metrics Evaluation</div>
        <ul style="list-style-type: none; padding-left: 0;">
          <li>• Energy Consumption</li>
          <li>• Carbon Footprint</li>
          <li>• Sustainability Score</li>
        </ul>
        <div style="background-color: #d9d2e9; padding: 5px; margin-top: 10px;">
          <strong>Tool:</strong> CodeCarbon
        </div>
      </td>
    </tr>
  </table>
  
  <div style="background-color: #f3f3f3; border: 1px solid #ccc; padding: 10px; margin-top: 10px; text-align: center;">
    <strong>Input:</strong> User's GitHub Repository &nbsp;&nbsp;&nbsp; <strong>Output:</strong> Optimization Results
  </div>
</div>

## Getting Started

Here’s the updated README based on the files and structure that were found in your project:

---

# **RefactorEarth: A Tool for Sustainable and Efficient Coding**

## **Setting Things Up**

### **Clone the Repository:**

Start by cloning the RefactorEarth repository to your local machine:

```bash
git clone https://github.com/yourusername/refactor-earth.git
cd refactor-earth
```

### **Install the Necessary Packages:**

Next, install all the required dependencies:

```bash
pip install -r requirements.txt
```

### **Set Up Your Environment:**

You’ll need to create a `.env` file in the root directory and add your GitHub token:

```plaintext
GITHUB_TOKEN=your_github_token
```

Then, load the environment variables:

```bash
export $(cat .env | xargs)
```

And that’s it! You’re ready to start optimizing your code with RefactorEarth.

---

## **Fine-Tuning CodeBERT**

### **Why Fine-Tune?**

Fine-tuning the CodeBERT model allows you to customize it for your specific needs, making it even more effective at optimizing your code.

### **How to Fine-Tune**

#### **Prepare Your Dataset:**

Your dataset should be in a format like CSV, with columns for the code (`input_text`) and any labels or descriptions (`output_text`).

#### **Use the Provided Jupyter Notebook:**

We’ve provided a Jupyter notebook (`Fine_Tuning_Codebert.ipynb`) that guides you through the entire process, from loading your dataset to training the model and saving it.

#### **Save the Model:**

Once you’ve fine-tuned the model, it will be saved as `models/codebert_finetuned.pth`. This is the model you’ll use in the optimization process.

### **Here’s What the Process Looks Like:**

```python
# Load necessary libraries
import torch
from transformers import RobertaTokenizer, RobertaForSequenceClassification, Trainer, TrainingArguments
from datasets import load_dataset

# Load and prepare the dataset
dataset = load_dataset('csv', data_files={'train': 'data/dataset.csv'})
tokenizer = RobertaTokenizer.from_pretrained("microsoft/codebert-base")

def tokenize_function(examples):
    return tokenizer(examples['input_text'], padding="max_length", truncation=True)

tokenized_datasets = dataset.map(tokenize_function, batched=True)

# Fine-tune the model
model = RobertaForSequenceClassification.from_pretrained("microsoft/codebert-base")
trainer = Trainer(
    model=model,
    args=TrainingArguments(output_dir='./models/codebert_finetuned', num_train_epochs=3),
    train_dataset=tokenized_datasets['train'],
)
trainer.train()

# Save the fine-tuned model
trainer.save_model('./models/codebert_finetuned')
```

---

## **How It All Works Together**

### **Integrating the Fine-Tuned Model**

After you’ve fine-tuned your CodeBERT model, it’s time to put it to work! The `refactor.py` script will automatically load your fine-tuned model and use it to optimize the code in your repository.

---

## **Workflow Using `refactor.py` Script in RefactorEarth**

### **Step 1: Clone the GitHub Repository**

The first step is to clone the target GitHub repository into a local directory. This repository contains the code that you want to analyze and optimize.

**How it's done in `refactor.py`:**

```python
def clone_repository(repo_url, target_dir):
    """
    Clone the target GitHub repository into a specified directory.
    """
    print(f"Cloning repository from {repo_url} into {target_dir}...")
    subprocess.run(['git', 'clone', repo_url, target_dir], check=True)
    print("Repository cloned successfully.")
```

**Example Workflow:**

- **Input:** The GitHub repository URL and the target directory where the repo should be cloned.
- **Output:** A local copy of the GitHub repository.

### **Step 2: Calculate Initial Metrics**

Once the repository is cloned, the script calculates the initial metrics such as energy consumption and carbon emissions. This is done by running a specific Python script from the cloned repository.

**How it's done in `refactor.py`:**

```python
def calculate_initial_metrics(directory, script_name='example_script.py'):
    """
    Calculate initial energy consumption and sustainability metrics for the code.
    """
    tracker = EmissionsTracker()

    script_path = os.path.join(directory, script_name)
    if not os.path.isfile(script_path):
        raise FileNotFoundError(f"The script {script_name} was not found in the directory {directory}.")

    print(f"Calculating initial metrics for the script {script_name}...")
    tracker.start()  # Start the emissions tracker

    subprocess.run(['python', script_path], check=True)

    tracker.stop()  # Stop the emissions tracker

    emissions_data = tracker.final_emissions_data
    metrics = {
        'energy_consumed': emissions_data.energy_consumed,  # in kWh
        'carbon_emissions': emissions_data.emissions  # in kgCO2
    }
    print("Initial metrics calculated successfully.")
    return metrics
```

**Example Workflow:**

- **Input:** The directory where the repo is cloned and the name of the script to run.
- **Output:** A dictionary containing the initial energy and carbon metrics.

### **Step 3: Optimize the Code**

After gathering initial metrics, the script uses an AI model (like a fine-tuned version of CodeBERT) to optimize the code in the repository.

**How it's done in `refactor.py`:**

```python
def optimize_code(repo_dir, github_token):
    """
    Optimize the code in the given directory using an AI model like CodeBERT.
    """
    print("Starting the code optimization process...")
    refactor = RefactorEarth(github_token=github_token)

    # Run the optimization process using the AI model
    results = refactor.optimize_repo(repo_dir)
    print("Code optimization completed successfully.")
    return results
```

**Example Workflow:**

- **Input:** The directory with the cloned repository and a GitHub token for accessing the repo.
- **Output:** A dictionary with the optimization results, which may include updated energy consumption, sustainability scores, or other relevant metrics.

### **Step 4: Measure the Impact of Optimizations**

Finally, after the code has been optimized, you can measure the impact by rerunning the script and comparing the new metrics to the initial ones. The `calculate_initial_metrics` function can be reused here with the updated code to see how the optimizations have improved performance and sustainability.

### **Example Workflow Implementation**

To tie everything together, you would run the script as follows:

```python
def main(repo_url, github_token, script_name='example_script.py'):
    """
    Main function to orchestrate the cloning, metric calculation, and optimization processes.
    """
    # Derive the repository name from the URL and set the target directory
    repo_name = repo_url.split('/')[-1].replace('.git', '')
    target_dir = os.path.join(os.getcwd(), repo_name)

    try:
        # Step 1: Clone the repository
        clone_repository(repo_url, target_dir)

        # Step 2: Calculate initial metrics
        initial_metrics = calculate_initial_metrics(target_dir, script_name)
        print(f"Initial Metrics: {initial_metrics}")

        # Step 3: Optimize the code
        optimization_results = optimize_code(target_dir, github_token)
        print(f"Optimization Results: {optimization_results}")

    except Exception as e:
        print(f"An error occurred in the process: {e}")

if __name__ == "__main__":
    # Example usage:
    # Replace with actual repo URL and GitHub token
    REPO_URL = "https://github.com/user/repo.git"
    GITHUB_TOKEN = "your_github_token"
    
    main(REPO_URL, GITHUB_TOKEN)
```

### **Running the Script**

**Execution:** Run the `refactor.py` script from the command line or your Python environment:

```bash
python refactor.py
```

**Outputs:** The script will:
- Clone the specified GitHub repository.
- Calculate the initial energy metrics by executing a script in the repository.
- Optimize the code using the AI model.
- Output the initial metrics and the results of the optimization.

This workflow automates the process of analyzing, optimizing, and measuring code, making it easy to see the impact of your optimizations in terms of energy efficiency and sustainability.

---

## **Advanced Tips & Tricks**

### **Customize Your Fine-Tuning**

- **Adjust Hyperparameters:** Play with settings like the number of epochs or batch size to get the best results.
- **Try Different Datasets:** Fine-tune the model on various datasets to tailor it to different coding styles or programming languages.

### **Extend to Other Languages**

RefactorEarth is built with Python in mind, but with some tweaks, you can adapt it for other programming languages. Modify the tokenizer and dataset preparation steps to handle different languages.

---

## **Contributing**

We’re excited to see what you can bring to RefactorEarth! Here’s how you can contribute:

### **Code Style**
- Follow PEP 8 for Python.
- Use clear and meaningful names for variables and functions.

### **Testing**
- Write tests for any new features.
- Make sure all tests pass before you submit a pull request.

### **Making a Pull Request**
- Fork the repo and create a new branch.
- Make your changes.
- Commit and push your changes.
- Open a pull request!

---

## **API Details**

If RefactorEarth provides any APIs, here’s where you’ll find the details. Some of the key endpoints include:

- **/optimize:** Optimizes a given repository.
- **

/metrics:** Retrieves sustainability metrics.

---

## **FAQs**

Here are some common questions about RefactorEarth:

- **What is RefactorEarth?**
  - It’s a tool that helps you optimize Python code for better efficiency and sustainability.
  
- **How does it track energy consumption?**
  - We use CodeCarbon to measure energy consumption and carbon footprint.
  
- **Do I need a GitHub token?**
  - Yes, you’ll need a GitHub token to access repositories.

---

## **What’s Next?**

Here’s what we’re working on:

- **New Features:** Support for more programming languages and additional sustainability tracking tools.
- **Long-Term Goals:** Build a community-driven database of optimized code patterns and create educational resources on sustainable coding.

---

## **References**

- [CodeCarbon Documentation](https://codecarbon.io/documentation/)
- [Microsoft's CodeBERT Research Paper](https://arxiv.org/abs/2002.08155)

---

## **About**

Hackathon winner at AI Engineer World Fair Hackathon: Transforming code, one function at a time, to reduce digital carbon footprints and create a more sustainable digital world.

- [More Information](https://www.notion.so/shalini-ananda-phd/Refactor-Earth-A-Comprehensive-Tool-for-Sustainable-and-Efficient-Coding-b921467f3e0d4a1daaa8d0af468a701b)

---

## **Resources**
- **Readme**
- **License**: MIT license

---

**Languages:**
- Python: 71.0%
- Jupyter Notebook: 29.0%

---

**Suggested Workflows Based on Your Tech Stack:**
- **Python Package:** Create and test a Python package on multiple Python versions.
- **Python Application:** Create and test a Python application.
- **Django:** Build and Test a Django Project.



