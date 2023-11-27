import os

class Config:
    API_ID = int( os.getenv("api_id","3335796") )
    API_HASH = os.getenv("api_hash","138b992a0e672e8346d8439c3f42ea78")
    CHANNEL = int( os.getenv("channel_files_chat_id","-1001792962793") )
    CHANNEL_USERNAME = os.getenv("channel_username","Seriesplus1")
    TOKEN = "5171401480:AAETkS3FGnRlbJauRPdPg3BUJFnG0jVa2t0")
    DOMAIN  = os.getenv("domain","https://neww-li-prod-divar-woaooq.mo5.mogenius.io")
