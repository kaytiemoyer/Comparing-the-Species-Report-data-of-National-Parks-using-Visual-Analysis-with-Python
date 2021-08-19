# Comparing-the-Species-Report-data-of-National-Parks-using-Visual-Analysis-with-Python
# Data-Science-Practicum-II
## Project Overview
Does the amount of acreage in a national park affect the number of wild fauna that are reported within its borders? 

Every national park in the United States has a designated amount of acreage that is managed by the National Parks Department (NPD). For each species of plant and animal seen within the borders of a national park, a report is created and submitted to record the presence of that species in that location. This can be helpful when working to determine migration patterns, breeding habits, how seasonality can affect habitats and ecosystems, in addition to supplying conservationists with data to help locate and actively protect endangered species. 

## Data
#### Source: 
The data was taken from https://www.kaggle.com/nationalparkservice/park-biodiversity and sourced from https://irma.nps.gov/NPSpecies. Both the parks.csv and the species.csv were used for this project. 

#### Scope: 
Fifty-seven national parks located within the United States, including Alaska and Hawaii, were used for this data set. From those fifty-seven national parks, 119,249 reports were submitted pertaining to wild plants and animals located within the parks. 
## Process
This process was completed on a Windows 10 system, with  Python 3.9.0 and Spyder IDE 4.2.5. 
#### 1.	Retrieving, cleaning and organizing the data. 
This involved downloading the data from Kaggle.com and importing it into Spyder. A new environment was created through Anaconda command prompt to manipulate the libraries and their versions present in the working Spyder interface. This method allowed the use of different libraries without compromising the version of Spyder that was being used. 

The parks.csv data was cleaned by making sure there were no duplicate rows/reports within the data set, so that each occurrence of the park could be counted as one. The species.csv data was cleaned by removing all occurrences that equaled "Not Present" (the species was alleged to be located within the park but was not proven), and the record status was not approved. After this, the data sheets were combined by merging them together. Separate dataframes were created to focus on different comparation aspects. 

#### 2.	Completing basic analysis of the data. 
This inclluded a comparison of the acreage of all included national parks, a comparison of the species report for each park, and a basic analysis of the top five parks with the highest acreage against the top five parks with species reports. This was also done with the bottom five parks for both categories to determine if there was correlation between the two.  

#### 3.	Creating visualizations for further analysis. 
First came populating a geopandas map with a scatter plot of the locations of the national parks across the fifty United States. Then an interactive scatterplot was created to determine if there was correlation between the location of the national park and the species record count as a possible avenue for future research or analysis. 

#### 4.	Comparing visualizations and analysis to the hypothesis/research goal. 
The basic analysis showed no evident correlation between high amounts of acreage and species report count. It also did not show correlation between low amounts of acreage and species count. The initial answer to the research question would be in this case, "No". Exploring the data a little bit more, I compiled lists of the highest and lowest acreage amounts, comparing them with the highest and lowest species report counts, to which only one park out of ten showed up on both lists. 

## Visualizations
Figure 1; The Acreage of National Parks in the United States 
Figure 2; Total Species Report Count from National Parks 
Figure 3; A Comparison of the 5 Largest and 5 Smallest National Parks by Acreage 
Figure 4; A Comparison of the National Parks with the Highest and Lowest Species Report 
Figure 5; Relationship of National Park Acreage to Species Reports
Figure 6; Relationship of National Park Acreage to the State location 
Figure 7; Relationship of the number of Species Reports to the State location
Figure 8; Locations of National Parks in the United States 
Figure 9; Number of Species Reports separated by State

