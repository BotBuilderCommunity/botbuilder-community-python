from botbuilder.core import Middleware,TurnContext
from botbuilder.schema import Activity,ActivityTypes
from typing import Awaitable,Callable

class ActivityTypeMiddleware(Middleware):
    def __init__(self,
        activitytype:ActivityTypes,
        callback):
        self._activitytype = activitytype
        self._callback = callback

    async def on_turn(self,
            context:TurnContext,
            next:Callable[[TurnContext],Awaitable]):
            if self._activitytype == context.activity.type:
                await self._callback(context)
            await next()

