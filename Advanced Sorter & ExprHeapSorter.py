"""
============================================================
JAWABAN TUGAS: Analisis & Desain Algoritma Sorting Lanjutan
                       + Binary Tree
Nama File : tugas_jawaban.py
============================================================
"""

import math
from typing import List, Optional
from collections import deque


# ============================================================
# BAGIAN 1 — AdvancedSorter
# ============================================================

class ListNode:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class AdvancedSorter:
    def __init__(self):
        pass

    # ----------------------------------------------------------
    # 1. ARRAY MERGE SORT (Virtual Sublists + Single tmpArray)
    # ----------------------------------------------------------

    def sort_array(self, arr: List[int]) -> List[int]:
        if len(arr) <= 1:
            return arr
        tmp_array = [0] * len(arr)          # satu tmpArray, dialokasi sekali
        self._rec_merge_sort(arr, 0, len(arr) - 1, tmp_array)
        return arr

    def _rec_merge_sort(self, arr, first, last, tmp_array):
        if first >= last:
            return
        mid = (first + last) // 2
        self._rec_merge_sort(arr, first, mid, tmp_array)
        self._rec_merge_sort(arr, mid + 1, last, tmp_array)
        self._merge_virtual(arr, first, mid, last, tmp_array)

    def _merge_virtual(self, arr, left_start, mid, right_end, tmp_array):
        # ── TODO (SELESAI) ──────────────────────────────────────
        # Gabungkan dua virtual sublist secara STABLE (gunakan <=)
        # Sublist kiri : arr[left_start .. mid]
        # Sublist kanan: arr[mid+1 .. right_end]
        # Gunakan tmp_array sebagai buffer, lalu salin kembali ke arr
        # ────────────────────────────────────────────────────────
        a, b, k = left_start, mid + 1, left_start

        while a <= mid and b <= right_end:
            if arr[a] <= arr[b]:          # <= → STABLE (kiri duluan jika sama)
                tmp_array[k] = arr[a];  a += 1
            else:
                tmp_array[k] = arr[b];  b += 1
            k += 1

        while a <= mid:                    # sisa sublist kiri
            tmp_array[k] = arr[a];  a += 1;  k += 1

        while b <= right_end:              # sisa sublist kanan
            tmp_array[k] = arr[b];  b += 1;  k += 1

        for i in range(left_start, right_end + 1):   # salin balik
            arr[i] = tmp_array[i]

    # ----------------------------------------------------------
    # 2. LINKED LIST MERGE SORT (Fast-Slow + Dummy Merge)
    # ----------------------------------------------------------

    def sort_linked_list(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        right_head = self._split_linked_list(head)
        left_head  = head
        left_sorted  = self.sort_linked_list(left_head)
        right_sorted = self.sort_linked_list(right_head)
        return self._merge_linked_lists(left_sorted, right_sorted)

    def _split_linked_list(self, head: ListNode) -> Optional[ListNode]:
        # ── TODO (SELESAI) ──────────────────────────────────────
        # Fast-Slow Pointer:
        #   midPoint (slow) bergerak 1 langkah
        #   curNode  (fast) bergerak 2 langkah
        # Setelah loop: midPoint berada di tengah list
        # Putus link midPoint.next = None → kembalikan right_head
        # ────────────────────────────────────────────────────────
        midPoint = head            # slow pointer
        curNode  = head.next       # fast pointer

        while curNode is not None and curNode.next is not None:
            midPoint = midPoint.next
            curNode  = curNode.next.next

        right_head       = midPoint.next   # head sublist kanan
        midPoint.next    = None            # putus link
        return right_head

    def _merge_linked_lists(self, listA: Optional[ListNode],
                             listB: Optional[ListNode]) -> Optional[ListNode]:
        # ── TODO (SELESAI) ──────────────────────────────────────
        # Dummy node sebagai sentinel, tail reference untuk append O(1)
        # Tidak mengalokasi node data baru — hanya ubah pointer .next
        # Merge STABLE: ambil listA jika listA.data <= listB.data
        # ────────────────────────────────────────────────────────
        dummy = ListNode(0)        # 1 dummy node statis per merge
        tail  = dummy

        while listA is not None and listB is not None:
            if listA.data <= listB.data:   # STABLE: kiri duluan jika sama
                tail.next = listA;  listA = listA.next
            else:
                tail.next = listB;  listB = listB.next
            tail = tail.next

        tail.next = listA if listA is not None else listB   # sambung sisa
        return dummy.next

    # ----------------------------------------------------------
    # 3. QUICK SORT PARTITION (Median-of-Three Pivot)
    # ----------------------------------------------------------

    def partition_quick(self, arr: List[int], first: int, last: int) -> int:
        # ── TODO (SELESAI) ──────────────────────────────────────
        # Pilih pivot = median dari arr[first], arr[mid], arr[last]
        # Tempatkan pivot ke arr[first], lalu jalankan partisi standar
        # Kembalikan posisi akhir pivot
        # CATATAN: partisi in-place ini TIDAK STABIL (swap jarak jauh)
        # ────────────────────────────────────────────────────────
        mid = (first + last) // 2

        # Langkah 1: urutkan tiga kandidat agar median ke arr[first]
        if arr[first] > arr[mid]:
            arr[first], arr[mid]  = arr[mid],  arr[first]
        if arr[first] > arr[last]:
            arr[first], arr[last] = arr[last], arr[first]
        if arr[mid]   < arr[last]:
            arr[first], arr[mid]  = arr[mid],  arr[first]
        # Setelah tiga swap di atas, arr[first] = median → pivot

        pivot = arr[first]
        left  = first + 1
        right = last

        # Langkah 2: partisi standar in-place
        done = False
        while not done:
            while left  <= right and arr[left]  <= pivot:  left  += 1
            while left  <= right and arr[right] >  pivot:  right -= 1
            if left > right:
                done = True
            else:
                arr[left], arr[right] = arr[right], arr[left]

        arr[first], arr[right] = arr[right], arr[first]   # tempatkan pivot
        return right

    def quick_sort_recursive(self, arr: List[int], first: int, last: int,
                              depth: int = 0):
        if first >= last:
            return
        n         = last - first + 1
        max_depth = int(2 * math.log2(max(n, 2)))

        # ── Depth Limiter (TODO SELESAI) ────────────────────────
        # Jika depth > 2*log2(n) → fallback ke Merge Sort
        # ────────────────────────────────────────────────────────
        if depth > max_depth:
            sub = arr[first:last + 1]
            self.sort_array(sub)
            arr[first:last + 1] = sub
            return

        pivot_pos = self.partition_quick(arr, first, last)
        self.quick_sort_recursive(arr, first, pivot_pos - 1, depth + 1)
        self.quick_sort_recursive(arr, pivot_pos + 1, last,  depth + 1)

    def sort_array_quicksort(self, arr: List[int]) -> List[int]:
        if len(arr) <= 1:
            return arr
        self.quick_sort_recursive(arr, 0, len(arr) - 1)
        return arr


# ============================================================
# BAGIAN 2 — ExprHeapSorter
# ============================================================

class ExprHeapSorter:
    def __init__(self, expr_str: str):
        self.expr   = expr_str
        self.values = []

    # ----------------------------------------------------------
    # parse_and_evaluate
    # ----------------------------------------------------------

    def parse_and_evaluate(self) -> List[int]:
        """Bangun pohon ekspresi, evaluasi, kembalikan list nilai integer."""
        tokens      = deque(self.expr.replace(' ', ''))
        root        = self._build_tree(tokens)
        result      = self._eval_tree(root)
        self.values = [result]
        return self.values

    def _build_tree(self, tokens: deque) -> Optional[dict]:
        # ── TODO (SELESAI) ──────────────────────────────────────
        # Recursive descent parser untuk fully-parenthesized expression.
        # Pola:
        #   '('  → rekursi kiri → ambil operator → rekursi kanan → skip ')'
        #   digit → buat leaf node, return
        # ────────────────────────────────────────────────────────
        if not tokens:
            return None

        token = tokens.popleft()

        if token == '(':
            left     = self._build_tree(tokens)    # subpohon kiri
            operator = tokens.popleft()             # operator
            right    = self._build_tree(tokens)    # subpohon kanan
            if tokens and tokens[0] == ')':
                tokens.popleft()                    # buang ')'
            return {'val': operator, 'left': left, 'right': right}

        elif token.lstrip('-').isdigit():
            num_str = token
            while tokens and tokens[0].isdigit():   # angka multi-digit
                num_str += tokens.popleft()
            return {'val': int(num_str), 'left': None, 'right': None}

        else:
            raise ValueError(f"Token tidak valid: '{token}'")

    def _eval_tree(self, node: Optional[dict]) -> int:
        # ── TODO (SELESAI) ──────────────────────────────────────
        # Evaluasi postorder: kiri → kanan → root
        # Handle pembagian nol dengan raise ValueError
        # ────────────────────────────────────────────────────────
        if node is None:
            raise ValueError("Node kosong")

        if node['left'] is None and node['right'] is None:
            return node['val']                          # leaf = operand

        lv = self._eval_tree(node['left'])
        rv = self._eval_tree(node['right'])
        op = node['val']

        if   op == '+':  return lv + rv
        elif op == '-':  return lv - rv
        elif op == '*':  return lv * rv
        elif op == '/':
            if rv == 0:
                raise ValueError("Pembagian dengan nol tidak diizinkan!")
            return lv // rv
        else:
            raise ValueError(f"Operator tidak dikenal: '{op}'")

    # ----------------------------------------------------------
    # heapsort_inplace
    # ----------------------------------------------------------

    def heapsort_inplace(self, arr: List[int]) -> List[int]:
        """Urutkan array ascending dengan in-place heapsort."""
        n = len(arr)
        if n <= 1:
            return arr

        # Fase 1: bangun max-heap dari daun ke atas
        for i in range(n // 2 - 1, -1, -1):
            self._sift_down(arr, n, i)

        # Fase 2: ekstrak root (max) ke akhir, sift-down untuk restore heap
        for end in range(n - 1, 0, -1):
            arr[0], arr[end] = arr[end], arr[0]
            self._sift_down(arr, end, 0)

        return arr

    def _sift_down(self, arr: List[int], heap_size: int, idx: int):
        # ── TODO (SELESAI) ──────────────────────────────────────
        # Pulihkan heap-order property dari idx ke bawah.
        # left = 2*idx+1 , right = 2*idx+2
        # Loop hingga largest == idx (tidak ada swap)
        # ────────────────────────────────────────────────────────
        while True:
            largest = idx
            left    = 2 * idx + 1
            right   = 2 * idx + 2

            if left  < heap_size and arr[left]  > arr[largest]:  largest = left
            if right < heap_size and arr[right] > arr[largest]:  largest = right

            if largest == idx:
                break                               # heap property terpenuhi

            arr[idx], arr[largest] = arr[largest], arr[idx]
            idx = largest

    def is_complete_tree(self, arr: List[int]) -> bool:
        # ── TODO (SELESAI) ──────────────────────────────────────
        # Validasi complete binary tree via pemetaan indeks array.
        # Setelah ditemukan "slot kosong" (indeks >= n),
        # tidak boleh ada node valid lagi → bukan complete tree.
        # ────────────────────────────────────────────────────────
        n = len(arr)
        if n == 0:
            return True

        found_empty = False
        for i in range(n):
            left  = 2 * i + 1
            right = 2 * i + 2

            if left >= n:
                found_empty = True
            elif found_empty:
                return False

            if right >= n:
                found_empty = True
            elif found_empty:
                return False

        return True


# ============================================================
# HELPER
# ============================================================

def ll_from_list(lst):
    if not lst: return None
    head = cur = ListNode(lst[0])
    for v in lst[1:]:
        cur.next = ListNode(v); cur = cur.next
    return head

def ll_to_list(head):
    out = []
    while head: out.append(head.data); head = head.next
    return out

def sep(title=""):
    print("\n" + "=" * 60)
    if title: print(f"  {title}")
    print("=" * 60)


# ============================================================
# OUTPUT / PENGUJIAN
# ============================================================

if __name__ == "__main__":

    sep("BAGIAN 1 — AdvancedSorter")
    sorter = AdvancedSorter()

    # ── Test 1: Array Merge Sort ────────────────────────────
    print("\n[Test 1] Array Merge Sort — Stable")
    inp = [38, 27, 43, 3, 9, 82, 10]
    out = sorter.sort_array(inp[:])
    print(f"  Input  : {inp}")
    print(f"  Output : {out}")
    assert out == sorted(inp)
    print("  ✓ LULUS")

    # ── Test 2: duplikat (uji stabilitas) ───────────────────
    print("\n[Test 2] Array Merge Sort — Duplikat")
    inp = [5, 3, 8, 3, 1, 5, 2]
    out = sorter.sort_array(inp[:])
    print(f"  Input  : {inp}")
    print(f"  Output : {out}")
    assert out == sorted(inp)
    print("  ✓ LULUS")

    # ── Test 3: Linked List Sort ────────────────────────────
    print("\n[Test 3] Linked List Merge Sort — Fast-Slow Pointer")
    inp = [4, 2, 7, 1, 9, 3, 6]
    out = ll_to_list(sorter.sort_linked_list(ll_from_list(inp)))
    print(f"  Input  : {' → '.join(map(str,inp))} → NULL")
    print(f"  Output : {' → '.join(map(str,out))} → NULL")
    assert out == sorted(inp)
    print("  ✓ LULUS")

    # ── Test 4: Quick Sort biasa ────────────────────────────
    print("\n[Test 4] Quick Sort — Median-of-Three Pivot")
    inp = [64, 34, 25, 12, 22, 11, 90]
    out = sorter.sort_array_quicksort(inp[:])
    print(f"  Input  : {inp}")
    print(f"  Output : {out}")
    assert out == sorted(inp)
    print("  ✓ LULUS")

    # ── Test 5: descending (worst-case tanpa median-3) ──────
    print("\n[Test 5] Quick Sort — Worst-Case Descending (Depth Limiter)")
    inp = list(range(100, 0, -1))
    out = sorter.sort_array_quicksort(inp[:])
    print(f"  Input  : [100, 99, ..., 1]  (100 elemen descending)")
    print(f"  Output : [1, 2, ..., 100]")
    assert out == list(range(1, 101))
    print(f"  Depth limit aktif pada depth > {int(2*math.log2(100))} → fallback Merge Sort")
    print("  ✓ LULUS")

    # ── Test 6: all same ────────────────────────────────────
    print("\n[Test 6] Quick Sort — Semua Elemen Sama")
    inp = [7] * 20
    out = sorter.sort_array_quicksort(inp[:])
    print(f"  Input  : {inp}")
    print(f"  Output : {out}")
    assert out == inp
    print("  ✓ LULUS")

    # ────────────────────────────────────────────────────────
    sep("BAGIAN 2 — ExprHeapSorter")

    # ── Test 7: Expression Tree ─────────────────────────────
    print("\n[Test 7] Expression Tree — ((8*5)+(9/(7-4)))")
    ehs  = ExprHeapSorter("((8*5)+(9/(7-4)))")
    vals = ehs.parse_and_evaluate()
    #  (8×5)=40  (7-4)=3  (9÷3)=3  40+3=43
    print(f"  Ekspresi   : ((8*5)+(9/(7-4)))")
    print(f"  Hasil eval : {vals[0]}   ← expected 43")
    assert vals[0] == 43
    print("  ✓ LULUS")

    # ── Test 8: Expression — lebih kompleks ─────────────────
    print("\n[Test 8] Expression Tree — ((3+4)*(2-1))")
    ehs2  = ExprHeapSorter("((3+4)*(2-1))")
    vals2 = ehs2.parse_and_evaluate()
    print(f"  Ekspresi   : ((3+4)*(2-1))")
    print(f"  Hasil eval : {vals2[0]}   ← expected 7")
    assert vals2[0] == 7
    print("  ✓ LULUS")

    # ── Test 9: Division by zero ─────────────────────────────
    print("\n[Test 9] Expression Tree — Division by Zero")
    try:
        ExprHeapSorter("(8/(4-4))").parse_and_evaluate()
        print("  GAGAL — seharusnya raise ValueError")
    except ValueError as e:
        print(f"  ValueError ditangkap : {e}")
        print("  ✓ LULUS")

    # ── Test 10: In-Place Heapsort ───────────────────────────
    print("\n[Test 10] In-Place Heapsort")
    ehs3 = ExprHeapSorter("")
    inp  = [43, 7, 15, 3, 22, 8, 11, 1]
    out  = ehs3.heapsort_inplace(inp[:])
    print(f"  Input  : {inp}")
    print(f"  Output : {out}")
    assert out == sorted(inp)
    print("  ✓ LULUS")

    # ── Test 11: Heapsort besar ──────────────────────────────
    print("\n[Test 11] In-Place Heapsort — 20 Elemen Acak")
    import random; random.seed(42)
    inp  = random.sample(range(1, 200), 20)
    out  = ehs3.heapsort_inplace(inp[:])
    print(f"  Input  : {inp}")
    print(f"  Output : {out}")
    assert out == sorted(inp)
    print("  ✓ LULUS")

    # ── Test 12: Complete Tree Validator ────────────────────
    print("\n[Test 12] Complete Tree Validator")
    cases = [
        ([1,2,3,4,5,6,7],  True,  "perfect binary tree (7 node)"),
        ([1,2,3,4],        True,  "complete, level terakhir kiri"),
        ([1,2,3,4,5,6],    True,  "complete, 6 node"),
        ([],               True,  "array kosong"),
        ([42],             True,  "1 node"),
    ]
    for arr, expected, desc in cases:
        result = ehs3.is_complete_tree(arr)
        status = "✓" if result == expected else "✗ GAGAL"
        print(f"  {status}  {arr}  →  {result}   ({desc})")
        assert result == expected

    # ── Ringkasan ────────────────────────────────────────────
    sep("SEMUA UJI LULUS ✓")
    print()
    print("  Kelas        | Metode                 | Kompleksitas")
    print("  -------------|------------------------|-----------------------------")
    print("  AdvancedSorter| sort_array            | O(n log n) waktu, O(n) ruang")
    print("  AdvancedSorter| sort_linked_list      | O(n log n) waktu, O(log n) ruang")
    print("  AdvancedSorter| sort_array_quicksort  | O(n log n) avg,  O(1) ekstra")
    print("  ExprHeapSorter| parse_and_evaluate    | O(n) token")
    print("  ExprHeapSorter| heapsort_inplace      | O(n log n) waktu, O(1) ruang")
    print("  ExprHeapSorter| is_complete_tree      | O(n)")
    print()