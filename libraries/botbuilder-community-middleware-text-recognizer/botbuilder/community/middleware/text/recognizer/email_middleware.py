from recognizers_sequence import SequenceRecognizer
from recognizers_text import Culture,ModelResult
from botbuilder.core import Middleware,TurnContext
from botbuilder.schema import Activity,ActivityTypes
from typing import Callable,Awaitable

class EmailRecognizerMiddleware(Middleware):
    def __init__(self,
            default_locale = None):
        if default_locale is None:
            default_locale = Culture.English

        self._default_locale = default_locale

    async def on_turn(self,
            context:TurnContext,
            next:Callable[[TurnContext],Awaitable]):
        if context.activity.type == ActivityTypes.message:
            email_recongnizer = SequenceRecognizer(self._default_locale)
            email_model = email_recongnizer.get_email_model()
            model_result = email_model.parse(context.activity.text)

            if len(model_result) > 0:
                email_entities = []
                for email in model_result:
                    value = email.resolution["value"]
                    email_entities.append(value)
                context.turn_state.setdefault("emailentities",email_entities)
        return await next()