#needs only Python, nothing to install EXCEPT WINGET (winget install -e --id Python.Python.3.12)
 
import hashlib
import math
import secrets
import string
import threading
import tkinter as tk
import urllib.request
 
COMMON = {
    "password", "123456", "123456789", "12345678", "12345", "qwerty", "abc123",
    "password1", "111111", "iloveyou", "admin", "welcome", "monkey", "dragon",
    "letmein", "login", "football", "baseball", "master", "sunshine",
    "princess", "qwerty123", "1q2w3e4r", "passw0rd", "trustno1", "superman",
    "batman", "shadow", "000000", "123123", "654321", "zaq12wsx",
}
LEET = str.maketrans({"0": "o", "1": "l", "3": "e", "4": "a", "5": "s",
                      "7": "t", "@": "a", "$": "s", "!": "i"})
SEQUENCES = ["abcdefghijklmnopqrstuvwxyz", "0123456789",
             "qwertyuiop", "asdfghjkl", "zxcvbnm"]
SYMBOLS = "!@#$%^&*-_+=?"
 
 
_WORD_TEXT = """
# general / common password words
love lovely hello welcome admin user login master secret super letmein access open
sesame trust forever always never maybe whatever nothing everything something
freedom liberty victory winner champion legend hero lucky happy angel heart sweet
baby honey darling sweetheart iloveyou loveyou magic power rocket diamond thunder
storm money dollar million rich house home music guitar piano dance school college
university student flower garden coffee chocolate cookie cookies pizza burger
pepper ginger banana apple orange cherry lemon mango peach grape sugar candy cake
horse battery staple correct qwerty asdf zxcv welcome1 passwd shadow sunshine
princess prince queen king knight warrior soldier captain doctor teacher buddy
mother father sister brother daddy mommy family friend friends
 
# animals / colors / nature
tiger panda eagle shark whale dolphin rabbit turtle bear puppy kitten snake spider
monkey donkey zebra giraffe elephant penguin parrot phoenix cobra viper falcon
panther cheetah leopard jaguar gorilla camel lion dragon wolf
black white green blue red pink purple brown yellow silver golden crimson
sunset sunrise rainbow cloud moon moonlight midnight star stars earth fire water
wind snow rain lightning tornado volcano desert beach island ocean river mountain
forest planet galaxy matrix summer winter spring autumn
 
# sports / games / hobbies
football soccer cricket tennis golf rugby boxing karate racing hockey baseball
basketball swimming cycling running gamer gaming game games player minecraft
fortnite roblox pokemon valorant zelda mario sonic pikachu barcelona realmadrid
chelsea arsenal liverpool united ronaldo messi neymar mbappe haaland salah
batman superman spiderman ironman avenger starwars naruto goku dragonball harry
potter hogwarts hunter killer ninja wizard
 
# tech
administrator root username logon password secure security private public system
server network internet online wifi router modem computer laptop mobile phone
linux ubuntu kali github python java coding code hacker hacking hack cyber crypto
bitcoin ethereum blockchain firewall default guest test testing temp temporary
changeme
 
# months / days / holidays
january february march april june july august september october november december
monday tuesday wednesday thursday friday saturday sunday holiday birthday
christmas ramadan eid
 
#NAMES: English / Western
james john robert michael william david richard joseph thomas charles christopher
daniel matthew anthony mark donald steven paul andrew joshua kenneth kevin brian
george timothy ronald edward jason jeffrey ryan jacob gary nicholas eric jonathan
stephen larry justin scott brandon benjamin samuel gregory alexander frank patrick
raymond jack dennis jerry tyler aaron jose adam nathan henry douglas zachary peter
kyle walter ethan jeremy harold keith christian roger noah gerald carl terry sean
austin arthur lawrence jesse dylan bryan billy bruce albert willie gabriel logan
alan juan wayne ralph randy eugene vincent russell elijah louis bobby philip
johnny bradley liam mason oliver lucas jayden aiden carter owen caleb connor isaac
landon wyatt luke jaxon gavin evan cooper blake colton cole chase tristan ian
adrian jordan charlie dallas harry jamie jonny tommy danny kenny jimmy timmy
mary patricia jennifer linda elizabeth barbara susan jessica sarah karen lisa nancy
betty margaret sandra ashley kimberly emily donna michelle dorothy carol amanda
melissa deborah stephanie rebecca sharon laura cynthia kathleen amy angela shirley
anna brenda pamela emma nicole helen samantha katherine christine debra rachel
carolyn janet catherine maria heather diane olivia julie joyce victoria kelly
christina lauren joan evelyn judith megan cheryl andrea hannah martha jacqueline
frances gloria teresa kathryn sara janice jean alice madison doris abigail julia
judy grace denise amber marilyn beverly danielle theresa sophia marie diana
brittany natalie isabella charlotte rose alexis kayla chloe zoey lily ella harper
scarlett aria layla riley nora zoe hazel violet aurora savannah audrey brooklyn
bella claire skylar lucy paisley everly caroline nova genesis emilia kennedy maya
willow kinsley naomi aaliyah elena ariana allison gabriella madelyn cora ruby
serenity adeline hailey gianna valentina isla eliana quinn nevaeh sadie piper
lydia alexa josephine emery delilah arianna vivian kaylee sophie brielle madeline
jenny jessie katie lizzie molly nikki sally stacy tiffany vanessa wendy
 
#NAMES: Arabic
muhammad mohammed mohammad mohamed ahmed ahmad abdullah abdulla abdulrahman
abdulaziz abdulmajid ibrahim ismail ismael yusuf yousef youssef yaqub yahya
zakaria idris musa harun dawood suleiman sulaiman omar umar uthman othman hassan
hasan hussein hussain husain hamza khalid khaled walid waleed tariq tarek tareq
bilal salman salmaan sultan saeed saleh salih rashid rashed majid maged mansour
mansoor nasser nasir naser faisal fahad fahd faris fares jaber jabir hamad hamed
hamdan mubarak mazen marwan mustafa moustafa nabil nader nadir osama usama rayan
rayyan rami ramy samir sameer sami sharif shareef talal tamim taher tahir tawfiq
wael yasser yasir zayed zaid zayd zaki ziad zuhair abbas anwar adnan ammar amir
ameer amin anas ayman azzam badr basil bassam bashir daniyal danish fadi fawaz
ghazi habib hadi hakim hamid haroon haitham hisham huzaifa imran iyad jamal jawad
kamal karim kareem labib latif luay mahdi mahmoud mahmood maher malik mohsin
mounir muaz moaz mujahid munir murad nawaf nizar noor numan qasim rabee rafiq
rahman rahim raed raja ramadan rida ridwan sadiq safwan salim shadi shihab suhail
taha talha thamer usman wasim yamin younis zahir fatima fatema fatimah aisha ayesha aishah maryam mariam maryum khadija khadijah
zainab zaynab zeinab hana hanan hanaa huda hoda layla laila leila lina leena nour
noura nouf nada nadia nadiyah rana rania ranya reem reema rima salma salwa samar
samia sana sanaa sumaya sumayyah safiya safiyah shaikha shamma shamsa meera mona
muna manal maha mahira mayar najwa nawal nisreen nusaiba rahma raghad rawan rasha
reham rukaya ruqayya sabah sabrina sahar sajida shahd shahad shaima suad suha
sundus tala tamara tasneem walaa warda widad yasmin yasmeen yara zahra zahraa
zubaida zeina dalal dana dina dima ebtisam eman esraa fadwa fajr farah farida
fawzia ghada ghaida haifa hajar halima hessa hind iman inas jamila jumana kawther
kholoud lamia lamya lubna lujain
 
#NAMES: Indian
aarav aryan arjun rohan rahul rohit vikram vijay amit ankit anil ajay akash aditya
abhishek deepak dinesh gaurav harish hemant jatin kunal manish mohit nikhil nitin
pankaj pradeep prakash pranav rajesh rakesh ramesh ravi sachin sanjay sandeep
santosh sumit sunil suresh tarun umesh varun vikas vinay vishal yash krishna
kiran kumar singh sharma gupta patel shah mehta joshi nair menon reddy naidu iyer
rao verma yadav mishra pandey tiwari kapoor khanna malhotra bhatia
priya pooja puja neha anjali divya kavya kavita sneha shreya shruti swati sunita
sushma radha rani rekha ritu sapna seema shilpa sonia sonam tanvi usha vandana
varsha asha anita deepa gita geeta jyoti komal lakshmi meena nisha payal preeti
ananya aditi aishwarya
zeeshan faizan farhan junaid kamran khurram sajid shahid waqas asif adeel haider
irfan zain
 
#NAMES: Latin / European / Asian 
miguel carlos antonio manuel pedro luis diego mateo santiago fernando ricardo
rafael pablo jorge sergio alejandro carmen lucia sofia isabel paula marta
ivan sergey dmitri vladimir alexei olga natasha tatiana svetlana yuri nikolai
pierre jacques marc antoine francois giovanni marco luca matteo giulia francesca
chiara klaus stefan jurgen wolfgang
chen wang zhang ming hiroshi takeshi kenji yuki sakura akira haruto sora
pierre jacques jean-luc louis henri philippe laurent nicolas julien thierry
sebastien maxime alexandre mathieu guillaume romain clement florian baptiste
etienne gaspard hugo leo lucien remi theo victor xavier yannick bastien cedric
claude denis didier fabien francois gerard jerome olivier thibault valentin
marie camille juliette margaux oceane manon chloe lea emilie amelie aurelie
brigitte celine charlotte clemence colette delphine elodie estelle eugenie
fabienne genevieve helene isabelle jacqueline josephine laetitia lucie madeleine
martine mathilde monique nathalie ophelie pauline sabine solange sylvie
valerie vanessa veronique yvette yvonne
hans klaus stefan jurgen wolfgang dieter gunter helmut karl heinz werner uwe
jorg jens lars mats nils olaf sven thorsten tobias lukas felix florian maximilian
matthias moritz markus michael niklas rainer rolf ulrich bernd detlef dirk
erik gustav gunnar henrik johan johannes magnus mikael oskar rasmus soren
anders bjorn leif ragnar torsten stellan viktor
anke birgit brigitte claudia gisela greta gudrun heike helga ingrid jutta
karin katja katrin kirsten lena marlene petra renate sabine sandra silke
sigrid sonja susanne ulrike ursula
giovanni marco luca matteo alessandro andrea antonio carlo claudio davide
domenico enrico enzo fabio federico filippo francesco gabriele giorgio
giuseppe guido lorenzo luigi massimo mauro nicola paolo pietro riccardo
roberto salvatore sergio simone stefano tommaso umberto valerio vincenzo
giulia francesca chiara alessia alessandra angela anna bianca carla caterina
cristina elisa elena federica gabriella gianna giorgia ilaria lorenza lucia
paola roberta serena silvia simona valentina
alejandro alvaro andres angel carlos cristian daniel diego eduardo emilio
enrique ernesto esteban fabian felipe fernando francisco gabriel gonzalo
guillermo gustavo hector ignacio javier joaquin jorge jose juan julio leonardo
lorenzo manuel marcos mario mateo miguel nicolas oscar pablo pedro rafael
ramon raul ricardo roberto rodrigo ruben santiago sergio tomas vicente xavier
alicia beatriz blanca carolina catalina claudia consuelo cristina dolores
elena esperanza eva gabriela guadalupe ines irene isabel lourdes lucia luisa
marisol marta monica natalia noelia paloma patricia pilar rocio rosario
sandra silvia sofia teresa valeria veronica
joao tiago bruno rui nuno goncalo hugo diogo andre filipe fabio paulo duarte
ana beatriz catarina filipa joana leonor margarida mariana marta sara
ivan sergey sergei dmitri dmitry vladimir alexei alexey andrei andrey boris
igor oleg pavel mikhail nikolai konstantin maxim anton artem denis evgeny
gleb grigory kirill leonid lev matvey nikita roman stanislav timur viktor
vitaly vasily yaroslav yuri bogdan dragan goran jovan marko milan milos
nikola nenad petar stefan vladimir zoran aleksandar damir darko luka tomislav
jan jakub tomasz piotr pawel marek krzysztof andrzej wojciech lukasz michal
mateusz adam zbigniew janusz kamil dawid
olga natasha natalia tatiana svetlana anastasia ekaterina elena galina irina
katya larisa ludmila marina nadia nina oksana polina sasha sofia tamara
valentina vera victoria yulia zoya agnieszka anna barbara beata dorota ewa
iwona joanna magdalena malgorzata monika natalia paulina zofia ana jelena
milica marija sanja tatjana vesna
patrick sean liam conor connor declan eamon finn fergus kieran niall oisin
padraig ronan seamus colm cillian donal rory angus callum duncan fraser
gordon hamish ewan murray alasdair iain dougal rhys owen gareth emrys dylan
aoife ciara siobhan niamh saoirse roisin orla maeve sinead eilidh fiona
morag kirsty isla catriona ailsa bronwen carys cerys megan seren
nikos giorgos dimitris yannis kostas panagiotis christos stavros alexandros
vasilis thanos spyros manolis petros andreas theodoros apostolos
maria eleni katerina sofia georgia anna despina ioanna christina vasiliki
dimitra angeliki konstantina
mehmet mustafa ahmet ali huseyin hasan ibrahim ismail yusuf emre burak
serkan murat ozan cem kemal volkan baris tolga
ayse fatma emine hatice zeynep elif merve selin esra gamze burcu derya
"""
WORDS = {
    word
    for line in _WORD_TEXT.splitlines()
    if not line.strip().startswith("#")
    for word in line.split()
}
WORDS_BY_LENGTH = sorted((w for w in WORDS if len(w) >= 4), key=len, reverse=True)
 
