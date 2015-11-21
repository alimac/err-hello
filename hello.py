from errbot import BotPlugin, botcmd


class HelloBot(BotPlugin):
    """Example 'Hello!' plugin for Errbot"""

    @botcmd
    def hello(self, msg, args):
        """Say hello to the world"""
        return "Hello, " + format(msg.frm)
