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

s = nuke.menu("Nuke").addMenu("PythonScripts")
i = s.addMenu("OpenExploreDir")
i.addCommand("Open nk or file dir", "openExploreDir.openFileDir()", "+b", icon="Lundy_Tools.png")
i.addCommand("Open .nuke dir", "openExploreDir.openDotNuke()", "+0", icon="Lundy_Tools.png")
i.addCommand("Open nuke installation dir", "openExploreDir.openExePath()", icon="Lundy_Tools.png")
```
