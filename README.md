## Introduction

The Sustainable Development Goals (SDGs) are part of the UN 2030 Agenda for Sustainable Development. The Office for National Statistics (ONS) reports the UK data for the SDG indicators on the [UK SDG data website](https://sdgdata.gov.uk/).


The aim of goal 11 is to make human settlements inclusive, safe, resilient and sustainable. Target 11.3 focuses on enhancing inclusive and sustainable growth of cities and the sustainable planning of human settlements in all countries by 2030. Indicator 11.3.1 measures sustainable growth of urban areas and populations.

### Indicator 11.3.1: **Ratio of land consumption rate to population growth rate**

### Data

Population growth rates were calculated using the [ONS mid-year population estimates](https://www.ons.gov.uk/peoplepopulationandcommunity/populationandmigration/populationestimates/datasets/populationestimatesforukenglandandwalesscotlandandnorthernireland) for 2013 and 2016. These annual mid-year figures are available for various administrative and electoral geographies and for different population sub-groups. 

OS provided initial analysis for this indicator using data on land-use, derived from the [OS Master Map Topography Layer](https://www.ordnancesurvey.co.uk/business-government/products/mastermap-topography). The data distinguishes between natural and man-made features. They used the coverage of surfaces identified as man-made, to compute growth rates of land consumption between 2013 and 2016. The growth rate of man-made land was calculated for every Lower layer Super Output Area (LSOA), for the three countries in Great Britain (England, Scotland and Wales) and for the whole of Great Britain. 


## Methodology

### 1. Data preparation ###
- population data from LSOA mid-year estimates (ONS) and 
- land area data from OS

### 2. Investigate data ###
- LAD boundary changes between 2016 and 2019

### 3. Load data into python ###

### 4. Analysis ###
- join/merge 2016 data and 2019 data
- calculate PGR
- calculate LCR
- calculate Ratio LCR/PGR

### 5. Results/Output ###
- csv
- N/A LADs

### Calculations	

**Ratio of land consumption rate to population growth rate** = Land consumption rate / Population growth rate



**Population growth rate** = Natural logarithm ( Measurement year population / Previous population ) / Time between the measurement periods

**Land consumption rate** = Natural logarithm ( Measurement year manmade land area / Previous manmade land area ) / Time between the measurement periods

** Rates were calculated using the formula in the [UN metadata](https://unstats.un.org/sdgs/metadata/?Text=&Goal=11&Target=11.3). 

## Results

In Great Britain, land consumption grew faster than the population growth rate between 2013 and 2016. Land consumption grew by 4.3% and the population by 1.5%. Only in Wales did the population grow faster than the land consumption rate. Between 2013 and 2016, the population in Wales grew by 1.9% and the land consumption rate by 1.4%. Land consumption rate versus the population growth rate was the highest in Scotland, where the population grew by 1.4% and land consumption by 6.1%. In England, land consumption also grew faster than the population, with land consumption growing by 4.4% and the population by 2.3%. Scotland had the smallest population growth and the highest growth in land consumption, contributing to the high ratio.

## Output


Indicator: [Indicator 11.3.1
Ratio of land consumption rate to population growth rate](https://sdgdata.gov.uk/11-3-1/)

Dataset: [Ratio of land consumption growth rate to population growth rate by country and Lower layer Super Output Area](https://www.ons.gov.uk/economy/environmentalaccounts/datasets/ratiooflandconsumptiongrowthratetopopulationgrowthratebycountryandlowerlayersuperoutputarea)


Publication: [Using innovative methods to report against the Sustainable Development Goals](https://www.ons.gov.uk/economy/environmentalaccounts/articles/usinginnovativemethodstoreportagainstthesustainabledevelopmentgoals/2018-10-22)

### Limitations

Data were only produced for Great Britain, as the OS Land Use Layer is not available for Northern Ireland.

Data could not be calculated for all the LSOAs in Great Britain due to the population growth rates. In areas where population neither grew or declined, the formula could not be applied.

There is on-going research within ONS Geography to provide a more scalable solution to the monitoring of land consumption rates, as OS data are only available for Great Britain. The aim is to use satellite imagery to examine the amount of built-up land, in the whole of the UK. We are currently still working to select the right methodologies and processes.

### Contacts


Emma Wood (SDG Team: ONS) 

Robert Shava (Geospatial Team: ONS) 

Heather Porter (Geospatial Team: ONS) 










