# What are rules?
Rules are context that the ai agent, that you are working with, should have at all times. 
They can be used to: 
    - Set the expertise of the ai agent
    - Set the level of detail the ai agent should provide in its outputs
    - Set the restrictions and constraints the ai agent should follow when generating outputs

# Example of a rule:
```
- You are a senior software engineer with 10 years of experience in Python and JavaScript.
- You should provide detailed explanations and code examples in your outputs.
- After implementing any functional unit or code you should test it by:
    - running the test suite
    - providing the test results in your output
    - if errors are found, mention the errors 
```

# where do you add rules?
depending on the IDE and the Ai agent that you are using for your software development, you can add the rules in different ways. 

*cursor*:
.cursor/
  rules/
    <some_rule>.md
(in the root of the project)

*codex*:  
AGENTS.md
(in the root of the project)

