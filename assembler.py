opcode = {
    "nope":"0000",
    "add":"0001",
    "sub":"0010",
    "addi":"0011",
    "jump":"0100",
    "gosub":"0101",
    "return":"0110",
    "loadi":"0111",
    "load":"1000",
    "storei":"1001",
    "store":"1010",
    "ass":"1011",
    "screen":"1100"
}
jumpCondition = {
    "np"	:	"0000"	,
    "=="	:	"0001"	,
    "<"	:	"0010"	,
    ">"	:	"0011"	,
    "!="	:	"0100"	,
    ">="	:	"0101"	,
    "<="	:	"0110"	,
    "sf1"	:	"0111"	,
    "sf2"	:	"1000"	,
    "sf3"	:	"1001"	,
    "sf4"	:	"1010"	,
}



hex = {
        "0000"	:	"0"	,
        "0001"	:	"1"	,
        "0010"	:	"2"	,
        "0011"	:	"3"	,
        "0100"	:	"4"	,
        "0101"	:	"5"	,
        "0110"	:	"6"	,
        "0111"	:	"7"	,
        "1000"	:	"8"	,
        "1001"	:	"9"	,
        "1010"	:	"a"	,
        "1011"	:	"b"	,
        "1100"	:	"c"	,
        "1101"	:	"d"	,
        "1110"	:	"e"	,
        "1111"	:	"f"	,
}


def dec2Bin(dec,dim):
    out=""
    flag = dec<0
    while dec != 0:
        out = str(dec % 2) + out
        dec = int(dec/2)
    outlen=len(out)
    if outlen<dim:
        app = out
        dif = dim - outlen
        i = 0
        while(i<dif):
            out=out[0:i]+"0"
            i+=1
        out = out[0:i]+app
            
    if flag:
        out = compl2(out)
    return out

def compl(str):
    out = ""
    for s in range(len(str)):
        if str[s] == "0":
            out += "1"
        elif str[s] == "1":
            out += "0"
    return(out)
            
def compl2(str):
    str1 = compl(str)
    out =str1
    i =len(str1)-1
    if str1[i] == "0":
        out = out[0:i]+"1"
    else:
        j="1"
        while i>=0 and j != "0":
            i-=1
            j= str1[i]
        
        out = out[0:i]+"1"
        for k in range(len(str1)-i-1):
            out = out[0:i+k+1]+"0"
    return(out)

def bin2Hex(str):
    out = ""
    for i in range(int(len(str)/4)):
        out += hex[str[i*4:i*4+4]]
    return out





def spaziEcostanti():
    text =""
    line = fin.read().split("\n")
    for linea in line:
        f = "" 
        parole = linea.split()
        if len(parole)>0:
                
            for parola in parole:
                if f!="":
                    constant[f]=parola
                elif "#" in parola: f=parola.replace("#","")
                elif parola!= "":
                    text+=parola+" "
                    
            if f=="":text+="\n"

    for cst in constant:
        text = text.replace(cst,constant[cst])
    return text

#line = text.split("\n")

def findTag():
    text=""
    testo = spaziEcostanti()
    line = testo.split("\n")
    daCanc = []
    for i in range(len(line)):
        if line[i].startswith(":"):
            tags[line[i].replace(":","").replace(" ","")] = i-len(tags)
            daCanc.append(i)
    for i in range(len(daCanc)-1,-1,-1):
        line.pop(daCanc[i])
    return line
def replaceTag():
    text=""
    
    line = findTag()
    for linea in line:
        parole = linea.split()
        if len(parole)>0:
            for parola in parole:
                if parola in tags:
                    text+=str(dec2Bin(tags[parola],8))+" "
                else:
                    text+=parola+" "
            text+="\n"
    return text

def textToBin():
    testo = replaceTag()
    istruzioni = []
    line = testo.split("\n")
    for linea in line:
        istr = ""
        parole = linea.split()
        i=0
        if len(parole)>0:
            for parola in parole:
                if parola in opcode:
                    print("opcode: ",opcode[parola])
                    istr = opcode[parola] + istr
                elif parola in jumpCondition:
                    print("condizione: ",jumpCondition[parola])
                    istr = jumpCondition[parola] + istr
                elif parola.startswith("a"):
                    print("reg: ",dec2Bin(int(parola.replace("a","")),4))
                    istr = dec2Bin(int(parola.replace("a","")),4) + istr
                elif parola.startswith("[") and parola.endswith("]"):
                    di = 4
                    if i>2: di=4
                    else:   di=8

                    print("imm: ",dec2Bin((int(parola.replace("[","").replace("]",""))),8))
                    istr = dec2Bin(int(parola.replace("[","").replace("]","")),di)+ istr
                else:
                    istr = parola+istr
                i+=1
        if len(istr)<16:
            for i in range(16-len(istr)):
                istr= "0"+istr
        print("istruzione: "+istr)
        istruzioni.append(istr)
    return(istruzioni)

def outFile():
    istruzioni = textToBin()
    testo = "v3.0 hex words addressed"
    cont = 0
    for i in range(len(istruzioni)):
        if i%16 == 0:
            testo+="\n" + bin2Hex(dec2Bin(i,8))+":"
            cont+=1
        testo+=" "+bin2Hex(istruzioni[i])
    print(testo)
    return testo

#####################################
# -valori assoluti tra []           #
# -valori binari 101                #
# -registri preceduti da a          #
# -tag preceduti da :               #
# -costanti formula #len = 3        #
# -per usare costante [len] o alen  #
#####################################


constant={"zero":"a0"}
tags={}
inputName = input("inserisci nome file\n")
fin =open(inputName+".txt","r")
saveName = input("inserisci nome salvataggio\n")
fout = open(saveName+".txt","w")
fout.write(outFile())
fout.close()
fin.close()



