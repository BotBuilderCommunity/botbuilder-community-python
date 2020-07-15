# Activity Type Middleware

This middleware package is a Python port of the [C# Activity Type middleware component](https://github.com/BotBuilderCommunity/botbuilder-community-dotnet/tree/develop/libraries/Bot.Builder.Community.Middleware.HandleActivityType) from the Bot Builder Community. It intercepts messages based on the activity type so that you can automatically handle certain types outside of the standard dialog flow.

## Installing

    Coming Soon

## Usage

```python

from activity_type_middleware import ActivityTypeMiddleware;

	async def turn_adapter_callback(turn_context:TurnContext):
          await turn_context.send_activity("Hey activity Middlware") 

activity_adapter.use(ActivityTypeMiddleware(ActivityTypes.message,turn_adapter_callback))

```
