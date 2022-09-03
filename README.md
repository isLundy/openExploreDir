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
import openDotNuke

nuke.menu("Nuke").addMenu("Python Script").addCommand("Open the .nuke folder", "openDotNuke.openDotNuke()", "Ctrl+Shift+.")
```
