import requests
import json
import sys
import datetime
DISCORD_ENDPOINT = sys.argv[1]
TRAVIS_BUILD_NUMBER = sys.argv[2]
TRAVIS_BUILD_WEB_URL = sys.argv[3]
TRAVIS_REPO_SLUG = sys.argv[4]

payload_json = {
    "embeds": [{
        "title": "WormJam CI Report",
        "color": 10027008,
        "description": "A build has failed from [%s](%s)"%(TRAVIS_REPO_SLUG,"https://github.com/"+TRAVIS_REPO_SLUG),
        "fields":[
            {
                "name": "Build Number",
                "value":str(TRAVIS_BUILD_NUMBER)
            },
            {
                "name":"Build logs",
                "value":"Logs can be found [here]("+TRAVIS_BUILD_WEB_URL+")"
            }
        ],
        "thumbnail": {
            "url": "https://travis-ci.com/images/logos/Tessa-1.png"
        },
        "timestamp": str(datetime.datetime.now().isoformat())
    }]
}
r =requests.post(DISCORD_ENDPOINT,data=json.dumps(payload_json), headers={"Content-Type": "application/json"})