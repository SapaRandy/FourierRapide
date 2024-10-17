# Analyses des compléxités

### Première implémentation
Pour la première implémentaion de la transformée de Fourier discrète nous avons utilisé une liste,un tableau numpy afin de pouvoir stocker les nombres complexes.
Nous avons également utilisé deux boucles for afin de parcourir le tableau. Avec tous ces paramètres la compléxité de notre algorithme vaut O(n²).Cette complexité est considéré commme très mauvaise.

### Deuxième implémentation
Pour la deuxième implémentation nous avons utilisé la transformée de Fourier rapide,nous avons utilisé un tableau numpy pour stocker les nombres complexes, une boucle des conditions et surtout de la récursion. Grâce à ces paramètres nous avons dimunier et donc améliorer la compléxité de notre algorithme qui vaut désormais O(n log n). 

### Comparaison des temps d'execution
Pour comparer la performance et l'efficacité des deux algorithmes nous avons mis en place une comapraison de leur temps d'execution.
Nous avons également calculé son temps d'execution grâce à la librairie time.
Nous mis ce code à la suite de nos fonctions afin de pouvoir calculer leurs temps d'execution.

![Code du temps d'execution](/ressources/Code1.png "Implémentation du calcul du temps d'execution")

Grâce à cette implémentation nous avons pu avoir le temps d'execution des deux fonctions 

![Resultat du temps d'execution](/ressources/temps.png " Résultat temps d'execution")

Avec ce résultats nous pouvons observer les différences de temps entre les deux algorithmes. Au vu de ce résultat nous pouvons affirmer que le deuxième algorithme est bien plus rapide que le premier, il est en moyenne 2,62s seconde de moins à s'executer, il est 218 fois plus rapide.

En conclusion abaisser la compléxité d'un code le rend bien plus performant.