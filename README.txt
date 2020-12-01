

Readme du projet PyQT5 de Regne Corentin et Jagline Lenael en CAI.

Pour pouvoir lancer le projet, il suffit d'avoir Python3 avec PyQt5.
Notre projet se lance en executant mainwindow.py

Une fenetre s'ouvre dans laquelle on peut retrouver:
  - une barre d'actions (toutes les actions possibles rangees dans des menus)
  - une barre d'outils (actions les plus courantes)
  - une zone cliente dans lequel les dessins sont traces avec menu surgissant (actions sur la zone cliente)
  - une barre d'etat

Vous pouvez tracer :
  - des lignes de differentes couleurs, epaisseurs et styles
  - des rectangles de differentes couleurs de remplissage et de contour et differents remplissages
  - des ellipses de differentes couleurs de remplissage et de contour et differents remplissages
  - des polygones de differentes couleurs de remplissage et de contour et differents remplissages
  - des textes de differentes polices et tailles

Specificites techniques:
  - lignes, rectangles, ellipses: une fois le type choisi, appuyer et rester appuyer sur la souris en glissant le curseur. Au relachement de la souris, votre forme va apparaitre
  - polygones: une fois le type choisi, cliquer la ou vous voulez mettre un des sommets de votre polygone. Double-cliquez lorsque vous posez le dernier sommet, le polygone va apparaitre.
  - textes: une fois la police choisie, cliquer a l'endroit ou vous voulez placer votre texte. Une zone de saisie de texte apparait, si vous confirmez, le texte apparait. 

Vous pouvez enregistrer, ouvrir, fermer ou encore creer un nouveau projet

Problemes rencontres:
- nous n'arrivons pas a recuperer les coordonnees du texte, et donc a la reouverture d'un document, ils ne sont plus a la bonne place.
- nous n'avons pas fait la selection de groupe