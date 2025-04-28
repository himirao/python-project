# python-project
electric vehicle program
As the global shift toward sustainable transportation accelerates, electric vehicles (EVs) have 
become a focal point of environmental and technological advancement. This analysis explores 
a real-world dataset detailing electric vehicle registrations across different regions, years, 
makes, and models. By leveraging Python libraries such as Pandas, Matplotlib, Seaborn, and 
SciPy, the study conducts a comprehensive data-driven exploration to uncover trends, patterns, 
and insights into EV adoption. The data is first cleaned and prepared to ensure reliability, 
followed by initial exploratory steps to understand the structure and quality of the dataset. 
The core of the analysis investigates several key aspects, including the distribution of EV types, 
leading manufacturers and models, regional adoption trends, and the evolution of EV usage 
over time. Visualizations such as bar charts, pie charts, and line graphs are used to make the 
insights more intuitive and impactful. Additionally, statistical techniques such as hypothesis 
testing, correlation analysis, and normality checks are applied to derive deeper meaning from 
the data. A notable inclusion is the estimation of CO₂ emissions potentially saved by EV usage, 
offering an environmental perspective to complement the market analysis. Together, these 
insights contribute to a clearer understanding of the current state and growth trajectory of 
electric vehicle adoption. 
.  
SOURCE: 
The 
data 
used 
in 
this 
project 
was 
from 
thehttps://catalog.data.gov/dataset/?res_format=CSV , Categories covered by this include: 
obtained 
 VIN (1-10) – Vehicle Identification Number (partial) 
 County – The county where the vehicle is registered 
 City – The city where the vehicle is registered 
 State – The state of registration (likely all WA) 
 Postal Code – ZIP code of the registered address 
 Model Year – Year the EV model was manufactured 
 Make – Vehicle manufacturer (e.g., Tesla, Nissan) 
 Model – Specific model name (e.g., Model 3, Leaf) 
 Electric Vehicle Type – BEV (Battery Electric) or PHEV (Plug-in Hybrid) 
 Clean Alternative Fuel Vehicle (CAFV) Eligibility – Whether the vehicle qualifies for 
Washington state incentives 
 Electric Range – Estimated electric-only driving range 
 Base MSRP – Manufacturer's suggested retail price 
 Legislative District – Political district of registration 
 DOL Vehicle ID – Department of Licensing ID 
 Vehicle Location – Latitude and longitude of the vehicle’s registered location 
 Electric Utility – The utility company servicing the address 
 2020 Census Tract – Census data tract code for demographic reference 
The raw CSV files were processed using Python to extract relevant attributes for deriving 
vehicle data, registrations and match environmental impact.  
LINK: 
https://catalog.data.gov/dataset/electric-vehicle-population
data/resource/fa51be35-691f-45d2-9f3e-535877965e69 
EXPLANATORY DATA ANALYSIS (EDA): 
The EDA process was carried out in a structured and categorized manner to reveal information 
in a systematic order. All steps followed in achieving a comprehensive EDA are listed below 
coupled with my personal understanding of what the data indicates as deemed necessary. 
1. Data Cleaning 
The first and most important step in EDA is ensuring the quality of data. In this process: 
 The dataset is loaded from a CSV file. 
 Rows with missing or incomplete key information—like vehicle type, make, model, location, 
and model year—are removed. This prevents unreliable results during analysis and ensures 
that only meaningful and valid data is retained. 
�
� 2. Initial Data Exploration 
After cleaning, we need to understand the structure and content of the dataset: 
 Viewing the first and last few records helps check if the data was read correctly. 
 Summary functions like info() and describe() give an overview of data types, value ranges, 
and statistics (like mean, median, mode, etc.). 
 Checking the shape tells us the number of rows and columns. 
 Counting missing values in each column helps assess data completeness. 
This stage builds familiarity with the dataset before deeper analysis begins. 
�
� 3. Univariate Analysis (Single-Variable Trends) 
This step involves analysing one variable at a time: 
 The proportion of Battery Electric Vehicles (BEVs) and Plug-in Hybrid Electric Vehicles 
(PHEVs) is shown using a pie chart. This reveals which type of EV is more common. 
 Distribution of EV types over model years is visualized with a stacked bar chart, showing 
how each type’s popularity has changed over time. 
�
� 4. Brand and Model Popularity 
Identifies the top 10 manufacturers by number of EVs registered. 
 Constructs a combined "Make + Model" name and finds the top 10 EV models. These bar 
plots highlight the dominant players in the EV market. 
�
� 5. Geographic Trends 
This part focuses on locations where EVs are popular: 
 The top 10 counties and cities with the highest number of EV registrations are visualized. 
This helps identify geographic hotspots of EV adoption. 
�
� 6. Trend Analysis Over Time 
To understand the evolution of EV adoption: 
 A line chart plots the number of vehicles registered over the years. 
 A grouped bar chart compares the number of BEVs and PHEVs registered year by year. 
This gives insight into growth trends and shifts in preferences between types. 
�
� 7. Environmental Impact Estimation 
A simple estimation is made of how much CO₂ emissions have been reduced due to the use of EVs: 
 It assumes a fixed average mileage and CO₂ emission rate for internal combustion vehicles. 
 The total emissions avoided is calculated and presented in millions of kilograms. 
This connects the dataset to broader environmental implications. 
�
� 8. Correlation Analysis 
The code then explores relationships between numeric variables: 
 A correlation heatmap shows how different numeric features are related (e.g., do newer cars 
cost more or travel farther?). This is useful to identify possible patterns or trends among 
numeric data. 
�
� 9. Statistical Analysis 
Finally, several statistical tests are applied: 
 A t-test compares the average model years of BEVs and PHEVs to see if one type tends to be 
newer. 
 A z-score analysis identifies manufacturers whose EV registration numbers are significantly 
higher than others (i.e., statistical outliers). 
Analysis 
**1. Data Cleaning & Preparation:** The first objective of the code is to ensure that the dataset is 
cleaned and organized, making it ready for analysis. Missing values in critical columns such as 
`Electric Vehicle Type`, `Make`, `Model`, `County`, `City`, and `Model Year` are dropped to avoid 
inaccuracies or biases in the results. Data cleaning is an essential step, as incomplete or irrelevant data 
can lead to misleading visualizations or incorrect statistical conclusions. By removing rows with 
missing values, the dataset becomes consistent and reliable, laying a strong foundation for further 
analysis. 
**2. Initial Data Exploration:** This objective focuses on understanding the dataset's structure and 
contents. The `.head()` and `.tail()` methods provide snapshots of the beginning and end of the dataset, 
helping to grasp its layout and range of entries. The `.info()` method sheds light on data types, null 
values, and memory usage, giving insight into the dataset's technical composition. Descriptive 
statistics are produced by `.describe(include='all')`, summarizing measures such as central tendency, 
dispersion, and frequency for numerical and categorical columns. Additionally, `.isnull().sum()` 
identifies the exact number of missing values across columns, ensuring no overlooked gaps in data
