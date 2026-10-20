Comment réproduire les résultats de TP1?

1. (x+y)+z == x+(y+z) : 
- python : exécute TP1/(x+y)+z == x+(y+z)/python_version.py dans vscode (python 3.12)
- c++ : ouvre TP1/(x+y)+z == x+(y+z)/cpp_version dans clion et éxecute (x+y)+z == x+(y+z)/cpp_version/main.cpp

2. banking : 
exécute TP1/banquier.py dans vscode

 
TP2 :
- Part 2 - Docker :
pour exécuter : 
```
cd TP2
docker build -t rep-lab2 . 
docker run --rm   --user "$(id -u):$(id -g)"   -v "$(pwd)":/out   -e OUTPUT_DIR=/out   rep-lab2
```

- Part 4 - LLM :
pour exécuter : 
```
cd TP2/Part_4_LLM
docker build -t rep-lab2_llm . 
docker run --rm   --user "$(id -u):$(id -g)"   -v "$(pwd)":/out   -e OUTPUT_DIR=/out   rep-lab2_llm
```

- Part 5 :

pour exécuter : 

d'abord modifier TP2/associativity.py et TP2/banquier.py (regarder dans les commentaires des 2 fichiers)
puis
```
cd TP2
nix-shell
python banquier.py ou python associativity.py
```
