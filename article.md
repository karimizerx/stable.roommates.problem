## Introduction

### Problème des mariages stables

Le problème des mariages stables, énoncé et résolu (par Gale et Shapley) en 1962, avec en vue le problème de l’affectation des étudiants aux diverses formations universitaires. Il est à la base du problème des colocataires.
Ce problème consiste à trouver, pour deux groupes distincts de personnes, une façon de former des binômes, tel qu'aucun binôme ne risque de ce dissocier, sachant que chaque personne a des préférences sur les personnes de l'autre groupe.
Plus formellement, le problème des mariages stables a été énoncé ainsi :

- On considère un même nombre de femmes et d'hommes.
- Chaque personne doit se marier avec une personne du sexe opposé.
- Chaque personne a classé les personnes de l'autre sexe par ordre de préférence, sans égalité ni omission.
- Une solution est une liste de couples (femme, homme) mariés.

> :information_source: L'objectif est de trouvé une solution stable, c'est-à-dire raisonnable.

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

Ces deux problèmes d'appariements répondent à problématiques réelles :

- Affecter de manière efficace les internes en médecine aux hôpitaux en tenant compte autant que possible des préférences de chacun.
- Affecter les étudiants aux diverses formations universitaires. Le service Admission Post-Bac du ministère français de l'Enseignement supérieur a utilisé l'algorithme de Gale Shapley entre 2009 et 2017. Les formations étaient dans le rôle des femmes et les étudiants dans celui des hommes.
- Affecter les rôles d'un projet à chacun des membres.
- Affecter des élèves comme colocataires d'un dortoir.

Cette liste n'est pas exhaustive, mais présente des problèmes qui ont été résolu à l'aide des algorithmes de Gale Shapley et d'Irving.

## Les Algorithmes et leur complexité

### 2.1 Algorithme de Gale Shapley

#### 2.1.1 Fonctionnement

#### 2.1.2 Complexité

### 2.2 Algorithme d'Irving

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
Maintenant que l'on a supprimé les candidats qui ne seront pas choisis
#### 2.2.2 Complexité

O(n<sup>2</sup>)

## Sources

- [_LE PRIX NOBEL D’ÉCONOMIE 2012_, par Jérôme Buzzi](https://images.math.cnrs.fr/Le-prix-Nobel-d-economie-2012.html?lang=fr#menu)
- [_Algorithme de Gale et Shapley_](https://fr.wikipedia.org/wiki/Algorithme_de_Gale_et_Shapley)
- [_Problème des mariages stables_](https://fr.wikipedia.org/wiki/Probl%C3%A8me_des_mariages_stables)
- [_Stable marriage problem_](https://en.wikipedia.org/wiki/Stable_marriage_problem)
- [_Irving's Algorithm and Stable Roommates Problem_](https://www.youtube.com/watch?app=desktop&v=5QLxAp8mRKo)
