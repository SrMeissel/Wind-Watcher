# Introduction

A system that runs in 3 parts:

- A desktop app to display accumulated and current data.
- A database that collects and stores all data collected within the network
- A data publisher that uploads data to the network

The netowrk connections are handled by Django. The GUI is implemented using Dearpygui (due to experience using imgui).

## notes

Running graphical apps on wsl requires an third-party X server like 'mDNS'

## dependencies

-DearPyGui <https://github.com/hoffstadt/DearPyGui#installation>
-Django
https://twisted.org/
https://pyinstaller.org/en/stable/
https://stackoverflow.com/questions/5458048/how-can-i-make-a-python-script-standalone-executable-to-run-without-any-dependen