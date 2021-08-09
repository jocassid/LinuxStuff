alias cpl='clear; pwd; ls'
alias cpla='clear; pwd; ls -a'
alias cpll='clear; pwd; ls -lh'
alias cplla='clear; pwd; ls -lah'
alias cplt='clear; pwd; ls -lht'

alias h='history 10'
alias h1='history 25'
alias h2='history 50'
alias h3='history 100'

alias mkalias='vim ~/.bash_aliases && source ~/.bash_aliases'

alias dsm='env | grep DJANGO_SETTINGS_MODULE'
alias migrations='./manage.py showmigrations | grep -i -P "^(\\S| \\[ \\])"'
alias summary='grep -n -P "^\s*(def|class) "'

alias hgs='hg status | grep -v -P "^\\?"'
alias gits='git status -uno'
