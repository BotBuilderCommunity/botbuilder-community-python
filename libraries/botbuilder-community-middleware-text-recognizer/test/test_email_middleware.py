import asyncio
import pathlib
import sys
import aiounittest
import pytest

current = pathlib.Path(__file__).parent.parent
print(current)
libpath = current.joinpath("botbuilder").joinpath("community").joinpath("middleware").joinpath("text").joinpath("recognizer")
sys.path.append(str(libpath))


from botbuilder.core import MessageFactory, TurnContext
from botbuilder.core.adapters import TestAdapter
from email_middleware import EmailRecognizerMiddleware

class EmailMiddleware(aiounittest.AsyncTestCase):
    async def test_email_prompt(self):
        async def exec_test(turn_context:TurnContext):
                item = turn_context.turn_state.get('emailentities')
                text = MessageFactory.text(item[0])
                await turn_context.send_activity(text)

        email_reg_middleware = EmailRecognizerMiddleware()
        email_adapter = TestAdapter(exec_test)
        email_adapter.use(email_reg_middleware)
        await email_adapter.test('My mail address is r.vinoth@live.com', 'r.vinoth@live.com')
