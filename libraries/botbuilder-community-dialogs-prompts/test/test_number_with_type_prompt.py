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
from number_with_type_prompt import NumberWithTypePrompt, NumberWithTypePromptType

class NumberWithTypeOrdinalPromptTests(aiounittest.AsyncTestCase):
    async def test_ordinal_prompt(self):
        async def exec_test(turn_context:TurnContext):
            dialog_context = await dialogs.create_context(turn_context)

            results = await dialog_context.continue_dialog()
            if results.status == DialogTurnStatus.Empty:
                options = PromptOptions(
                    prompt = Activity(
                        type = ActivityTypes.message, 
                        text = "test the ordinalnumber type api"
                        )
                )
                await dialog_context.prompt("ordinal_number_prompt", options)
            elif results.status == DialogTurnStatus.Complete:
                reply = results.result
                await turn_context.send_activity(reply)

            await conv_state.save_changes(turn_context)

        adapter = TestAdapter(exec_test)

        conv_state = ConversationState(MemoryStorage())

        dialog_state = conv_state.create_property("dialog-state")
        dialogs = DialogSet(dialog_state)
        dialogs.add(NumberWithTypePrompt("ordinal_number_prompt", NumberWithTypePromptType.Ordinal))

        step1 = await adapter.test('Hello', 'test the ordinalnumber type api')
        step2 = await step1.send('tenth')
        await step2.assert_reply("10")
        

class NumberWithPercentagePrompt(aiounittest.AsyncTestCase):
    async def test_percentage_prompt(self):
        async def exec_test(turn_context:TurnContext):
            dialog_context = await dialogs.create_context(turn_context)

            results = await dialog_context.continue_dialog()

            if results.status == DialogTurnStatus.Empty:
                options = PromptOptions(
                    prompt = Activity(
                        type = ActivityTypes.message, 
                        text = "test the percentage type api"
                        )
                )
                await dialog_context.prompt("percentagePrompt", options)
            elif results.status == DialogTurnStatus.Complete:
                reply = results.result
                await turn_context.send_activity(reply)

            await conv_state.save_changes(turn_context)

        adapter = TestAdapter(exec_test)

        conv_state = ConversationState(MemoryStorage())

        dialog_state = conv_state.create_property("dialog-state")
        dialogs = DialogSet(dialog_state)
        dialogs.add(NumberWithTypePrompt("percentagePrompt", NumberWithTypePromptType.Percentage))

        step1 = await adapter.test('percentagePrompt', 'test the percentage type api')
        step2 = await step1.send('two hundred percents')
        await step2.assert_reply("200%")