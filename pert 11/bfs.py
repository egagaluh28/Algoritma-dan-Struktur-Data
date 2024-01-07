graph = {
    '1': set(['2', '5']),       # Graf dengan node '1' memiliki '2' dan '5'
    '2': set(['1', '3', '5']),  # Graf dengan node '2' memiliki '1', '3', dan '5'
    '3': set(['2', '4']),       # Graf dengan node '3' memiliki '2' dan '4'
    '4': set(['3', '5', '6']),  # Graf dengan node '4' memiliki '3', '5', dan '6'
    '5': set(['1', '2', '4']),  # Graf dengan node '5' memiliki '1', '2', dan '4'
    '6': set(['4'])             # Graf dengan node '6' memiliki '4'
}
def bfs_terdekat(graph, mulai, tujuan): # Mendefiniskan fungsi bfs_terdekat
    explored = []      # Daftar node yang telah dikunjungi
    queue = [[mulai]]  # Antrian jalur yang akan dijelajahi

    if mulai == tujuan:
        return "Awal adalah tujuan" # Jika node awal dan tujuan sama, langsung kembalikan pesan ini

    while queue: 
        jalur = queue.pop(0)  # Ambil jalur pertama dari antrian
        node = jalur[-1]      # Ambil node terakhir dalam jalur

        if node not in explored: # jika node tidak explored
            neighbours = graph[node]  # neighbour node saat ini
            for neighbour in neighbours: 
                jalur_baru = list(jalur)  # jalur saat = list jalur saat ini
                jalur_baru.append(neighbour)  # Tambahkan neighbour ke jalur baru
                queue.append(jalur_baru)  # Tambahkan jalur baru ke antrian

                if neighbour == tujuan:  # Jika neighbour adalah tujuan
                    return jalur_baru  # Kembalikan jalur baru

            explored.append(node)  # node telah yang dikunjungi

    return "Node tujuan tidak dapat dicapai" # Jika tidak ada jalur yang mencapai tujuan, kembalikan pesan ini

mulai = input("Masukkan node awal: ")  # Input node awal dari pengguna
tujuan = input("Masukkan node tujuan: ")  # Input node tujuan dari pengguna
print(bfs_terdekat(graph, mulai, tujuan))  # Panggil fungsi bfs_terdekat dengan graf, node awal, dan node tujuan
