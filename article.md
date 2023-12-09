## Introduction

### Problème des mariages stables

Le problème des mariages stables, énoncé et résolu (par Gale et Shapley) en 1962, avec en vue le problème de l’affectation des étudiants aux diverses formations universitaires. Il est à la base du problème des colocataires.
Ce problème consiste à trouver, pour deux groupes distincts de personnes, une façon de former des binômes, tel qu'aucun binôme ne risque de ce dissocier, sachant que chaque personne a des préférences sur les personnes de l'autre groupe.
Plus formellement, le problème des mariages stables a été énoncé ainsi :

- On considère un même nombre de femmes et d'hommes.
- Chaque personne doit se marier avec une personne du sexe opposé.
- Chaque personne a classé les personnes de l'autre sexe par ordre de préférence, sans égalité ni omission.
- Une solution est une liste de couples (femme, homme) mariés.

> L'objectif est de trouver une solution stable, c'est-à-dire raisonnable.

Gale et Shapley définissent une solution à ce problème comme stable s'il n'y a pas de mariage tel qu'une femme et un homme se préfèrent mutuellement à leurs conjoints.

**Exemple:**

> Supposons que la solution propose les mariages (Alice, Bob) et (Julie, Pierre). Si :
>
> - Alice préfère être avec Pierre qu'avec Bob
> - Pierre préfère être avec Alice qu'avec Julie
>   Alors la solution est instable. En effet, on peut imaginer qu’alors, ils divorceraient pour se remarier.
>   La solution ne doit pas prescrire de mariages tels qu’une femme A et un homme b se préfèrent mutuellement à leurs conjoints prévus. Formellement, il ne doit pas y avoir deux mariages distincts (A,a) et (B,b) tels que A et b (ou a et B) préféreraient être mariés ensemble.

### Problème des colocataires

Le problème des colocataires consiste à trouver, parmi un nombre pair de personnes, une façon stable de former des paires de personnes qui pourront être colocataires. Chaque personne a classé les autres personnes par ordre de préférence, sans égalité ni omission. La stabilité de la solution est la même que pour le problème des mariages stables énoncé plus haut.
La différence avec le problème des mariages stables est que les personnes ne sont pas séparés en deux groupes distincts. Ici, une personne peut former un binôme avec n'importe quelle autre.

### Applications réelles

Ces deux problèmes d'appariements répondent à problématiques réelles :

- Affecter de manière efficace les internes en médecine aux hôpitaux en tenant compte autant que possible des préférences de chacun.
- Affecter les étudiants aux diverses formations universitaires. Le service Admission Post-Bac du ministère français de l'Enseignement supérieur a utilisé l'algorithme de Gale Shapley entre 2009 et 2017. Les formations étaient dans le rôle des femmes et les étudiants dans celui des hommes.
- Affecter les rôles d'un projet à chacun des membres.
- Affecter des élèves comme colocataires d'un dortoir.

Cette liste n'est pas exhaustive, mais présente des problèmes qui ont été résolu à l'aide des algorithmes de Gale Shapley et d'Irving.

## Les Algorithmes et leur complexité

### Algorithme de Gale Shapley

#### Fonctionnement

L'algorithme de Gale-Shapley procède par élimination. Tant qu'il existe un homme qui n'est pas en couple, on parcourt la liste des hommes,
et chaque homme fait une requète à son choix de préfèrence qui ne l'a pas encore refusé. Si une femme reçoit une demande et n'en a pas d'autres, elle accepte temporairement.
Si elle a déjà reçu une demande, elle conserve son choix préféré et l'homme qui a été refusé devra faire une nouvelle demande.

#### Complexité

Dans le pire des cas, l'algorithme de Gale-Shapley va faire toutes les demandes possibles de chaque homme pour trouver un couplage stable, soit n demandes pour n hommes.
La complexité de cet algorithme est donc O(n²) ou O(n) dans le meilleur cas, où chaque homme trouve son couplage stable dès la première demande, sans conflit.

### Algorithme d'Irving

Un algorithme efficace pour résoudre le problème des colocataires est énoncé par Irving en 1985.

Celui-ci détermine si un appariement stable exite ou pas, et renvoie un tel appariement s'il existe.

#### 2.2.1 Fonctionnement

Cet algorithme se déroule en trois phases : une phase de propositions entre les individus, une phase de rejet des individus et une phase de suppression des cycles.

