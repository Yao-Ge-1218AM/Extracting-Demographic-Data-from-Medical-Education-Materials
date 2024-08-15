# Natural Language Processing Evaluation of Medical Education Cases
## Overview

This project aims to evaluate the presence and representation of Diversity, Equity, Inclusion, and Justice (DEIJ) topics within medical education case materials. Specifically, it focuses on analyzing medical case vignettes used in four courses during the third year of a medical school curriculum. The goal is to identify patterns in the association between demographic identifiers (e.g., race, ethnicity, sex) and medical topics (e.g., substance abuse, heart disease), which may perpetuate stereotypes and biases in the hidden curriculum.

## Objectives

**Extract Language from Medical Cases:** The project involves extracting text from medical education cases presented in PowerPoint or PDF formats throughout the School of Medicine (SOM) curriculum.

**Evaluate DEIJ Topics:** Analyze the extracted text for topics related to health inequities, with a focus on implicit biases held by physicians and healthcare workers.

**Identify Biased Language:** Identify the use of biased language in the cases, such as transitioning from terms like "heavy drinker" to more clinical terms like "alcohol use disorder."

**Analyze Demographic Data:** Evaluate when and how demographic data is connected to specific social determinants of health or specific pathologies.

## Dataset

The analysis is conducted on case vignettes from four courses:

Cardiology: 31 files  
Neurology: 22 files  
Global Health and Underserved Populations (GHUP): 26 files  
Immunology: 15 files  

## Methodology

**Text Extraction:**
    Convert PDF and PowerPoint files to text.
    Delete references and merge paragraphs into single lines.

**NLP Analysis:**
    Use GPT-4o with a specific prompt to identify and extract passages containing demographic data.
    Focus on specific identifiers: Age, Sex, Race, Ethnicity, Religion, Gender, Sexual Orientation, Socioeconomic Status (SES), Immigration Status, Housing, Addiction, Cigarette Smoking, Mental Health, and Suicidal tendencies.

**Batch Processing:**
    Process files in batches to manage large datasets efficiently.

**Output:**
    Generate an analyzable output (e.g., Excel) for statistical analysis.

**Model Parameters:**
    Model: GPT-4o  
    Temperature: 0.2  
    Max Tokens: 4096  
    Top_p: 0.1  
    Batch Size: 10  

## Challenges

1. Text Integrity: Difficulties in maintaining the integrity of text segments due to formatting issues in PDFs and PowerPoint files.  
2. Batch Size: The size of text segments can affect the accuracy of information extraction.  
3. Rare Demographics: Some demographic information (e.g., Religion, Housing, Suicidal tendencies) appears infrequently, complicating analysis.  

## Usage

**Data Preparation:** Prepare the text by converting PDFs and PowerPoint files and preprocessing them as outlined.
**Run Analysis:** Use the provided scripts to run the NLP analysis on the preprocessed text.
**Review Results:** Analyze the output files for insights into DEIJ topics and potential biases in medical education cases.
