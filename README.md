## Introduce

original name: winExploreDir, author: code written by Thorsten, release by Varun Hadkar.

Name and code have been all changed by me and republished on NukePedia, new features added and available for Windows, Linux, Mac.

## Installation example

### init.py
> example
```python
import nuke

nuke.pluginAddPath('./directory') # directory = The path of openDotNuke.py file relative to .nuke folder
```

### menu.py
> example
```python
import nuke
import openExploreDir

s = nuke.menu("Nuke").addMenu("PythonScripts/Misc")
i = s.addMenu("OpenExploreDir")
i.addCommand("Open nk or file dir", "openExploreDir.openFileDir()", "+b", icon="Lundy_Tools.png")
i.addCommand("Open .nuke dir", "openExploreDir.openDotNuke()", "+0", icon="Lundy_Tools.png")
i.addCommand("Open nuke installation dir", "openExploreDir.openExePath()", icon="Lundy_Tools.png")
```
