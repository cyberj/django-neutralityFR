=========================
Description du middleware
=========================

django-neutralityFR est une extension anti Internet, une atteinte délibérée à la Neutralité du Net. 
Basé à l'origine sur WP-neutralityFR, plugin wordpress.

Il s'agit d'une réponse stupide à la position idiote de la député Muriel Marland-Militello qui semble avoir du mal à faire la différence entre un Net neutre et un Net "optimalisé" [1]_.
django-NeutralityFR bloque des plages d'adresses IP appartenant à l'Assemblée Nationale.

Bloquer le range d'IP de l'Assemblée Nationale est une mesure extrême et stupide. Elle met en évidence le danger de décisions de blocage unilatérales "optimalisées", au détriment de règles simples d'accès universel, sans discrimination.

Le problème de fond
===================

Le concept de neutralité est précisement ce qui a permis de nous offrir aujourd'hui le Net tel que nous le connaissons. L'assymétrie des flux (et non le manque de bande passante comme l'e-gnorance de la député le souligne), est sujette à de nombreuses questions d'ordre économique sur la neutralité. Ces questions économiques sont conjoncturelles, donc secondaires.

Elles ne peuvent et ne doivent en aucun cas éluder les questions bien plus importantes car structurelles : à quoi servirait une réflexion économique sur un écosystème dont on détruirait la valeur [2]_.

La mise en place de listes de blocage secrètes (vous pouvez bloquer les ip que vous voulez en modifiant le code source du middleware et rendre public ou non ce que vous souhaitez bloquer), sans l'intervention d'un juge, de manière ouvertement discriminatoire, c'est précisément ce que vous propose cette django-NeutralityFR. Un middleware pour avoir moins d'Internet.

Objectif
========

L'objectif est bien de faire entrer la Neutralité du Net dans la loi en pointant du doigt les risques inhérents à la pratique du blocage de sites : 
 * discrimination
 * censure bête et méchante sans décision judiciaire
 * surblocage
 * cloisonnement d'Internet

Cette version est proposée pour le moment uniquement en Français mais elle est parfaitement localisable et nous invitons les défenseurs de la neutralité du Net à l'internationaliser et à adapter les blocs IP en fonction des institutions locales impliquées dans des blocages de sites.

Installation
============

Une fois l'application ``django-neutralityFR`` installée et présente dans ``INSTALLED_APPS`` sous le nom ``neutralityFR``, ajoutez juste le middleware ``'neutralityFR.middleware.3M.DuctTapeMiddleware'`` dans la liste de vos middlewares Django.

Comment cela fonctionne techniquement
=====================================

django-NeutralityFR bloque 3 blocs d'IP appartenant à l'Assemblée Nationale : 
   * 80.118.139.160 à 80.118.139.191 (80.118.39.160/27)
   * 62.160.71.0 à 62.160.71.255 (62.160.71.0/24)
   * 84.233.174.48 à 84.233.174.63 (84.233.174.48/28)
Si un visiteur est détecté comme en provenance de l'une de ces adresses IP, ceci retourne une page explicative à nos députés.

Ce middleware a été réalisé très rapidement et est évidemment perfectible. Ne vous gênez donc pas pour l'améliorer et l'adapter par exemple pour d'autres CMS.

Pour plus d'informations
========================

 * Le rapport parlementaire sur la Neutralité du Net : http://www.pcinpact.com/actu/news/63057-rapport-parlementaire-neutralite-internet-net.htm
 * Les positions de Madame Marland-Militello : http://marland-militello.fr/2011/04/20/la-neutralite-du-net-une-utopie-seduisante/
 * La réponse de Reflets.info : http://reflets.info/optimiser-son-internet-a-la-sauce-marland-militello/

Contributeurs
=============

 * Lucas Fernandez (c0daz) / http://kasey.fr/ 
 * Bluetouff & Kitetoa (specs & #man) / http://reflets.info 
 * Paul Da Silva (Landing Page) / http://www.paulds.fr
 * Johan Charpentier (Django) / http://cyberj.me/

Remerciements
=============

 * La Quadrature du Net [3]_ : http://www.laquadrature.net/soutien 
 * French Data Network : http://www.fdn.fr/ 
 * Bearstech : http://bearstech.com 

--

.. [1] Ne cherchez pas ce mot dans le dictionnaire il est "®2011 Marland Militello", c'est le seul bout de code propriétaire de ce middleware.
.. [2] Loi de Metcalfe : L’utilité d’un réseau est proportionnelle au carré du nombre de ses utilisateurs.
.. [3] Pour un Net libre, ouvert et neutre, il est capital de supporter la Quadrature du Net : http://www.laquadrature.net/soutien

