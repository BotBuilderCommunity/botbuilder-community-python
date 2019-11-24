from botbuilder.dialogs.prompts import Prompt, PromptOptions,PromptRecognizerResult
from botbuilder.core.turn_context import TurnContext
from botbuilder.schema import ActivityTypes
from recognizers_text import Culture, ModelResult,StringUtility
from recognizers_sequence import SequenceRecognizer
from typing import Callable, Dict


class GuidPrompt (Prompt):
    def __init__(self, 
        dialog_id,
        validator : object = None,
        defaultLocale = None):
        super().__init__(dialog_id, validator=validator)        
        if defaultLocale is None:
            defaultLocale = Culture.English

        self._defaultLocale = defaultLocale
        

    async def on_prompt(self, turn_context, state, options, is_retry):
        if not turn_context:
            raise TypeError("turn_context Can’t  be none")
        if not options:
            raise TypeError("options Can’t  be none")

        if is_retry and options.retry_prompt is not None:
            await turn_context.send_activity(options.retry_prompt)
        else:
            if options.prompt is not None:
                await turn_context.send_activity(options.prompt)

    async def on_recognize( self,
            turn_context: TurnContext,
            state: Dict[str, object],
            options: PromptOptions) -> PromptRecognizerResult():
        if not turn_context:
            raise TypeError("turn_context Can’t be none")

        if turn_context.activity.type == ActivityTypes.message:
            utterance = turn_context.activity.text
            
            turn_context.activity.locale = self._defaultLocale

            recognizer_result = PromptRecognizerResult()

            mode = SequenceRecognizer(turn_context.activity.locale)
            model = mode.get_guid_model()
        
            model_result = model.parse(utterance)

            if len(model_result) > 0 and len(model_result[0].resolution) > 0:
                recognizer_result.succeeded = True
                recognizer_result.value = model_result[0].resolution["value"]

            return recognizer_result