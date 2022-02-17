**Arch Based**
  ```
  sudo pacman -S python-pillow python-wand python3
  ```  
**Gentoo**
  ```
  sudo emerge --ask dev-python/wand dev-python/pillow dev-lang/python
  ```
**Install**
  ```
  git clone https://github.com/JustCoww/videoimagecreator ~/.local/share/vic && chmod +x ~/.local/share/vic/vic.py && sudo ln -s ~/local/share/vic/vic.py /usr/bin/vic
  ```
**Uninstall**
  ```
  rm -rf ~/.local/bin/vic && sudo rm /usr/bin/vic
  ```
