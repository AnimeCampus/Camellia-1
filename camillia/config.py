class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    API_ID = 16743442
    API_HASH = "12bbd720f4097ba7713c5e40a11dfd2a"

    CASH_API_KEY = "PRPSG4AY3Q3H0QG0"  # Get this value for currency converter from https://www.alphavantage.co/support/#api-key

    DATABASE_URL = "postgres://hreknqvs:5KD5-zQPbj_kkm-blz09HsJIbtuT9QUz@lucky.db.elephantsql.com/hreknqvs"  # A sql database url from elephantsql.com

    EVENT_LOGS = (-1001596651023)  # Event logs channel to note down important bot level events

    MONGO_DB_URI = "mongodb+srv://sonu55:sonu55@cluster0.vqztrvk.mongodb.net/?retryWrites=true&w=majority"  # Get ths value from cloud.mongodb.com

    # Telegraph link of the image which will be shown at start command.
    START_IMG = "https://graph.org/file/846d364810a42cb1c598b.jpg"

    SUPPORT_CHAT = "MissCamelliaSupport"  # Your Telegram support group chat username where your users will go and bother you

    TOKEN = "5876546515:AAE0vVvCy6ucPjSc4oS0gECtmjAUmkP9tuo"  # Get bot token from @BotFather on Telegram

    TIME_API_KEY = "S3J6EISOC17L"  # Get this value from https://timezonedb.com/api

    OWNER_ID = 6198858059  # User id of your telegram account (Must be integer)

    # Optional fields
    BL_CHATS = []  # List of groups that you want blacklisted.
    DRAGONS = []  # User id of sudo users
    DEV_USERS = []  # User id of dev users
    DEMONS = []  # User id of support users
    TIGERS = []  # User id of tiger users
    WOLVES = []  # User id of whitelist users

    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True
    LOAD = []
    NO_LOAD = []
    STRICT_GBAN = True
    TEMP_DOWNLOAD_DIRECTORY = "./"
    WORKERS = 8


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
