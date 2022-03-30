

# Create a new config.py file in same dir and import, then extend this class.
class Config(object):
    LOGGER = True

    # REQUIRED
    API_KEY = "5211869898:AAHCu5DsWRSLwfluIYxIFiaIFm1FAbP0lKw"
    OWNER_ID = "925710749" # If you dont know, run the bot and do /id in your private chat with it
    OWNER_USERNAME = "AmazerS_xD"

    # RECOMMENDED
    SQLALCHEMY_DATABASE_URI = 'postgresql://zoibwgcensmcfq:7f87f99ad446af82b2005c14f335b566d74693e74275a5349c48eb4a49b0d4c7@ec2-54-216-56-125.eu-west-1.compute.amazonaws.com:5432/d9hdn6pa5hbel2'  # needed for any database modules
    MESSAGE_DUMP = None  # needed to make sure 'save from' messages persist
    LOAD = []
    NO_LOAD = ['translation', 'rss']
    WEBHOOK = False
    URL = None

    # OPTIONAL
    SUDO_USERS = []  # List of id's (not usernames) for users which have sudo access to the bot.
    SUPPORT_USERS = []  # List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    WHITELIST_USERS = []  # List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    DONATION_LINK = None  # EG, paypal
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = False  # Whether or not you should delete "blue text must click" commands
    STRICT_GBAN = False
    WORKERS = 8  # Number of subthreads to use. This is the recommended amount - see for yourself what works best!
    BAN_STICKER = 'CAADAgADOwADPPEcAXkko5EB3YGYAg'  # banhammer marie sticker
    ALLOW_EXCL = False  # Allow ! commands as well as /


class Production(Config):
    LOGGER = False


class Development(Config):
    LOGGER = True
