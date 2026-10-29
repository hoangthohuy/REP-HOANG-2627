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
TP3 :
- Part 1 :
Banquier
| Program | result | Reason for the result |
  |---|---|---|
  | mine, in L1 (lab #1) |  1.5080147488022342e+85| Mauvais algorithme (noté dans TP1/banquier.py) |
  | LLM, in L1 (lab #2) | 0.02 |Utiliser pluisieurs nombre de décimals pour obtenir le bon résultat  |
  | others (celui de Mathis Roquain), in L1|-4.3968039301820685e+48|  naive float arithmetic |

Associativiy
| Program | result |
  |---|---|
  | mine, in L1 (lab #1) | 82%|
  | LLM, in L1 (lab #2) | plusieurs résultats pour plusieurs plages de nombres différentes |
  | others (celui de Mathis Roquain), in L1| 75% (C), 82%(python) |

Raisons : compiler différents, formats des nombres, plages différentes (comme montré dans TP2/Part_4_LLM/associativity_llm.py), problèmes diifférentes


Note : Quand je faisais le TP2, j'ai mal compris l'anonce de la partie 4 et donc j'ai généré des scripts en python vu que j'avais déjà écrit les scripts de TP1 en ce langage. Pour cette raison, je n'ai que 2 programmes au lieu de 3 

- Part 2 :
```
Pour tester
git checkout Part2_TP3
git push pour tester le workflow
```
- Part 3 : 
    + 3.1 : try different numbers of repetitions, from 100 to 1,000,000. What happens to the answer?
converge to a certain percentage when increase the numbers of repetitions
    + 3.2 : to run :  ./TP3/bash_cli.sh 
    Same arguments, same answer? Within the range of [0, 1) : approximately same result when number of rep increase. , different ranges not yet tested
    + 3.3 : 



