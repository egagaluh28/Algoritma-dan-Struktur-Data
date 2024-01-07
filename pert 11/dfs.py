graph = {
    1: [2, 5],        # Graf dengan node 1 memiliki 2 dan 5
    2: [1, 3, 5],     # Graf dengan node 2 memiliki 1, 3, dan 5
    3: [2, 4],        # Graf dengan node 3 memiliki 2 dan 4
    4: [3, 5, 6],     # Graf dengan node 4 memiliki 3, 5, dan 6
    5: [1, 2, 4],     # Graf dengan node 5 memiliki 1, 2, dan 4
    6: [4]            # Graf dengan node 6 memiliki 4
}

def dfs(graph, start): #mendefinisikan fungsi dfs
    visited = set()  # Set untuk melacak node-node yang telah dikunjungi

    def dfs_helper(node): # mendefinisikan fungsi dfs_helper
        visited.add(node)  # Tandai node saat ini sebagai dikunjungi
        print(node, end=" ")  # Cetak node saat ini

        for neighbor in graph[node]:  # Iterasi melalui tetangga node saat ini
            if neighbor not in visited:  # Jika tetangga belum dikunjungi
                dfs_helper(neighbor)  # Rekursi: Lanjutkan ke tetangga yang belum dikunjungi

    dfs_helper(start)  # Memulai DFS dari node awal

dfs(graph, 5)  # Panggil fungsi DFS dengan node awal 5
