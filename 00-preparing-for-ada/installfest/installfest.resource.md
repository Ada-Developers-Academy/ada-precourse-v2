# Installfest

<iframe src="https://adaacademy.hosted.panopto.com/Panopto/Pages/Embed.aspx?id=74b0dc57-aec2-497a-a14b-ac9f0020d987&autoplay=false&offerviewer=true&showtitle=true&showbrand=false&start=0&interactivity=all" height="405" width="720" style="border: 1px solid #464646;" allowfullscreen allow="autoplay"></iframe>

## Overview

This time is dedicated to ensuring everyone has all of the tools, the right tools, and the right versions of tools to begin programming with the Ada curriculum.

Many of you will have some set of these tools installed, but we're going to go through them together and make sure everyone is set to go.

Follow the steps below, typing any necessary code into the Terminal application.

If you've got pieces installed, help your fellow students via Slack!

## Xcode Command-line Developer tools

Apple provides a set of UNIX-style development tools on the command-line.  To install it go to terminal and enter

```
xcode-select --install
```

You will then be prompted to allow it to install.

![Xcode command line tools install](../images/confirm-install-command-line-tools-mac-os-x.jpg)

At this point, get some coffee... it may take a while... maybe homebrewed coffee!

## Install Homebrew, Python 3, Node & Optionals

The following script will install some tools we will use including:

- Homebrew
- Python 3
- Pip 3
- Git
- Node

It will also give you some options to automatically install:

- Firefox
- Google Chrome
- VS Code
- Slack for Mac

Copy the line below in it's entirety, paste it into the terminal and hit enter.  You will be prompted for your password.  Don't be alarmed if you don't see your password, it's still getting entered.

```bash
/bin/bash -c "$(curl -fsSL https://gist.githubusercontent.com/CheezItMan/e31aebdb0f686c1a194e980b24f3cea4/raw/5710e04d17a7840df3df0ea95502da275a9943cb/ada_c14_installfest.bash)"
```

**When the install finishes quit and restart your terminal.** Without doing this, the installation above may not take affect.

### About Homebrew

