TP 2 
Part 4 — What about LLMs? (cette partie joue le rôle des 2 fichers LLM_associativity.md et LLM_banking.md )
LLM utilisé : Claude Sonnet 5.5



+ question 1 
write 2 seperate  py file to solve these two problems :

1. How often (x+y)+z == x+(y+z)? Write a program that prints a percentage. The question is deliberately under-specified ("x, y, z: number"), so you will have to make choices. Make them, and write each one down: they are part of your result.
2. The banking problem: do the same. "My banker proposed this investment to me: you give me e ≈ 2.71828… The following year, I take 1 euro as a fee and multiply by 1. The next year, I take 1 euro as a fee and multiply by 2. The next year, I take 1 euro as a fee and multiply by 3. […] After n years, I take 1 euro as a fee and multiply by n. To retrieve my money, there is a 1 euro fee. In 50 years, for my retirement, how much money will I have?"

+ réponse 1 :
I wrote both scripts and ran them. The choices I made are also documented at the top of each file.

**`associativity.py`**
- **Choices:**
  - Numbers are IEEE 754 doubles with round-to-nearest-even.
  - The main case is x, y, z drawn independently and uniformly from [0, 1).
  - It samples 10 million triples with a fixed seed.
  - "Equal" means exactly equal, with no tolerance.
- **Result:** about **82.8 %** of triples satisfy (x+y)+z == x+(y+z) in the main case.
- **Other distributions:** the answer depends heavily on the distribution, so the script prints several. For example, it is 74.5 % for uniform [0, 1000), 68.1 % for a normal distribution, and 100 % for small integers or values in [-1, 1).

**`banking.py`**
- **Choices:**
  - Each year the fee is subtracted first and then the amount is multiplied, with one more 1 € fee at the end.
  - It uses the true constant e, computed to about 150 digits, in 200-digit decimal arithmetic.
  - It cross-checks against a closed form: the amount after year n is n!·Σ_{k≥n} 1/k! = 1 + 1/(n+1) + 1/((n+1)(n+2)) + ….
- **Result:** after 50 years you hold about 1.01999 €, and after the final fee **about 0.0200 € (roughly 2 cents)**.
- **Why it is fragile:** any error in e is multiplied by 50! ≈ 3×10⁶⁴. Plain float arithmetic gives about −4×10⁴⁸ €, and e = 2.71828 gives about −6×10⁵⁸ €. You need about 70 decimals of e to get the 2 cents right, and 65 decimals still gives −0.10 €.

+ question 2 : 
change these files so that i can able to write the results to a file


```python
output_dir = Path(os.environ.get("OUTPUT_DIR", "/out"))
output_dir.mkdir(parents=True, exist_ok=True)

output_file = output_dir / "resultat_associativity_llm.txt"
output_file.write_text("something)
```

+ reponse 2 : 

Both scripts now still print to the console and also write their full output to a text file, using the same `OUTPUT_DIR` pattern as your snippet.

- **Output files:** `associativity.py` writes `resultat_associativity_llm.txt` and `banking.py` writes `resultat_banking_llm.txt`. I chose the second name myself to match the first, so rename it if you need something different.
- **Output directory:** It is read from the `OUTPUT_DIR` environment variable and defaults to `/out`. The directory is created if it doesn't exist.
- **Fallback:** If the directory can't be created or written to, for example `/out` on a machine without permission, the script prints a warning and writes to the current directory instead of crashing. I added this beyond your snippet.
- **How it works:** I replaced each `print(...)` with a small `out(...)` helper that prints the line and keeps a copy. `write_results(filename)` writes everything at the end.

I tested both scripts with `OUTPUT_DIR=/tmp/o`, and both wrote their files with the same content as the console output. The numbers are unchanged. For example, you can run:

```
OUTPUT_DIR=./results python3 associativity.py
```

- Commentaire : Sonnet 5.5 essaie de donne une réponse le plus spécifique que possible et il test tous les cases possibles dans les 2 problèmes. Il essaie aussi d'expliquer ces problèmes et pourquoi les réponse varient en fonction des choix techniques. 

