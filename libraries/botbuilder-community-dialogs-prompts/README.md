# Dialog Prompts

This is a (currently experimental) suite of dialog prompts that uses Microsoft's recognizer text suite to recognize certain types of input during a dialog prompt. Microsoft's Bot Framework team has implemented a handful of prompts using recognizers from the recognizer text suite. This library is meant to fill the gaps.

## Installation

You can install this library via PIP:

    pip install botbuilder-community-dialogs-prompts

You can then import required types, for example:

```python
    from botbuilder.community.dialogs.prompts import NumberWithUnitPrompt, NumberWithUnitPromptType
```

## Number with Unit

The number with unit prompt allows you to prompt for four different unit types:

* Currency
* Temperature
* Age
* Dimension (eg. miles / meters)

```python
dialogs.add(new NumberWithUnitPrompt('numberPrompt', NumberWithUnitPromptType.Currency);
```

Then, you can call the bot by specifying your PromptOptions and calling PromptAsync.

```python
options = PromptOptions(
                    prompt = Activity(
                        type = ActivityTypes.message, 
                        text = "Enter the curreny info"
                        )
                )
        await step_context.prompt("numberprompt",options)
		
```

The prompt will return a NumberWithUnitResult.The object contains a value and unit type.
For example, if a user enters "twenty three dollars" when you are using the Currency prompt type, the resulting NumberWithUnitResult object will have Unit: "Dollar", Value: "23". Below is an example of how you might use this result.

```python
result = f"currency : {turn_context.result.value} and unit : {turn_context.result.unit}"
await turn_context.send_activity(result)
```

## Number with Type

Number with type allows you to accept numbers from the follow type enum:

* Ordinal
* Percentage

```python
dialogs.add(new NumberWithTypePrompt('numberPrompt', NumberWithTypePromptType.Ordinal);
```
The prompt will a return a result based on the NumberWithTypePromptType type. 
For example , If user enters “eleventh” Ordinal type return the result as 11.
Below is an example of how you might use this result.

```python
result = step_context.result
await turn_context.send_activity(result)
```

## Phone Number

The `PhoneNumberPrompt` will extract a phone number from a message from the user.

```python
dialogs.add(new PhoneNumberPrompt('phprompt');
```

Example

```python
User : My phone number is 1 (877) 609-2233
PhoneNumberPrompt return as 1 (877) 609-2233
```

## Email Address

The `EmailPrompt` will extract an email address from a message from the user.

```python
dialogs.add(new EmailPrompt('eprompt');
```

Example

```python
User : My email id is r.vinoth@live.com
EmailPrompt return as r.vinoth@live.com
```

## Internet Protocols

The `InternetProtocolPrompt` will extract one of the following types based on which InternetProtocolPromptType enum value is passed in:

* IPAddress
* URL

```python
dialogs.add(InternetProtocolPrompt("urlprompt",InternetProtocolPromptType.URL))
```
Example

```python
User : My favorite web site is http://rvinothrajendran.github.io/
InternetProtocolPrompt return as http://rvinothrajendran.github.io/
```

## GUID

The `GUIDPrompt` will extract a GUID from a message from the user.

```python
dialogs.add(new GuidPrompt('gprompt');
```

Example

```python
User : my azure id is "7d7b0205-9411-4a29-89ac-b9cd905886fa"
GUIDPrompt return as "7d7b0205-9411-4a29-89ac-b9cd905886fa"
```
