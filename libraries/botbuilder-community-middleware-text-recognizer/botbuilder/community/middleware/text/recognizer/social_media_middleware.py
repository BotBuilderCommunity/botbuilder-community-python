from recognizers_sequence import SequenceRecognizer
from recognizers_text import Culture,ModelResult
from botbuilder.core import Middleware,TurnContext
from botbuilder.schema import Activity,ActivityTypes
from typing import Callable,Awaitable

class SocialMediaRecognizerMiddleware(Middleware):
    def __init__(self,
            default_locale = None):
        if default_locale is None:
            default_locale = Culture.English

        self._default_locale = default_locale

    async def on_turn(self,
            context:TurnContext,
            next:Callable[[TurnContext],Awaitable]):
        if context.activity.type == ActivityTypes.message:
            social_recongnizer = SequenceRecognizer(self._default_locale)
            mention_model = social_recongnizer.get_mention_model()
            model_result = mention_model.parse(context.activity.text)

            if len(model_result) > 0:
                mention_entities = []
                for mention in model_result:
                    value = mention.resolution["value"]
                    mention_entities.append(value)
                context.turn_state.setdefault("mentionentities",mention_entities)

            hash_model = social_recongnizer.get_hashtag_model()
            model_result = hash_model.parse(context.activity.text)

            if len(model_result) > 0:
                hash_entities = []
                for hashmodel in model_result:
                    value = hashmodel.resolution["value"]
                    hash_entities.append(value)
                context.turn_state.setdefault("hashentities",hash_entities)
                          
        return await next()