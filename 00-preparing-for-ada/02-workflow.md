# Programming Workflow

## MacOS 

An operating system provides the behind-the-scenes operations that allow humans to interact with computers. Some of these operations include:
- allocating memory and storage to run scheduled tasks
- enforcing security mechanisms and regulating the behavior of processes
- providing common services and functionalities for software applications

The [operating system](https://en.wikipedia.org/wiki/Operating_system) we'll be using at Ada is **MacOS**, a unix-based operating system owned and distributed by Apple Inc. 

### !callout-info

## Updating Software

We'll find that our Macs will need to update the operating system periodically to keep up with security and new features Apple builds. Generally, it is a good idea to update our Mac's software. The version of MacOS we'll use at Ada is **Monterrey**. Unless we make an announcement stating otherwise, we will use Monterrey for the entirety of the program.  

To check our machine's MacOS version, we go to the top left corner of our screen and click  > About This Mac. 

### !end-callout


## MacOS Screen Setup

<iframe src="https://adaacademy.hosted.panopto.com/Panopto/Pages/Embed.aspx?id=209606a9-85a4-4945-b34e-acb5001d2a0e&autoplay=false&offerviewer=true&showtitle=true&showbrand=false&start=0&interactivity=all" height="405" width="720" style="border: 1px solid #464646;" allowfullscreen allow="autoplay"></iframe>

It's very helpful to split our screen when writing code with one half of the screen consisting of our editor and the other the terminal or browser.  This way we can go back and forth between the editor and terminal with minimal disruption. 

There are a number of tools available to help us split our screen including:

* [MacOS Split Desktops](https://www.digitaltrends.com/computing/how-to-use-split-view-on-a-mac/)
* Install [Rectangle](https://rectangleapp.com/) - Free
* Install [Moom App](https://manytricks.com/moom/) - $10

## Terminal

<iframe src="https://adaacademy.hosted.panopto.com/Panopto/Pages/Embed.aspx?id=2cdaf784-ea88-4e27-872f-abd6002f4863&autoplay=false&offerviewer=true&showtitle=true&showbrand=false&start=0&interactivity=all" width=720 height=405 style="border: 1px solid #464646;" allowfullscreen allow="autoplay"></iframe>

As web developers we regularly use the terminal to run, edit, test and debug our applications.  As such it's important to get familiar with using the MacOS terminal. 

To launch terminal hit <kbd>cmd</kbd> + <kbd>spacebar</kbd> and then type terminal.  

![launch terminal](images/launch-terminal.png)

We can also add the terminal application to our dock, by right-clicking on the application. 

![add terminal to dock](images/add-to-dock.png)

There are a variety of keyboard combinations and commands we can use when using the terminal.

We can even write programs to automate the terminal and thus the operating system, which is called **shell programming**.  

### The Mac Keyboard

Macs have a number of special keys which are a little different from Windows.  You can read more about it on [keyshorts.com](https://keyshorts.com/blogs/blog/41999105-the-ultimate-guide-to-macbook-keyboard).  The control, alt/option and command keys are used for a variety of shortcuts in the terminal.

![Mac Keyboard Diagram](images/keyboard.png)

#### Terminal Shortcuts

| Command                             | Description                                                                                         |
| :---------------------------------- | :-------------------------------------------------------------------------------------------------- |
| <kbd>cmd</kbd> + <kbd>k</kbd>       | clear your screen                                                                                   |
| `touch <filename>`                  | creates a new file named filename                                                                   |
| `pwd`                               | <b>p</b>rints the <b>w</b>orking <b>d</b>irectory (displays the full path of the current directory) |
| `cd`                                | <b>c</b>hange <b>d</b>irectory                                                                     |
| `cd ..`                             | go back a directory                                                                                 |
| `cd ~`                              | choose home directory                                                                               |
| `ls`                                | list the items in the directory                                                                     |
| `ls -a`                             | list the items in the directory, including hidden files                                             |
| `mkdir <dirname>`                   | make a new directory                                                                                |
| `rm <filename>`                     | removes the file named filename                                                                     |
| `rm -r <dirname>`                   | removes the directory named dirname (and everything in it)                                          |
| <kbd>&#8593;</kbd>                  | view the previous command                                                                           |
| <kbd>ctrl</kbd> + <kbd>a</kbd>      | go to beginning of line                                                                             |
| <kbd>ctrl</kbd> + <kbd>e</kbd>      | go to end of line                                                                                   |
| <kbd>alt</kbd> + <kbd>&#8594;</kbd> | move to the right, one word                                                                         |
| <kbd>alt</kbd> + <kbd>&#8592;</kbd> | move to the left, one word                                                                          |
| <kbd>ctrl</kbd> + <kbd>c</kbd>      | interrupt/stop a command                                                                            |

### !callout-info

## Command Practice & Tips

In the terminal, let's make a new directory and change our current directory to the new one. 

First let's create a new directory using `mkdir` followed by the directory name `first_folder`. 
    - Ex: `mkdir first_folder`
Then we can change the current directory using `cd` followed by the directory name. Rather than type the entire name of the directory, we can press the **tab** key to have __autocomplete__ the name for us!  
    - Ex: `cd first` then press the **tab** key to see the terminal filled in the rest of the directory name for us! Autocomplete is a handy feature that makes navigating the command line and code easier for us. 
### !end-callout

### The Python Repl

We can enter `python` in the terminal to enter a Read-Eval-Print-Loop environment.  This lets us enter individual lines of Python 3 code and see it immediately evaluated.

There are a few shortcut commands that are helpful to know.

#### Python Repl commands

| Command                                  | Description                    |
| :--------------------------------------- | :----------------------------- |
| `python`   or `python3`                  | start interactive Python session |
| `exit()` or <kbd>ctrl</kbd> + <kbd>d</kbd> | exit Python session          |
| <kbd>ctrl</kbd> + <kbd>c</kbd>           | interrupt/stop a command       |

### Running Python Files

We can run python files from the terminal by typing `python3` followed by the name of the file.  

For example if we have a file named, `example_file.py`, we could run the file from the terminal with the following.

```bash
$ python3 example_file.py
```

### Additional Resources
- https://www.davidbaumgold.com/tutorials/command-line/




