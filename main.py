#!/usr/bin/env python3

import os
import sys

TEXT_PATH = '/Users/lucafulgenzi/tmp.txt'

def main(space):
  if space != '1':
    createSpace(space)
  else:
    os.system('yabai -m space --focus ' + space + ' || skhd -k "ctrl + alt + cmd - ' + space + '"')


def createSpace(space):
  data = open(TEXT_PATH, 'w+')
  os.system('yabai -m query --windows --space | jq \'.[].id\' >> ' + TEXT_PATH)

  windowOpen = data.read()
  data.write('')
  data.close()

  if len(windowOpen) == 0:
    os.system('yabai -m space --destroy')
  else:
    toSpace = os.system('yabai -m query --windows --space ' + space)

    if toSpace == 256:
      os.system('yabai -m space --create')

  os.system('yabai -m space --focus ' + space + ' || skhd -k "ctrl + alt + cmd - ' + space + '"')


if __name__ == "__main__":
  main(sys.argv[1])
