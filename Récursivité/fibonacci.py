def fib(n, mem = None): # Ne jamais passer un type mutable en paramètre par défaut [], {}...
    if mem == None:
        mem={0:0, 1:1} #On mémorise les 2 premieres valeurs
    """
    Si la clé n'existe pas, on affecte le résultat de l'appel récursif dans la mémoire
    Dans tous les cas, on retourne le résultat présent dans la mémoire
    """
    if n < 2:
        return n
    elif n in mem.keys():
        return mem[n]
    else:
        return(mem[n] = fib(n-1)+fib(n-2))
    


fib(3)   
