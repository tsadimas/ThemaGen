#!/bin/bash

#font="AlphaTV_Texts-Normal"
font="NotoSans Nerd Font"
for i in $(ls -1 assets/files | grep -E "*.md")
do
    file=$(basename -- $i .md)
    echo $file
    pandoc --pdf-engine=xelatex  -V mainfont="$font" -V geometry:a4paper,margin=2cm  -s "../assets/files/$i" -o "../assets/files/$file".pdf
done
