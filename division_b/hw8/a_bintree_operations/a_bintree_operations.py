"""
A. Бинарное дерево (вставка, поиск, обход)
Ограничение времени	1 секунда
Ограничение памяти	64Mb
Ввод	стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt

Напишите программу, которая будет реализовывать действия в бинарном дереве
поиска «вставить» и «найти» (по значению). Программа должна обрабатывать
запросы трёх видов:

ADD n — если указанного числа еще нет в дереве, вставлять его и выводить слово
«DONE», если уже есть — оставлять дерево как было и выводить слово «ALREADY».

SEARCH — следует выводить слово «YES» (если значение найдено в дереве) или
слово «NO» (если не найдено). Дерево при этом не меняется.

PRINTTREE — выводить все дерево, обязательно используя алгоритм, указанный в
формате вывода результатов.

Формат ввода
В каждой строке входных данных записан один из запросов ADD n или SEARCH n или
PRINTTREE. Гарантируется, что запросы PRINTTREE будут вызываться только в
моменты, когда дерево не пустое. Общее количество запросов не превышает 1000,
из них не более 20 запросов PRINTTREE.

Формат вывода
Для каждого запроса выводите ответ на него. Для запросов ADD и SEARCH —
соответствующее слово в отдельной строке. На запрос PRINTTREE надо выводить
дерево, обязательно согласно такому алгоритму:

1) Распечатать левое поддерево

2) Вывести количество точек, равное глубине узла

3) Вывести значение ключа

4) Распечатать правое поддерево

Пример
Ввод	Вывод
ADD 2
ADD 3
ADD 2
SEARCH 2
ADD 5
PRINTTREE
SEARCH 7
        DONE
        DONE
        ALREADY
        YES
        DONE
        2
        .3
        ..5
        NO
"""

from typing import Optional, Any
from dataclasses import dataclass


@dataclass
class Node:
    key: Any
    val: Any
    left: Optional["Node"] = None
    right: Optional["Node"] = None


class BST:
    root: Optional[Node] = None

    def add(self, key, val):
        self.root = self._add(key, val, self.root)

    def _add(self, key, val, node):
        if node is None:
            return Node(key, val)
        if node.key > key:
            node.left = self._add(key, val, node.left)
        if node.key < key:
            node.right = self._add(key, val, node.right)
        return node

    def get(self, key):
        x = self.root
        while x is not None:
            if x.key == key:
                return x.val
            if key < x.key:
                x = x.left
            elif key > x.key:
                x = x.right
        return None

    def print(self):
        self._print(self.root, 0)

    def _print(self, node, depth):
        if node is None:
            return
        self._print(node.left, depth + 1)
        print("." * depth, node.key, sep="")
        self._print(node.right, depth + 1)


def test():
    bst = BST()
    bst.add(2, 0)
    bst.add(3, 0)
    bst.add(1, 1)
    bst.add(5, 0)
    bst.add(4, 0)
    bst.add(-1, 0)
    bst.add(-0.5, 0)
    bst.add(6, 0)
    assert bst.get(2) == 0
    assert bst.get(3) == 0
    assert bst.get(1) == 1
    assert bst.get(0) is None
    bst.print()
    bst = BST()
    bst.add(2, 0)
    bst.add(3, 0)
    bst.add(5, 1)
    # bst.print()


# test()


def main():
    with open("input.txt", "r") as f:
        queries = f.readlines()
    bst = BST()
    for q in queries:
        # print(q)
        if q.startswith("ADD"):
            key = int(q.split()[1])
            if bst.get(key) is not None:
                print("ALREADY")
            else:
                bst.add(key, 0)
                print("DONE")
        elif q.startswith("SEARCH"):
            key = int(q.split()[1])
            if bst.get(key) is not None:
                print("YES")
            else:
                print("NO")
        elif q.startswith("PRINTTREE"):
            bst.print()


main()
