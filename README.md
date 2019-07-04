# Scrape javascript based webpages with using scrapy and splash 
simple application for scrape sinhala web articles which are related to science topics by using css selectors of their web site.
First of all clone this repo `git clone https://github.com/MaheshSuranga/WebScraping.git`
# Prerequisites
1. Install scrpay either in PyPI or conda

    `conda install -c conda-forge scrapy` or `sudo pip install Scrapy`
  
2. Install [Docker](https://www.docker.com/) and log into your docker account through your terminal

    `docker login -u <username> -p <password>`
    
3. Pull the image

    `sudo docker pull scrapinghub/splash`
    
4. Intsall scrapy-splash

    `pip install scrapy-splash`
    
5. Edit the `settings.py` file with following script
    ```
    SPLASH_URL = 'http://localhost:8050'
    DOWNLOADER_MIDDLEWARES = {
        'scrapy_splash.SplashCookiesMiddleware': 723,
        'scrapy_splash.SplashMiddleware': 725,
        'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 810,
    }
    SPIDER_MIDDLEWARES = {
        'scrapy_splash.SplashDeduplicateArgsMiddleware': 100,
    }
    DUPEFILTER_CLASS = 'scrapy_splash.SplashAwareDupeFilter'
    ```
    
6. Start the container

    `sudo docker run -p 8050:8050 scrapinghub/splash`
    
7. Finally run our script inside root folder

    `scrapy crawl articles -o article.json`
    
