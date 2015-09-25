# BigData_Handling
To generate analytics from a given large dataset of US temperature and weather
The following codes are attached in this repository

	1. maxtemp.py
	2. mintemp.py
	3. output1.R
	4. output2.R
	5. temp.html
	6. temp1.html
	7. view.html


	1. maxtemp.py is python file which does spark's in-memory map and reduce operations and thus for a given day it calculates the average max_temperature.  
	2. mintemp.py is python file which does spark's in-memory map and reduce operations and thus for a given day it calculates the average min_temperature.  
	3. output1.R is R script file which uses the max_temperature table of analytics database and uses googleVis to produce the necessary visualisation.
	4. output2.R is R script file which uses the minimum_temp table of analytics database and uses googleVis to produce the necessary visualisation.
	5. temp.html and temp1.html are necessary html file produced by R's googleVis module.
	6. view.html uses iframe's to showcase the the two generated visualisation which are actually columnCharts.
