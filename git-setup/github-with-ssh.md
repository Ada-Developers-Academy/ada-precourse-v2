# Connecting To Github Over SSH

<iframe src="https://adaacademy.hosted.panopto.com/Panopto/Pages/Embed.aspx?id=226728e9-67c1-437a-bb3e-ae3801219f73&autoplay=false&offerviewer=true&showtitle=true&showbrand=false&captions=true&interactivity=all" height="405" width="720" style="border: 1px solid #464646;" allowfullscreen allow="autoplay"></iframe>

## Introduction

The **S**ecure **S**hell **P**rotocol is a cryptographic network protocol for operating network services securely over an unsecured network. As developers we often use SSH to remotely login or connect to servers over a network. Github allows users to connect their personal git to their remote repositories on Github using SSH among other methods.

With SSH we generate two cryptographic keys a *public key* and a *private key*.  We share the public key with Github and a private key we keep on our local machine.  When we make git commands to github they are encrypted using our private key and Github can use the public key to decrypt them.  If the keys match properly Github will be able to decrypt our commands and execute them.

## Generating A New SSH Key Pair

First we can open the terminal and run the following command, **substituting your Github email address**.

```
$ ssh-keygen -t ed25519 -C "your_email@example.com"
```

We will be prompted to "Enter a file in which to save the key".  We can **press Enter** to accept the default filename.

```
Generating public/private ed25519 key pair.
Enter file in which to save the key (/Users/chrismcanally/.ssh/id_ed25519):
```

Then we will be prompted to enter a "passphrase".  We can enter any phrase to generate the keys.

```
 Enter passphrase (empty for no passphrase): [Type a passphrase]
 Enter same passphrase again: [Type passphrase again]
```

### Add SSH Key To SSH Agent

We can then start the SSH agent, a program to handle ssh connections, to run in the background.

```
$ eval "$(ssh-agent -s)"
Agent pid 34342
```

We can then modify our `~/.ssh/config` file to automatically load keys into the ssh-agent and store passphrases in our keychain, the tool MacOS uses to store passwords and security tokens.

We can check to see if the file exists

```
$ cat ~/.ssh/config
```

If we get a message that the file does not exist we can create it.

```
$ touch ~/.ssh/config
```

Then we can open the file with the command:

```
$ code ~/.ssh/config
```

And make it match the contents making sure the filename matches the one we created.

```
Host *
  AddKeysToAgent yes
  UseKeychain yes
  IdentityFile ~/.ssh/id_ed25519
```

### Add SSH Private Key to the SSH Agent

We can then add the private key to the ssh-agent matching `id_ed25519` to the file we created earlier.

```
$ ssh-add -K ~/.ssh/id_ed25519
```

## Add New SSH Key To Github

Next we can add our public SSH key to Github.

First we can copy the public key to the clipboard (so we can paste it later) with the command:

```
$ pbcopy < ~/.ssh/id_ed25519.pub
```

Making sure that `id_ed25519.pub` matches the file we created earlier.

Then we can go to `Settings` in our [Github](https://github.com) Account.

![Github Settings](images/github-setup__github-settings.png)

Then we can find the `SSH and GPG Keys` section under `Access`.

![SSH and GPG Keys](images/github-setup__github-ssh-and-gcp-keys.png)

Then we can add a new ssh key with the `New SSH Key` button.

![Create New SSH Key](images/github-setup__generate-new-ssh-key.png)

Then we can give the key a name and paste the public key into the `Key` field.  

![SSH Key Details](images/github-setup__new-public-ssh-key.png)

We may need to confirm our password.

![Password confirmation](images/github-setup__confirm-password.png)

Then we can save the key.

## Cloning a Repository with SSH

We can then test the keys with the by cloning a repository with SSH. 

First CD into our `Developer` folder.

```
$ cd ~/Developer
```

Then go to a sample git repository on github.  

Go to [https://github.com/AdaGold/python-fizzbuzz](https://github.com/AdaGold/python-fizzbuzz).

Select the SSH Clone option

![SSH Clone](images/github-setup__clone-with-ssh.png)

1.  First click on the Green `Code` Button
1.  Next Click on the `SSH` option
1.  Lastly click on the copy button to copy the link to the clipboard

Next in terminal you can clone the repository by typing `git clone ` and pasting the link you copied from the browser with `command-v`.

```
$ git clone git@github.com:AdaGold/python-fizzbuzz.git
```

You should see a new subfolder in your `~/Developer` directory named `python-fizzbuzz`.

The following commands should move the terminal to the `python-fizzbuzz` directory and then open the project with VS Code.

```
$ cd python-fizzbuzz
$ code .
```

In the future you can download repository starter code with:

1.  Go to the repository page in Github.com
1.  Click on the Code button and copy the SSH link
1.  Type `git clone ` paste the link to the repository and press `Enter`.

This will clone a repository to your local computer.

## Other Useful Commands

### Check For Existing SSH Keys

We can check for existing SSH keys by running the following command:

```
$ ls -al ~/.ssh
```

The command should list the contents of the `~/.ssh` directory.

```
-rw-r--r--   1 username  staff    80 Jul 23  2021 config
-rw-------   1 username  staff   484 Jul 23  2021 id_ed25519
-rw-r--r--   1 username  staff   112 Jul 23  2021 id_ed25519.pub
```

By default files containing ssh keys can be named one of the following:

- `id_rsa.pub`
- `id_ecdsa.pub`
- `id_ed25519.pub`

## Summary

In this lesson we walked through how to set git to connect to Github and authenticate using SSH. SSH is one method of connecting to Github and allows us to securely move files including code between our local computers and the Github servers.

## Resources

- [Github on SSH Key Authentication](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/about-ssh)