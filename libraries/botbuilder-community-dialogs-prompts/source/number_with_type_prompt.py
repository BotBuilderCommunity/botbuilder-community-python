from botbuilder.dialogs.prompts import Prompt, PromptOptions, PromptRecognizerResult
from botbuilder.core.turn_context import TurnContext
from botbuilder.schema import ActivityTypes
from recognizers_number import NumberRecognizer
from recognizers_text import Culture, ModelResult
from typing import Callable, Dict
import enum

class NumberWithTypePromptType(enum.Enum):
    Ordinal = 0, 
    Percentage = 1  


class NumberWithTypePrompt(Prompt):
    def __init__(
        self, 
        dialog_id, 
        prompt_type : NumberWithTypePromptType, 
        validator: object = None,
        default_locale = None
        ):       
        super().__init__(dialog_id, validator)

        if default_locale is None:
            default_locale = Culture.English

        self._default_locale = default_locale
        self._prompt_type = prompt_type

    async def on_prompt(
        self, 
        turn_context: TurnContext, 
        state: Dict[str, object], 
        options: PromptOptions, 
        is_retry: bool, 
    ):
        if not turn_context:
            raise TypeError("turn_context can’t  be none")
        if not options:
            raise TypeError("options can’t  be none")

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
            raise TypeError("turn_context can’t be none")

        if turn_context.activity.type == ActivityTypes.message:
            utterance = turn_context.activity.text
    
        turn_context.activity.locale = self._default_locale
        
        recognizer_result = PromptRecognizerResult()

        recognizer = NumberRecognizer(turn_context.activity.locale)
        
        if (self._prompt_type == NumberWithTypePromptType.Ordinal):
            model = recognizer.get_ordinal_model()
        elif (self._prompt_type == NumberWithTypePromptType.Percentage):
            model = recognizer.get_percentage_model()          
    
        model_result = model.parse(utterance)
        if len(model_result) > 0 and len(model_result[0].resolution) > 0:
            recognizer_result.succeeded = True
            recognizer_result.value = model_result[0].resolution["value"]
        
        return recognizer_result