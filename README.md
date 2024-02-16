## Introduction


The Sustainable Development Goals (SDGs) are part of the UN 2030 Agenda for Sustainable Development. The Office for National Statistics (ONS) reports the UK data for the SDG indicators on the [UK Sustainable Development Goals webpage](https://sdgdata.gov.uk/), contributing to progress towards a sustainable global future. 

Included in the 17 SDGs is Goal 11, which aims to ["Make cities and human settlements inclusive, safe, resillient and sustainable"](https://sdgs.un.org/goals/goal11). One indicator that supports this goal is **11.3.1: Ratio of land consumption rate to population growth rate**. 

This code aims to provide an automated calculation of SDG indicator 11.3.1 for the timely reporting on progress towards Goal 11. The most recent reporting of this indicator by the UK covers the years [2013-2016](https://sdgdata.gov.uk/11-3-1/).


## Set-up 


1. **Clone this repository** into the root directory you'd like to work from. 

2. **Install the SDG base class:** In the command-line interface, navigate to the root directory of the project and enter:

    `pip install .`

   The SDG base class handles methods common to all SDG indicator calculations and can be found in [this repository](https://github.com/ONSgeo/sdg_base).

4. **Create an environment variable** to set the address of the root directory. Using environment variables negates the need to enter personal information into the script. Open Notepad and write:

    `ROOT_DIR=C:\root\directory\address`
    
    Save this as the extension ".env" in the root directory. 

5. **Specify user parameters:** `user_params.py` requires user input:

- `root directory` will be taken from the environment variable.
- `data_dir` refers to the location of input data. If none is provided, it will assume the data is located within the root directory, in a folder named "sdg_x_x_x_data".
- `output_dir` refers to the location in which outputs should be stored. If none is provided, data will be output to the root directory as "sdg_x_x_x_output".
- For each population dataset (3 in total, t1 refers to "timestep 1"):
   
     - `pop_t1_file_path`: the file path for the population data for t1.
     - `pop_t1_kwargs`: any keyword arguments needed for reading the file.
     - `pop_t1_year`: the year the data is from.
     - `pop_t1_age_col`: the column with the population counts (generally will be all ages).
- For each land dataset (3 in total, t1 refers to "timestep 1"):
   
     - `land_t1_file_path`: the file path for the land coverage data for t1.
     - `land_t1_kwargs`: any keyword arguments needed for reading the file.
     - `land_t1_land_col`: the column with the land area data.
     - `land_t1_filter_land_flag`: flag if the data needs to be filtered at all.
     - `land_t1_filter_land_col`: column to filter the data on.
     - `land_t1_filter_land_value`: keeps the rows with the value in filter_land_col.


## Usage

Running `SDG11_3_1_Calculate.ipynb` will calculate SDG indicator 11.3.1.

### Input Data

This SDG indicator requires 3 distinct data types to be input: 

1. **Population estimates for a given time periods.** These should be to the smallest possible granularity. The assumed format for this data is .csv.

2. **Cover of land by manmade, urban, or built up structures for given time periods.** The assumed format of this data is .shp. 

3. **The geographical boundaries of the areas for which population estimates used were collected.** This is so that land consumption can be accuratley compared against population growth. The assumed format of this data is .shp.

Since this SDG indicator considers **rates**, the time at which the input data has been collected is important. Population estimates and land cover data to be compared should be collected **within the same year**, and preferably the same month. A wider temporal range between samples (5-10 years is recommended) will caputure more change than using consectutive years. Geographical boundaries must be uniform used to should correspond to the **most recent year** for which population has been sampled.  

Since the United Kingdom is made up of four countries, each with their own methods of collecting and publishing data, total input data will likely amount to more than 3 sources. The SDG indicator should only be calculated for countries where a full input dataset is available.  

[Further detail on requirements for SGG 11.3.1 as specified by the UN.](https://unstats.un.org/sdgs/metadata/files/Metadata-11-03-01.pdf) 

### Methodology

1. Data pertaining to population for time periods 1, 2 and 3 are read. The columns of interest (containing total population of all ages) in each dataframe are renamed to include the sampling year and the index is set the the geography code. The columns of interest are taken as series' and concatenated to a dataframe. This resultant dataframe contains population counts for geographies for each of the three time periods sampled. 

2. Population growth rate for each geography is calculated between time periods 1 and 2 and 2 and 3 by ((ln recent pop - ln past pop) / n of years) in a columnwise fashion. The results for each geography are stored as series' and concatenated into a dataframe of population growth rates.

3. Population numbers and population growth rates for each geography are combined into a comprehsive dataframe of population data required for each sampled time period. 

4. Data pertaining to landcover by urban areas for time periods 1, 2 and 3 are read in. If at this stage, if they need to be filtered (eg. if the data contains multiple types of land cover), this is specified using a boolean flag and completed. Geography code is set as the index and the series' are concatenated into a dataframe with containing land cover by urban areas for geogrpahies for each sampled time period. 

5. Land consumption rate for each geography is calculated between time periods 1 and 2 and 2 and 3 by (((recent consumption rate - past consumption rate)/past)/ n of years) in a columnwise fashion. The results for each geography are stored as series' and concatenated into a dataframe of land consumption rates.

6. Land cover and land consumption rates for each geography are combined into a comprehsive dataframe of urban-cover required for each sampled time period. 

7. Population growth rate and land consumption rate are concatenated into a dataframe for columnwise calulation of the ratio of land consumption rate to population growth rate by (land consumption rate/ population growth rate) for time periods 1 and 2 and 2 and 3.

8. A full report is created by concatenating all raw and calculated values for each geography and between sampled time periods. The corresponding name of geography code is reintroduced for clarity in reporting.

9. The additonal metric of built- up area per capita is calculated for each sampled year by (built-up area / population) for each geography. 

10. To enable reporting on a national level, the first character of each geography code is isolated and assigned to a new column from which groupby.sum() is used.

Full programatic calculation and methodology is found within `in sdg_11_3_1_src/sdg_11_3_1.py`. 

### Outputs

Currently available outputs include:

- A full report of population numbers, land cover, population growth rate, land consumption rate, ratio of land consumption to population growth rate and built-up area per captita per small area geography for (and between) each sampled time period (.csv). 

- A full report of the same metrics as above, for each country (.csv). 


## Notes


### Previously used data sources
    
Great Britain (land consumption): Ordnance Survey Master Map Topography, manmade layer. 
(https://www.ordnancesurvey.co.uk/products/os-mastermap-topography-layer)
    
England and Wales (population):Lower-Layer Super Output Area (LSOA) Population estimates, ONS.             (https://www.ons.gov.uk/peoplepopulationandcommunity/populationandmigration/populationestimates/datasets/lowersuperoutputareamidyearpopulationestimates)
        
England and Wales (statistical geography boundaries): LSOAs, ONS Open Geography Portal. 
(https://geoportal.statistics.gov.uk/datasets/3011969ff4e84966b2cbc3b642ae32de_0/explore?location=50.170958%2C-5.597654%2C5.68)
    
Scotland (population): Small Area Population Estimates (SAPE), Data Zone based, National Records of Scotland. 
(https://www.nrscotland.gov.uk/statistics-and-data/statistics/statistics-by-theme/population/population-estimates/small-area-population-estimates-2011-data-zone-based/time-series)
    
Scotland (statistical geography boundaries): Data Zones, SpatialData.gov.scot.
(https://spatialdata.gov.scot/geonetwork/srv/eng/catalog.search#/metadata/7d3e8709-98fa-4d71-867c-d5c8293823f2)

Northern Ireland (population): Small Area population estimates, Northern Ireland Statistics and Research Agency.
(https://www.nisra.gov.uk/publications/2019-mid-year-population-estimates-small-areas)

Northern Ireland (statistical geography boundaries): Small Areas, Northern Ireland Statistics and Research Agency.
(https://www.nisra.gov.uk/support/output-geography-census-2011/small-areas)

Northern Ireland (land consumption): Ordnance Survey Northern Ireland - NOT CURRENTLY AVAILABLE: will need discussion with OSNI as may not be free as under the GB PSGA agreement.  

### Considerations
 - wihotut the third time period, this wouldnt work. if you dont have a third data set a null dataset can be put in that wont calcualte and results but the first time period will be calcualted as normal. 
- shouldn't use division with logs (even thought the UN say to). in log space, division and subtraction are the samebut the subrtraction is safer for undefined values.
-  the code is unreadbale and could be in more functions.
-  Assumed data formats - if they're not used and better ones are found, changes to the methods will be required.
-  manmade coverage does acocunt for upwards building. 
