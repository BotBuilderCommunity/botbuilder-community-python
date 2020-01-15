import asyncio
import pathlib
import sys
import aiounittest
import pytest

current = pathlib.Path(__file__).parent.parent
libpath = current.joinpath("botbuilder").joinpath("community").joinpath("middleware").joinpath("text").joinpath("recognizer")
sys.path.append(str(libpath))


from botbuilder.core import MessageFactory, TurnContext
from botbuilder.core.adapters import TestAdapter
from url_middleware import UrlRecognizerMiddleware

class URLMiddleware(aiounittest.AsyncTestCase):
    async def test_url_prompt(self):
        async def exec_test(turn_context:TurnContext):
                item = turn_context.turn_state.get('urlentities')
                text = MessageFactory.text(item[0])
                await turn_context.send_activity(text)

        url_reg_middleware = UrlRecognizerMiddleware()
        url_adapter = TestAdapter(exec_test)
        url_adapter.use(url_reg_middleware)
        await url_adapter.test('My web site is https://rvinothrajendran.github.io/', 'https://rvinothrajendran.github.io/')
