---
name: template_skill # the name of the skill should match the name of the folder where the skill is located.
description: This is a template skill, you can copy and modify it to create your own skill # a brief description of the skill, what it does and how it can be used. (descriptive)
---
license: 
allowed-tools:
compatibility:
metadata:
  author: 
  version:

# What are skills?

Agent Skills are a lightweight, open format for extending AI agent capabilities with specialized knowledge and workflows.
At its core, a skill is a folder containing a SKILL.md file. This file includes metadata (name and description, at minimum) and instructions that tell an agent how to perform a specific task. Skills can also bundle scripts, templates, and reference materials.

my-skill/
├── SKILL.md          # Required: instructions + metadata
├── scripts/          # Optional: executable code
├── references/       # Optional: documentation
└── assets/           # Optional: templates, resources

Skills use progressive disclosure to manage context efficiently:
Discovery: At startup, agents load only the name and description of each available skill, just enough to know when it might be relevant.
Activation: When a task matches a skill’s description, the agent reads the full SKILL.md instructions into context.
Execution: The agent follows the instructions, optionally loading referenced files or executing bundled code as needed.
This approach keeps agents fast while giving them access to more context on demand.

# Where to add skills?
Depending on the IDE and the AI agent that you are using for your software development, you can add the skills in different ways. Here are some examples:

*cursor*: 
.cursor/
  skills/
    <some_skill>/
      SKILL.md 
      scripts/ 
      templates/
      references/
      assets/
      license.txt 
(in the root of the project)

You can also install or manually add skills (with cursor) and they will be stored in the loction: ~/.cursor/skills-cursor/
These skills are global and get applied when working on any project. 

*codex*:
.agents/
  skills/
    <some_skill>/
      SKILL.md 
      scripts/ 
      templates/
      references/
      assets/
      license.txt
(in the root of the project)

You can also install or manually add skills (with codex) and they will be stored in the loction: ~/.codex/skills/
These skills are global and get applied when working on any project. 
