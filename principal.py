import rpc
import time
from time import mktime

print("Discord com Presença rica")
client_id = 'ID_DO_SEU_CLIENT'  # Id da sua aplicação
rpc_obj = rpc.DiscordIpcClient.for_platform(client_id)
print("RPC conectado")

time.sleep(5)
start_time = mktime(time.localtime())
while True:
    activity = {
            "state": "Open-source is the way",  # Estado
            "details": "Dev em Shell Linux",  # Detalhes
            "timestamps": {
                "start": start_time
            },
            "assets": {
                "small_text": "Verificado",  # Texto da imagem pequena
                "small_image": "https://c.tenor.com/TgKK6YKNkm0AAAAi/verified-verificado.gif",  # Imagem pequena
                "large_text": "Sudo Rm -RF",  # Texto da imagem grande
                "large_image": "img"  # Imagem grande
            },
            "buttons": [
                {
                    "label": "Github",
                    "url": "https://github.com/JakeDystopia"
                },
                {
                    "label": "LinkTree",
                    "url": "https://linktr.ee/JakeDystopia"
                }
            ]
        }
    rpc_obj.set_activity(activity)
    time.sleep(900)

