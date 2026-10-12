Comment réproduire les résultats de TP1?

1. (x+y)+z == x+(y+z) : 
- python : exécute TP1/(x+y)+z == x+(y+z)/python_version.py dans vscode (python 3.12)
- c++ : ouvre TP1/(x+y)+z == x+(y+z)/cpp_version dans clion et éxecute (x+y)+z == x+(y+z)/cpp_version/main.cpp

2. banking : 
exécute TP1/banquier.py dans vscode

 
TP2 :
- Part 2 - Docker :
pour exécuter : 
docker build -t rep-lab2 . 
puis 
docker run --rm   --user "$(id -u):$(id -g)"   -v "$(pwd)":/out   -e OUTPUT_DIR=/out   rep-lab2



