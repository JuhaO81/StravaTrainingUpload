# StravaTrainingUpload
Simple Python script based tool to upload all your trainings to Strava. Strava web client allows to upload only small amount of files per day and this script fixes that issue. Please note that Strava will still set some limitations to API usage. Check your limits from https://www.strava.com/settings/api. I was able to upload 200 files every 15 minutes.

# Needed tools
- Install these tools if needed
   * Python
   * Python request "pip install requests"
- Download stravaGetTokenAndUpload.py

# Uploading to Strava
- Open Command Prompt
- type command: python stravaGetTokenAndUpload.py
- Follow instructions from script
   * Files to be uploaded can be placed to folder next to script
   * Supported files are: fit, fit.gz, tcx, tcx.gz, gpx, gpx.gz
   * Only one type of files per upload. 
     
     ![image](https://github.com/JuhaO81/StravaTrainingUpload/assets/29195184/f695b61d-4565-44aa-99e7-6cbca4c72aee)

## Tips to download trainings
- Guide how to get all Sports Tracker trainings easily.
   * From below page just follow step 1 and use stravaGetTokenAndUpload.py to upload trainings
   * https://jarkkotervonen.com/2021/suoritustietojen-siirtaminen-sports-trackerista-stravaan/
- Guide how to download all Polar trainings
   * https://support.polar.com/en/how-to-download-all-your-data-from-polar-flow
   * stravaGetTokenAndUpload.py is not supportin json format that Polar outputs so you need to convert to fit files using this tool: https://www.tredict.com/polarjson2fit-converter/

Contact: juhao81@gmail.com
