#!/usr/bin/env python

import itertools
import subprocess
import argparse
import json
import sys
from typing import List, TypedDict

# __USAGE__
#   gnome-custom-shortcut.py add <name> <binding> <command>
#   gnome-custom-shortcut.py add test-shortcut '<Super>period' 'notify-send hello'
#
#   gnome-custom-shortcut.py list
#   [
#     {
#       "path": "/org/gnome/settings-daemon/plugins/media-keys/custom-keybindings/custom0/",
#       "name": "test-shortcut",
#       "binding": "<Super>period",
#       "command": "notify-send hello"
#     }
#   ]
#
#   gnome-custom-shortcut.py remove <name>
#   gnome-custom-shortcut.py remove test-shortcut

# references
#   https://askubuntu.com/questions/597395/how-to-set-custom-keyboard-shortcuts-from-terminal


#
# utils
#


class Shortcut(TypedDict):
    path: str
    name: str
    binding: str
    command: str


def run_command(command: str) -> str:
    return subprocess.check_output(command, shell=True, encoding="utf-8").strip()


#
# gsettings wrapper
#

LIST_GET_COMMAND = (
    "gsettings get org.gnome.settings-daemon.plugins.media-keys custom-keybindings"
)
LIST_SET_COMMAND = (
    "gsettings set org.gnome.settings-daemon.plugins.media-keys custom-keybindings '{}'"
)
GET_COMMAND = (
    "gsettings get org.gnome.settings-daemon.plugins.media-keys.custom-keybinding:{} {}"
)
SET_COMMAND = "gsettings set org.gnome.settings-daemon.plugins.media-keys.custom-keybinding:{} {} '{}'"

KEY_PATH = "/org/gnome/settings-daemon/plugins/media-keys/custom-keybindings/{}"


def get_shortcuts() -> List[Shortcut]:
    list_output = run_command(LIST_GET_COMMAND)
    if list_output == "@as []":
        return []

    ls = eval(list_output)  # sorry
    assert isinstance(ls, list)

    result: List[Shortcut] = []
    for path in ls:
        assert isinstance(path, str)
        shortcut = Shortcut(
            path=path,
            name=run_command(GET_COMMAND.format(path, "name")).strip("'"),
            binding=run_command(GET_COMMAND.format(path, "binding")).strip("'"),
            command=run_command(GET_COMMAND.format(path, "command")).strip("'"),
        )
        result.append(shortcut)
    return result


def set_shortcut_paths(paths: str):
    run_command(LIST_SET_COMMAND.format(json.dumps(paths)))


def add_shortcut(shortcuts: List[Shortcut], to_add: Shortcut):
    path = to_add["path"]
    paths = [s["path"] for s in shortcuts]
    paths.append(path)
    set_shortcut_paths(paths)
    run_command(SET_COMMAND.format(path, "name", to_add["name"]))
    run_command(SET_COMMAND.format(path, "binding", to_add["binding"]))
    run_command(SET_COMMAND.format(path, "command", to_add["command"]))


def get_next_path(shortcuts: List[Shortcut]) -> str:
    current_paths = [s["path"] for s in shortcuts]
    for i in itertools.count():
        path = KEY_PATH.format(f"custom{i}/")
        if path not in current_paths:
            return path


#
# main
#


def main_list() -> None:
    shortcuts = get_shortcuts()
    print(json.dumps(shortcuts, indent=2))


def main_add(name: str, binding: str, command: str) -> None:
    shortcuts = get_shortcuts()
    path = get_next_path(shortcuts)
    to_add = Shortcut(path=path, name=name, binding=binding, command=command)
    add_shortcut(shortcuts, to_add)


def main_remove(name: str):
    shortcuts = get_shortcuts()
    if not any(s["name"] == name for s in shortcuts):
        print(f"Not found shortcut: '{name}'")
        return 1
    paths = [s["path"] for s in shortcuts if s["name"] != name]
    set_shortcut_paths(paths)


def main() -> None:
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="subcommand", required=True)
    subparsers.add_parser("list")

    command_add = subparsers.add_parser("add")
    command_add.add_argument("name")
    command_add.add_argument(
        "binding",
        help="e.g. '<Super>period' (see the list https://gitlab.gnome.org/GNOME/gtk/-/blob/dbaaa59758303aad1bfeaddcbe3e86baf8b4b0ba/gdk/gdkkeysyms.h)",
    )
    command_add.add_argument("command")

    command_remove = subparsers.add_parser("remove")
    command_remove.add_argument("name")

    args = parser.parse_args().__dict__
    status = globals()[f"main_{args.pop('subcommand')}"](**args)
    sys.exit(status)


if __name__ == "__main__":
    main()
