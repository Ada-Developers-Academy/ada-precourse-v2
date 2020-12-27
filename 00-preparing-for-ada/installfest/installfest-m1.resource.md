# Getting an M1 Macbook Ready for Ada

Currently many of the packages we use at Ada through the package manager Homebrew are not fully supported to run on M1 Macs, also known as Apple Silicon.

To get around this we will set up a development environment using [Rosetta 2](https://developer.apple.com/documentation/apple_silicon/about_the_rosetta_translation_environment).  This will let us run our development tools/packages in Intel emulation mode.  In other words we'll have Rosetta pretend to be an Intel Mac and translate their Intel commands into M1 commands.

Here’s the workaround until native support arrives:

1.  Locate the Terminal application within the Utilities folder (Finder > Go menu > Utilities) 
1.  Select Terminal.app and right-click on it, then choose “Duplicate”
1.  Rename the duplicated Terminal app something obvious and distinct, like ‘Rosetta Terminal’
1.  Now select the freshly renamed ‘Rosetta Terminal’ app and right-click and choose “Get Info” (or hit Command+i)
1.  Check the box for “Open using Rosetta”, then close the Get Info window
1.  Run the “Rosetta Terminal” as usual, which will fully support Homebrew and other x86 command line apps
1.  Until homebrew becomes fully supported, use the "Rosetta Terminal" exclusively until Homebrew is ready to work natively.  Just ignore the regular terminal.

## Then do the Intel-based Installfest

After you have your Rosetta Terminal set up, you can then start the [Intel installfest](installfest-intel.resource.md) substituting the Rosetta Terminal for the regular'ole terminal.

## Exceptions - Chrome & Slack

You can just use the intel installfest to install Chrome & Slack, or manually install them (not using homebrew).

- [Install Chrome](https://www.google.com/chrome/)
- [Install Slack](https://slack.com/downloads/mac)

## Resources

- [This guide is taken from OSX Daily](https://osxdaily.com/2020/11/18/how-run-homebrew-x86-terminal-apple-silicon-mac/)
- [Homebrew's Current status on Apple Silicon](https://github.com/Homebrew/brew/issues/10152)
