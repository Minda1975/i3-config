#!/bin/sh

cmd=$(printf "poweroff\nreboot\nlock\n" | dmenu -p "Execute:" $*)

if [ -z "$cmd" ]; then
	exit 0
fi

case "$cmd" in
	poweroff)
		systemctl poweroff ;;
	reboot)
		systemctl reboot ;;
	lock)
		i3lock --color '#000000'  ;;
	*)
		printf "Option not recognized: %s\n" "$cmd" >&2
esac