RATINGS = [
    (28, "Very weak", "#c0392b"),
    (36, "Weak", "#e67e22"),
    (60, "Fair", "#d4ac0d"),
    (80, "Strong", "#27ae60"),
    (10**9, "Very strong", "#1e8449"),
]
 
 
def has_repeats(pw, run=3):
    count = 1
    for a, b in zip(pw, pw[1:]):
        count = count + 1 if a == b else 1
        if count >= run:
            return True
    return False
 
 
def has_sequence(pw, size=3):
    low = pw.lower()
    for seq in SEQUENCES:
        for s in (seq, seq[::-1]):
            for i in range(len(s) - size + 1):
                if s[i:i + size] in low:
                    return True
    return False
 
 
def find_words(pw):
    """Common words hidden in the password (also catches p@ssw0rd-style swaps)."""
    s = pw.lower().translate(LEET)
    found = []
    for w in WORDS_BY_LENGTH:
        while w in s:
            found.append(w)
            s = s.replace(w, "#" * len(w), 1)
    return found
 
def is_common(pw):
    return pw.lower() in COMMON or pw.lower().translate(LEET) in COMMON
 
 
def pool_size(pw):
    pool = 0
    if any(c.islower() for c in pw):
        pool += 26
    if any(c.isupper() for c in pw):
        pool += 26
    if any(c.isdigit() for c in pw):
        pool += 10
    if any(c in string.punctuation for c in pw):
        pool += 32
    if any(ord(c) > 127 for c in pw):
        pool += 100
    return pool
 
 
