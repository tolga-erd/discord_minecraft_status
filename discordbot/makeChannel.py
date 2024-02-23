import requests

# Sunucu (guild) ID'sini, yeni kategori adını ve yeni kanal adını değiştirin (sunucu ID'si, yeni kategori adı ve yeni kanal adıyla değiştirin)
guild_id = "GUILD_ID"
new_category_name = "SUNUCU DURUMU"
new_channel_name = "KAPALI"

# Bot tokeninizi ekleyin
token = "YOUR_DISCORD_API_KEY"

# Yeni kategori oluşturma
category_url = f"https://discord.com/api/v10/guilds/{guild_id}/channels"

category_data = {
    "name": new_category_name,
    "type": 4  # Kategori türü
}

headers = {
    "Authorization": f"Bot {token}",
    "Content-Type": "application/json"
}

r = requests.post(category_url, headers=headers, json=category_data)

if r.status_code == 201:
    category = r.json()
    print(f"{new_category_name} adında yeni bir kategori oluşturuldu.")

    # Kategoriye bağlı yeni kanal oluşturma
    channel_url = f"https://discord.com/api/v10/guilds/{guild_id}/channels"

    channel_data = {
        "name": new_channel_name,
        "type": 2,  # Metin kanalı türü
        "parent_id": category["id"]  # Kategoriye bağlama
    }

    r = requests.post(channel_url, headers=headers, json=channel_data)

    if r.status_code == 201:
        channel = r.json()
        print(f"{new_channel_name} adında yeni bir kanal oluşturuldu.")

        # Kategoriyi en üst sıraya taşıma
        positions_url = f"https://discord.com/api/v10/guilds/{guild_id}/channel_positions"

        positions_data = [
            {
                "id": category["id"],
                "position": 0  # Kategoriyi en üst sıraya taşımak için 0 yapın
            }
        ]

        r = requests.patch(positions_url, headers=headers, json=positions_data)

        if r.status_code == 200:
            print(f"{new_category_name} kategorisi en üst sıraya taşındı.")
        else:
            print(f"Kategori Taşıma Hata Kodu: {r.status_code}, Hata Mesajı: {r.text}")

    else:
        print(f"Kanal Oluşturma Hata Kodu: {r.status_code}, Hata Mesajı: {r.text}")

else:
    print(f"Kategori Oluşturma Hata Kodu: {r.status_code}, Hata Mesajı: {r.text}")
