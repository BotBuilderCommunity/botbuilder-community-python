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
from number_with_unit_prompt import NumberWithUnitPrompt, NumberWithUnitPromptType

class NumberWithUnitAgePromptTests(aiounittest.AsyncTestCase):
    async def test_age_unit_prompt(self):
        async def exec_test(turn_context:TurnContext):
            dialog_context = await dialogs.create_context(turn_context)
            results = await dialog_context.continue_dialog()

            if results.status == DialogTurnStatus.Empty:
                options = PromptOptions(
                    prompt = Activity(
                        type = ActivityTypes.message,
                        text = "test the age unit api"
                        )
                )
                await dialog_context.prompt("AgePrompt", options)
            elif results.status == DialogTurnStatus.Complete:
                reply = results.result
                result = f"Age : {reply.value} and unit : {reply.unit}"
                await turn_context.send_activity(result)

            await conv_state.save_changes(turn_context)

        adapter = TestAdapter(exec_test)

        conv_state = ConversationState(MemoryStorage())

        dialog_state = conv_state.create_property("dialog-state")
        dialogs = DialogSet(dialog_state)
        dialogs.add(NumberWithUnitPrompt("AgePrompt", NumberWithUnitPromptType.Age))

        step1 = await adapter.test('Hello', 'test the age unit api')
        step2 = await step1.send('am twenty seven years of age')
        await step2.assert_reply("Age : 27 and unit : Year")
        
class NumberWithUnitCurrencyPromptTests(aiounittest.AsyncTestCase):
    async def test_currency_prompt(self):
        async def exec_test(turn_context:TurnContext):
            dialog_context = await dialogs.create_context(turn_context)
            results = await dialog_context.continue_dialog()

            if results.status == DialogTurnStatus.Empty:
                options = PromptOptions(
                    prompt=Activity(
                        type = ActivityTypes.message,
                        text="test the currency unit api"
                        )
                )
                await dialog_context.prompt("currencyprompt",options)
            elif results.status == DialogTurnStatus.Complete:
                reply = results.result
                result = f"currency : '{reply.value}' and unit : '{reply.unit}'"
                await turn_context.send_activity(result)

            await conv_state.save_changes(turn_context)

        adapter = TestAdapter(exec_test)

        conv_state = ConversationState(MemoryStorage())

        dialog_state = conv_state.create_property("dialog-state")
        dialogs = DialogSet(dialog_state)
        dialogs.add(NumberWithUnitPrompt("currencyprompt",NumberWithUnitPromptType.Currency))

        step1 = await adapter.test('Hello','test the currency unit api')
        step2 = await step1.send('Interest expense in the 2018 third quarter was $ 15.3 million')
        await step2.assert_reply("currency : '15300000' and unit : 'Dollar'")

class NumberWithDimensionsPromptTests(aiounittest.AsyncTestCase):
    async def test_dimensions_prompt(self):
        async def exec_test(turn_context:TurnContext):
            dialog_context = await dialogs.create_context(turn_context)
            results = await dialog_context.continue_dialog()

            if results.status == DialogTurnStatus.Empty:
                options = PromptOptions(
                    prompt = Activity(
                        type = ActivityTypes.message, 
                        text = "test the Dimensions unit api"
                        )
                )
                await dialog_context.prompt("Dimensionsprompt", options)
            elif results.status == DialogTurnStatus.Complete:
                reply = results.result
                result = f"Dimensions : '{reply.value}' and unit : '{reply.unit}'"
                await turn_context.send_activity(result)

            await conv_state.save_changes(turn_context)

        adapter = TestAdapter(exec_test)

        conv_state = ConversationState(MemoryStorage())

        dialog_state = conv_state.create_property("dialog-state")
        dialogs = DialogSet(dialog_state)
        dialogs.add(NumberWithUnitPrompt("Dimensionsprompt", NumberWithUnitPromptType.Dimension))

        step1 = await adapter.test('Hello', 'test the Dimensions unit api')
        step2 = await step1.send('The six-mile trip to my airport hotel that had taken 20 minutes earlier in the day took more than three hours')
        await step2.assert_reply("Dimensions : '6' and unit : 'Mile'")
    
class NumberWithTemperaturePromptTests(aiounittest.AsyncTestCase):
    async def test_temperature_prompt(self):
        async def exec_test(turn_context:TurnContext):
            dialog_context = await dialogs.create_context(turn_context)
            results = await dialog_context.continue_dialog()

            if results.status == DialogTurnStatus.Empty:
                options = PromptOptions(
                    prompt = Activity(
                        type = ActivityTypes.message, 
                        text = "test temperature unit api"
                        )
                )
                await dialog_context.prompt("temperatureprompt", options)
            elif results.status == DialogTurnStatus.Complete:
                reply = results.result
                result = f"temperature : '{reply.value}' and unit : '{reply.unit}'"
                await turn_context.send_activity(result)

            await conv_state.save_changes(turn_context)

        adapter = TestAdapter(exec_test)

        conv_state = ConversationState(MemoryStorage())

        dialog_state = conv_state.create_property("dialog-state")
        dialogs = DialogSet(dialog_state)
        dialogs.add(NumberWithUnitPrompt("temperatureprompt", NumberWithUnitPromptType.Temperature))

        step1 = await adapter.test('Hello', 'test temperature unit api')
        step2 = await step1.send('Set the temperature to 18 degrees celsius"')
        await step2.assert_reply("temperature : '18' and unit : 'C'")