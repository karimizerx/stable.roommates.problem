```
1. Introduction
   1.1 Présentation du problème du mariage stable
   1.2 Présentation du problème des colocataires
   1.3 Applications réelles

   2.2 Algorithme d'Irving
   2.2.1 Comment utilise-t-il Gale Shapley ?
   2.2.2 Fonctionnement
   2.2.3 Complexité
```

## Introduction

### Problème des mariages stables

Le problème des mariages stables, énoncé et résolu (par Gale et Shapley) en 1962, est à la base du problème des colocataires.
Ce problème consiste à trouver, pour deux groupes distincts de personnes, une façon de former des binômes, tel qu'aucun binôme ne risque de ce dissocier, sachant que chaque personne a des préférences sur les personnes de l'autre groupe.
Plus formellement, le problème des mariages stables a été énoncé ainsi :

- On considère un même nombre de femmes et d'hommes.
- Chaque personne doit se marier avec une personne du sexe opposé.
- Chaque personne a classé les personnes de l'autre sexe par ordre de préférence, sans égalité ni omission.
- Une solution est une liste de couples (femme, homme) mariés.

> L'objectif est de trouvé une solution stable (raisonnable).

Gale et Shapley définissent une solution à ce problème comme stable s'il n'y a pas de mariage tel qu'une femme et un homme se préfèrent mutuellement à leurs conjoints.

**Exemple:**

> Supposons que la solution propose les mariages (Alice, Bob) et (Julie, Pierre). Si :
>
> - Alice préfère être avec Pierre qu'avec Bob
> - Pierre préfère être avec Alice qu'avec Julie
>   Alors la solution est instable. En effet, on peut imaginer qu’alors, ils divorceraient pour se remarier.
>   La solution ne doit pas prescrire de mariages tels qu’une femme A et un homme b se préfèrent mutuellement à leurs conjoints prévus. Formellement, il ne doit pas y avoir deux mariages distincts (A,a) et (B,b) tels que A et b (ou a et B) préféreraient être mariés ensemble. En effet, (on peut imaginer qu’alors) ils divorceraient pour se remarier.

### Problème des colocataires

Le problème des colocataires consiste à trouver, parmi un nombre pair de personnes, une façon stable de former des paires de personnes qui pourront être colocataires. Chaque personne a classé les autres personnes par ordre de préférence, sans égalité ni omission. La stabilité de la solution est la même que pour le problème des mariages stables énoncé plus haut.
La différence avec le problème des mariages stables est que les personnes ne sont pas séparés en deux groupes distincts. Ici, une personne peut former un binôme avec n'importe quelle autre.

### Applications réelles

Ces deux problèmes d'appariements répondent à problématiques réelles.

- Comment affecter de manière efficace les internes en médecine aux hôpitaux en tenant compte autant que possible des préférences de chacun ?
- affectation des internes en médecine aux hôpitaux (GS)
- affectation des élèves comme colocataires d'un dortoir (I)
- Le problème des mariages stables a été énoncé en 1962, avec en vue le problème de l’affectation des étudiants aux diverses formations universitaires.Le service Admission Post-Bac du ministère français de l’Enseignement supérieur a utilisé l’algorithme de Gale Shapley entre 2009 et 2017. Dans l’admission Post-Bac, les formations étaient dans le rôle des femmes et les étudiants dans celui des ̇hommes. (GS)
- affectation des rôles pour les membres d'un projet.

#### Sources

- [_LE PRIX NOBEL D’ÉCONOMIE 2012_, par Jérôme Buzzi](https://images.math.cnrs.fr/Le-prix-Nobel-d-economie-2012.html?lang=fr#menu)
- Wikipedia : _Problème des mariages stables_ [en français](https://fr.wikipedia.org/wiki/Probl%C3%A8me_des_mariages_stables) et [en anglais](https://en.wikipedia.org/wiki/Stable_marriage_problem)
- [Wikipedia : _Algorithme de Gale et Shapley_](https://fr.wikipedia.org/wiki/Algorithme_de_Gale_et_Shapley)
