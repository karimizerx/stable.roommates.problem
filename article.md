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

Le projet des colocataires consiste à trouver parmi **2n personne** une liste de paires de personnes qui pourront être colocataires. Les individus peuvent indiquer leurs préférences
pour les personnes avec qui elle accepteraient d’être mises en colocation. On dit qu’une
liste est instable s’il existe deux individus qui ne sont pas appariés et qui préfèreraient
tous les deux être ensemble plutôt que de rester avec la personne qui leur a été affectée.
Un cas particulier de ce problème est le problème de l’appariement stable (classiquement
appelé mariage stable). Dans ce cas, les 2nindividus sont répartis en deux groupes, et
le but est de constituer une liste de binômes, où chaque binôme est constitué de per-
sonnes dans des groupes différents. Un appariement est dit instable si, comme dans le cas
précédent, deux personnes de binômes différents préfèrent être ensemble qu’avec les personnes à qui elles ont été
affectées.
