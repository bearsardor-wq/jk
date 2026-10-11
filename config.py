import os

BOT_TOKEN = os.getenv("BOT_TOKEN", "8729235570:AAHtlsdBhenTt6CYepGxQtjg7Z5gDKaFoEw")
ADMIN_ID = int(os.getenv("ADMIN_ID", "2010030869"))
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://baza_5i6m_user:lryoKfPr9bKPqWsEihrWLTuavA4WuOVo@dpg-db5ggblckfvc73a4m3t0-a.oregon-postgres.render.com/baza_5i6m")

# Telethon uchun
API_ID = int(os.getenv("API_ID", "38486800"))
API_HASH = os.getenv("API_HASH", "c5fc7e4d2190b89e5ce8ea01c0369f09")
