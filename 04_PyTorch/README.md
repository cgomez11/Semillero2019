# PyTorch tutorial
This is an introduction to PyTorch. We aim to cover main aspects such as tensor manipulation, Autograd, training models and some examples.


## Useful tools

### Linux Screen 
Screen is a terminal multiplexer. Processes running in screen will continue to run when their window is not visible even if 
you get disconnected. 

* Check if it is installed on your system by typing:
```bash
screen --version
```

* Create a named session when you run multiple screen sessions:
```bash
screen -S session_name
```

This will open a screen session, create a new window and start a shell in that window.

* Detach from Linux screen session at any time:
```bash
Ctrl+a d
```

The program running in the screen session will continue to run after you detach from the session.
Be careful to use the complete command, if you only type Ctrl+d, the screen will terminate. 


* Reattach or resume a Linux screen:
```bash
screen -r session_name
```

If you have multiple screen sessions running, you can find the session ID list with:
```bash
screen -ls 
```

There is a unique number for each session, followed by the name your assigned it. You can also
check the status of each screen session (Detached or attached).

* If your screen session is attached, you cannot resume with -r, you have to detach it first:
```bash
screen -d session_name
```

* To end a detached screen session:
```bash
screen -XS session_name kill
```
This short introduction was based on [How To Use Linux Screen](.https://linuxize.com/post/how-to-use-linux-screen/).

### The Python Debugger: pdb
The module pdb defines an interactive source code debugger for Python programs. It supports setting breakpoints and single stepping at the source line level.

The typical usage to break into the debugger from a running program is to insert:
```bash
import pdb; pdb.set_trace()
```
at the location you want to break into the debugger. You can then step through the code following this statement (type n), and continue running without the debugger using the continue command. If you want to quit debugging, type q. 

## June 28
Now that you are familiarized with PyTorch:
* Create your dataloader with your own data, verify that the data is loaded correctly, that you apply the transformations, 
and can iterate over the loaders. 

* Once you have loaded your data, train a small network! you can use the one from MNIST example, or load a pretrained model
(we will learn this today). 


## Acknowledgments
Some of the basic tutorial codes are based on [jcjohnson's PyTorch basic examples](https://github.com/jcjohnson/pytorch-examples). Other sources and examples are taken directly from PyTorch documentation. 

