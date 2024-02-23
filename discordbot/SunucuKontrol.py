from mcstatus import JavaServer

def sunucuDurumu(ip,port=None):
    if port == None or port== 0:
        server = JavaServer.lookup(f"{ip}")
    else:
        server = JavaServer.lookup(f"{ip}:{port}")
    try:
        status = server.status()
        return f"Sunucu Aktif, {status.players.online} oyuncu bağlı"
    except Exception:
        return "Sunucu Kapalı"