import time
import SunucuKontrol
import ChannelSetName
import json

oldStatus = None

while True:
    with open("Settings.txt","r") as file:
        settings = json.load(file)

    Status = SunucuKontrol.sunucuDurumu(settings["ip"])
    if Status != oldStatus:
        ChannelSetName.SetName(Status,settings["channelId"])
        oldStatus = Status
        print(Status)
    time.sleep(30)




