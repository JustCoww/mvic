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
  mkdir ~/.local/bin && git clone https://github.com/JustCoww/videoimagecreator ~/local/bin/ && chmod +x ~/.local/bin/videoimagecreator/vic.py && sudo ln -s ~/local/bin/videoimagecreator/vic.py /usr/bin/vic
  ```
**Uninstall**
  ```
  rm -rf ~/local/bin/videoimagecreator && sudo rm /usr/bin/vic
  ```