> Dans la suite, nous utiliserons l'exemple présent dans l'[annexe](https://docs.google.com/presentation/d/12gVfTqXWskSEo31JIrgMDtM8NyO91mQGmD2sAJUlm2U/edit#slide=id.g2a3e3583abe_0_53).

##### Phase 1 :

- Tout le monde se propose à son favoris.
- Les destinataires de la proposition choisissent leur meilleur candidat et rejettent les autres.
- Ceux qui ont été rejetés continuent de faire des propositions jusqu'à ce qu'il soient acceptés.

> :warning: **Si quelqu'un est rejeté par tous les autres, il n'y a pas d'appariement stable !**
>
> Cette première étape consiste finalement en une application modifiée de l'algorithme de Gale Shapley, puisqu'elle autorise les cycles.

##### Phase 2 :

- Tous les candidats moins dérisables que le candidat actuel sont supprimés.

##### Phase 3 :

Maintenant que l'on a supprimé les candidats qui ne seront pas choisis, il faut supprimer les cycles. En effet, comme nous l'avons indiqué plus haut, l'algorithme d'irving applique l'algorithme de Gale Shapley en autorisant les cycles. Les étapes suivantes permettent de supprimer les cycles :

On répète les étapes suivantes jusqu'à ce que tous les noeuds n'aient plus qu'un seul candidat :

- On cherche un noeud `N` avec plus d'un candidat.
- Répéter jusqu'à ce que `N` apparaise de nouveau:
  On note `(a,b)`, avec `a` le 2<sup>ème</sup> meilleur candidat de `N` et `b` le pire candidat de `a`.
- On supprime ensuite toutes les paires `(a,b)`, c'est-à-dire les arêtes qui relient `a` et `b`.

> Si une solution stable existe, alors chaque noeud est relié à exactement un autre noeud. Sinon, il n'ya pas de solution stable.

#### Complexité

Etant donné la complexité de l'algorithme de Gale Shapley, dans le meilleur et le pire des cas, l'algorithme d'Irving peut s'implémenter en O(n²), c'est-à-dire lorsque chaque noeud n'a qu'un seul candidat. Pour le pire cas, c'est différent.
Dans la **phase 1**, il s'agit du cas où aucune solution stable existe et où un noeud va faire des demandes à tous les autres noeuds jusqu'à ce qu'il y ait une demande et une requète par noeud. Elle s'exécute donc en temps O(n²) car plusieurs demandes peuvent être faites par chaque noeud.
Dans la **phase 2**, il suffit de retirer les options moins intéressantes que l'offre courrante pour chaque noeud, cela s'éxecute en temps O(n²) dans le cas où il faut retirer tous les choix d'un même noeud.
Pour la **phase 3**, il s'agit de passer par tous les candidats de tous les noeuds pour trouver les cycles à supprimer, soit O(n²).

Donc dans tous les cas, l'algorithme d'Irving possède une **complexité en temps en O(n²)**, comme chaque étape modifie l'état pour la suivante, si deux phases s'éxecute en temps O(n), la troisième s'éxecutera en temps O(n²).

### Solution stable

#### Obstacles trouvés par l'algo de Gale Shapley

L'algorithme doit assurer que chaque personne à coupler est couplée avec son meilleur partenaire possible. Comme les hommes décrèmentent progressivement leur demande avec les rejets, ils sont sûrs d'avoir le meilleur partenaire stable possible. 
Cependant, comme les femmes ne peuvent pas faire de demande, elles ne peuvent pas assurer d'avoir leur partenaire stable préféré. Ainsi, les femmes sont toujours couplées avec leur pire partenaires stables, car elles ne peuvent qu'accepter les demandes et refuser les partenaires instables.

#### Comment expliquer et être sûr qu'une solution stable n'existe pas ?

L'algorithme de Gale-Shapley est capable de trouver systématiquement une solution stable car on cherche à former des couples entre 2 ensembles distincts de même taille.
Ainsi, il existe toujours exactement une solution pour tous deux ensembles. Cependant, il devient impossible d'assûrer l'existence d'un tel couplage stable si l'on pioche dans un seul ensemble.

## Sources

- [_LE PRIX NOBEL D’ÉCONOMIE 2012_, par Jérôme Buzzi](https://images.math.cnrs.fr/Le-prix-Nobel-d-economie-2012.html?lang=fr#menu)
- [_Algorithme de Gale et Shapley_](https://fr.wikipedia.org/wiki/Algorithme_de_Gale_et_Shapley)
- [_Problème des mariages stables_](https://fr.wikipedia.org/wiki/Probl%C3%A8me_des_mariages_stables)
- [_Stable marriage problem_](https://en.wikipedia.org/wiki/Stable_marriage_problem)
- [_Irving's Algorithm and Stable Roommates Problem_](https://www.youtube.com/watch?app=desktop&v=5QLxAp8mRKo)
