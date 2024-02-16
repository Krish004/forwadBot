from os import environ
class Config(object):
    API_ID = environ.get("API_ID", "1779071")
    API_HASH = environ.get("API_HASH", "3448177952613312689f44b9d909b5d3")
    BOT_TOKEN = environ.get("BOT_TOKEN", "6092537699:AAFdfZ5oo-P5peFlWJTN2iqzr_govF0jD-M")
    STRING_SESSION = environ.get("STRING_SESSION", "BQAMEZX36Dygi5nsxbV8U8LkVv9Dz3bMDKewZePgO7MbGv94dx9nqB1tKcwc-eYZc_XEjksUFaQjbQEe6aZcxkpuWaa-sWlze6Wz5Izq_pxCkRwUhNKhgsHUX-EG-P5snp6K-g0CKM6h3RBa1IGzUl1PobQack6Nsk4n7Ophg2WNikX_aMEAIN006yMoRyKCzB2FHgt1nTlZHGFroyYgQVbyl31QRQAe-JrKAEm_A26_hCHk6FrzpV0aH5biDC9HAdXNSXrhFuMlaMhEIDI5Y2xLyRvMdn4CG6WooxxAZla0-gNVzs93uqVDkljzTrPrKonIMaFHiQThrm9U8k5Xq8ruAAAAAY4EawwA")
    SUDO_USERS = environ.get("SUDO_USERS", "1169076058")
    COMMAND_HAND_LER = environ.get("COMMAND_HAND_LER", "^/")
    HELP_MSG = """
    💢 **ᴛʜᴇ ᴄᴏᴍᴍᴀɴᴅs ɪɴ ᴛʜᴇ ʙᴏᴛ ᴀʀᴇ:**
    
    🔻 **Command :** /forward
    **Usage : ** Forwards messages from a channel to other.
    🔻 **Command :** /count
    **Usage : ** Returns the Total message sent using the bot.
    🔻 **Command :** /reset
    **Usage : ** Resets the message count to 0.
    🔻 **Command :** /restart
    **Usage : ** Updates and Restarts the Bot.
    🔻 **Command :** /join
    **Usage : ** Joins the channel.
    🔻 **Command :** /help
    **Usage : ** Get the help of this bot.
    🔻 **Command :** /status
    **Usage :** Check current status of Bot.
    🔻 **Command :** /uptime
    **Usage :** Check uptime of Bot.
    
    ⭕ **ʙᴏᴛ ɪs ᴄʀᴇᴀᴛᴇᴅ ʙʏ** **@KingVJ01**
    """
