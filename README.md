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
    + 3.3 : run generate.py
    + 3.4 to run 
    ```
    docker build --build-arg PYTHON_VERSION=3.10 -t assoc:3.10 . && docker run --rm assoc:3.10
    ```

- Part 4 : 
    + Save.uvl is based on three programs : TP3/associativity.py, TP3/associativity_llm.py, TP3/main.cpp (with the help of copilot and my own modifications)

- Part 5 :
    + To generate
    ```
    cd TP3
    python sample.py Save.uvl --size 30 --seed 1  -o sample.csv
    ```

- Part 6 :
    + J'ai utilisé copilot pour généré ces 3 scipts : 
        1. run_sample.sh is the shell entry point.
        2. run_sample.py reads the sample CSV, skips rows where Language is Cpp, and runs each Python configuration multiple times.
        3. associativity_variant.py accepts the feature choices as runtime arguments and calculates the percentage of equal results.
    + to run :  `run_sample.sh --runs 3 --seed 1 -o results.csv` (résultat dans le fichier results.csv )

- Part 7 : 
 




