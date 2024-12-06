def game_labirin():
    print("Selamat datang di game Labirin!")
    print("Tugas lu adalah menemukan jalan keluar (E).")
    print("Pakai perintah 'w' (naik), 's' (turun), 'a' (kiri), 'd' (kanan) untuk bergerak.\n")

    # Peta labirin
    labirin = [
        ["#", "#", "#", "#", "#"],
        ["#", " ", " ", " ", "#"],
        ["#", " ", "#", " ", "#"],
        ["#", " ", "#", "E", "#"],
        ["#", "#", "#", "#", "#"],
    ]

    # Posisi awal pemain
    posisi_pemain = [1, 1]

    def tampilkan_labirin():
        for i, baris in enumerate(labirin):
            for j, kolom in enumerate(baris):
                if [i, j] == posisi_pemain:
                    print("P", end=" ")  # P untuk pemain
                else:
                    print(kolom, end=" ")
            print()

    while True:
        tampilkan_labirin()
        gerakan = input("Gerakan lu (w/a/s/d): ").lower()

        if gerakan not in ["w", "a", "s", "d"]:
            print("Input salah, coba lagi!")
            continue

        # Hitung posisi baru
        x, y = posisi_pemain
        if gerakan == "w":
            x -= 1
        elif gerakan == "s":
            x += 1
        elif gerakan == "a":
            y -= 1
        elif gerakan == "d":
            y += 1

        # Cek apakah gerakan valid
        if labirin[x][y] == "#":
            print("Bentur tembok, cok!")
        else:
            posisi_pemain = [x, y]

        # Cek apakah sudah sampai tujuan
        if labirin[x][y] == "E":
            print("Selamat, lu berhasil keluar dari labirin!")
            break

game_labirin()
