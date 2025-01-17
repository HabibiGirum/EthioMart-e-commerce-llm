# week-5  
![Build Status](https://github.com/HabibiGirum/EthioMart-e-commerce-llm/actions/workflows/unittests.yml/badge.svg)

# Project Overview
EthioMart is envisioned as the primary hub for Telegram-based e-commerce activities in Ethiopia. With the growing popularity of Telegram for business transactions, the current decentralized structure of multiple independent e-commerce channels presents significant challenges. To address this, EthioMart aims to create a centralized platform that consolidates real-time data from multiple Telegram channels into one unified interface.
Key to this initiative is the fine-tuning of a Language Model (LLM) for Amharic Named Entity Recognition (NER), which extracts essential business entities such as product names, prices, and locations from text, images, and documents shared in these channels. The extracted data is used to populate EthioMart's centralized database, ensuring a seamless and comprehensive experience for customers and vendors.

# Key Objectives
1. Real-time Data Extraction: Fetch data from multiple Ethiopian Telegram e-commerce channels in real time.
2. Fine-tuned NER System: Extract critical entities such as:
    - Product Names or Types
    - Material or Ingredients
    - Location Mentions
    - Monetary Values or Prices


## Installation

To run the code in this repository, follow these steps:

### Prerequisites

Make sure you have Python 3.11. You can check your Python version by running:

```bash
python --version
```

### Clone the Repository

Clone the repository to your local machine:

```bash
git clone https://github.com/HabibiGirum/EthioMart-e-commerce-llm.git
cd EthioMart-e-commerce-llm
```

### Create a Virtual Environment (Optional but Recommended)

Create a virtual environment to isolate the project dependencies:

```bash
python3 -m venv venv
```

Activate the virtual environment:

- On Windows:
  ```bash
  .\venv\Scripts\activate
  ```
- On macOS/Linux:
  ```bash
  source venv/bin/activate
  ```

### Install Required Packages

Install the necessary packages using `pip`:

```bash
pip install -r requirements.txt
```

### Running the Analysis

Once you have set up the environment and installed the dependencies, you can run the EDA scripts:

```notbooks/analysis.ipynb```

## About the Analysis


<!-- ## Further documentation :
[click me](https://drive.google.com/file/d/15aGTZZdOCfE5vhIW5yV4cRS2wzHES72a/view?usp=sharing)
 -->

## Author  
GitHub: [HabibiGirum](https://github.com/HabibiGirum)

Email:  habtamugirum478@gmail.com