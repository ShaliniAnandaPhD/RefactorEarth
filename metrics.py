import os
import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import ast
import git
from git import Repo
from git.exc import NoSuchPathError, GitCommandError
import json
import logging
import re
import math
from collections import Counter
from memory_profiler import memory_usage, profile
from codecarbon import EmissionsTracker
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

# Load our fine-tuned CodeBERT model for generating and refactoring code
model_name = "finetunecodebert"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)
code_generator = pipeline("text-generation", model=model, tokenizer=tokenizer)

# Set up logging to keep track of our app’s activities
logging.basicConfig(filename='sustainability_dashboard.log', level=logging.INFO, format='%(asctime)s %(levelname)s:%(message)s')

# Function to track emissions with CodeCarbon
def track_emissions(func):
    def wrapper(*args, **kwargs):
        tracker = EmissionsTracker()
        tracker.start()
        result = func(*args, **kwargs)
        emissions = tracker.stop()
        return result, emissions
    return wrapper

# Function to track and log function details like memory usage, time, and emissions
def function_tracker(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        mem_usage_before = memory_usage()[0]
        result, emissions = track_emissions(func)(*args, **kwargs)
        mem_usage_after = memory_usage()[0]
        duration = time.time() - start_time
        mem_diff = mem_usage_after - mem_usage_before

        logging.info(f"Function {func.__name__}: Duration: {duration}s, Memory Usage: {mem_diff} MiB, Emissions: {emissions} CO2eq")
        return result
    return wrapper

@function_tracker
def your_function():
    # Example function logic
    for i in range(1000000):
        pass

# Streamlit Dashboard
def main():
    st.set_page_config(layout="wide")
    st.title("Enhanced Code Sustainability Dashboard with CodeBERT")

    # Set up the sidebar for user inputs and actions
    configure_sidebar()

    # Display the main sections of the dashboard
    display_primary_metrics()
    display_code_analysis()
    display_performance_metrics()
    display_environmental_impact()
    display_optimization_suggestions()
    display_sustainability_metrics()
    display_benchmarking_and_goals()
    display_expanded_metrics()

def configure_sidebar():
    st.sidebar.header("Input Code")
    user_code = st.sidebar.text_area("Enter your Python code here:", height=200, value=st.session_state.get('user_code', ''))
    if st.sidebar.button("Analyze Code"):
        if user_code.strip():
            st.session_state.user_code = user_code
            analyze_code(user_code)
        else:
            st.sidebar.error("Please enter some code to analyze.")

    st.sidebar.header("Git Integration")
    repo_url = st.sidebar.text_input("Repository URL:", "https://github.com/ShaliniAnandaPhD/Temporal--Odyssey")
    repo_path = os.path.join(os.getcwd(), repo_url.split('/')[-1].replace('.git', ''))

    if st.sidebar.button("Analyze Last Commit"):
        if repo_url:
            clone_or_open_repo(repo_url, repo_path)
            analyze_last_commit(repo_path)
        else:
            st.sidebar.error("Please enter a repository URL.")

    st.sidebar.header("Generate Sustainable Code")
    description = st.sidebar.text_area("Enter a description for code generation:", height=100)
    if st.sidebar.button("Generate Code"):
        if description:
            generated_code = generate_sustainable_code(description)
            st.session_state.generated_code = generated_code
            st.sidebar.code(generated_code, language='python')
            analyze_code(generated_code)
        else:
            st.sidebar.error("Please enter a description for code generation.")

    st.sidebar.header("Refactor Code")
    if st.sidebar.button("Refactor Code"):
        if 'user_code' in st.session_state:
            refactor_code(st.session_state.user_code)
        else:
            st.sidebar.error("Please analyze code before refactoring.")

    st.sidebar.header("Logs")
    if st.sidebar.button("Download Logs"):
        download_logs()

def analyze_code(code):
    try:
        tree = ast.parse(code)
        st.session_state.time_complexity = calculate_time_complexity(tree)
        st.session_state.space_complexity = calculate_space_complexity(tree)
        st.session_state.code_quality = calculate_code_quality(tree)
        st.session_state.scalability_score = calculate_scalability(tree)
        st.session_state.maintainability_index = calculate_maintainability_index(tree)
        st.session_state.test_coverage = calculate_test_coverage(code)

        energy_consumption, carbon_footprint, sustainability_score, energy_by_operation = analyze_energy_and_carbon_footprint(tree)

        st.session_state.energy_consumption = energy_consumption
        st.session_state.carbon_footprint = carbon_footprint
        st.session_state.sustainability_score = sustainability_score
        st.session_state.energy_by_operation = energy_by_operation

        st.success("Code analysis completed successfully.")
    except Exception as e:
        st.error(f"Error analyzing code: {str(e)}")
        logging.error(f"Error analyzing code: {str(e)}")

def generate_sustainable_code(description):
    prompt = f"Generate sustainable and efficient Python code based on the following description:\n\n{description}\n\nPython code:"
    generated_code = code_generator(prompt, max_length=1000, num_return_sequences=1)[0]['generated_text']
    return generated_code.strip()

def refactor_code(code):
    st.subheader("Refactored Code for Improved Sustainability")
    prompt = f"Refactor the following Python code to improve its sustainability and efficiency:\n\n{code}\n\nRefactored code:"
    refactored_code = code_generator(prompt, max_length=2000, num_return_sequences=1)[0]['generated_text']
    st.code(refactored_code, language='python')
    analyze_code(refactored_code)

def get_optimization_suggestions(code):
    prompt = f"Provide optimization suggestions to improve the sustainability and efficiency of the following Python code:\n\n{code}\n\nOptimization suggestions:"
    suggestions = code_generator(prompt, max_length=1000, num_return_sequences=1)[0]['generated_text']
    return suggestions.split('\n') if suggestions else ["No suggestions available"]

if __name__ == "__main__":
    main()

