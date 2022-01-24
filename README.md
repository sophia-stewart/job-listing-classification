# job-listing-classification

This repository holds all of my work and deliverables for my individual project.

Data Source: https://www.kaggle.com/shivamb/real-or-fake-fake-jobposting-prediction

---

# About the Project

## Project Goal
The goal of this project is to identify elements of fraudulent job postings so that I can predict whether or not a job posting is real.

## Project Description
Fraudulent job postings are becoming more common and more sophisticated. Most of the time they look just like the real thing, so how can I know if I should apply? With this project, I intend to create models to accurately classify job postings as either authentic or fraudulent based on other features of the job posting. To do this, I will use data from Kaggle (url above) which includes nearly 18,000 job postings, of which approximately 800 are fraudulent. I will prepare and explore the data for modeling and hopefully get a better idea of how to distinguish fake job postings from real ones.


## Initial Questions
 1. Are job listings without a higher education requirement more likely to be fake?
 2. Is there a region that is more likely to have fake job listings?
 3. Is there a difference in frequency of fake job listings across employment types? 
 4. Are there any words or phrases that occur commonly in fake job listings?

## Data Dictionary
| Variable | Meaning |
| -------- | ------- |
| jobs     | Full dataframe of job listing information |
| telecommuting | True for telecommuting positions. |
| has_company_logo | True if company logo is present. |
| has_questions | True if screening questions are present. |
| employment_type | Full-type, Part-time, Contract, etc. |
| required_experience | Executive, Entry level, Intern, etc. |
| required_education | Doctorate, Master’s Degree, Bachelor, etc. |
| fraudulent | Target variable, whether a job posting is authentic (0) or fraudulent (1)|
| desc     | Dataframe consisting only of the job description and `fraudulent` |
| train    | Sample (56%) of `jobs` used for exploring data and fitting/training models|
| validate | Sample (24%) of `jobs` used to evaluate multiple models |
| test     | Sample (20%) of `jobs` used to evaluate the best model |
| x_train  | `train`, but only with scaled columns |
| y_train  | `train`, but only the target |
| x_validate | `validate`, but only with scaled columns |
| y_validate | `validate`, but only the target |
| x_test   | `test`, but only with scaled columns |
| y_test   | `test`, but only the target |

---
## The Plan

### Wrangle

1. Define a function to acquire the necessary job listing data from a csv file.
2. Define a function to clean the acquired data.
3. Define a function to split the cleaned data.
4. Define a function to scale the split data.
5. Define a function to combine the previous steps into a single function.
6. Ensure all functions work properly and add them to wrangle.py file.

### Explore
1. Ask a clear question.
2. Develop null and alternative hypotheses for that question.
3. Use visualizations and statistical tests to find answers.
4. Clearly state the answer to the question and summarize findings.
5. Repeat for a total of at least 4 questions.
6. Summarize key findings, takeaways, and actions.

### Model
1. Select a metric to use for evaluating models and explain why that metric was chosen.
2. Create and evaluate a baseline model.
    - Find mode value of target
    - Set all predictions to that value
    - Evaluate based on selected evaluation metric
3. Develop three models.
4. Evaluate all three models on the train sample, note observations.
5. Evaluate the top two models on the validate sample, note observations.
6. Evaluate the top performing model on the test sample, note observations.

### Deliver
1. Ensure final report notebook is thoroughly code commented.
2. Ensure notebook contains enough Markdown cells to guide the reader through the report.
3. Write a conclusion summary.
4. Suggest next steps and recommendations for research and/or model improvement.
5. Run final report notebook from beginning to be sure that there are no errors.
6. Submit link to repository containing project files.

---
## Steps to Reproduce

1. Clone this repository, ensuring the following files have successfully been cloned:
 - jobs.csv
 - Report.ipynb
 - wrangle.py
 - wrangle.ipynb
 - explore.ipynb
 - model.ipynb
2. If not already installed on your system, install pycountry-convert and wordcloud:
 - `pip install pycountry-convert`
 - `pip install wordcloud`
3. Run all cells in Report.ipynb.
4. If desired, run all cells in the other Jupyter notebooks (wrangle.ipynb, explore.ipynb, model.ipynb) in this repository to see my full, in-depth step-by-step process for this project.

---
## Conclusion

### Summary
Through exploring this data, I discovered fraudulent job postings are very similar to authentic job postings. By using the features in this dataset, I was able to create a model for classifying job postings as real or fake with an accuracy of 95.32%. There is still room for improvement and it is in all job seekers' best interest to be able to accurately discern whether a job posting is real or not.

### Recommendation
Always stay vigilant when giving personal information to potential employers. Fake job listings are becoming both more common and more sophisticated. Some red flags to keep an eye out for include:

### Next Steps
Given more time and resources, I would like to find more job listings that do specify a salary range. The majority of entries in this dataset did not have a salary range but I think it would be interesting to see what, if any, correlation there is between stated salary ranges and authenticity of job postings.