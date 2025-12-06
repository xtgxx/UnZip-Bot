import os

class Config(object):
     
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "8519660840:AAFr2vvWaHy3cQdShO25Gy_7RHCjMnE9Hrk")
    API_ID = int(os.environ.get("API_ID", 30507113))
    API_HASH = os.environ.get("API_HASH", "c3fcba6b883580362fef567fe452c1ba")
    MAX_FILE_SIZE = 2194304000
    
    
