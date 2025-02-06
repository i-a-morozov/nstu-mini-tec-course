<!-- SECTION  -->
# Navigation
- [Virtual box](#virtual-box)
- [Ubuntu](#ubuntu)
- [Anaconda](#anaconda--basic-python-scientific-env)
- [git](#optional-git)
- [zsh](#optional-zsh-and-plugins)
- [p10k](#optional-p10k-zsh-theme-for-ohmyzsh)
- [tmux](#optional-tmux-and-plugins)
- [neovim](#optional-neovim-and-configuration-with-kickstartnvim)
- [ssh](#optional-ssh)
- [VSCode](#optional-vscode)
- [Wolfram Engine](#optional-wolfram-engine)

# Virtual box
[Back to Top](#navigation)

- Download and install [VirtualBox 7.1](https://www.virtualbox.org/wiki/Downloads) for your OS. On Ubuntu use the following commands:

```bash
sudo apt install software-properties-common
wget -q https://www.virtualbox.org/download/oracle_vbox_2016.asc -O- | sudo apt-key add -
echo "deb [arch=amd64] https://download.virtualbox.org/virtualbox/debian $(lsb_release -cs) contrib" | sudo tee /etc/apt/sources.list.d/virtualbox.list
sudo apt update
sudo apt install virtualbox-7.1
```

# Ubuntu
[Back to Top](#navigation)

- Download [Ubuntu 24.04](https://ubuntu.com/download/desktop) image
- Launch VirtualBox and click on `New` (`Ctrl+N`)
- Set `Name`, `Folder`, `ISO Image`, select `Skip Unattended Installation`
- Go to `Hardware` section, set `Base Memory` (4096+ MBs should be fine), `Processors` (around half of the available **physical** cores)
- Go to `Hard Disk` section, set `Create a Virtual Hard Disk Now` (default 25 GBs should be fine)
- Review sections and click `Finish`
- Now, start your virtual machine and follow `Ubuntu` installation steps (set your user name and password)
- Restart VM, login using your user and password, finish the first time setup
- Click `Show Apps` in the left bottom and search to `Terminal`, click the icon to open it
- (optional) Update & upgrade your Linux software
    - In `Terminal` type `sudo apt update` and press enter
    - Enter your password, wait for the command to finish
    - Type `sudo apt upgrade`, type `Y` and press enter
    - Wait for the command to finish and you are done!

# Anaconda & basic python scientific environment
[Back to Top](#navigation)

- [Download](https://www.anaconda.com/download/) Miniconda for Linux  (from your virtual machine, search for `firefox` browser in `Apps`)
- Install (follow installation steps and restart terminal when the installation is finished)
    ```bash
    cd ~/Downloads
    chmod u+x Miniconda3-latest-Linux-x86_64.sh
    ./Miniconda3-latest-Linux-x86_64.sh
    ```
- You should see a modified prompt `(base) <username>@<hostname>:~$`
- Update conda
    ```bash
    conda update conda
    ```
- Create and activate virtual environment (you can use `conda deactivate` to deactivate it)
    ```bash
    conda create -n nstu python=3.13
    conda activate nstu
    ```
- You should see a modified prompt `(nstu) <username>@<hostname>:~$`    
- Install python libs
    ```bash
    pip install jupyterlab numpy scipy matplotlib
    ```
- Start `jupyter-lab`
    ```bash
    jupyter-lab
    ```
- Press `Ctrl+C` twice to close it in `Terminal`
- Or go to `File` and select `Shut Down`
- Your basic course development environment is ready!

# (optional) git
[Back to Top](#navigation)

```bash
sudo apt install git
```

# (optional) zsh and plugins
[Back to Top](#navigation)

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
Hit `Crt-O` and press `Enter` to save, then `Crt-X` to exit. Finally, restartls `zsh`:

```bash
zsh
```
Now, each time you open a terminal, you can start `zsh` shell or it can be set as a default one.

Note, you also need to initialize `zsh` shell in `conda`:

```bash
conda init zsh
```
You will be able to activate your conda environment in `zsh` shell after restarting `zsh`.

# (optional) p10k (zsh theme for ohmyzsh)
[Back to Top](#navigation)

```bash
git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k
```

Open `~/.zshrc`, find the line that sets `ZSH_THEME`, and change its value to `"powerlevel10k/powerlevel10k"`. Restart `zsh`, this will launch `p10k` theme config. Run `p10k configure` to reconfigure it.

# (optional) tmux and plugins
[Back to Top](#navigation)

```bash
sudo apt install tmux
```

Try [TPM](https://github.com/tmux-plugins/tpm) as your plugins manager (also see list of [plugins](https://github.com/tmux-plugins/list)).

# (optional) neovim and configuration with kickstart.nvim
[Back to Top](#navigation)

Download [nvim.appimage](https://github.com/neovim/neovim/releases/tag/stable) for `x86_64` and follow installation instructions.

```bash
cd ~/Downloads
chmod u+x nvim-linux-x86_64.appimage
./nvim-linux-x86_64.appimage --appimage-extract
./squashfs-root/usr/bin/nvim
```

Find out how to exit `nvim` (or `vim`).

Go to [kickstart.nvim](https://github.com/nvim-lua/kickstart.nvim), follow installation instructions. Don't foget to install prerequisites.

# (optional) ssh
[Back to Top](#navigation)

- Install ssh server (VM)
    ```bash
    sudo apt install openssh-server 
    ```
- In VB settings go to `Network`, click `Port Forwarding` and add new:

    | Name | Protocol | Host IP | Host Port | Guest IP | Guest Port |
    |------|----------|---------|-----------|----------|------------|
    | ssh  | TCP      |         | 8822      |          | 22         |

- `ssh` from host to VM
    ```bash
    ssh -p 8822 <user>@localhost
    ```

Now you can `ssh` into your VM. Try the following exercise:
- Start VM
- Open `Terminal`
- Create `tmux` session (`tmux new -s nstu`)
- Switch to `zsh` and activate conda environment (`conda activate nstu`)
- `ssh` to your VM and do `tmux attach`
- Do `tmux detach` to detach from your `tmux` session
- Use `exit` to end your `ssh` session

Here is another one:
- Create `tmux` session as before
- Enter and execute `jupyter-lab --no-browser --port 8080`
- Start `ssh` session with port forwarding on the host machine `ssh -p 8822 -L 8080:localhost:8080 <user>@localhost`
- Go to your browser `http://localhost:8080/` (you'll need token or copy link)
- Now you run `jyupyter-lab` server on your VM inside a `tmux` session and use it from you host machine browser!

# (optional) ollama (local LLM)
[Back to Top](#navigation)

- Go to [Ollama](https://github.com/ollama/ollama) and read about the project and installation instructions
- install with `curl -fsSL https://ollama.com/install.sh | sh` (on your virtual machine)
- run `ollama run deepseek-r1:8b` or select other model to pull.

It is not a good idea to run a local LLM on a VM, do it on your host machine instead if you are feeling adventurous.

# (optional) VSCode
[Back to Top](#navigation)

- [Download](https://code.visualstudio.com/) and install for your system
- Suggested extensions to try
    - Python
    - Jupyter

# (optional) Wolfram Engine
[Back to Top](#navigation)

- [Download](https://www.wolfram.com/engine/) installer
- Get your license (you'll need to register and enter your credentials after installation)
- Install Wolfram Engine
    ```bash
    cd ~/Downloads
    chmod u+x WolframEngine_14.1.0_LIN.sh
    sudo ./WolframEngine_14.1.0_LIN.sh
    ```
- Start `WolframKernel` and enter your credentials (user name and password)
    ```bash
    WolframKernel 
    Wolfram Language 14.1.0 Engine for Linux x86 (64-bit)
    Copyright 1988-2024 Wolfram Research, Inc.

    In[1]:= Exit[]     
    ```
- Install [Wolfram Language kernel for Jupyter](https://github.com/WolframResearch/WolframLanguageForJupyter)
    ```bash
    cd ~/Downloads
    git clone https://github.com/WolframResearch/WolframLanguageForJupyter.git
    cd WolframLanguageForJupyter
    ./configure-jupyter.wls add
    ```
