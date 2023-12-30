import logging
import os
from typing import List
import pandas as pd
from .utils import utils
from .constants import (
    CKB_ENG_LINKS_URL,
    CKB_SENTENCES_DETAILED_URL,
    ENG_SENTENCES_DETAILED_URL,
)

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")


class Tatoeba:
    """A class to download and process data from Tatoeba website.

    Methods:
        bz2url_to_df(url: str) -> pd.DataFrame: Download a bz2-compressed file from a URL and return a pandas DataFrame.
        download_eng_ckb_data_from_tatoeba(ckb_eng_links_url: str = CKB_ENG_LINKS_URL, ckb_sentences_detailed_url: str = CKB_SENTENCES_DETAILED_URL, eng_sentences_detailed_url: str = ENG_SENTENCES_DETAILED_URL) -> None: Download and merge English and Central Kurdish data from Tatoeba website.
        get_data(data_path: str = "data", source: str = "eng_ckb_tatoeba") -> pd.DataFrame: Get the data from a given source.
        get_data_sources() -> list: Get the list of supported data sources.
    """

    def __init__(self):
        pass

    def bz2url_to_df(self, url: str) -> pd.DataFrame:
        """Download a bz2-compressed file from a URL and return a pandas DataFrame.

        Args:
            url: A string representing the URL of the file to download.

        Returns:
            A pandas DataFrame containing the data from the file.
        """
        logging.info(f"Downloading {url}...")
        return pd.read_csv(url, sep="\t", header=None, compression="bz2")

    def download_eng_ckb_data_from_tatoeba(
        self,
        ckb_eng_links_url: str = CKB_ENG_LINKS_URL,
        ckb_sentences_detailed_url: str = CKB_SENTENCES_DETAILED_URL,
        eng_sentences_detailed_url: str = ENG_SENTENCES_DETAILED_URL,
    ) -> None:
        """Download and merge English and Central Kurdish data from Tatoeba website.

        Args:
            ckb_eng_links_url: A string representing the URL of the file containing the links between English and Central Kurdish sentences.
            ckb_sentences_detailed_url: A string representing the URL of the file containing the details of the Central Kurdish sentences.
            eng_sentences_detailed_url: A string representing the URL of the file containing the details of the English sentences.

        Returns:
            None. The merged data is saved as a CSV file in the data path.
        """
        # Download the data files
        ckb_eng_links = self.bz2url_to_df(ckb_eng_links_url)
        ckb_sentences_detailed = self.bz2url_to_df(ckb_sentences_detailed_url)
        eng_sentences_detailed = self.bz2url_to_df(eng_sentences_detailed_url)

        logging.info("Downloading complete!")

        # Rename the columns
        ckb_eng_links.columns = ["ckb_id", "eng_id"]
        ckb_sentences_detailed.columns = [
            "ckb_id",
            "language",
            "ckb_sentence",
            "ckb_username",
            "created_date",
            "updated_date",
        ]
        eng_sentences_detailed.columns = [
            "eng_id",
            "language",
            "eng_sentence",
            "eng_username",
            "created_date",
            "updated_date",
        ]

        # Merge the data frames
        data = pd.merge(
            pd.merge(ckb_eng_links, ckb_sentences_detailed, on="ckb_id"),
            eng_sentences_detailed,
            on="eng_id",
        )[
            [
                "eng_id",
                "ckb_id",
                "eng_sentence",
                "ckb_sentence",
                "eng_username",
                "ckb_username",
            ]
        ]

        # Save the data as a CSV file
        data.to_csv(
            os.path.join(self.data_path, "eng_ckb_tatoeba.tsv"), sep="\t", index=False
        )

    def get_data(
        self,
        data_path: str = "data",
        source: str = "eng_ckb_tatoeba",
    ) -> pd.DataFrame:
        """Get the data from a given source.

        Args:
            data_path: A string representing the path where the data is stored or will be stored.
            source: A string representing the name of the data source. Currently, only "eng_ckb_tatoeba" is supported.

        Returns:
            A pandas DataFrame containing the data from the source.

        Raises:
            ValueError: If the source is invalid or not supported.
        """
        # Set the data path attribute
        self.data_path = data_path

        # Create the data path directory if it does not exist
        if not os.path.exists(self.data_path):
            os.makedirs(self.data_path)

        if source == "eng_ckb_tatoeba":
            try:
                return pd.read_csv(
                    os.path.join(self.data_path, "eng_ckb_tatoeba.tsv"), sep="\t"
                )
            except:
                self.download_eng_ckb_data_from_tatoeba()
                return pd.read_csv(
                    os.path.join(self.data_path, "eng_ckb_tatoeba.tsv"), sep="\t"
                )
        else:
            raise ValueError(
                f"Invalid source. Please choose from {self.get_data_sources()}"
            )

    def get_data_sources(self) -> list:
        """Get the list of supported data sources.

        Returns:
            A list of strings representing the names of the data sources.
        """
        return ["eng_ckb_tatoeba"]
