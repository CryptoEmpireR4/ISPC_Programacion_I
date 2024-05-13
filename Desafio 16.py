diccionario_letras={
    "A":".—",
    "B":"—...",
    "C":"—.—.",
    "D":"—..",
    "E":".",
    "F":"..—.",
    "G":"——.",
    "H":"....",
    "I":"..",
    "J":".———",
    "K":"—.—",
    "L":".—..",
    "M":"——",
    "N":"—.",
    "O":"———",
    "P":".——.",
    "Q":"——.—",
    "R":".—.",
    "S":"...",
    "T":"—",
    "U":"..—",
    "V":"...—",
    "W":".——",
    "X":"—..—",
    "Y":"—.——",
    "Z":"——..",
    "1":".————",
    "2":"..———",
    "3":"...——",
    "4":"....—",
    "5":".....",
    "6":"—....",
    "7":"——...",
    "8":"———..",
    "9":"————.",
    "0":"—————",
    " ":"  "}
diccionario_morse={
    "_":" ",
    ".—":"A",
    "—...":"B",
    "—.—.":"C",
    "—..":"D",
    ".":"E",
    "..—.":"F",
    "——.":"G",
    "....":"H",
    "..":"I",
    ".———":"J",
    "—.—":"K",
    ".—..":"L",
    "——":"M",
    "—.":"N",
    "———":"O",
    ".——.":"P",
    "——.—":"Q",
    ".—.":"R",
    "...":"S",
    "— ":"T",
    "..—":"U",
    "...—":"V",
    ".——":"W",
    "—..—":"X",
    "—.——":"Y",
    "——..":"Z",
    ".————":"1",
    "..———":"2",
    "...——":"3",
    "....—":"4",
    ".....":"5",
    "—....":"6",
    "——...":"7",
    "———..":"8",
    "————.":"9",
    "—————":"0",
}
traduccion=[]
traducir=input("insertar palabra o frase a traductir: ")
espacio=0
espacio+=traducir.find(".")+traducir.find("—")
print(espacio)

def palabras(traducir):
    traducir=traducir.upper()
    trad_list=list(traducir)
    print(trad_list)
    for value in trad_list:
        traduccion.append(diccionario_letras[value])
    print(traduccion)

def morse(traducir):
    traducir=traducir.replace("  "," _ ")
    trad_list=traducir.split()
    print(trad_list)
    for value in trad_list:
        traduccion.append(diccionario_morse[value])
    print(traduccion)

if espacio<1:
    palabras(traducir)
else: morse(traducir)
