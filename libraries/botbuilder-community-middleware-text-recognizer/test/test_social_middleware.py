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
from social_media_middleware import SocialMediaRecognizerMiddleware

class SocialMiddleware(aiounittest.AsyncTestCase):
    async def test_mention_prompt(self):
        async def exec_test(turn_context:TurnContext):
                item = turn_context.turn_state.get('mentionentities')
                text = MessageFactory.text(item[0])
                await turn_context.send_activity(text)

        social_adapter = TestAdapter(exec_test)
        social_adapter.use(SocialMediaRecognizerMiddleware())
        await social_adapter.test('My Twitter handle is @vinothrajendran', '@vinothrajendran')

    async def test_hash_prompt(self):
        async def exec_test(turn_context:TurnContext):
                item = turn_context.turn_state.get('hashentities')
                text = MessageFactory.text(item[0])
                await turn_context.send_activity(text)

        social_adapter = TestAdapter(exec_test)
        social_adapter.use(SocialMediaRecognizerMiddleware())
        await social_adapter.test('Follow the #botframework hashtag', '#botframework')
