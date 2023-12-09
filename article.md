### 2.1 Algorithme de Gale Shapley

#### 2.1.1 Fonctionnement

L'algorithme de Gale-Shapley procède par élimination. Tant qu'il existe un homme qui n'est pas en couple, on parcourt la liste des hommes, 
et chaque homme fait une requète à son choix de préfèrence qui ne l'a pas encore refusé. Si une femme reçoit une demande et n'en a pas d'autres, elle accepte temporairement.
Si elle a déjà reçu une demande, elle conserve son choix préféré et l'homme qui a été refusé devra faire une nouvelle demande.

#### 2.1.2 Complexité

Dans le pire des cas, l'algorithme de Gale-Shapley va faire toutes les demandes possibles de chaque homme pour trouver un couplage stable, soit n demandes pour n hommes.
La complexité de cet algorithme est donc O(n²) ou O(n) dans le meilleur cas, où chaque homme trouve son couplage stable dès la première demande, sans conflit.


## 3. Solution Stable

### 3.1 Obstacles trouvés par l'algorithme de Gale Shapley

L'algorithme doit assurer que chaque personne à coupler est couplée avec son meilleur partenaire possible. Comme les hommes décrèmentent progressivement 
leur demande avec les rejets, ils sont sûrs d'avoir le meilleur partenaire stable possible. Cependant, comme les femmes ne peuvent pas faire de demande, elles ne peuvent
pas assurer d'avoir leur partenaire stable préféré. Ainsi, les femmes sont toujours couplées avec leur pire partenaires stables, car elles ne peuvent qu'accepter les demandes 
et refuser les partenaires instables.

### 3.2 Comment expliquer et être sûr qu'une solution stable n'existe pas ?

L'algorithme de Gale-Shapley est capable de trouver systématiquement une solution stable car on cherche à former des couples entre 2 ensembles distincts de même taille. 
Ainsi, il existe toujours exactement une solution pour tous deux ensembles. Cependant, il devient impossible d'assûrer l'existence d'un tel couplage stable si l'on 
pioche dans un seul ensemble.


## Sources

- [_LE PRIX NOBEL D’ÉCONOMIE 2012_, par Jérôme Buzzi](https://images.math.cnrs.fr/Le-prix-Nobel-d-economie-2012.html?lang=fr#menu)
- Wikipedia : _Problème des mariages stables_ [en français](https://fr.wikipedia.org/wiki/Probl%C3%A8me_des_mariages_stables) et [en anglais](https://en.wikipedia.org/wiki/Stable_marriage_problem)
- [Wikipedia : _Algorithme de Gale et Shapley_](https://fr.wikipedia.org/wiki/Algorithme_de_Gale_et_Shapley)
