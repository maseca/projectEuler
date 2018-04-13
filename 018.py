# Find the maximum total from top to bottom of the triangle
dag = []


def main():
    file = open("p018.txt")

    for line in file:
        dag.append(line.split(' '))

    for layer in range(len(dag)):
        for node in range(len(dag[layer])):
            dag[layer][node] = int(dag[layer][node]) + max_parent(layer, node)

    print(max(dag[-1]))


def max_parent(l, n):
    if l is 0:
        return 0
    elif n is 0:
        return dag[l-1][0]
    elif n is l:
        return dag[l-1][n-1]
    else:
        return max(dag[l-1][n-1], dag[l-1][n])


if __name__ == '__main__':
    main()