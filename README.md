# Covid-19 Informational Site to Help NYC Residents Feel Calmer and More Humanized After Searching the Term "Covid-19 Cases NYC"
Dashboard for visualizing Covid-19 cases in NYC. 

[Talk on why we made the site](https://www.youtube.com/watch?v=hhVuUESnl6Q&t=6s)


* AWS Lambda Functions pull up-to-date data from city, state and world to store into a relational database to update plotly graphs on the site. 
* We used Route53 to route our Elastic Beanstalk app to covid19casesnyc.com.
* We are working on implementing AWS CloudFront as a CDN Elastic Cache to speed up loading performance. 

![workflow](https://i.imgur.com/HfwEXi7.png)
![database](https://i.imgur.com/tooJ5Ys.jpg)
![automation diagram](https://i.imgur.com/SMR5WEQ.jpg)
![site](https://i.imgur.com/zqNhLHD.png)
![nyc graphs](https://i.imgur.com/foSe3R7.png)
![nyc demographics with covid](https://i.imgur.com/tF1jDBQ.png)
![ny state cases](https://i.imgur.com/IOLOOtw.png)
![ny state counties](https://i.imgur.com/k5MqVvE.png)
![stacked graphs](https://i.imgur.com/DcUaGsp.png)
![us china italy day to day changes](https://i.imgur.com/6sY4QwC.png)
![us predictions](https://i.imgur.com/gFOkNtl.png)
![data sources](https://i.imgur.com/onG401r.png)