def crack_time(entropy):
    """Average time to guess, assuming 10 billion guesses/second (offline attack)."""
    if entropy <= 0:
        return "instantly"
    if entropy > 120:
        return "longer than the age of the universe"
    seconds = (2 ** (entropy - 1)) / 1e10
    units = [("second", 60), ("minute", 60), ("hour", 24), ("day", 365),
             ("year", 1000), ("thousand years", 1000), ("million years", 1000),
             ("billion years", 1000)]
    if seconds < 1:
        return "instantly"
    value = seconds
    for name, step in units:
        if value < step:
            n = int(value)
            if name in ("second", "minute", "hour", "day", "year"):
                return f"{n} {name}{'s' if n != 1 else ''}"
            return f"{n} {name}"
        value /= step
    return "trillions of years"
 
 
def analyze(pw):
    checks = [
        ("At least 12 characters", len(pw) >= 12),
        ("Has an uppercase letter", any(c.isupper() for c in pw)),
        ("Has a lowercase letter", any(c.islower() for c in pw)),
        ("Has a number", any(c.isdigit() for c in pw)),
        ("Has a symbol (! @ # ...)", any(not c.isalnum() for c in pw)),
        ("Not a common password", bool(pw) and not is_common(pw)),
        ("No sequences (abc, 123, qwe)", bool(pw) and not has_sequence(pw)),
        ("No repeated characters (aaa)", bool(pw) and not has_repeats(pw)),
        ("No common words (love, dragon...)", bool(pw) and not find_words(pw)),
    ]
    if not pw:
        return {"entropy": 0, "label": "Type a password", "color": "#888888",
                "fraction": 0, "crack": "-", "checks": checks}
 
    raw = len(pw) * math.log2(max(pool_size(pw), 2))
    penalty = 0.0
    if is_common(pw):
        penalty += raw
    if has_repeats(pw):
        penalty += raw * 0.15
    if has_sequence(pw):
        penalty += raw * 0.20
    if len(set(pw)) <= len(pw) // 2:
        penalty += raw * 0.10
    per_char = math.log2(max(pool_size(pw), 2))
    for w in find_words(pw):
        penalty += max(0.0, len(w) * per_char - 12)
    entropy = max(0.0, raw - penalty)
 
    for limit, label, color in RATINGS:
        if entropy < limit:
            break
    return {"entropy": entropy, "label": label, "color": color,
            "fraction": min(entropy / 100, 1), "crack": crack_time(entropy),
            "checks": checks}
 
 
