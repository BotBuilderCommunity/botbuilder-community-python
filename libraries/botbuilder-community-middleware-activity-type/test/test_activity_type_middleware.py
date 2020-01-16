import asyncio
import pathlib
import sys
import aiounittest
import pytest

current = pathlib.Path(__file__).parent.parent
libpath = current.joinpath("botbuilder").joinpath("community").joinpath("middleware").joinpath("activity").joinpath("type")
sys.path.append(str(libpath))


from botbuilder.core import MessageFactory, TurnContext
from botbuilder.core.adapters import TestAdapter
from botbuilder.schema import ActivityTypes
from activity_type_middleware import ActivityTypeMiddleware

class TestActivityMiddleware(aiounittest.AsyncTestCase):
    async def test_adapter_middleware(self):

        async def turn_adapter_callback(turn_context:TurnContext):
              await turn_context.send_activity("Hey activity Middlware")      

        async def exec_test(turn_context:TurnContext):
                await turn_context.send_activity("Test activity Middleware")   

        activity_adapter = TestAdapter(exec_test)
        activity_adapter.use(ActivityTypeMiddleware(ActivityTypes.message,turn_adapter_callback))
        await activity_adapter.test('Hello, activity type bot!', 'Hey activity Middlware')

    