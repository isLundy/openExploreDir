## Introduce

Original name: winExploreDir. 

Original author: The code written by Thorsten and released by Varun Hadkar.

The name and code of the script all have been changed by me, `new features` added and available for `Windows`, `Linux`, `Mac`.

<br />

## Feature 

open `current project` directory or node `file knob` directory (like `Read Node`, `Write` Node, `ReadGeo` Node, `Camera` Node, `WriteGeo`, etc)- - - - - - - shortcut: `Shift + B`

open the `.nuke` directory - - - - - - - shortcut: `Shift + 0`

open the `nuke installation` directory

<br />

## Installation example
### init.py
> example
```python
import nuke

nuke.pluginAddPath('./PythonScripts/openExploreDir')
```

### menu.py
> example
```python
import nuke
import openExploreDir

s = nuke.menu("Nuke").addMenu("PythonScripts")
h = s.addMenu("OpenExploreDir")
h.addCommand("Open nk or file dir", "openExploreDir.openFileDir()", "+b")
h.addCommand("Open .nuke dir", "openExploreDir.openDotNuke()", "+0")
h.addCommand("Open nuke installation dir", "openExploreDir.openExePath()")
```
