from copy import copy


class BinTree:
    def __init__(self, data=None, right=None, left=None):
        self.data = data
        self.right = right
        self.left = left

    def insert_node(self, data):
        if self.data:
            if data > self.data:
                if self.right:
                    self.right.insert_node(data)
                else:
                    self.right = BinTree(data)
            elif data < self.data:
                if self.left:
                    self.left.insert_node(data)
                else:
                    self.left = BinTree(data)
        else:
            self.data = data

    def get_height(self):
        if self.data:
            if self.left:
                left_height = self.left.get_height()
            else:
                left_height = 0
            if self.right:
                right_height = self.right.get_height()
            else:
                right_height = 0
            if left_height > right_height:
                return left_height + 1
            else:
                return right_height + 1
        else:
            return 0

    def print_tree(self, level=0):
        if self.right:
            self.right.print_tree(level+1)
        print("\t"*level, self.data)
        if self.left:
            self.left.print_tree(level+1)

    def __repr__(self):
        return f"BinTree[{self.data:^5}]"


def hafman_cod() -> int:
    """2. Закодируйте любую строку из трех слов по алгоритму Хаффмана."""

    def char_coding(hm_tree: BinTree, code="", char_dict={}) -> dict:
        """функция для вычисления кодировки символов на основе дерева Хаффмана"""
        if hm_tree.left is None and hm_tree.right is None:
            char_dict[hm_tree.data] = code
            return char_dict
        else:
            char_coding(hm_tree.left, code + "0")
            char_coding(hm_tree.right, code + "1")
        return char_dict

    coding_str = input("Введите исходную фразу для кодирования:\n")
    char_frequent = {}
    for ch in coding_str:
        char_frequent.setdefault(ch, 0)
        char_frequent[ch] += 1
    char_frequent = list((sorted(char_frequent.items(), key=lambda x: x[1])))
    hafman_tree = BinTree()
    # строим дерево Хаффмана
    while len(char_frequent) > 1:
        if type(char_frequent[0]) == BinTree:
            freq_sum = char_frequent[0].data
            hafman_tree.left = char_frequent.pop(0)
        else:
            freq_sum = char_frequent[0][1]
            hafman_tree.left = BinTree(char_frequent.pop(0)[0])
        if type(char_frequent[0]) == BinTree:
            freq_sum += char_frequent[0].data
            hafman_tree.right = char_frequent.pop(0)
        else:
            freq_sum += char_frequent[0][1]
            hafman_tree.right = BinTree(char_frequent.pop(0)[0])
        hafman_tree.data = freq_sum
        for j in range(len(char_frequent)):
            if type(char_frequent[j]) == BinTree:
                if freq_sum <= char_frequent[j].data:
                    char_frequent.insert(j, copy(hafman_tree))  # копируем объект целиком
                    break
            else:
                if freq_sum <= char_frequent[j][1]:
                    char_frequent.insert(j, copy(hafman_tree))   # копируем объект целиком
                    break
            if j == len(char_frequent) - 1:
                char_frequent.append(copy(hafman_tree))
    # вычисляем код для каждого символа
    cod_table = char_coding(hafman_tree)
    print(f"Итоговая кодировочная таблица:\n{cod_table}")
    print("Полученная закодированная фраза:")
    for ch in coding_str:
        print(cod_table[ch], end="")
    return 0
