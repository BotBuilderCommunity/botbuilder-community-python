import sys
import pathlib
import pytest
import aiounittest
import asyncio

current = pathlib.Path(__file__).parent.parent
libpath = current.joinpath("botbuilder").joinpath("community").joinpath("dialogs").joinpath("prompts")
sys.path.append(str(libpath))

from botbuilder.dialogs.prompts import (
    AttachmentPrompt, 
    PromptOptions, 
    PromptValidatorContext, 
)

from botbuilder.core import (
    TurnContext, 
    ConversationState, 
    MemoryStorage, 
    MessageFactory, 
)
from botbuilder.schema import Activity, ActivityTypes, Attachment
from botbuilder.core.adapters import TestAdapter
from botbuilder.dialogs import DialogSet, DialogTurnStatus
from internet_protocol_prompt import InternetProtocolPrompt,InternetProtocolPromptType

class InternetProtocolPromptTest(aiounittest.AsyncTestCase):
    async def test_ip_address_prompt(self):
        async def exec_test(turn_context:TurnContext):
            dialog_context = await dialogs.create_context(turn_context)

            results = await dialog_context.continue_dialog()
            if (results.status == DialogTurnStatus.Empty):
                options = PromptOptions(
                    prompt = Activity(
                        type = ActivityTypes.message, 
                        text = "What is your DNS?"
                        )
                    )
                await dialog_context.prompt("ipaddressprompt", options)

            elif results.status == DialogTurnStatus.Complete:
                reply = results.result
                await turn_context.send_activity(reply)

            await conv_state.save_changes(turn_context)

        adapter = TestAdapter(exec_test)

        conv_state = ConversationState(MemoryStorage())

        dialog_state = conv_state.create_property("dialog-state")
        dialogs = DialogSet(dialog_state)
        dialogs.add(InternetProtocolPrompt("ipaddressprompt",InternetProtocolPromptType.IPAddress))

        step1 = await adapter.test('Hello', 'What is your DNS?')
        step2 = await step1.send('am using microsoft DNS 127.0.0.1')
        await step2.assert_reply("127.0.0.1")

    
    async def test_ip_url_prompt(self):
        async def exec_test(turn_context:TurnContext):
            dialog_context = await dialogs.create_context(turn_context)

            results = await dialog_context.continue_dialog()
            if (results.status == DialogTurnStatus.Empty):
                options = PromptOptions(
                    prompt = Activity(
                        type = ActivityTypes.message, 
                        text = "What is your favorite web site?"
                        )
                    )
                await dialog_context.prompt("urlprompt", options)

            elif results.status == DialogTurnStatus.Complete:
                reply = results.result
                await turn_context.send_activity(reply)

            await conv_state.save_changes(turn_context)

        adapter = TestAdapter(exec_test)

        conv_state = ConversationState(MemoryStorage())

        dialog_state = conv_state.create_property("dialog-state")
        dialogs = DialogSet(dialog_state)
        dialogs.add(InternetProtocolPrompt("urlprompt",InternetProtocolPromptType.URL))

        step1 = await adapter.test('Hello', 'What is your favorite web site?')
        step2 = await step1.send('My favorite web site is http://rvinothrajendran.github.io/')
        await step2.assert_reply("http://rvinothrajendran.github.io/")