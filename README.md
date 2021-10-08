# Azure SSH keys and PAT expiration monitoring

This python script was created to monitor the expiration date of Azure Personal Access Tokens (PAT) and SSH Keys.

It basically uses 2 APIs, one for SSK Keys and the other one for PAT. The APIs respond in a JSON object so the script basically goes through the JSON objects gathering different information and validating if the PAT/SSH Keys are still valid or not.

If any PAT/SSH Key will expire within the next 30 days, the script will show a message that says:
```less
PAT/SSH Key: "NAME OF KEY" will EXPIRE in one month or less
```
and exit with the corresponding error code (2).

</br><h2>Important:</h2>
To be able to use the script, you first need to create a PAT and provide it to the script, otherwise there is no way to authenticate to Azure.