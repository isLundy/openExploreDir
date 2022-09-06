## Introduce

Original name: winExploreDir. 

Original author: code written by Thorsten, release by Varun Hadkar.

The name and code of the script have been all changed by me and republished on NukePedia, new features added and available for Windows, Linux, Mac.

<br />

`Feature`: 

open the directory of the current project and the file directory of the read node # shortcut: Shift + B

open .nuke directory # shortcut: Shift + 0

open nuke installation directory

## Installation example

### init.py
> example
```python
import nuke

nuke.pluginAddPath('./openExploreDir') # openExploreDir = The path of openExploreDir.py file relative to .nuke folder
```

### menu.py
> example
```python
import nuke
import openExploreDir

s = nuke.menu("Nuke").addMenu("PythonScripts/Misc")
i = s.addMenu("OpenExploreDir")
i.addCommand("Open nk or file dir", "openExploreDir.openFileDir()", "+b")
i.addCommand("Open .nuke dir", "openExploreDir.openDotNuke()", "+0")
i.addCommand("Open nuke installation dir", "openExploreDir.openExePath()")
```
