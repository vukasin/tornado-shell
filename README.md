tornado-shell
=============

A interactive shell for tornado processes. **The commands are executed INSIDE the main IOLoop so blocking calls will cause the IOLoop to block.**

Here's a code example. This will open a prompt where you can interact with the system. A variable named 'ioloop' will be visible.

```python
import tornado.ioloop as io
import tornadoshell

ioloop = io.IOLoop.instance()

shell = tornadoshell.Shell(context={'ioloop': ioloop})
shell.start()

ioloop.start()
```

Here's an example interaction using the above code:

```bash
mbpro:tornado-shell vukasin$ python3 test.py 
$>ioloop
<tornado.platform.kqueue.KQueueIOLoop object at 0x1006ccd90>
$>__name__
'builtins'
$>exit()
mbpro:tornado-shell vukasin$ 
```
