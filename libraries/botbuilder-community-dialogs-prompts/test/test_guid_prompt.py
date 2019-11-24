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
from guid_prompt import GuidPrompt

class GuidPromptTest(aiounittest.AsyncTestCase):
    async def test_guid_phone_prompt(self):
        async def exec_test(turn_context:TurnContext):
            dialog_context = await dialogs.create_context(turn_context)

            results = await dialog_context.continue_dialog()
            if (results.status == DialogTurnStatus.Empty):
                options = PromptOptions(
                    prompt = Activity(
                        type = ActivityTypes.message, 
                        text = "test the guid format"
                        )
                    )
                await dialog_context.prompt("guidprompt", options)

            elif results.status == DialogTurnStatus.Complete:
                reply = results.result
                await turn_context.send_activity(reply)

            await conv_state.save_changes(turn_context)

        adapter = TestAdapter(exec_test)

        conv_state = ConversationState(MemoryStorage())

        dialog_state = conv_state.create_property("dialog-state")
        dialogs = DialogSet(dialog_state)
        dialogs.add(GuidPrompt("guidprompt"))

        step1 = await adapter.test('Hello', 'test the guid format')
        step2 = await step1.send('my azure id is 7d7b0205-9411-4a29-89ac-b9cd905886fa')
        await step2.assert_reply("7d7b0205-9411-4a29-89ac-b9cd905886fa")