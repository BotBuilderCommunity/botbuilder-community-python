from botbuilder.dialogs.prompts import Prompt, PromptOptions, PromptRecognizerResult
from botbuilder.core.turn_context import TurnContext
from botbuilder.schema import ActivityTypes
from recognizers_number_with_unit import NumberWithUnitRecognizer
from recognizers_text import Culture, ModelResult
from typing import Callable, Dict
import enum

class NumberWithUnitPromptType(enum.Enum):
     Currency = 0
     Temperature = 1
     Age = 2
     Dimension = 3

class NumberWithUnitResult:
    def __init__(self, unit , value ):
        self._unit = unit
        self._value = value
    
    @property
    def unit(self):
        return self._unit
    @property
    def value(self):
        return self._value
    

class NumberWithUnitPrompt(Prompt):
    def __init__(
        self, 
        dialog_id, 
        prompt_type: NumberWithUnitPromptType, 
        validator: object = None, 
        default_locale = None
        ):
        super().__init__(dialog_id, validator)

        if default_locale is None:
            default_locale = Culture.English
            
        self._default_locale = default_locale 
        self._prompt_type  = prompt_type

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

            recognizer = NumberWithUnitRecognizer(turn_context.activity.locale)

            if self._prompt_type == NumberWithUnitPromptType.Age:
                model = recognizer.get_age_model()            
            elif self._prompt_type == NumberWithUnitPromptType.Currency:
                model = recognizer.get_currency_model()            
            elif self._prompt_type == NumberWithUnitPromptType.Dimension:
                model = recognizer.get_dimension_model()
            elif self._prompt_type == NumberWithUnitPromptType.Temperature:
                model = recognizer.get_temperature_model()

            model_result = model.parse(utterance)

            if len(model_result) > 0 and len(model_result[0].resolution) > 1:
                recognizer_result.succeeded = True
                recognizer_result.value = NumberWithUnitResult(
                    model_result[0].resolution["unit"], 
                    model_result[0].resolution["value"]
                    )
        
            return recognizer_result