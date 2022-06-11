## Installation example

### init.py
```
import nuke

nuke.pluginAddPath('./path') # path= The path of openDotNuke.py file relative to .nuke folder
```

### menu.py
```
import nuke
import openDotNuke

nuke.menu("Nuke").addMenu("Python Script").addCommand("Open the .nuke folder", "openDotNuke.openDotNuke()", "^+.")
```
