
library(DataCombine)
library(rpart)
library(stringr)
library(RSelenium)
library(rvest)
library(XML)
library(digest)

options(stringsAsFactors = F)
#Get standard league table from skysports.com
Dat <- NULL
for (i in 2009:2017){
teamStats <- readHTMLTable(paste0("http://www.skysports.com/premier-league-table/", i))
names(teamStats) <- NULL
teamStats <- data.frame(teamStats)
teamStats$Year <- i
Dat <- rbind(Dat, teamStats)
}

####Housekeeping!#####
Dat$X. <- NULL
Dat$Last.6 <- NULL

Dat[, 2 : 9] <- apply(Dat[, 2:9], 2, function(x) as.integer(as.character(x)))
Dat$Team <- factor(str_replace_all(as.character(Dat$Team),pattern = "[*]",''))

#Create a lead variable for the Premier League points 
datasetLagged <- slide(Dat,Var = "Pts",TimeVar = "Year",GroupVar = "Team",slideBy = +1)
names(datasetLagged)[ncol(datasetLagged)] <- 'leadPoints'


####Rendering whoscored.com website using a remote selenium driver and getting data####
 remDr <- remoteDriver(port = 4445)
 remDr$open()
 remDr$navigate("https://www.whoscored.com/Regions/252/Tournaments/2/Seasons/5826/Stages/12496/TeamStatistics/England-Premier-League-2016-2017")
 inTable <- NULL
 for (i in 2:8){
 clicktype <- remDr$findElement(using = "css selector", '#seasons')
 remDr$mouseMoveToLocation(webElement = clicktype)
 clicktype$click()
 clicktype <- remDr$findElement(using = "css selector", paste0('#seasons > option:nth-child(',i,')'))
 remDr$mouseMoveToLocation(webElement = clicktype)
 clicktype$click()
 clicktype <- remDr$findElement(using = "css selector", '#sub-navigation > ul:nth-child(1) > li:nth-child(3) > a:nth-child(1)')
 remDr$mouseMoveToLocation(webElement = clicktype)
 clicktype$click()
 doc <- remDr$getPageSource()[[1]]
 firstTable <- htmlParse(doc)
 

v=readHTMLTable(firstTable, as.data.frame = T)
v= v[c(1,3,6)]
names(v) = NULL
v=lapply(v, function(x){data.frame(x)})
 write.table(v, file = "footyData.csv", na = "", sep=',')
 }
