# Dialog Prompts

This is a (currently experimental) suite of dialog prompts that uses Microsoft's recognizer text suite to recognize certain types of input during a dialog prompt. Microsoft's Bot Framework team has implemented a handful of prompts using recognizers from the recognizer text suite. This library is meant to fill the gaps.

> Currently, this library and subsequent PIP are experimental. Please use at your own risk. Feel free to test, debug, and submit pull requests if you come across any issues.

## Installation

You can install this library via PIP:

    ## Coming soon

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
