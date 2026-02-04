import os


def ft_tqdm(lst: range) -> None:  # type: ignore
    """ - Fonction imitant le comportement de tqdm,
permet de montrer une barre de progression dans le terminal

- On prend en argument une liste (range) et
on yield (renvoie) un elem a chaque iteration

- On recupere la taille du terminal pour ajuster la barre

- On calcule le pourcentage avec le nombre d'iterations
 faites et le nombre total d'iterations a faire

- On calcule l'avancement de la barre en fonction
 de la taille de la barre et du pourcentage

- On construit la barre avec les caracteres et
on multiplie par filled_length pour avoir la partie remplie,
et on complete avec des ' ' pour le reste non fini.

 -!- Le vrai tqdm sait dans quel environnement il est, mais
 get_terminal_size non ,donc la barre depasse sur VSCODE c'est normal -!- """

    try:
        screen_size = os.get_terminal_size().columns
    except OSError:
        screen_size = 80

    try:
        max_iter = len(lst)
    except TypeError:
        max_iter = sum(1 for _ in lst)

    for item in range(len(lst)):
        try:
            percent = int(100 * (item + 1) // max_iter)
            counter = f"{item + 1}/{max_iter}"
            prefix = f"{percent}%|"
            suffix = f"| {counter}"

            bar_size = min(40, screen_size - len(prefix) - len(suffix) - 1)
            filled_length = int(bar_size * (item + 1) // max_iter)

            bar = "█" * filled_length + " " * (bar_size - filled_length)

            print(f"\r{prefix}{bar}{suffix}", end="", flush=True)
        except Exception:
            pass
        yield item

# ========= TESTSSSS ==============
# from time import sleep
# from tqdm import tqdm
# for elem in ft_tqdm(range(333)):
#     sleep(0.005)
# print()
# for elem in tqdm(range(333)):
#     sleep(0.005)
# print()
