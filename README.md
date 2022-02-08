# btd6
This started out as an attempt to determine what the hit boxes for each tower in Bloons Tower Defense 6 were, but eventually became a script for placing perfectly tesselated tower grids of any tower type, as well as automating various processes such as upgrading and tower selling / etc. Could most likely be used to automate a btd6 race but I'll leave that to someone else for testing.

If you wish to dive deeper into automating btd6 with python, and need access to things such as the round count; You may find my [other btd6 based repo](https://github.com/56kyle/bloons_auto) helpfull. It contains a lot more info and uses Frida to dynamically hook into some of the games methods, but it isn't explained very well. If you would like more of an explanation feel free to message me about it, I could go on for way too long about that whole endeavor.

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

