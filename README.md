This repository includes automated tests for [Version 1](https://demo.applitools.com/gridHackathonV1.html) 
and [Version 2](https://demo.applitools.com/gridHackathonV2.html) of `Applifashion`.


## Languages and Frameworks
The project uses the following languages and frameworks:
* Python 3.x as the programming language
* pytest as the test framework
* Selenium WebDriver as the web browser automation framework
* webdriver-manager as the Selenium binaries manager
* Applitools Eyes SDK for visual testing


## Setup and Running Tests
* `requirements.txt` file includes all the necessary packages to install on your virtual environment.
* Applitools API Key is being used as an environment variable.
* To run tests, use the `python -m pytest ./tests/test_traditional_v1.py` command. 
By default, the tests will be running on the Chrome browser and on the Laptop device. 
If you want to run them with other parameters, use the following options in the terminal: 
`--browser=firefox --device=tablet`.  
Acceptable values for browsers: `chrome`, `firefox`, `edge_chromium`, `ie`  
Acceptable values for devices: `laptop`, `tablet`, `mobile`
* The results of traditional tests will be recorded in txt files. The separate files have been created for 
Version 1 and Version 2.


## Author
Vica Markosyan