# btd6
This started out as an attempt to determine what the hit boxes for each tower in Bloons Tower Defense 6 were, but eventually became a script for placing perfectly tesselated tower grids of any tower type, as well as automating various processes such as upgrading and tower selling / etc. Could most likely be used to automate a btd6 race but I'll leave that to someone else for testing.

P.S. - If you would like to see what the tower hitboxes look like, go to towers/hitboxes for some examples

## Example
The following code:
```python
from towers.dart import Dart
import time

if __name__ == "__main__":
    time.sleep(1)
    darts = Dart.box(3, 3, upgrades=[2, 4, 0])
    time.sleep(2)
    del darts
```
      
will produce this as a result:

![gif of dart monkeys being placed](https://github.com/56kyle/btd6/blob/master/dart_box.gif)

