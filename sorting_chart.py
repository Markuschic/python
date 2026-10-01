import matplotlib.pyplot as plt

# Данные из таблицы (O3 optimization)
N = [10, 500, 1000, 50000, 1000000]
N_labels = ['10', '500', '1K', '50K', '1M']

algorithms = {
    'Bubble':    {'gcc': [0.000375, 0.221584, 0.952917, 858.407041, 2624835.343542],
                  'clang': [0.000667, 0.158417, 0.849916, 849.28495, 2624835.343542]},
    'Selection': {'gcc': [0.000292, 0.1065, 0.498375, 287.968, 121126.526291],
                  'clang': [0.000417, 0.087042, 0.38525, 290.040834, 121769.346083]},
    'Insertion': {'gcc': [0.00025, 0.150541, 0.874208, 764.22625, 596559.61525],
                  'clang': [0.000542, 0.111333, 0.525084, 764.066834, 306841.983583]},
    'Quick':     {'gcc': [0.000708, 0.016083, 0.043166, 0.695041, 14.566292],
                  'clang': [0.000958, 0.013084, 0.035667, 0.702042, 15.060208]},
    'Merge':     {'gcc': [0.004083, 0.10875, 0.232583, 3.94875, 80.630583],
                  'clang': [0.003667, 0.093041, 0.20075, 3.9285, 82.914583]},
    'Heap':      {'gcc': [0.000666, 0.028209, 0.071458, 1.986209, 52.921917],
                  'clang': [0.000583, 0.023375, 0.066084, 2.043541, 52.93175]},
    'Counting':  {'gcc': [0.000583, 0.001792, 0.002459, 0.034875, 0.551792],
                  'clang': [0.001042, 0.001209, 0.002167, 0.035208, 0.547709]},
    'Radix':     {'gcc': [0.000667, 0.004166, 0.004583, 0.084375, 1.508541],
                  'clang': [0.000584, 0.003834, 0.0085, 0.082292, 1.636667]},
    'Bucket':    {'gcc': [0.003625, 0.014083, 0.018125, 0.337959, 7.624458],
                  'clang': [0.002541, 0.012334, 0.023458, 0.330375, 7.756917]},
    'Qsort':     {'gcc': [0.000598, 0.012168, 0.038267, 0.634103, 13.126736],
                  'clang': [0.000624, 0.01389, 0.037112, 0.681986, 13.688214]},
}

colors = {
    'Bubble': '#d62728', 'Selection': '#ff7f0e', 'Insertion': '#2ca02c',
    'Quick': '#1f77b4', 'Merge': '#9467bd', 'Heap': '#8c564b',
    'Counting': '#e377c2', 'Radix': '#7f7f7f', 'Bucket': '#bcbd22',
    'Qsort': '#17becf',
}

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(22, 9), sharey=False)

# --- Подграфик 1: O(N²) алгоритмы ---
slow_algos = ['Bubble', 'Selection', 'Insertion']
for algo in slow_algos:
    ax1.plot(N, algorithms[algo]['gcc'],   color=colors[algo], linewidth=2.5,
             label=f'{algo} (GCC)',   linestyle='-',  marker='o', markersize=6)
    ax1.plot(N, algorithms[algo]['clang'], color=colors[algo], linewidth=2.5,
             label=f'{algo} (Clang)', linestyle='--', marker='s', markersize=6)

ax1.set_xscale('log')
ax1.set_yscale('log')
ax1.set_xticks(N)
ax1.set_xticklabels(N_labels, fontsize=11)
ax1.set_xlabel('Input size N', fontsize=14)
ax1.set_ylabel('Execution time (ms)', fontsize=14)
ax1.set_title('O(N²) Algorithms — Bubble, Selection, Insertion\n(O3 Optimization)', 
              fontsize=15, fontweight='bold', pad=15)
ax1.grid(True, which='both', linestyle=':', alpha=0.5)
ax1.legend(loc='upper left', fontsize=11, framealpha=0.9)

# --- Подграфик 2: Эффективные алгоритмы ---
fast_algos = ['Quick', 'Merge', 'Heap', 'Counting', 'Radix', 'Bucket', 'Qsort']
for algo in fast_algos:
    ax2.plot(N, algorithms[algo]['gcc'],   color=colors[algo], linewidth=2.5,
             label=f'{algo} (GCC)',   linestyle='-',  marker='o', markersize=6)
    ax2.plot(N, algorithms[algo]['clang'], color=colors[algo], linewidth=2.5,
             label=f'{algo} (Clang)', linestyle='--', marker='s', markersize=6)

ax2.set_xscale('log')
ax2.set_yscale('log')
ax2.set_xticks(N)
ax2.set_xticklabels(N_labels, fontsize=11)
ax2.set_xlabel('Input size N', fontsize=14)
ax2.set_title('Efficient Algorithms — Quick, Merge, Heap, Counting, Radix, Bucket, Qsort\n(O3 Optimization)',
              fontsize=15, fontweight='bold', pad=15)
ax2.grid(True, which='both', linestyle=':', alpha=0.5)
ax2.legend(loc='upper left', fontsize=10, framealpha=0.9, ncol=2)

fig.suptitle('Sorting Algorithm Performance Comparison — Mac OS (O3 optimization)\n'
             'Solid = GCC  |  Dashed = Clang',
             fontsize=18, fontweight='bold', y=1.02)

plt.tight_layout()
plt.savefig('sorting_comparison_mac_o3_final.png', dpi=150, bbox_inches='tight')
plt.show()