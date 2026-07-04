import os
from dotenv import load_dotenv

load_dotenv(
    "config.env" if os.path.isfile("config.env") else "sample_config.env"
)

# ─── بيانات تليجرام الأساسية ──────────────────────────────────────────
BOT_TOKEN = "8760356868:AAHwM62YgmuOkTkAGdzPAENFiAYtr2BXNSs"
API_ID = 30277522
API_HASH = "b29960a02bab1055e027101852d7fb7f"

# ─── جلسة الحساب المساعد (USERBOT) ───────────────────────────────────
SESSION_STRING = "BAHN_5IArBTfzWLByVOz_kTAicch3e4IDPq__PGkTYCEqCq_XbTSPg-cspsfOhVdwmx23OI3N7MbygtEk6XkLX-Yl60yKcDk1YhvjC7ESGT0VxvsbmT0485XK8cm275F5FqQ651vRHBq6c9wZRdJsJdu7xnYM7RQ6lLKgNYHyHoQoVwXZGJzkHaoJzFw4d_XJ0pVadNb-fnL2pk1tkkzgb51LnPDkTKTIlv3PXTdvSzbMc1x2GEnqthSFhRG1RsrKJZD4nsTqu6SkuOXhol4m9TBPf_W_7oVLA2oTv4sod36wTC0dkN4hRSz84ciUngrmiEVnxnuvs9WzVczwUYYoyRy4AsG5wAAAAGsZEBGAA"
USERBOT_PREFIX = "\\"
PHONE_NUMBER = "+201097023670"

# ─── بيانات المطور والملكية (سورس السيادة) ─────────────────────────────
SUDO_USERS_ID = [7187218502]  # معرف حسابك الشخصي (البروف)
OWNER_ID = 7187218502
OWNER_USER = "@pro0of_m"
SOURCE_CHANNEL = "https://t.me/sovereign2026source"  # رابط قناة سورس السيادة

# ─── جروبات وقنوات السجلات والدعم ─────────────────────────────────────
LOG_GROUP_ID = -1003861810384        # جروب السجلات (Log Group)
GBAN_LOG_GROUP_ID = -1003861810384   # سجلات الحظر العام
MESSAGE_DUMP_CHAT = -1003861810384   # تخزين الرسائل
SUPPORT_GROUP = -1003861810384       # جروب الدعم الخاص بك

# ─── قاعدة البيانات والخدمات الخارجية ──────────────────────────────────
MONGO_URL = "mongodb+srv://m7mddemo0o_db_user:NZ.-nRkv6/@WD<t@cerberus-cluster.7rm2frg.mongodb.net/?appName=Cerberus-cluster"
ARQ_API_KEY = "ZHEWFS-GFYZYB-UORXZN-ZRJXJA-ARQ"
ARQ_API_URL = "https://arq.hamker.dev"

# ─── إعدادات التشغيل الافتراضية ────────────────────────────────────────
WELCOME_DELAY_KICK_SEC = 300  # وقت حل الكابتشا (5 دقائق)
LOG_MENTIONS = True
RSS_DELAY = 300
PM_PERMIT = True
