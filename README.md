# StravaTrainingUpload
## Needed tools
- Python
- Python request "pip install requests"
- Download stravaGetTokenAndUpload.py

## Download trainings
- Guide how to get all Sports Tracker trainings easily.
   * From below page just follow step 1 and use stravaGetTokenAndUpload.py to upload trainings
   * https://jarkkotervonen.com/2021/suoritustietojen-siirtaminen-sports-trackerista-stravaan/
- Guide how to download all Polar trainings
   * stravaGetTokenAndUpload.py is not supportin json format that Polar outputs so you need to convert to fit files using this tool: https://www.tredict.com/polarjson2fit-converter/
   * https://support.polar.com/en/how-to-download-all-your-data-from-polar-flow

## Uploading to Strava
- Open Command Promt
- type command: python stravaGetTokenAndUpload.py
- Follow instructions from script
   * Files can be placed to folder next to script
     
     ![image](https://github.com/JuhaO81/StravaTrainingUpload/assets/29195184/f695b61d-4565-44aa-99e7-6cbca4c72aee)


Credits: Juha Oravainen 
