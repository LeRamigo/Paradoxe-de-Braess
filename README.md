# Paradoxe-de-Braess

Mon projet de Tipe sur le thème de la ville.

les matrices représente les routes avec des couples composés du type de la route (ce type donne un temps de parcours par exemple le type 1 donne 5 minutes de parcours) et de la probabilité que les conducteurs utilisent la route.

Hypothèses simplificatrices:
-Tous les conducteurs partent du point A pour aller au B (pas d'ajout ou de retrait en cours)
- le programme foctionne par tour, un tour finit quand tous les conducteurs ont parcouru une route, donc à chaque tour ils partent tous en même temps, peu importe leurs précédents temps de parcours.
- pas d'accidents, de travaux, d'obstacles,... autres que ceux prévus ( avec les fonctions intégrer_obst et obstacles)
