Ce package a ete cree dans le cadre d'un projet 42.
Il contient seulement la fonction : "ft_tqdm".

# Build
python -m build

# Install
pip install ./dist/ft_package-0.0.1.tar.gz

# Display
pip show -v ft_package

# comment l'utiliser :

from ft_package import ft_tqdm

for x in ft_tqdm(range(333))
	pass
