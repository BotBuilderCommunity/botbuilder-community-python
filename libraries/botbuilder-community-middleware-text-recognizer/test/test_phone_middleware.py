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
from phone_middleware import PhoneRecognizerMiddleware

class PhoneNumberMiddleware(aiounittest.AsyncTestCase):
    async def test_phone_prompt(self):
        async def exec_test(turn_context:TurnContext):
                item = turn_context.turn_state.get('phonenumberentities')
                text = MessageFactory.text(item[0])
                await turn_context.send_activity(text)

        phone_reg_middle = PhoneRecognizerMiddleware()
        phone_adapter = TestAdapter(exec_test)
        phone_adapter.use(phone_reg_middle)
        await phone_adapter.test('My phone number is 540-123-4321', '540-123-4321')
