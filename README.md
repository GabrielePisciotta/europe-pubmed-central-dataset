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
    
_All the files needed to build the dataset will be automatically downloaded from the script._

You'll find the result in `{path}/csv/dataset.csv`.



## How to start it
Install the dependencies with `pip install -r requirements.txt` 

### Configuration
Specify the parameters in the `config.py` file:
- __start_path__: the full path to the directory where everything will be stored e.g.: "/temp_data_europepubmed-central-dataset"
- __writing_multiple_csv__: a boolean that let you specify if you want to store the results directly to the final CSV during the process,
  or if you want to store all the results in separate CSV and then merge all. Set to True for high speed. 
- __skip_download__: a boolean to specify if you want to download the dumps or if you want to skip this phase (e.g.: you 
  already downloaded manually the ones that you want)
- __download_workers__: the number of processes spawned to download the dumps
- __max_retry__: max number of retries if something goes wrong while downloading an OA dump
- __sec_between_retry__: seconds between each retry 
- __unzip_threads__: number of threads involved in the extraction of the dumps
- __process_article_threads__: number of threads involved in the processing of the extracted XML articles
- __max_file_to_download__: max number of OA dumps to download. Set to _None_ in order to download all.
- __folder_articles__: the number of directories that will be created for each dump where will be stored the XMLs 

_Don't set an high number for unzip_threads and process_article_threads, because you can encounter
of memory saturation and the error of having "Too many open files"._

### Run
Run it with `$ python3 EuropePubMedCentralDataset.py`