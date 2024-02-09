# Virtual box

- Download and install [VirtualBox >=7.0.12](https://www.virtualbox.org/wiki/Downloads) for your OS. On Ubuntu use `apt` to install the package, run the following command from the directory with `*.deb` file:

```bash
chmod u+x virtualbox-7.0_7.0.12-159484~Ubuntu~jammy_amd64.deb
sudo apt install ./virtualbox-7.0_7.0.12-159484~Ubuntu~jammy_amd64.deb 
```

# Ubuntu

- Download [Ubuntu 22.04](https://ubuntu.com/download) image
- Launch VirtualBox and click on `New` (`Ctrl+N`)
- Set `Name`, `Folder`, `ISO Image` and click `Next`
- Set user name and password, check `Guest Additions` box and click `Next`
- Set `Base Memory` (2048+ MBs should be fine), `Processors` (around half of the available **physical** cores), optionally check `EFI` and click `Next`
- Set `Create a Virtual Hard Disk Now` (40+ GBs should be fine) and click `Next`
- Review summary and click `Finish`
- Wait for `Ubuntu` installation process to finish (you can do the following optional steps while installation is in process, note, both features require `Guest Additions` to work)
- (optional) Set `Shared Clipboard` to `Bidirectional` in `Settings -> General -> Advanced`
- (optional) Add a shared folder in `Settings -> Shared Folders`, set mount point to `/home/<user>/data` and check the `Auto-mount` box
- After installation VM will automatically restart, login using your user and password, finish the first time setup
- Click `Show Applications` in the left bottom and search to `Terminal`, click the icon to open it
- For `VB 7.0.12` and `Ubuntu 22.04.3` the terminal won't open due to wrong lang encoding config during automatic installation, to fix it go to `Show Applications`, search and click `Settings`, navigate to `Language and Region` and set `Language` to `United Kingdom`, ones changed do not `Restart`, but click on the right top corner and `Power Off`; start VM again and the terminal should be fixed


- Add user to sudo group (replace `<user>` with your user name, need to restart VM or logout after adding)
    ```bash
    su
    adduser <user> sudo
    exit
    ```
- (optional) Update & upgrade your Linux software, in `Terminal` type `sudo apt update` in the terminal and press enter, enter your password, wait for the command to finish; type `sudo apt upgrade`, type `Y` and press enter, wait for the command to finish and you are done!

# Anaconda & basic python env

- [Download](https://www.anaconda.com/download/)
- Install (type yes to all prompts and restart terminal when the installation is finished)
    ```bash
    cd ~/Downloads
    chmod u+x Anaconda3-2023.09-0-Linux-x86_64.sh
    ./Anaconda3-2023.09-0-Linux-x86_64.sh
    ```
- Update
    ```bash
    conda update conda
    ```
- Create and activate virtual environment (use `conda deactivate` to deactivate it)
    ```bash
    conda create -n nstu python=3.12
    conda activate nstu
    ```
- Install python libs
    ```bash
    pip install jupyterlab numpy pandas scipy matplotlib
    ```
- Start `jupyter-lab` (you can press `Ctrl+C` twice to close it in `Terminal`)
    ```bash
    jupyter-lab
    ```

# (optional) git

```bash
sudo apt install git
```

# (optional) zsh and plugins

```bash
sudo apt install zsh
```

[ohmyzsh](https://github.com/ohmyzsh/ohmyzsh) is a framework for managing zsh configuration

```bash
sudo apt install curl
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
```

After installation of `ohmyzsh`, the shell will switch to `zsh` (say no to default), but default shell is still `bash`. 
Install `zsh` plugins:
```bash
git clone --depth 1 https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions
git clone --depth 1 https://github.com/unixorn/fzf-zsh-plugin.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/fzf-zsh-plugin
git clone --depth 1 https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting
```

Next, type `nano .zshrc` (simple text editor) and replace
```
plugins=(git)
```
with
```
plugins=(git z zsh-autosuggestions fzf-zsh-plugin zsh-syntax-highlighting)
```
Hit `Crt-O` and press `Enter` to save, then `Crt-X` to exit. Finally, restart `zsh`:

```bash
zsh
```
Now, each time you open a terminal, you can start `zsh` shell

# (optional) tmux

```bash
sudo apt install tmux
```

# (optional) ssh

- Install ssh server (VM)
    ```bash
    sudo apt install openssh-server 
    ```
- In VB settings go to `Network`, expand `Advanced` flag, click `Port Forwarding` and add new:

    | Name | Protocol | Host IP | Host Port | Guest IP | Guest Port |
    |------|----------|---------|-----------|----------|------------|
    | ssh  | TCP      |         | 8822      |          | 22         |

- `ssh` from host to VM
    ```bash
    ssh -p 8822 nstu@localhost
    ```

# (optional) Gemini LLM (requires VPN)

- Setup [API key](https://makersuite.google.com/app/apikey)
- Test (or use) gemini with `curl`
    ```bash
    curl \
      -H 'Content-Type: application/json' \
      -d '{"contents":[{"parts":[{"text":"Write a story about a magic backpack"}]}]}' \
      -X POST https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key=YOUR_API_KEY
    ```
- See [quickstart guide](https://ai.google.dev/tutorials/python_quickstart)
- See provided python examples

# (optional) VSCode

- [Download](https://code.visualstudio.com/) and install for your system
- Suggested extensions to try
    - Python
    - Jupyter

# (optional) Wolfram Engine

- [Download](https://www.wolfram.com/engine/) installer
- Get your license (you'll need to register and enter your credentials after installation)
- Install Wolfram Engine
    ```bash
    cd ~/Downloads
    chmod u+x WolframEngine_14.0.0_LINUX.sh
    sudo ./WolframEngine_14.0.0_LINUX.sh
    ```
- Start `WolframKernel` and enter your credentials (user name and password)
    ```bash
    WolframKernel 
    Wolfram Language 14.0.0 Engine for Linux x86 (64-bit)
    Copyright 1988-2023 Wolfram Research, Inc.

    In[1]:= Exit[]     
    ```
- Install [Wolfram Language kernel for Jupyter](https://github.com/WolframResearch/WolframLanguageForJupyter)
    ```bash
    cd ~/Downloads
    git clone https://github.com/WolframResearch/WolframLanguageForJupyter.git
    cd WolframLanguageForJupyter
    ./configure-jupyter.wls add
    ```
