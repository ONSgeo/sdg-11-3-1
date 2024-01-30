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

4. Userparams class 

## Usage 
?

## Input Data

This SDG indicator requires 3 distinct data types to be input: 

1. **Population estimates for a given time periods.** These should be to the smallest possible granularity (LSOAs have been used previously). The likely format for this data is .csv.

2. **Cover of land by manmade, urban, or built up structures for given time periods.** The likely format of this data is .shp. 

3. **The geographical boundaries of the areas for which population estimates used were collected.** This is so that land consumption can be accuratley compared against population growth. The likely format of this data is .shp.

Since this SDG indicator considers **rates**, the time at which the input data has been collected is important. Population estimates and land cover data to be compared should be collected **within the same year**, and preferably the same month. A wider temporal range between samples (5-10 years is recommended) will caputure more change than using consectutive years. Geographical boundaries must be uniform used to should correspond to the **most recent year** for which population has been sampled.  

Since the United Kingdom is made up of four countries, each with their own methods of collecting and publishing data, total input data will likely amount to more than 3 sources. 

[Further detail on requirements for SGG 11.3.1 as specified by the UN.](https://unstats.un.org/sdgs/metadata/files/Metadata-11-03-01.pdf) 

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

## Methodology


       

## Outputs


### Considerations

