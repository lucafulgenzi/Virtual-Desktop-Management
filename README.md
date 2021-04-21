# Virtual Desktop Management Script

Script for managing virtual desktops on macOS, such as i3.
Based on [skhd](https://github.com/koekeishiya/skhd) and [yabai](https://github.com/koekeishiya/yabai) 

## Usage

Edit `main.py` and change `TEXT_PATH`

TEXT_PATH is the path of a text document used to control virtual desktop

Example

`User/<user_name>/screen.txt`



Edit `.skhdrc`

`cmd - 1: PATH/TO/SCRIPT <number_of_virtual_desktop>`

#### Example confiugration 

```
# create/focus desktop
cmd - 1 : workspace_man 1
cmd - 2 : workspace_man 2
cmd - 3 : workspace_man 3
cmd - 4 : workspace_man 4
cmd - 5 : workspace_man 5
cmd - 6 : workspace_man 6
cmd - 7 : workspace_man 7
cmd - 8 : workspace_man 8
cmd - 9 : workspace_man 9
```
(workspace_man is an alias )

## How work
If the desktop we want to create already exists, we are simply redirected to it, if it is not present it creates one and redirects us.
If the desktop we want to move from is empty that desktop is deleted and we are redirected to whatever we want. 

### WORKS WITH ONLY ONE SCREEN 

## Future features
- [ ] Work on multiple display
- [ ] Move an application between desktop
