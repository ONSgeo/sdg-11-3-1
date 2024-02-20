import os
from typing import Dict, Optional, Union

from dotenv import load_dotenv

from src.sdg_11_3_1_src.utils import InputFile

load_dotenv()  # take environment variables from .env.


class UserParams:
    def __init__(self) -> None:
        # the root directory to work from
        self.root_dir: Optional[str] = os.getenv("ROOT_DIR")

        # the directory where the data is located
        # if none the class will assume it is in: f'{self._root_dir}/{self._sdg_name}_data'
        # e.g.  'C:/Users/name/Scripts/SDGs/sdg_11_3_1_data'
        self.data_dir: Optional[str] = None

        # the directory where the output is saved
        # if none the class will assume it is in: f'{self._root_dir}/{self._sdg_name}_output'
        # e.g.  'C:/Users/name/Scripts/SDGs/sdg_11_3_1_output'
        self.output_dir: Optional[str] = None

        # population data for t1
        # the file path for the population data for t1
        self.pop_t1_file_path = f"{self.root_dir}/sdg_11_3_1_data/2019_2016_2013/population/SAPE_mid2013_ew.xls"

        # any keyword arguments needed for reading the file
        # if none set as empty dict: {}
        self.pop_t1_kwargs = {
            "sheet_name": "Mid-2013 Persons",
            "skiprows": 4,
            "index_col": "Area Codes",
            "thousands": ",",
        }

        # the year the data is from
        self.pop_t1_year = 2013

        # the column with the population counts (generally will be all ages)
        self.pop_t1_age_col = "all ages"

        # population data for t2
        # the file path for the population data for t2
        self.pop_t2_file_path = f"{self.root_dir}/sdg_11_3_1_data/2019_2016_2013/population/popn-mid-2016-lsoa-ew.xls"

        # any keyword arguments needed for reading the file
        # if none set as empty dict: {}
        self.pop_t2_kwargs = {
            "sheet_name": "Mid-2016 Persons",
            "skiprows": 4,
            "index_col": "Area Codes",
            "thousands": ",",
        }

        # the year the data is from
        self.pop_t2_year = 2016

        # the column with the population counts (generally will be all ages)
        self.pop_t2_age_col = "all ages"

        # population data for t3
        # the file path for the population data for t3
        self.pop_t3_file_path = f"{self.root_dir}/sdg_11_3_1_data/2019_2016_2013/population/popn-mid-2019-lsoa-ew.xlsx"

        # any keyword arguments needed for reading the file
        # if none set as empty dict: {}
        self.pop_t3_kwargs = {
            "sheet_name": "Mid-2019 Persons",
            "skiprows": 4,
            "engine": "openpyxl",
            "index_col": "LSOA Code",
            "thousands": ",",
        }

        # the year the data is from
        self.pop_t3_year = 2019

        # the column with the population counts (generally will be all ages)
        self.pop_t3_age_col = "all ages"

        # land coverage data for t1
        # the file path for the land coverage data for t1
        self.land_t1_file_path: str = (
            f"{self.root_dir}/sdg_11_3_1_data/2019_2016_2013/lsoa2016_2013_landcover_area_GB.csv"
        )

        # any keyword arguments needed for reading the file
        # if none set as empty dict: {}
        self.land_t1_kwargs: Dict[str, Union[str, int]] = {
            "index_col": "LSOA11CD",
            "thousands": ",",
        }

        # the column with the land area data
        self.land_t1_land_col: str = "area_2013"

        # flag if the data needs to be filtered at all
        self.land_t1_filter_land_flag: bool = False

        # column to filter the data on
        self.land_t1_filter_land_col: Optional[str] = None

        # keeps the rows with the value in filter_land_col
        self.land_t1_filter_land_value: Optional[str] = None

        # land coverage data for t2
        # the file path for the land coverage data for t2
        self.land_t2_file_path: str = (
            f"{self.root_dir}/sdg_11_3_1_data/2019_2016_2013/lsoa2016_2013_landcover_area_GB.csv"
        )

        # any keyword arguments needed for reading the file
        # if none set as empty dict: {}
        self.land_t2_kwargs: Dict[str, Union[str, int]] = {
            "index_col": "LSOA11CD",
            "thousands": ",",
        }

        # the column with the land area data
        self.land_t2_land_col: str = "area_2016"

        # flag if the data needs to be filtered at all
        self.land_t2_filter_land_flag: bool = False

        # column to filter the data on
        self.land_t2_filter_land_col: Optional[str] = None

        # keeps the rows with the value in filter_land_col
        self.land_t2_filter_land_value: Optional[str] = None

        # land coverage data for t3
        # the file path for the land coverage data for t3
        self.land_t3_file_path: str = (
            f"{self.root_dir}/sdg_11_3_1_data/2019_2016_2013/lsoa2019_landcover_area_GB - Copy.csv"
        )

        # any keyword arguments needed for reading the file
        # if none set as empty dict: {}
        self.land_t3_kwargs: Dict[str, Union[str, int]] = {
            "index_col": "LSOA11CD",
            "thousands": ",",
        }

        # the column with the land area data
        self.land_t3_land_col: str = "area_2019"

        # flag if the data needs to be filtered at all
        self.land_t3_filter_land_flag: bool = True

        # column to filter the data on
        self.land_t3_filter_land_col: Optional[str] = "landcover_type"

        # keeps the rows with the value in filter_land_col
        self.land_t3_filter_land_value: Optional[str] = "Manmade"

        # Option to save the resulting csv files
        self.save_csv_file: bool = True

        self.set_input_files()

    def print_params(self) -> None:
        for k, v in vars(self).items():
            print(f"{k} = {v}")

    def set_input_files(self) -> None:
        self.input_files: Dict[str, InputFile] = {
            "pop_t1": InputFile(
                self.pop_t1_file_path,
                kwargs=self.pop_t1_kwargs,
                year=self.pop_t1_year,
                pop_col_init=self.pop_t1_age_col,
            ),
            "pop_t2": InputFile(
                self.pop_t2_file_path,
                kwargs=self.pop_t2_kwargs,
                year=self.pop_t2_year,
                pop_col_init=self.pop_t2_age_col,
            ),
            "pop_t3": InputFile(
                self.pop_t3_file_path,
                kwargs=self.pop_t3_kwargs,
                year=self.pop_t3_year,
                pop_col_init=self.pop_t3_age_col,
            ),
            "land_t1": InputFile(
                self.land_t1_file_path,
                kwargs=self.land_t1_kwargs,
                land_col=self.land_t1_land_col,
                filter_land_flag=self.land_t1_filter_land_flag,
                filter_land_col=self.land_t1_filter_land_col,
                filter_land_value=self.land_t1_filter_land_value,
            ),
            "land_t2": InputFile(
                self.land_t2_file_path,
                kwargs=self.land_t2_kwargs,
                land_col=self.land_t2_land_col,
                filter_land_flag=self.land_t2_filter_land_flag,
                filter_land_col=self.land_t2_filter_land_col,
                filter_land_value=self.land_t2_filter_land_value,
            ),
            "land_t3": InputFile(
                self.land_t3_file_path,
                kwargs=self.land_t3_kwargs,
                land_col=self.land_t3_land_col,
                filter_land_flag=self.land_t3_filter_land_flag,
                filter_land_col=self.land_t3_filter_land_col,
                filter_land_value=self.land_t3_filter_land_value,
            ),
        }
