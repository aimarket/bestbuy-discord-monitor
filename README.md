# Bestbuy Discord Monitor
![](https://img.shields.io/badge/stage-Pre--Alpha-orange)

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/f/f5/Best_Buy_Logo.svg/800px-Best_Buy_Logo.svg.png" alt="drawing" width="200" height="140"/><img src="https://i.imgur.com/ZOKp8LHg.png" alt="drawing" width="140" height="140"/>

## follow instructions in the main file
Detects if a product is back in stock and will notify on Discord using webhook

This uses the selenium webdriver for javascript websites(BESTBUY) to load in a headless browser.

I tried my best to add comments but if something needs better explination please let me know.

## Downloads:
Must have these:
[Firefox](https://www.mozilla.org/en-US/exp/firefox/new/),
[Geckodriver](https://github.com/mozilla/geckodriver/releases)
## Dependencies:
`pip install`
- selenium
- requests
- bs4

## HOW TO USE:
  `python main.py`

## Using on a CLI server:
If you want to use this on a server that only has a Command Line Interface refer to:
[Run Selenium Firefox Without GUI](https://stackoverflow.com/questions/10399557/is-it-possible-to-run-selenium-firefox-web-driver-without-a-gui)
