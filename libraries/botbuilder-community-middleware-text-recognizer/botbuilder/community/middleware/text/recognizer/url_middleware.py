from recognizers_sequence import SequenceRecognizer
from recognizers_text import Culture,ModelResult
from botbuilder.core import Middleware,TurnContext
from botbuilder.schema import Activity,ActivityTypes
from typing import Callable,Awaitable

class UrlRecognizerMiddleware(Middleware):
    def __init__(self,
            default_locale = None):
        if default_locale is None:
            default_locale = Culture.English

        self._default_locale = default_locale

    async def on_turn(self,
            context:TurnContext,
            next:Callable[[TurnContext],Awaitable]):
        if context.activity.type == ActivityTypes.message:
            url_recongnizer = SequenceRecognizer(self._default_locale)
            url_model = url_recongnizer.get_url_model()
            model_result = url_model.parse(context.activity.text)

            if len(model_result) > 0:
                url_entities = []
                for url in model_result:
                    value = url.resolution["value"]
                    url_entities.append(value)
                context.turn_state.setdefault("urlentities",url_entities)
        return await next()