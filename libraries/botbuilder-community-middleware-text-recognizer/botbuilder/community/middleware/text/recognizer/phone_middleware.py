from recognizers_sequence import SequenceRecognizer
from recognizers_text import Culture,ModelResult
from botbuilder.core import Middleware,TurnContext
from botbuilder.schema import Activity,ActivityTypes
from typing import Callable,Awaitable

class PhoneRecognizerMiddleware(Middleware):
    def __init__(self,
            default_locale = None):
        if default_locale is None:
            default_locale = Culture.English

        self._default_locale = default_locale

    async def on_turn(self,
            context:TurnContext,
            next:Callable[[TurnContext],Awaitable]):
        if context.activity.type == ActivityTypes.message:
            phone_recongnizer = SequenceRecognizer(self._default_locale)
            phone_model = phone_recongnizer.get_phone_number_model()
            model_result = phone_model.parse(context.activity.text)

            if len(model_result) > 0:
                phonenumber_entities = []
                for phone in model_result:
                    value = phone.resolution["value"]
                    phonenumber_entities.append(value)
                context.turn_state.setdefault("phonenumberentities",phonenumber_entities)
        return await next()