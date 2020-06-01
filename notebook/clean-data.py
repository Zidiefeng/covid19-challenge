#!/usr/bin/env python
# coding: utf-8

# ## About this notebook
#
# In this notebook, I quickly explore the `biorxiv` subset of the papers. Since it is stored in JSON format, the structure is likely too complex to directly perform analysis. Thus, I not only explore the structure of those files, but I also provide the following helper functions for you to easily format inner dictionaries from each file:
# * `format_name(author)`
# * `format_affiliation(affiliation)`
# * `format_authors(authors, with_affiliation=False)`
# * `format_body(body_text)`
# * `format_bib(bibs)`
#
# Feel free to reuse those functions for your own purpose! If you do, please leave a link to this notebook.
#
# Throughout the EDA, I show you how to use each of those files. At the end, I show you how to generate a clean version of the `biorxiv` as well as all the other datasets, which you can directly use by choosing this notebook as a data source ("File" -> "Add or upload data" -> "Kernel Output File" tab -> search the name of this notebook).
#
# ### Update Log
#
# * V9: First release.
# * V10: Updated paths to include the [14k new papers](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge/discussion/137474).

# In[1]:


import os
import json
from pprint import pprint
from copy import deepcopy

import numpy as np
import pandas as pd
from tqdm.notebook import tqdm


print("Define Functions")

# ## Helper Functions

# Unhide the cell below to find the definition of the following functions:
# * `format_name(author)`
# * `format_affiliation(affiliation)`
# * `format_authors(authors, with_affiliation=False)`
# * `format_body(body_text)`
# * `format_bib(bibs)`

# In[2]:


def format_name(author):
    middle_name = " ".join(author['middle'])

    if author['middle']:
        return " ".join([author['first'], middle_name, author['last']])
    else:
        return " ".join([author['first'], author['last']])


def format_affiliation(affiliation):
    text = []
    location = affiliation.get('location')
    if location:
        text.extend(list(affiliation['location'].values()))

    institution = affiliation.get('institution')
    if institution:
        text = [institution] + text
    return ", ".join(text)

def format_authors(authors, with_affiliation=False):
    name_ls = []

    for author in authors:
        name = format_name(author)
        if with_affiliation:
            affiliation = format_affiliation(author['affiliation'])
            if affiliation:
                name_ls.append(f"{name} ({affiliation})")
            else:
                name_ls.append(name)
        else:
            name_ls.append(name)

    return ", ".join(name_ls)

def format_body(body_text):
    texts = [(di['section'], di['text']) for di in body_text]
    texts_di = {di['section']: "" for di in body_text}

    for section, text in texts:
        texts_di[section] += text

    body = ""

    for section, text in texts_di.items():
        body += section
        body += "\n\n"
        body += text
        body += "\n\n"

    return body

def format_bib(bibs):
    if type(bibs) == dict:
        bibs = list(bibs.values())
    bibs = deepcopy(bibs)
    formatted = []

    for bib in bibs:
        bib['authors'] = format_authors(
            bib['authors'],
            with_affiliation=False
        )
        formatted_ls = [str(bib[k]) for k in ['title', 'authors', 'venue', 'year']]
        formatted.append(", ".join(formatted_ls))

    return "; ".join(formatted)


# Unhide the cell below to find the definition of the following functions:
# * `load_files(dirname)`
# * `generate_clean_df(all_files)`

# In[3]:


def load_files(dirname):
    filenames = os.listdir(dirname)
    raw_files = []

    for filename in tqdm(filenames):
        filename = dirname + filename
        file = json.load(open(filename, 'rb'))
        raw_files.append(file)

    return raw_files

def generate_clean_df(all_files):
    cleaned_files = []

    for file in tqdm(all_files):
        features = [
            file['paper_id'],
            file['metadata']['title'],
            format_authors(file['metadata']['authors']),
            format_authors(file['metadata']['authors'],
                           with_affiliation=True),
            format_body(file['abstract']),
            format_body(file['body_text']),
            format_bib(file['bib_entries']),
            file['metadata']['authors'],
            file['bib_entries']
        ]

        cleaned_files.append(features)

    col_names = ['paper_id', 'title', 'authors',
                 'affiliations', 'abstract', 'text',
                 'bibliography','raw_authors','raw_bibliography']

    clean_df = pd.DataFrame(cleaned_files, columns=col_names)
    clean_df.head()

    return clean_df

print("Load pdf json Data")

pmc_dir = '../data/document_parses/pdf_json/'
pmc_files = load_files(pmc_dir)
pmc_df = generate_clean_df(pmc_files)

print("Save pdf json Data")

pmc_df.to_csv('../data/clean_doc_pdf.csv', index=False)
pmc_df.head()

