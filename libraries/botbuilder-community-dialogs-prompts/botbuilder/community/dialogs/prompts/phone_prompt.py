import asyncio
from botbuilder.dialogs.prompts import (
    Prompt,
    PromptOptions, 
    PromptRecognizerResult
)
from botbuilder.core.turn_context import TurnContext
from botbuilder.schema import ActivityTypes
from recognizers_text import Culture, ModelResult
from recognizers_sequence import SequenceRecognizer
from typing import Callable, Dict

class PhoneNumberPrompt (Prompt):
    def __init__(
        self,
        dialog_id,
        validator : object = None,
        default_locale = None):
        super().__init__(dialog_id, validator = validator)

        if default_locale is None:
            default_locale = Culture.English      

        self._default_locale = default_locale

    async def on_prompt(
        self, 
        turn_context: TurnContext, 
        state: Dict[str, object], 
        options: PromptOptions, 
        is_retry: bool, 
    ):
        if not turn_context:
            raise TypeError("turn_context Can’t  be none")
        if not options:
            raise TypeError("options Can’t  be none")

        if is_retry and options.retry_prompt is not None:
            await turn_context.send_activity(options.retry_prompt)
        else:
            if options.prompt is not None:
                await turn_context.send_activity(options.prompt)

    async def on_recognize(
        self, 
        turn_context: TurnContext, 
        state: Dict[str, object], 
        options: PromptOptions, 
    ) -> PromptRecognizerResult:
        
        if not turn_context:
            raise TypeError("turn_context Can’t be none")

        if turn_context.activity.type == ActivityTypes.message:
            utterance = turn_context.activity.text
            
            turn_context.activity.locale = self._default_locale 
            
            result = PromptRecognizerResult()

            sequence_recongnizer = SequenceRecognizer(turn_context.activity.locale)
            phone_model = sequence_recongnizer.get_phone_number_model()
            phone_parse = phone_model.parse(utterance)

            if len(phone_parse) > 0 and len(phone_parse[0].resolution) > 0:
                result.succeeded = True
                result.value = phone_parse[0].resolution["value"]
        
            return result