library(RMySQL)
library(googleVis)

#connecting database in R

con2<- dbConnect(MySQL(), user="root" , password="iiita", dbname="analytics" , host="localhost")

#selecting the required dataframe 
qryStr <- paste("select date, minimum_temp from minimum_temp")

regData <- dbGetQuery(con2, qryStr)

#generating the output

bar <- gvisColumnChart(regData)

cat(bar$html$chart, file="tmp.html")