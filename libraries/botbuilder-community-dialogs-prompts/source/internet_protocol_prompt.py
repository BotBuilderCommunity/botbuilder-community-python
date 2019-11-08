from botbuilder.dialogs.prompts import Prompt, PromptOptions,PromptRecognizerResult
from botbuilder.core.turn_context import TurnContext
from botbuilder.schema import ActivityTypes
from recognizers_sequence import SequenceRecognizer
from recognizers_text import Culture, ModelResult
from typing import Callable, Dict
import enum

class InternetProtocolPromptType(enum.Enum):
    IPAddress = 0,
    URL = 1,
    
class InternetProtocolPrompt(Prompt):
    def __init__(self,
        dialog_id,
        promptType:InternetProtocolPromptType,
        validator : object = None,
        defaultLocale = None):       
        super().__init__(dialog_id,validator)
         
        if defaultLocale is None:
            defaultLocale = Culture.English

        self._defaultLocale = defaultLocale
        self._promptType = promptType

    async def on_prompt(
        self, 
        turn_context: TurnContext, 
        state: Dict[str, object], 
        options: PromptOptions, 
        is_retry: bool):
          if not turn_context:
              raise TypeError("turn_context Can’t  be none")
          if not options:
              raise TypeError("options Can’t  be none")
    
          if is_retry and options.retry_prompt is not None:
              await turn_context.send_activity(options.retry_prompt)
          else:
              if options.prompt is not None:
                 await turn_context.send_activity(options.prompt)

    async def on_recognize(self,
        turn_context: TurnContext, 
        state: Dict[str, object], 
        options: PromptOptions, 
    ) -> PromptRecognizerResult:
        if not turn_context:
            raise TypeError("turn_context Can’t be none")

        if turn_context.activity.type == ActivityTypes.message:
            utterance = turn_context.activity.text
        
            turn_context.activity.locale = self._defaultLocale 
        
            recognizer_result = PromptRecognizerResult()
            mode = SequenceRecognizer(turn_context.activity.locale)

            if (self._promptType == InternetProtocolPromptType.IPAddress):
                model = mode.get_ip_address_model()
            elif (self._promptType == InternetProtocolPromptType.URL):
                model = mode.get_url_model()
        
            model_result = model.parse(utterance)
            if len(model_result) > 0 and len(model_result[0].resolution) > 0:
                recognizer_result.succeeded = True
                recognizer_result.value = model_result[0].resolution["value"]
            
            return recognizer_result