def check_breach(pw):
    """Returns breach count, 0 if clean, None if offline.
    Only the first 5 characters of the SHA-1 hash are sent (k-anonymity)."""
    sha1 = hashlib.sha1(pw.encode()).hexdigest().upper()
    start, rest = sha1[:5], sha1[5:]
    req = urllib.request.Request(
        "https://api.pwnedpasswords.com/range/" + start,
        headers={"Add-Padding": "true", "User-Agent": "keep-your-self-safe"})
    try:
        data = urllib.request.urlopen(req, timeout=8).read().decode()
    except Exception:
        return None
    for line in data.splitlines():
        tail, _, count = line.partition(":")
        if tail.strip() == rest:
            return int(count.strip() or 0)
    return 0
 
 
def generate(length):
    pools = [string.ascii_lowercase, string.ascii_uppercase, string.digits, SYMBOLS]
    chars = [secrets.choice(p) for p in pools]
    everything = "".join(pools)
    chars += [secrets.choice(everything) for _ in range(length - len(chars))]
    secrets.SystemRandom().shuffle(chars)
    pw = "".join(chars)
    if find_words(pw) or has_sequence(pw) or has_repeats(pw):
        return generate(length) 
    return pw
 
BG = "#f5f6fa"
root = tk.Tk()
root.title("Keep Your Self Safe")
root.geometry("460x730")
root.configure(bg=BG)
root.resizable(False, False)
 
