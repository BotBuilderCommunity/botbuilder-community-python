import sys
import pathlib
import pytest
import aiounittest
import asyncio

current = pathlib.Path(__file__).parent.parent
libpath = current.joinpath("source")
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
from phone_prompt import PhoneNumberPrompt

class PhoneNumberPromptTest(aiounittest.AsyncTestCase):
    async def test_phone_prompt(self):
        async def exec_test(turn_context:TurnContext):
            dialog_context = await dialogs.create_context(turn_context)

            results = await dialog_context.continue_dialog()
            if (results.status == DialogTurnStatus.Empty):
                options = PromptOptions(
                    prompt = Activity(
                        type = ActivityTypes.message, 
                        text = "test the phone number type api"
                        )
                    )
                await dialog_context.prompt("phoneprompt", options)

            elif results.status == DialogTurnStatus.Complete:
                reply = results.result
                await turn_context.send_activity(reply)

            await conv_state.save_changes(turn_context)

        adapter = TestAdapter(exec_test)

        conv_state = ConversationState(MemoryStorage())

        dialog_state = conv_state.create_property("dialog-state")
        dialogs = DialogSet(dialog_state)
        dialogs.add(PhoneNumberPrompt("phoneprompt"))

        step1 = await adapter.test('Hello', 'test the phone number type api')
        step2 = await step1.send('My phone number is 1 (877) 609-2233')
        await step2.assert_reply("1 (877) 609-2233")