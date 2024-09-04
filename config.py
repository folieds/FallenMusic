from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID","27896987"))
API_HASH = getenv("API_HASH","0e017f716c49a52a0ba4a8bfa95ccaf7")

BOT_TOKEN = getenv("BOT_TOKEN", "6949336800:AAHNtDQPyrkbYisGDymH9SQtRmJY2D2aMjE")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID", "7067559685"))

PING_IMG = getenv("PING_IMG", "https://te.legra.ph/file/6f99c49bdb4679acad717.jpg")
START_IMG = getenv("START_IMG", "https://te.legra.ph/file/f8ba75bdbb9931cbc8229.jpg")

SESSION = getenv("SESSION", "BQGprJsAwjsisILI3vBz3DBS-KTwOMCng0zNCOBk0yxMrwTtr2R5SU7KxIwsAARmScoIH7ZQWO57v1be7-o9-jRlJnvr26cHcRRleknVIJb0hOBqeAhDhiWg1cm8CFbLqkVdccfWvQkwGswoX0lBbt-_ptnjaM4JGDJVfQn0zpxQv9B5KmlGu3S3OnAOEyl8gFQbaS4PpTt1CPa-SrJjvEKRcaS7PMTVCQ_SHDIe8rOi_MA5a5oa8Br_IBpeSNU5WO1GiX1FH72NkdQNdVZjHBr8V68Ag97fhiSDdWF61QK-zcZ7tW5F8kr2KXpSwLYQJu964sXDLW-qfHjnPtAFoshZecIp5gAAAAGlQmcFAA")

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/offchats")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/outlawbots")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6076683960").split()))


FAILED = "https://te.legra.ph/file/4c896584b592593c00aa8.jpg"
