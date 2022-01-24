import pandas as pd
import numpy as np
import pycountry_convert as pc

def fix_edu(jobs1):
    jobs1.required_education = np.where(jobs1.required_education.isna(), 'None', jobs1.required_education)
    jobs1.required_education = np.where(jobs1.required_education.isin(['High School or equivalent', 'Unspecified','Some College Coursework Completed', 'Some High School Coursework']), 'None', jobs1.required_education)
    jobs1.required_education = np.where(jobs1.required_education.isin(['Bachelor\'s Degree', 'Master\'s Degree', 'Associate Degree', 'Doctorate']), 'College', jobs1.required_education)
    jobs1.required_education = np.where(jobs1.required_education.isin(['Certification', 'Vocational', 'Vocational - HS Diploma', 'Vocational - Degree', 'Professional']), 'Vocational', jobs1.required_education)
    return jobs1

def fix_exp(jobs1):
    jobs1.required_experience = np.where(jobs1.required_experience.isna(), 'Low', jobs1.required_experience)
    jobs1.required_experience = np.where(jobs1.required_experience.isin(['Entry level', 'Associate', 'Not Applicable', 'Internship']), 'Low', jobs1.required_experience)
    jobs1.required_experience = np.where(jobs1.required_experience == 'Mid-Senior level', 'Med', jobs1.required_experience)
    jobs1.required_experience = np.where(jobs1.required_experience.isin(['Director', 'Executive']), 'High', jobs1.required_experience)
    return jobs1

def fix_emp(jobs1):
    jobs1.employment_type = np.where(jobs1.employment_type.isna(), 'Unspecified', jobs1.employment_type)
    jobs1.employment_type = np.where(jobs1.employment_type == 'Other', 'Unspecified', jobs1.employment_type)
    jobs1.employment_type = np.where(jobs1.employment_type.isin(['Full-time', 'Part-time']), 'Employee', jobs1.employment_type)
    jobs1.employment_type = np.where(jobs1.employment_type.isin(['Contract', 'Temporary']), 'Non-employee', jobs1.employment_type)
    return jobs1

def wrangle_jobs():
    '''
    This function takes in no arguments; it acquires and prepares job listing data
    from a local csv file named fake_job_postings.csv.
    '''
    jobs = pd.read_csv('fake_job_postings.csv')
    cols_to_drop = ['job_id', 'title', 'company_profile', 'description', 'requirements', 'benefits', 'department', 'salary_range', 'industry', 'function']
    jobs = jobs.drop(columns=cols_to_drop)
    jobs = fix_emp(fix_exp(fix_edu(jobs)))
    jobs = jobs.dropna()
    jobs['continent'] = [pc.country_alpha2_to_continent_code(loc) for loc in jobs.location.str[:2]]
    jobs.drop(columns='location', inplace=True)
    return jobs