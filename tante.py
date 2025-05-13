import sys
import time

def run_lyric():
    lyric = [
        ("Sudah biasa terjadi tante...", 0.1),
        ("Teman datang ketika lagi butuh saja...", 0.11),
        ("Coba kalau lagi susah...", 0.11),
        ("Mereka semua menghilaaaaannnngggg...", 0.05),
        ("Apakah spek standar seperti ini yang para pemirsa inginkan?...", 0.07),
        ("Tanteeeeeeeee...", 0.08),
    ]
    
    delay = [0.3, 0.3, 0.4, 0.3, 0.5, 0.3, 0.4] 
    print("\n~~Tante culik aku dong~~")
    time.sleep(1)

    for i, (line_song, delay_character) in enumerate(lyric):
        for char in line_song:
            print(char, end='')
            sys.stdout.flush()
            time.sleep(delay_character)
        time.sleep(delay[i % len(delay)])
        print('')

run_lyric()
