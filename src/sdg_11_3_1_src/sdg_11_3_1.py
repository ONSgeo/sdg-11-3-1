from typing import Dict, List, Optional, Tuple, Union
import numpy as np
import pandas as pd
import geopandas as gpd
import rasterio as rio

from src.sdg_11_3_1_src.sdg_base.src.sdg_base_src.sdg_base import SDGBase
from src.sdg_11_3_1_src.utils import InputFile
from user_params import UserParams

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


    def calculate_sdg(
            self, 
            input_files: Dict[str, InputFile],
            merge_col: str,
            pop_cols: List[str],
            land_cols: List[str],
            years: int,
            years_merge_suffixes: Tuple[str, str],
            data_suffix: str
        ) -> bool:
        self.data_suffix: str = data_suffix

        pop_old = self.load_data(
            input_files["pop_old"].file_path, 
            kwargs=input_files["pop_old"].kwargs, 
            index=input_files["pop_old"].index_col
        )
        pop_new = self.load_data(
            input_files["pop_new"].file_path, 
            kwargs=input_files["pop_new"].kwargs, 
            index=input_files["pop_new"].index_col
        )

        pop_merge = self.merge_population_calc_pgr(pop_old, pop_new, merge_col, pop_cols, years_merge_suffixes, years)


        land_area_old = self.load_data(
            input_files["land_area_old"].file_path, 
            kwargs=input_files["land_area_old"].kwargs, 
            index=input_files["land_area_old"].index_col
        )
        land_area_new = self.load_data(
            input_files["land_area_new"].file_path, 
            kwargs=input_files["land_area_new"].kwargs, 
            index=input_files["land_area_new"].index_col
        )

        filt_old_cond = (land_area_old["ctry"] == "E") | (land_area_old["ctry"] == "W") # filter to separate EW data
        land_area_old_filtered= land_area_old.loc[filt_old_cond].copy()

        filt_new_cond = (land_area_new["landcover_type"]=="Manmade") # filter "manmade" landcover for EW
        land_area_new_filtered = land_area_new.loc[filt_new_cond]

        land_area19_16ewmm = self.merge_land_consumption_calc_lcr(land_area_old_filtered, land_area_new_filtered, merge_col, land_cols, years_merge_suffixes, years)


        lcrpop_merge = self.merge_lcr_pgr(pop_merge, land_area19_16ewmm, merge_col, [f"lcr_{self.data_suffix}", f"pgr_{self.data_suffix}"], ("_pgr", "_lcr"))

        final_df = pd.concat([pop_merge, land_area19_16ewmm, lcrpop_merge], axis=1)
        
        return final_df.loc[:,~final_df.columns.duplicated()]



def run_sdg11_3_1(params: UserParams) -> None:
    
    gfr: SDG11_3_1 = SDG11_3_1("", params.root_dir, params.data_dir, params.output_dir)

    if params.single_year_test and all([params.raster_file_path, params.ruc_file_path, params.lad_file_path, params.roads_file_path, params.year_start]):
        print(f"Running single year export for year: {params.year_start}")
        gfr.calculate_sdg(
            ""
            # raster_file_path = params.raster_file_path,
            # ruc_file_path = params.ruc_file_path,
            # lad_file_path = params.lad_file_path,
            # roads_file_path = params.roads_file_path,
            # rural_class_col = params.rural_class_col,
            # road_class_col = params.road_class_col,
            # road_classif_list = params.road_classif_list,
            # dissolve_col = params.dissolve_col,
            # year = params.year_start,
            # save_shp_file=params.save_csv_file,
        )

    else:
        print("Execution failed, please check necessary params:\n")
        params.print_params()