import os
import hello
from errbot.backends.test import testbot


class TestHelloBot(object):
    extra_plugin_dir = '.'

    def test_hello(self, testbot):
        testbot.push_message('!hello')
        assert 'Hello, gbin@localhost' in testbot.pop_message()
