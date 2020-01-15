# Text Recognizer Middleware

The Text Recognizer Middleware library is a compliment to the Text Recognizer dialog prompts. These middleware components can be used to identify certain text sequences that you might want to alter prior to appearing on the chat window. For example, turning a URL into an actual link, or turning a hashtag into a link that points to a Twitter search.

## Installing

    Coming soon

## Usage

All middleware is created and used in the same way. For example, for social media recognition, import the `SocialMediaRecognizerMiddleware` class from the package, and add it to your bot adapter:

    from social_media_middleware import SocialMediaRecognizerMiddleware

    adapter.use(SocialMediaRecognizerMiddleware());

When used, the `turn_state` on the `TurnContext` will have a property named `mentionentities`, which will be an array of strings with the `@` syntax elements.

Supported middleware classes include:

| Class | Property/Properties on `turn_state` |
| ---- | ----------- |
| `EmailRecognizerMiddleware` | `context.turn_state.get("emailentities")` |
| `UrlRecognizerMiddleware` | `context.turn_state.get("urlentities")` |
| `PhoneRecognizerMiddleware` | `context.turn_state.get("phonenumberentities")` |
| `SocialMediaRecognizerMiddleware` | `context.turn_state.get("mentionentities")` or `context.turn_state.get("hashentities")` |

In each case, the `turn_state` of the `TurnContext` contains an array with the various recognized entities.
