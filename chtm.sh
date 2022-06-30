#!/bin/bash

############################################################################################################################
# this is a very basic theme "handler" so to speak and it can save, list and change the current                            #
# theme of most WM's and the respective common software relating to it, for anything other than the following:             #
# (polybar, rofi, bspwm, alacritty, neofetch and thunar) you will have to specify the path of the config directory or file.#
# Don't complain if this "breaks" your themes or doesnt work, you know what you're getting into if you use this.           #
# THIS DOES NOT AUTO-SAVE YOUR THEMES. Please back them up either with this tool or manually                               #
# if you got this far you should be good to go                                                                             #
############################################################################################################################

if [ "$1" == '-l' ]
then
    ls ~/themes
elif [ "$1" == '-r' ]
then
    if [ "$2" != '' ]
    then
        echo Are you sure you would like to remove "$2"? [y/n]
        read yn
        if [ "$yn" == 'y' ]
        then
            rm -r ~/themes/"$2"
        else
            exit
        fi
    else
        ls ~/themes
        echo What theme would you like to remove?
        read rm
        echo Are you sure you would like to remove "$rm"? [y/n]
        read yn
        if [ "$yn" == 'y' ]
        then
            rm -r ~/themes/"$rm"
        else
            exit
        fi
    fi
elif [ "$1" == '-s' ]
then
    if [ "$2" != '' ]
    then
        # This is where you will specify any and all program configs you want it to save
        mkdir ~/themes/"$2"
        cp -r ~/.config/polybar ~/themes/"$2"
        cp -r ~/.config/rofi ~/themes/"$2"
        cp -r ~/.config/bspwm ~/themes/"$2"
        cp -r ~/.config/alacritty ~/themes/"$2"
        cp -r ~/.config/neofetch ~/themes/"$2"
        cp -r ~/.config/Thunar ~/themes/"$2"
    else
        echo Theme name:
        read name
        mkdir ~/themes/"$name"
        cp -r ~/.config/polybar ~/themes/"$name"
        cp -r ~/.config/rofi ~/themes/"$name"
        cp -r ~/.config/bspwm ~/themes/"$name"
        cp -r ~/.config/alacritty ~/themes/"$name"
        cp -r ~/.config/neofetch ~/themes/"$name"
        cp -r ~/.config/Thunar ~/themes/"$name"
    fi
elif [ "$1" == '-c' ]
then
    if [ "$2" != '' ]
    then
        echo Are you sure you would like to change your theme to "$2"? [y/n]:
        read yn
        if [ "$yn" != 'y' ]
        then
            echo Changing theme
            cp -r ~/themes/"$2"/* ~/.config/
            if [ "$?" != 0 ]
            then
                echo No theme named "$2"
                exit
            fi
        else
            echo ok
            exit
        fi
    else
        echo Theme name:
        read theme
        echo Are you sure you would like to change your theme to "$theme"? [y/n]:
        read yn
        if [ "$yn" != 'y' ]
        then
            echo Changing theme
            cp -r ~/themes/"$theme"/* ~/.config/
            if [ "$?" != 0 ]
            then
                echo No theme named "$theme"
                exit
            fi
        else
            echo ok
            exit
        fi
    fi
else
    echo "Options: -r (remove), -s (save), -c (change)"
fi
