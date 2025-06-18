### Overview:
This pipeline ingests tweledata security master and a subset of its end of day timeseries market data products. This is a personal project to deepen the understanding of multiprocessing, multithreading/coroutines in Python. 

TwelveData API: 
https://twelvedata.com/docs#getting-started


Pipeline Overview
#TODO - Add image

### How Its Made:
Language: Python, 
Libraries: Requests, Asyncio
Platforms Tools : AWS S3 

#### Security Master Ingestion


#### Timseries Data 
The local data is then staged and flattened for SQL consupmtion. 



### Optimizations

#### General


Known Errors and other:
- Their team  already has a package for processing their data in python: https://github.com/twelvedata/twelvedata-python. This is just project is just for **exploring API Ingestions**