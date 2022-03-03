# How to use Text Adventure Creator
---

The file structure goes as follows:
```
Root -
        Example Chapter -
                            story.txt (required)
                            area.txt  (optional)
        story_chapters.txt
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
  - The command 


[^1]: The colors you can use are: Black, Red, Green, Yellow, Blue, Magenta, Cyan, and White