tk.Label(root, text="Keep Your Self Safe", font=("Arial", 18, "bold"),
         bg=BG).pack(pady=(16, 6))
 
# --- input row
pw_var = tk.StringVar()
entry = tk.Entry(root, textvariable=pw_var, width=30, font=("Consolas", 13),
                 show="*", relief="solid", bd=1)
entry.pack(pady=(14, 4), ipady=4)
entry.focus()
 
show_var = tk.BooleanVar(value=False)
tk.Checkbutton(root, text="Show password", variable=show_var, bg=BG,
               command=lambda: entry.config(show="" if show_var.get() else "*")
               ).pack()
 
# --- strength meter
meter = tk.Canvas(root, width=380, height=14, bg="#dcdde1", highlightthickness=0)
meter.pack(pady=(12, 4))
bar = meter.create_rectangle(0, 0, 0, 14, fill="#888888", width=0)
 
strength_label = tk.Label(root, text="", font=("Arial", 15, "bold"), bg=BG)
strength_label.pack()
detail_label = tk.Label(root, text="", font=("Arial", 10), fg="#555555", bg=BG)
detail_label.pack(pady=(0, 6))
 
# --- checklist
box = tk.LabelFrame(root, text=" Requirements ", bg=BG, font=("Arial", 10))
box.pack(padx=24, fill="x")
check_labels = []
for _ in range(9):
    lab = tk.Label(box, text="", anchor="w", font=("Arial", 10), bg=BG)
    lab.pack(fill="x", padx=10)
    check_labels.append(lab)
 
