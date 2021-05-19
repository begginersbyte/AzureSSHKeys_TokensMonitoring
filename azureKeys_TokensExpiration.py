import requests
import json
from datetime import date, timedelta, datetime
import sys

authenticationCode = 'AzurePATCodeHere'
#authenticationCode = str(sys.argv[1]) #Enable this option if you want to pass the PATCode as a parameter
today = date.today()
output = ''
expireSoon = 0
return_code = 0
#today = datetime.strptime('2025-02-17', '%Y-%m-%d').date() #THIS IS A TEST TO VALIDATE THE SOON TO EXPIRE KEYS

#CHECKING EXPIRATION DATE OF PERSONAL TOKENS
try:
    r = requests.get("https://vssps.dev.azure.com/<COMPANY>/_apis/Token/SessionTokens?displayFilterOption=1&api-version=5.0-preview.1", auth=('', '{}'.format(authenticationCode)))
    tokens = (r).json()

    for token in tokens.get("value"):
        if token.get("isValid") == True:
            datetime_object = datetime.strptime('T'.join(token.get("validTo").split('T')[:-1]), '%Y-%m-%d').date()
            lessOneMonth = datetime_object - timedelta(days=30)
            if today >= lessOneMonth:
                output += "Token: '" + token.get("displayName") + "' will EXPIRE in one month or less" + "\n"
                expireSoon = 1
            else:
                output += "Token: '" + token.get("displayName") + "' will not expire soon" + "\n" 


    #CHECKING EXPIRATION DATE OF SSH KEYS
    r = requests.get("https://vssps.dev.azure.com/<COMPANY>/_apis/Token/SessionTokens?isPublic=true&includePublicData=true&api-version=5.0-preview.1", auth=('', '{}'.format(authenticationCode)))
    sshkeys = (r).json()

    for sshkey in sshkeys.get("value"):
        if sshkey.get("isValid") == True:
            datetime_object = datetime.strptime('T'.join(sshkey.get("validTo").split('T')[:-1]), '%Y-%m-%d').date()
            lessOneMonth = datetime_object - timedelta(days=30)
            if today >= lessOneMonth:
                output += "SSH Key: '" + sshkey.get("displayName") + "' will EXPIRE in one month or less" + "\n"
                expireSoon = 1
            else:
                output += "SSH Key: '" + sshkey.get("displayName") + "' will not expire soon" + "\n" 

    if expireSoon == 1:
        return_code = 2

    print(output)
    sys.exit(return_code)

except Exception as e:
    print("Error when running the script. Check if the URL or authentication Token is correct")
    sys.exit(2)