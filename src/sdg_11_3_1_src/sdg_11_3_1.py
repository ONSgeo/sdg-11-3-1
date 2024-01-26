from typing import Dict, List, Optional, Tuple, Union
import numpy as np
import pandas as pd
import geopandas as gpd
import rasterio as rio

from src.sdg_11_3_1_src.sdg_base.src.sdg_base_src.sdg_base import SDGBase
from src.sdg_11_3_1_src.utils import InputFile
from user_params import UserParams

import warnings
warnings.filterwarnings('ignore', category=UserWarning, module='openpyxl')

class SDG11_3_1(SDGBase):
    """Defines input and output directories for data.
    
    Attributes (inherited)
    ----------
    root_dir
        The main directory in which data is stored.
    input_data_dir
        The main directory from which data is input.
    output_data_dir
        The main directory to which data is output.
    test_in_dir
        The main directory from which tests are drawn.
    test_out_dir
        The main directory to which tests are output.
    
    """ 
    
    def __init__(self, sdg_name: str, root_dir: Optional[str], data_dir: Optional[str] = None, output_dir: Optional[str] = None) -> None:
        """To retrieve input and save output data.
        
        Parameters
        ----------
        root_in_dir: str
            The main directory that the data is stored.
            For example: "C:/Users/{user}/Scripts/geo_work/sdg_9_1_1/data"
        root_out_dir: Optional[str]
            This is for if the user wants to save the output elsewhere.
            If not the root out directory will be the same as the input directory.
            
        Returns
        -------
        None
        """

        self._sdg_name = "sdg_11_3_1"
        super().__init__(self._sdg_name, root_dir, data_dir, output_dir)


    def population_growth_rate(
            self, 
            past_pop: pd.Series, 
            present_pop: pd.Series, 
            years: int
        ) -> pd.Series:
        return (np.log(present_pop) - np.log(past_pop)) / years


    def land_consumption_rate(
            self, 
            past: pd.Series, 
            present: pd.Series, 
            years
        ) -> pd.Series:
        return ((present - past)/past) / years


    def land_consumption_rate_population_growth_rate_ratio(
            self, 
            lcr: pd.Series, 
            pgr: pd.Series
        ) -> pd.Series:
        return lcr / pgr


    def filter_land_on_col(self, df: pd.DataFrame, flag: bool, col: str, val: str) -> pd.DataFrame:
        if flag:
            return df[df[col] == val]
        return df


    def built_up_area_per_capita(self, bua: pd.Series, population: pd.Series) -> pd.Series:
        return bua / population


    def calculate_sdg(
            self, 
            input_files: Dict[str, InputFile],
            save_csv: bool
        ) -> bool:

        t1_t2_years = abs(input_files["pop_t2"].year - input_files["pop_t1"].year)
        t2_t3_years = abs(input_files["pop_t3"].year - input_files["pop_t2"].year)


        # Population calculations
        pop_t1 = self.load_data(input_files["pop_t1"].file_path, kwargs=input_files["pop_t1"].kwargs).sort_index()
        pop_t2 = self.load_data(input_files["pop_t2"].file_path, kwargs=input_files["pop_t2"].kwargs).sort_index()
        pop_t3 = self.load_data(input_files["pop_t3"].file_path, kwargs=input_files["pop_t3"].kwargs).sort_index()

        pop_t1 = pop_t1.rename(columns={input_files["pop_t1"].pop_col_init: input_files["pop_t1"].pop_col_rename})
        pop_t2 = pop_t2.rename(columns={input_files["pop_t2"].pop_col_init: input_files["pop_t2"].pop_col_rename})
        pop_t3 = pop_t3.rename(columns={input_files["pop_t3"].pop_col_init: input_files["pop_t3"].pop_col_rename})

        pop_counts = [pop_t1[input_files["pop_t1"].pop_col_rename], pop_t2[input_files["pop_t2"].pop_col_rename], pop_t3[input_files["pop_t3"].pop_col_rename]]
        comb_pop = pd.concat(pop_counts, axis=1).dropna()

        t1_t2_pgr = self.population_growth_rate(
            comb_pop[input_files["pop_t1"].pop_col_rename], 
            comb_pop[input_files["pop_t2"].pop_col_rename], 
            t1_t2_years
        ).rename("t1_t2_pgr")

        t2_t3_pgr = self.population_growth_rate(
            comb_pop[input_files["pop_t2"].pop_col_rename], 
            comb_pop[input_files["pop_t3"].pop_col_rename], 
            t2_t3_years
        ).rename("t2_t3_pgr")

        pgrs = pd.concat([t1_t2_pgr,t2_t3_pgr], axis=1)

        pop_calcs = pd.concat([comb_pop, pgrs], axis=1)


        # Land coverage calculations
        land_t1 = self.load_data(input_files["land_t1"].file_path, kwargs=input_files["land_t1"].kwargs)
        land_t2 = self.load_data(input_files["land_t2"].file_path, kwargs=input_files["land_t2"].kwargs)
        land_t3 = self.load_data(input_files["land_t3"].file_path, kwargs=input_files["land_t3"].kwargs)

        land_t1 = self.filter_land_on_col(
            land_t1,
            input_files["land_t1"].filter_land_flag, 
            input_files["land_t1"].filter_land_col, 
            input_files["land_t1"].filter_land_value
        )[[input_files["land_t1"].land_col]]

        land_t2 = self.filter_land_on_col(
            land_t2,
            input_files["land_t2"].filter_land_flag, 
            input_files["land_t2"].filter_land_col, 
            input_files["land_t2"].filter_land_value
        )[[input_files["land_t2"].land_col]]

        land_t3 = self.filter_land_on_col(
            land_t3,
            input_files["land_t3"].filter_land_flag, 
            input_files["land_t3"].filter_land_col, 
            input_files["land_t3"].filter_land_value
        )[[input_files["land_t3"].land_col]]

        comb_land = pd.concat([land_t1, land_t2, land_t3], axis=1).dropna()

        t1_t2_lcr = self.land_consumption_rate(comb_land[input_files["land_t1"].land_col], comb_land[input_files["land_t2"].land_col], t1_t2_years).rename("t1_t2_lcr")
        t2_t3_lcr = self.land_consumption_rate(comb_land[input_files["land_t2"].land_col], comb_land[input_files["land_t3"].land_col], t2_t3_years).rename("t2_t3_lcr")

        lcrs = pd.concat([t1_t2_lcr, t2_t3_lcr], axis=1)

        land_calcs = pd.concat([comb_land, lcrs], axis=1)


        # combining for final calculations
        comb_derived_values = pd.concat([pgrs, lcrs], axis=1)

        lcr_pgr_ratio_t1_t2 = self.land_consumption_rate_population_growth_rate_ratio(comb_derived_values["t1_t2_lcr"], comb_derived_values["t1_t2_pgr"]).rename("lcr_pgr_ratio_t1_t2")
        lcr_pgr_ratio_t2_t3 = self.land_consumption_rate_population_growth_rate_ratio(comb_derived_values["t2_t3_lcr"], comb_derived_values["t2_t3_pgr"]).rename("lcr_pgr_ratio_t2_t3")

        final_values = pd.concat([lcr_pgr_ratio_t1_t2, lcr_pgr_ratio_t2_t3], axis=1)

        full_report = pd.concat([pop_t3["lsoa name"], pop_calcs, land_calcs, final_values], axis=1)
        full_report["bua_per_capita_t1"] = self.built_up_area_per_capita(full_report[input_files["land_t1"].land_col], full_report[input_files["pop_t1"].pop_col_rename])
        full_report["bua_per_capita_t2"] = self.built_up_area_per_capita(full_report[input_files["land_t2"].land_col], full_report[input_files["pop_t2"].pop_col_rename])
        full_report["bua_per_capita_t3"] = self.built_up_area_per_capita(full_report[input_files["land_t3"].land_col], full_report[input_files["pop_t3"].pop_col_rename])

        if save_csv:
            self.save_data(full_report, "sdg11_3_1")

        return True


def run_sdg11_3_1(params: UserParams) -> None:
    
    gfr: SDG11_3_1 = SDG11_3_1("", params.root_dir, params.data_dir, params.output_dir)

    gfr.calculate_sdg(
        params.input_files,
        params.save_csv_file
    )
