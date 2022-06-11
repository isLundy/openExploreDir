# open the .nuke folder
python script for Nuke.

## Installation example

### init.py
```python
nuke.pluginAddPath('./path') # path= The path of openDotNuke.py file rea]lative to .nuke folder
```

### menu.py
```python
import openDotNuke
nuke.menu("Nuke").addMenu("Python Script").addCommand("Open the .nuke folder", "openDotNuke.openDotNuke()", "^+.")
```