# --- breach check
breach_label = tk.Label(root, text="", font=("Arial", 11, "bold"),
                        bg=BG, wraplength=400)
breach_btn = tk.Button(root, text="Check if leaked online", font=("Arial", 11),
                       command=lambda: start_breach_check())
breach_btn.pack(pady=(14, 4))
breach_label.pack()
 
# --- generator
gen = tk.LabelFrame(root, text=" Password generator ", bg=BG, font=("Arial", 10))
gen.pack(padx=24, pady=(12, 0), fill="x")
length_var = tk.IntVar(value=16)
row = tk.Frame(gen, bg=BG)
row.pack(fill="x", padx=10, pady=(6, 0))
tk.Label(row, text="Length:", bg=BG).pack(side="left")
tk.Scale(row, from_=12, to=32, orient="horizontal", variable=length_var,
         bg=BG, highlightthickness=0, length=250).pack(side="left", padx=8)
btns = tk.Frame(gen, bg=BG)
btns.pack(pady=8)
status_label = tk.Label(gen, text="", fg="#1e8449", bg=BG)
 
 
def on_generate():
    pw_var.set(generate(length_var.get()))
    show_var.set(True)
    entry.config(show="")
    status_label.config(text="")
 
 
def on_copy():
    pw = pw_var.get()
    if not pw:
        return
    root.clipboard_clear()
    root.clipboard_append(pw)
    status_label.config(text="Copied to clipboard!")
    root.after(2000, lambda: status_label.config(text=""))
 
 
tk.Button(btns, text="Generate", width=12, command=on_generate).pack(side="left", padx=5)
tk.Button(btns, text="Copy", width=12, command=on_copy).pack(side="left", padx=5)
status_label.pack(pady=(0, 6))
 
 
tk.Label(root, text="Strength is an estimate, not a guarantee. Use unique passwords + a password manager.",
         font=("Arial", 8), fg="#888888", bg=BG, wraplength=400).pack(pady=(10, 0))
 
 
# --- live update
def refresh(*_):
    pw = pw_var.get()
    r = analyze(pw)
    meter.coords(bar, 0, 0, 380 * r["fraction"], 14)
    meter.itemconfig(bar, fill=r["color"])
    strength_label.config(text=r["label"], fg=r["color"])
    if pw:
        detail_label.config(
            text=f"~{r['entropy']:.0f} bits  |  Time to crack: {r['crack']}")
    else:
        detail_label.config(text="")
    for lab, (text, ok) in zip(check_labels, r["checks"]):
        lab.config(text=("\u2714  " if ok else "\u2718  ") + text,
                   fg="#1e8449" if ok else "#c0392b")
    breach_label.config(text="") 
 
result = {}
 
 
def worker(pw):
    result["count"] = check_breach(pw)
    result["done"] = True
 
def poll():
    if result.get("done"):
        c = result["count"]
        if c is None:
            breach_label.config(text="Could not check (no internet)", fg="#555555")
        elif c == 0:
            breach_label.config(text="Not found in known leaks", fg="#1e8449")
        else:
            breach_label.config(text=f"FOUND in {c:,} leaks. Do not use it!",
                                fg="#c0392b")
        breach_btn.config(state="normal")
    else:
        root.after(100, poll)
 
def start_breach_check():
    pw = pw_var.get()
    if not pw:
        breach_label.config(text="Type a password first", fg="#555555")
        return
    breach_label.config(text="Checking...", fg="#555555")
    breach_btn.config(state="disabled")
    result.clear()
    threading.Thread(target=worker, args=(pw,), daemon=True).start()
    poll()
 
 
pw_var.trace_add("write", refresh)
refresh()
root.mainloop()
 
