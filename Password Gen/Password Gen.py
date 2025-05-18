import random
import hashlib
import pyfiglet
import time


def print_banner():
    ascii_banner = pyfiglet.figlet_format("PASSWORD GEN")
    print(ascii_banner)
    print("Created by Emir".center(80))
    print("="*80)

wordlist = [
    "zephyr", "quokka", "nautilus", "bonsai", "jigsaw", "havoc", "glyph", "kismet",
    "labyrinth", "mosaic", "nimbus", "obelisk", "pangolin", "quasar", "rune",
    "sphinx", "talisman", "umber", "wraith", "xenon", "yarrow", "zeppelin",
    "echelon", "fjord", "gossamer", "halcyon", "icarus", "jubilee", "kaleidoscope"


]

leet_map = {'a':'4', 'e':'3', 'i':'1', 'o':'0', 's':'5', 't':'7'}

def leet_random(word):
    result = ""
    for c in word:
        if c.lower() in leet_map and random.random() < 0.5:  # %50 şansıyla leet yap
            result += leet_map[c.lower()]
        else:
            result += c
    return result

def get_seed(site_name):
    h = hashlib.md5(site_name.encode()).hexdigest()
    seed = int(h[:8], 16)
    return seed

def generate_password(site_name, length=12, special_chars="!@#$%^&*"):
    seed = get_seed(site_name)
    random.seed()
    
    word_count = random.choice([2,3])
    chosen_words = random.sample(wordlist, word_count)
    
    processed_words = []
    for w in chosen_words:
        w = w.capitalize()
        w = leet_random(w)
        processed_words.append(w)
    
    site_chars = ''.join(random.sample(site_name, min(3, len(site_name))))
    
    parts = []
    site_inserted = False
    
    for i, w in enumerate(processed_words):
        parts.append(w)
        if i < len(processed_words) - 1:
            if not site_inserted and random.random() < 0.7:
                parts.append(random.choice(special_chars))
                parts.append(site_chars)
                parts.append(random.choice(special_chars))
                site_inserted = True
            else:
                parts.append(random.choice(special_chars))
    
    if not site_inserted:
        parts.append(random.choice(special_chars))
        parts.append(site_chars)
        parts.append(random.choice(special_chars))
    
    number = str(random.randint(10, 99))
    
    password = ''.join(parts) + number
    
    if len(password) > length:
        password = password[:length]
    else:
        while len(password) < length:
            password += random.choice(special_chars + "0123456789")
    
    return password

def main():
    print_banner()
    time.sleep(1)
    site = input("🔹 Şifre üretilecek site/adı yaz: ")
    length = int(input("🔹 Şifre uzunluğu (en az 10): "))
    special = input("🔹 Özel karakterler (varsayılan !@#$%^&*): ")
    if not special:
        special = "!@#$%^&*"
    
    print("\n🔑 İşte 3 önerilen şifren:\n")
    for _ in range(3):
        print("→", generate_password(site, length, special))

if __name__ == "__main__":
    main()
    input("\nÇıkmak için Enter’a bas...")
