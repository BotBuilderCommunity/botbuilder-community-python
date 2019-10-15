from botbuilder.dialogs.prompts import Prompt, PromptOptions,PromptRecognizerResult
from botbuilder.core.turn_context import TurnContext
from botbuilder.schema import ActivityTypes
from recognizers_number_with_unit import NumberWithUnitRecognizer
from recognizers_text import Culture, ModelResult
from typing import Callable, Dict
import enum

class NumberWithUnitPromptType(enum.Enum):
     Currency=0
     Temperature=1
     Age=2
     Dimension=3

class NumberWithUnitResult:
    def __init__(self, Unit , Value ):
        self.Unit = Unit
        self.Value = Value
    
    @property
    def unit(self):
        return self.Unit
    @property
    def value(self):
        return self.Value
    

class NumberWithUnitPrompt(Prompt):
    def __init__(self, dialog_id,type:NumberWithUnitPromptType,validator=None,defaultLocale=None):
        super().__init__(dialog_id,validator)        
        self.DefaultLocale = defaultLocale 
        self.PromptType  = type

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

    async def on_recognize( self,turn_context: TurnContext,state: Dict[str, object],
    options: PromptOptions) -> PromptRecognizerResult():    

        if not turn_context:
            raise TypeError("turn_context Can’t be none")

        if turn_context.activity.type == ActivityTypes.message:
            message = turn_context.activity
            
            if turn_context.activity.locale is not None:
                turn_context.activity.locale = self.DefaultLocale 
            else:
                turn_context.activity.locale = Culture.English

            result = PromptRecognizerResult()        
            mode = NumberWithUnitRecognizer(turn_context.activity.locale)

            if self.PromptType == NumberWithUnitPromptType.Age:
                model = mode.get_age_model()            
            elif self.PromptType == NumberWithUnitPromptType.Currency:
               model = mode.get_currency_model()            
            elif self.PromptType == NumberWithUnitPromptType.Dimension:
               model = mode.get_dimension_model()
            elif self.PromptType == NumberWithUnitPromptType.Temperature:
                model = mode.get_temperature_model()

            numberresult = model.parse(message.text)

            if len(numberresult) > 0 and len(numberresult[0].resolution) > 1:
                result.succeeded = True
                unit = numberresult[0].resolution["unit"]
                value = numberresult[0].resolution["value"]
                numberwithunitresult = NumberWithUnitResult(unit,value)
                result.value = numberwithunitresult
        
            return result