Ce package a ete cree dans le cadre d'un projet 42.
Il contient seulement les fonctions : "ft_tqdm", "count_in_list".

# Build
python -m build

# Install
pip install ./dist/ft_package-0.0.1.tar.gz

# Display
pip show -v ft_package

# comment l'utiliser :

from ft_package_mjameau.Loading import ft_tqdm
from ft_package_mjameau.count_in_list import count_in_list

ft_tqdm :
for x in ft_tqdm(range(333))
	pass

count_in_list :
print(count_in_list(["toto", "tata", "toto"], "toto"))

# tester.py :
from ft_package_mjameau.count_in_list import count_in_list
from ft_package_mjameau.Loading import ft_tqdm
from time import sleep

print("---- TEST COUNT_IN_LIST ----")
print(count_in_list(["toto", "tata", "toto"], "toto"))  # output: 2
print(count_in_list(["toto", "tata", "toto"], "tutu"))  # output: 0

print("---- TEST FT_TDQM ----")
for elem in ft_tqdm(range(333)):
    sleep(0.005)

