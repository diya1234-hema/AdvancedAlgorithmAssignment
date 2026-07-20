import random
import string
import time

from bst import BST
from avl import AVLTree
from hash_table import HashTable
from min_heap import MinHeap


def random_city():
    return ''.join(random.choices(string.ascii_uppercase, k=8))


sizes = [100, 1000, 10000]

print("=" * 70)
print("PERFORMANCE ANALYSIS")
print("=" * 70)

for size in sizes:

    cities = []

    for i in range(size):
        cities.append((random_city(), random.randint(10000, 1000000)))

    # BST
    bst = BST()

    start = time.perf_counter()

    for city, pop in cities:
        bst.root = bst.insert(bst.root, city, pop)

    bst_insert = time.perf_counter() - start

    target = cities[-1][0]

    start = time.perf_counter()

    bst.search(bst.root, target)

    bst_search = time.perf_counter() - start

    # AVL

    avl = AVLTree()

    start = time.perf_counter()

    for city, pop in cities:
        avl.root = avl.insert(avl.root, city, pop)

    avl_insert = time.perf_counter() - start

    # AVL Search (simple recursive search)

    def avl_search(root, key):
        if root is None:
            return None

        if root.city_name == key:
            return root

        if key < root.city_name:
            return avl_search(root.left, key)

        return avl_search(root.right, key)

    start = time.perf_counter()

    avl_search(avl.root, target)

    avl_search_time = time.perf_counter() - start

    # Hash Table

    ht = HashTable()

    start = time.perf_counter()

    for city, pop in cities:
        ht.insert(city, pop)

    hash_insert = time.perf_counter() - start

    start = time.perf_counter()

    ht.search(target)

    hash_search = time.perf_counter() - start

    # Heap

    heap = MinHeap()

    start = time.perf_counter()

    for city, pop in cities:
        heap.insert(random.randint(1, 100000), city)

    heap_insert = time.perf_counter() - start

    start = time.perf_counter()

    heap.get_next_city()

    heap_extract = time.perf_counter() - start

    print("\nDATASET:", size)

    print(f"BST Insert       : {bst_insert:.6f} sec")
    print(f"BST Search       : {bst_search:.6f} sec")

    print(f"AVL Insert       : {avl_insert:.6f} sec")
    print(f"AVL Search       : {avl_search_time:.6f} sec")

    print(f"Hash Insert      : {hash_insert:.6f} sec")
    print(f"Hash Search      : {hash_search:.6f} sec")

    print(f"Heap Insert      : {heap_insert:.6f} sec")
    print(f"Heap Extract Min : {heap_extract:.6f} sec")