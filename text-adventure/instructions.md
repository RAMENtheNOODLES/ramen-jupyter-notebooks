# How to use Text Adventure Creator
---

The file structure goes as follows:
```
.
├── Example Chapter             # Chapter Files
│   ├── story.txt               # Required file that contains the story for the chapter
│   ├── [area_name].txt         # Optional secondary file that contains the story for an area
│   └── ...                     # You can add as many area files as you want
├── story_chapters.txt          # Required file that contains the names of all the chapters (the folder name)
└── plugins                     # Optional folder that contains all of the plugins for the adventure
    ├── [plugin_name].plugin    # Optional plugin file that contains the code that is customizable
    └── ...                     # You can create as many plugins as you want
```
---
## Commands
- Text
  - Example:
    - `text: This is some text!`
  - Usage:
    - `text: [text to display to the user]`
  - The text command is used to display text to the user
- Text, (Color)
  - Example:
    - `text, red: This text is shown in red!`
  - Adding `, [color]` after the text command can change the color[^1] of the text displayed to the user
- Prompt
  - Example:
    - `prompt, (n, e, s, w) > (north, east, south, west): Hello!`
  - The prompt command can be used to prompt the user. Using it goes as follows:
    - `prompt, ([choices]) > ([name of the files to goto]): [Text to display after the prompt]`
- Wait
  - Example:
    - `wait, 2: You waited for 2 seconds!`
  - Usage:
    - `wait, [# of seconds to wait]: [Display text]`
  - The command waits for the specified amount of time, then displays some text to the user
- Goto
  - Example:
    - `goto: north`
  - Usage:
    - `goto: [name of file to go to]`
  - The command switches to another file ***in the same chapter*** and reads from there
- Goto > (chapter): (file)
  - Example:
    - `goto > middle: story`
  - Usage:
    - `goto > [chapter]: [file in the chapter]`
  - The command switches to another file in ***another*** chapter, set the file to **story** to read the main file
- Plugin
  - This command is currently not implemented

[^1]: The colors you can use are: Black, Red, Green, Yellow, Blue, Magenta, Cyan, and White
