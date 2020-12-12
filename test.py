from EuropePubMedCentralDataset import EuropePubMedCentralDataset
from pathlib import Path


def main():
    Path("data").mkdir(parents=True, exist_ok=True)

    e = EuropePubMedCentralDataset(start_path="data",
                                   writing_multiple_csv=True,
                                   skip_download=False,
                                   download_workers=1,
                                   unzip_threads=1,
                                   process_article_threads=100,
                                   max_file_to_download=1)

    e.start()

if __name__ == '__main__':
    main()