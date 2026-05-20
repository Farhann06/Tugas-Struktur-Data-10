# Analisis & Desain Algoritma Sorting Lanjutan + Binary Tree

Implementasi berbagai algoritma sorting lanjutan dan struktur data binary tree menggunakan Python.

---

## 📌 Fitur Program

### 🔹 AdvancedSorter
- Merge Sort Array (Stable)
- Merge Sort Linked List
- Quick Sort Median-of-Three
- Depth Limiter Fallback

### 🔹 ExprHeapSorter
- Expression Tree Builder
- Expression Evaluator
- In-place HeapSort
- Complete Binary Tree Validator

---

# 📂 Struktur Project

```bash
project/
│
├── tugas_jawaban.py
└── README.md
```

---

# ⚙️ Teknologi

- Python 3
- Recursion
- Linked List
- Binary Tree
- Heap
- Divide and Conquer

---

# 🚀 Cara Menjalankan

## 1. Clone Repository

```bash
git clone https://github.com/username/nama-repository.git
```

## 2. Masuk Folder Project

```bash
cd nama-repository
```

## 3. Jalankan Program

```bash
python tugas_jawaban.py
```

atau

```bash
python3 tugas_jawaban.py
```

---

# 🧠 Penjelasan Algoritma

## 1. Merge Sort Array

Menggunakan:
- Virtual Sublists
- Single `tmp_array`
- Stable Merge

### Kompleksitas
| Jenis | Kompleksitas |
|---|---|
| Waktu | O(n log n) |
| Ruang | O(n) |

---

## 2. Linked List Merge Sort

Menggunakan:
- Fast-Slow Pointer
- Dummy Node
- Pointer Manipulation

### Kompleksitas
| Jenis | Kompleksitas |
|---|---|
| Waktu | O(n log n) |
| Ruang | O(log n) |

---

## 3. Quick Sort Median-of-Three

Menggunakan:
- Median Pivot
- In-place Partition
- Depth Limiter

### Kompleksitas
| Jenis | Kompleksitas |
|---|---|
| Average | O(n log n) |
| Worst Case | O(n²) |
| Extra Space | O(1) |

---

## 4. Expression Tree

Contoh ekspresi:

```python
((8*5)+(9/(7-4)))
```

Menggunakan:
- Recursive Descent Parser
- Postorder Traversal

---

## 5. In-Place HeapSort

Menggunakan:
- Max Heap
- Sift Down
- In-place Swap

### Kompleksitas
| Jenis | Kompleksitas |
|---|---|
| Waktu | O(n log n) |
| Ruang | O(1) |

---

## 6. Complete Binary Tree Validator

Validasi properti:
- Complete Binary Tree

### Kompleksitas

```python
O(n)
```

---

# 🧪 Pengujian Program

| Test | Deskripsi |
|---|---|
| Test 1 | Array Merge Sort |
| Test 2 | Merge Sort Duplikat |
| Test 3 | Linked List Merge Sort |
| Test 4 | Quick Sort Median-of-Three |
| Test 5 | Worst-case Descending |
| Test 6 | Semua Elemen Sama |
| Test 7 | Expression Tree |
| Test 8 | Expression Kompleks |
| Test 9 | Division by Zero |
| Test 10 | In-place HeapSort |
| Test 11 | HeapSort Random |
| Test 12 | Complete Binary Tree |

---

# 📊 Kompleksitas Algoritma

| Class | Method | Kompleksitas |
|---|---|---|
| AdvancedSorter | sort_array | O(n log n) |
| AdvancedSorter | sort_linked_list | O(n log n) |
| AdvancedSorter | sort_array_quicksort | O(n log n) average |
| ExprHeapSorter | parse_and_evaluate | O(n) |
| ExprHeapSorter | heapsort_inplace | O(n log n) |
| ExprHeapSorter | is_complete_tree | O(n) |

---

# ✅ Hasil Program

```bash
============================================================
  SEMUA UJI LULUS ✓
============================================================
```

---

# 👨‍💻 Author
Farhan Bagas Firmansyah_039

Tugas Analisis & Desain Algoritma  
Sorting Lanjutan + Binary Tree 
