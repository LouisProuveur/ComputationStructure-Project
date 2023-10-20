Louis Prouveur

=========================================
How to use?

Ce programme prend en entrée un fichier texte contenant l'opcode et le code de controle correspondant (format voir section suivante).
Il crée/modifie un autre fichier texte pouvant être utilisé pour setup la ROM du bloc de control logic.

Pour l'utiliser, il suffit de le placer dans un dossier et de le lancer depuis l'invite de commande. (python ControlLogic.py)

Il demandera de spécifier un fichier source (chemin d'acces si dossier différent de celui du programme).



=========================================
Format

Le fichier source doit être formatté comme suit : 
OPCODE <Espace> BitCode

avec	OPCODE l'OPCODE en hexadécimal de l'instruction
	<Espace> un espace vide
	BitCode le code en binaire (12 bits) correspondant à l'instruction, c-à-d ce que doit renvoyer le control logic

Exemple avec mon ADD:
20 000111010000


 

======================================== 
Disclaimer

Il n'y a aucune garantie que ce code fonctionne, je voulais juste le faire pour dire d'avoir essayé.
Quitte à l'avoir fait, autant qu'il serve à quelqu'un d'autre

Le fichier "Test2.txt" fourni en exemple ne fonctionne que avec mon implémentation du control logic.