[Homebrew](https://brew.sh/) is a package manager for Mac.  Basically that means that Homebrew helps you install programs, update them and prevent conflicts between applications or tools.
#### Verification

You can verify that it homebrew is working properly by entering in the terminal

```
brew doctor
```

You should see, after a bit of processing, `Your system is ready to brew.`

### About Python 3

Macs come with an older version of Python, usually 2.7.x.  However we will be using a version of Python 3 and we need to set up the Mac to use it.  Thus we used homebrew to install it.

#### PIP - Python's Package Installer Programm

We also use a program called **pip** to install additional python packages we can then use in our programs.  Pip was installed with Python 3

#### Verification

You can verify that it worked with the command `python --version` and see that it prints something like `Python 3.9.1`. If it is not using the correct version, perhaps you missed the step above about restarting your terminal. Try quitting your terminal and reopening it to see if that fixes it...If not, reach out to a classmate or instructor!

You should also verify that `pip` is working with `pip --version` and it should be in a python3 folder and say something like `pip 20.3.1 from /usr/local/lib/python3.9/site-packages/pip (python 3.9)`

### VS Code

* [VS Code](https://code.visualstudio.com/) is a very extensible open-source editor which supports a variety of languages including Python, and JavaScript.  
* In VS Code, type <kbd>shift</kbd> + <kbd>cmd</kbd> + <kbd>p</kbd> and type **>shell command install code command in path**.
  * This only needs to be done once to allow you to launch VS code from the terminal
* Now, to launch VS Code from terminal, type `code` followed by the file name or directory name
  * For example `code .` will open the present directory as a project folder.
* Then open the command-palette with <kbd>shift</kbd> + <kbd>cmd</kbd> + <kbd>p</kbd>  and enter `Python: select interpreter`

![VS Code Select Python Interpreter](../images/select-interpreter.png)

![Python 3.9 interpreter](../images/python-3.9-interpreter.png)

#### VS Code Extensions

VS Code also comes with a number of extensions which you can install to provide new or different functionality. 

Extensions can be searched for and installed from the "Extensions" menu on the sidebar of VS Code. 

![Extensions Sidebar Button](../images/vscode-extensions.png)

Some of the recommended extensions include:

*  [Live Share](https://marketplace.visualstudio.com/items?itemName=MS-vsliveshare.vsliveshare) - A way to collaborate on source code like Google Docs.
*  [Markdown All in One](https://marketplace.visualstudio.com/items?itemName=yzhang.markdown-all-in-one) - An extension to help writing markdown files
*  [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python) - The standard Python extension to provide syntax highlighting and code suggestions.
*  [Indent Rainbow](https://marketplace.visualstudio.com/items?itemName=oderwat.indent-rainbow) - A nice extension to help you line up your indentations.
*  [Bracket Pair Colorizer](https://marketplace.visualstudio.com/items?itemName=CoenraadS.bracket-pair-colorizer) - This extension colors matching brackets {} to match and make them easier to identify.
*  [Python Test Explorer](https://marketplace.visualstudio.com/items?itemName=LittleFoxTeam.vscode-python-test-adapter) - This extension lets you run tests individually in VS code via the Test Explorer UI.
*  [ESLint](https://marketplace.visualstudio.com/items?itemName=dbaeumer.vscode-eslint) - A style checker for JavaScript code.

You are welcome to experiment with a variety of plugins for VS Code.

### About Git

Git is an open source distributed version control system. We will talk about git in significant detail later. The short version is that we will use Git to version and share our code with others. We will spend a lot of time using Git in the Terminal, so it will become important that we configure the Terminal to have all of our Git preferences it and personalize it with our personal information.

#### Trust but Verify

You can make sure git is installed properly by entering the following at the terminal.

- `git config --get user.name` Should show your name
- `git config --get user.email` Should show the email address associated with your GitHub account

## Browsers

We will be using [Firefox](https://www.mozilla.org/en-US/firefox/) as our primary browser at Ada.  If you did not elect to install it automatically above you can install it with:

```bash
brew install --cask firefox
```

Or you can go to the website and install it manually.

You may also want to use Google Chrome, which is also a fine browser.  You can install Google Chrome with Homebrew by typing:

```bash
brew install --cask google-chrome
```

Or again, you can go to Google's website and install it manually.

## It's All About Communication! Slack

Lastly we you should already have Ada's primary mode of communication installed... [**Slack!**](https://slack.com/downloads/osx). While it is **possible** to get by using the Slack website.  We recommend **strongly** to use the Desktop client.  If you did not use our script to install it, you can install Slack with homebrew and the command:

```bash
brew install --cask slack
```

Or you can go to [slack.com](https://slack.com) and install it manually.

### Why Slack?

When Ada has announcements or students want to share general information, we will generally use Slack.  If we have updates to projects or homework, we will use Slack.  We only use e-mail for personal communication and things we need to keep a record of (like absences).

That being said, please get familiar and comfortable with Slack, and make it your own space to build special-interest channels and discussion spaces.

It's also critically important to use emojis (not really, but it's fun!).  So once you have Slack running follow the directions [**here**](https://get.slack.help/hc/en-us/articles/206870177-Create-custom-emoji) to install a Slack Emoji of your choice.

You can find a great site for Slack Emoji [**here**](https://slackmojis.com/).


## Customizing Your Shell - Optional

*This is totally optional!*

### Setting zsh as the default shell

A shell is a set of commands and user interface for controlling an operating system via the terminal.  With newly purchased Macs the default shell is zsh, while older macs use an older version of the Bash shell.

You can read more about [zsh vs bash](https://dev.to/jasmin/a-brief-difference-between-zsh-and-bash-5ebp) if you are interested.  

To set your shell to zsh first start terminal and then go to preferences.

![set terminal preferences](../images/terminal-preferences.png)

Then set the **Shells open with:** to `/bin/zsh`.

![set default shell to zsh](../images/set-default-shell.png)

### Oh My Zsh

Zsh is very customizable environent in zsh and there's a great community-driven framework for managing zsh configurations providing thousands of helper functions, plugins and themes.  Basically it lets you customize the look and feel of the terminal and add custom commands and shortcuts.  The most amazing thing is that **it comes with git integration!**

Using **Oh My Zsh** is completely optional at Ada, but it can be handy for it's support of git and extensibility.  You are welcome to install it if you are interested.

You can install it with:

```zsh
sh -c "$(curl -fsSL https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"
```

You can read more about it on the [oh my zsh homepage](https://ohmyz.sh/).

## Note

If for any of these applications you get the following warning.

![Unsigned Application Warning](../images/unsigned-app.png)

You can fix it by going to **System Preferences-->Security & Privacy** and selecting the button **Open Anyway**.

![System Preferences](../images/systempreferences.png)

![Security & Privacy](../images/security-and-privacy.png)

![Open anyway](../images/open-anyway.jpg)

## In this lesson we installed:

1.  Xcode Command-line tools
1.  Python 3
1.  VS Code
1.  Firefox
1.  Git
1.  Slack

These tools will be important as we begin to write programs at Ada.  
