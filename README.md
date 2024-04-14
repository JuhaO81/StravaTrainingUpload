# StravaTrainingUpload
## Needed tools
- Python
- Python request "pip install requests"
- Download stravaGetTokenAndUpload.py

## Download trainings
- Guide how to get all Sports Tracker training easily. From here just follow step 1 and use stravaGetTokenAndUpload.py to upload trainings https://jarkkotervonen.com/2021/suoritustietojen-siirtaminen-sports-trackerista-stravaan/
- Guide how to download all Polar trainings: https://support.polar.com/en/how-to-download-all-your-data-from-polar-flow
   * stravaGetTokenAndUpload.py is not supportin json format that Polar outputs so you need to convert to fit files using this tool: https://www.tredict.com/polarjson2fit-converter/

## Running the script
- Open Command Promt
- type command: python stravaGetTokenAndUpload.py
- Follow instructions from script
