# login-then-scrape-temperature

## Overview
This code will automatically do the following:
* Login to https://automated.pythonanywhere.com/login/
* Go to the Home Page
* Scrape the temperature and output it in a file 5 times.

## Prerequisite
* Install Python
* Install Selenium ("pip install selenium")
* Download Driver for launching the automation
  * For Chrome you can download the driver from https://chromedriver.storage.googleapis.com/index.html
  * Be sure to match the version of Chrome you have
* Input value for "driver_path" and "save_file_here" in info.json file.
  * "driver_path" is the path for your browser's driver
  * "save_file_here" is where you want the output file to be created/saved
