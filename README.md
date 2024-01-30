## Introduction

The Sustainable Development Goals (SDGs) are part of the UN 2030 Agenda for Sustainable Development. The Office for National Statistics (ONS) reports the UK data for the SDG indicators on the [UK Sustainable Development Goals webpage](https://sdgdata.gov.uk/), contributing to progress towards a sustainable global future. 

Included in the 17 SDGs is Goal 11, which aims to ["Make cities and human settlements inclusive, safe, resillient and sustainable"](https://sdgs.un.org/goals/goal11). One indicator that supports this goal is **11.3.1: Ratio of land consumption rate to population growth rate**. 

This code aims to provide an automated calculation of SDG indicator 11.3.1 for the timely reporting on progress towards Goal 11. The most recent reporting of this indicator by the UK covers the years [2013-2016](https://sdgdata.gov.uk/11-3-1/).

## Set-up 
?
1. Clone this repository into the directory you'd like to work from. 
    
2. Create a .env file to set the directory from which inputs will be imported and results will be exported:

   Open the Notepad app and write ROOT_DIR= followed by the directory in which the input data is stored (and results we be exported to),  eg: 
    
    ROOT_DIR=C:\Users\username\scripts\sdg11_3_1     

Save this notepad as a .env file within the cloned repository.

4. Userparams class assumes that input data will be located in the main directory within a folder named sdg_name_data, eg:

## Usage 
?

## Input Data

This SDG indicator requires 3 distinct data types to be input: 

1. **Population estimates for a given time periods.** These should be to the smallest possible granularity (LSOAs have been used previously). The likely format for this data is .csv.

2. **Cover of land by manmade, urban, or built up structures for given time periods.** The likely format of this data is .shp. 

3. **The geographical boundaries of the areas for which population estimates used were collected.** This is so that land consumption can be accuratley compared against population growth. The likely format of this data is .shp.

Since this SDG indicator considers **rates**, the time at which the input data has been collected is important. Population estimates and land cover data to be compared should be collected **within the same year**, and preferably the same month. Geographical boundaries must be uniform used to should correspond to the **most recent year** for which population has been sampled.  

Since the United Kingdom is made up of four countries, each with their own 

### Definitions	

According to the Food and Agriculture Organization of the United Nations (FAO), Forest is defined as: “land spanning more than 0.5 hectares with trees higher than 5 meters and a canopy cover of more than 10 percent, or trees able to reach these thresholds in situ. It does not include land that is predominantly under agricultural or urban land use”. In the United Kingdom, forest is defined as below:

**Forest/woodland** all forest and woodland area over 0.5 hectare with a minimum of 20% canopy cover (25% in Northern Ireland) (or the potential to achieve it) and a minimum width of 20 metres, including areas of new planting, clearfell, windblow and restocked areas. This differs from the UN definition for which the minimum canopy cover is 10% (or the potential to achieve it)

**Land area**  is the country area excluding area under inland waters and coastal waters. For this analysis, total land area is calculated using Standard Area Measurements (**SAM**) available on the [ONS Open Geography portal](https://geoportal.statistics.gov.uk/search?collection=Dataset&sort=name&tags=all(PRD_SAM)). All measurements provided are ‘flat’ as they do not take into account variations in relief e.g. mountains and valleys. Measurements are given in hectares (10,000 square metres) to 2 decimal places. Four types of measurements are included: total extent (AREAEHECT), area to mean high water (coastline) (AREACHECT), area of inland water (AREAIHECT) and area to mean high water excluding area of inland water (land area) (AREALHECT) which is the type used for this analysis.



### Data

       Forest/Woodland data - Forestry Commission Open Data (GB) and DAERA (NI).  
       Land area - Local authority districts (LADs) boundaries from ONS Open Geography portal.
       SAM for LADs from ONS Open Geography portal.

### Methodology

    SDGBase was designed to present a resusable base class applicable to the analysis of multiple SDGs.   

    SDG15_1_1 is a child class of SDGBase and performs functions relevant to the analysis of SDG15_1_1. It is potentially applicable to the
    analysis of further SDGs with input data of a similar structure. 
    
    UserParams class offers customisation to the user; directories from which to input data, save output data and select
    the years for which the SDG is to be calculated. 
    
    Once UserParams are specified, SDG15_1_1_Calculate.ipynb allows the user to calculate SDG15_1_1 across multiple years and 
    outputs results as both a data frame and a choropleth map.   
    
    SDG15_1_1_Analysis.ipynb offers the user further insight into the data, allowing SDG metrics to be explored by individual land               divisions across time. 
       
### Calculation
    
    Forest area as a proportion of total land area (PFATLA) = Forest area (reference year)/Land area (reference year)*100 

### Analysis

    SDGBase presents an abstract base class enabling the defintion of input and output directories for data analysis, use of relevant
    read methods based on the file extension of inputs, and the joining of dataframes; applicable to 
    analysis of additional SDGs.  
    
    SDG15_1_1 is a child class of SDGBase and allows for the automatic pairing of data input files published in the same year, 
    analysis across multiple years, calculation of SDG15_1_1 and plotting and saving of results.     
    
    SDG15_1_1_Calculate.ipynb allows the user to calculate SDG15_1_1 from the file directories specified in UserParams class and produces
    and saves outputs (forest area as a proportion of total land area for each specified land division) for each available year as both a       .csv file and as a choropleth map (.jpeg).
    
    SDG15_1_1_Analysis.ipynb allows plotting of a time series of forest area as a proportion of total land area for each land division         across available years.   
              
### Outputs



    SDG15_1_1_Calculate.ipynb produces outputs for each specified year as a .csv file (forest area as a proportion of total land area for       each specified land division) and a.jpeg (choropleth map of forest area as a proportion of total land area). 
    
    SDG15-1_1_Analysis.ipynb allows plotting of a time series of forest area as a proportion of total land area for each land division         across available years.   
       
       
