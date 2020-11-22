# Europe PubMed Central Citations dataset
This tool let us create a dataset from the EuropePMC OpenAccess dumps. 
At the end of the process we'll have a final CSV file with, for each row,
the identifier of the citing document and the related cited documents.

This tool has been created as
part of the [Open Biomedical Citations in Context Corpus](https://wellcome.ac.uk/grant-funding/people-and-projects/grants-awarded/open-biomedical-citations-context-corpus) research project, actually used for speed up OpenCitations Bibliographic Entries Extractor (BEE) process.


### Workflow
The workflow is divided in the following steps:
- download the dumps (skippable)
- download IDs file and generate a pickle dump of it to enable a fast search
- unzip the articles from each dump and store their xml separately, deleting in the end the original dump (concurrently-> specify the number)
- process the article. Each XML is transformed in a row of the dataset having the following fields:
    - `cur_doi`
    - `cur_pmid`
    - `cur_pmcid`
    - `cur_name` (the reference to the XML file needed for BEE/Jats2OC)
    - `references` (json dumped string containing a list of identifiers of the cited documents)
 
    If any of the previous IDs are not contained in the XML, we will exploit the PMID or PMCID to find the missing ones
    in the IDs file. 
    
    If a citing article or a cited one doesn't have any ID, we don't save it. If a citing article doesn't have cited 
    references, we don't save it.
    
    This process is run in parallel (-> specify the number). You can specify to store everything in a single dataset.csv (slow)
    or to store in many CSV files and then concatenate them (fast).
    
You'll find the result in `{path}/csv/dataset.csv`.

### How to start it
All the files needed to build the dataset will be automatically downloaded from the script.

Install the dependencies with `pip install -r requirements.txt` 

Run it with `$ python3 EuropePubMedCentralDataset.py`, and change the default values of the parameters if you want.
