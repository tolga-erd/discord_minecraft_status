import requests


def SetName(new_name,channelid):
    url = f"https://discord.com/api/v10/channels/"+str(channelid)

    headers = {
        "Authorization": f"Bot YOUR_DISCIRD_API_KEY",
        "Content-Type": "application/json"
    }

    data = {
        "name": new_name
    }

    requests.patch(url, headers=headers, json=data)

