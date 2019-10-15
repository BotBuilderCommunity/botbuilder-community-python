from botbuilder.dialogs.prompts import Prompt, PromptOptions,PromptRecognizerResult
from botbuilder.core.turn_context import TurnContext
from botbuilder.schema import ActivityTypes
from recognizers_number import NumberRecognizer
from recognizers_text import Culture, ModelResult
from typing import Callable, Dict
import enum

class NumberWithTypePromptType(enum.Enum):
    Ordinal =0,
    Percentage=1  


class NumberWithTypePrompt(Prompt):
    def __init__(self,dialog_id,promptType:NumberWithTypePromptType,validator=None,DefaultLocale=None):       
        super().__init__(dialog_id,validator)
        self.defaultLocale = DefaultLocale
        self.PromptType = promptType

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
            utterance = turn_context.activity.text
        
            if turn_context.activity.locale is not None:
                turn_context.activity.locale = self.defaultLocale 
            else:
                turn_context.activity.locale = Culture.English
        
            result = PromptRecognizerResult()
            mode = NumberRecognizer(turn_context.activity.locale)
            if (self.PromptType == NumberWithTypePromptType.Ordinal):
                model = mode.get_ordinal_model()
            elif (self.PromptType == NumberWithTypePromptType.Percentage):
                model = mode.get_percentage_model()          
        
            modelresult = model.parse(utterance)
            if len(modelresult) > 0 and len(modelresult[0].resolution) > 0:
                result.succeeded = True
                result.value = modelresult[0].resolution["value"]
            
            return result