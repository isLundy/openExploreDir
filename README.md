## Installation example

### init.py
```python
import nuke

nuke.pluginAddPath('./path') # path= The path of openDotNuke.py file relative to .nuke folder
```

### menu.py
```python
import nuke
import openDotNuke

nuke.menu("Nuke").addMenu("Python Script").addCommand("Open the .nuke folder", "openDotNuke.openDotNuke()", "^+.")
```
