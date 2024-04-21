import pandas as pd

from abc import ABC, abstractmethod
from pathlib import Path
from utils.paths import get_filetype


class DataStrategy(ABC):
    @abstractmethod
    def load_data(self, data_path: str):
        pass


class DataIngestingStrategy(DataStrategy):
    def load_data(self, data_path: str | Path):
        """
        Loads the data from the file.

        Args:
            data_path: str, path to the dataset
        """
        return self.read_data(data_path)

    def read_data(self, data_path: str | Path):
        filetype = get_filetype(data_path)

        match filetype:
            case "csv":
                data = pd.read_csv(data_path)
            case "tsv":
                data = pd.read_csv(data_path, delimiter="\t")
            case _:
                raise TypeError("Not a valid file type.")
        return data
