# TimeSeries_CCF_BotsandHumans
#### This repository provides code to reproduce the results of "The Rise of Humans: The influence of humans on bots in political discussions" (under review)

1. **botornot.py** fetches user scores from botornot API.
   - It processes a CSV file, which contains a set of Tweet IDs, makes a call to the Twitter API to fetch the User ID for each Tweet ID and sends each User ID to the botometer API to collect results for each user. 

2. **toneanalyzer.py** fetches the tone analysis results for each Tweet Text. 
   - It proccesses a CSV file, which contains a set of Tweet IDs, makes a call to the Twitter API to fetch the full text data for each Tweet ID and sends each tweet text to the IBM Watson Tone Analyzer to collect results for each tweet text. 

3. **TimeSeriesCCF.rmd** assesses the relationship (cross correlation) between two time series. 
   - It checkes for auto-correlation, specifies an ARIMA model, pre-whitens series to remove the auto-correlation between time points, runs a correlation analysis with prewhitened series and produces a plot of the results as output. 
