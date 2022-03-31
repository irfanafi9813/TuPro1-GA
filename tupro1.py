import math
import random as rd

ukuranPopulasi = 50
ukuranTurnamen = 5
generasi = 100
probC = 0.7
probM = 0.1

xmax = 5
xmin = -5
ymax = 5
ymin = -5

def kromosom(ukuranKromosom): 
# fungsi untuk membuat gen dalam sebuah kromosom bertipe interger
    arrKromosom = []
    for i in range(ukuranKromosom):
        arrKromosom.append(rd.randint(0,9))
    return arrKromosom

def populasi(ukuranPopulasi): 
# fungsi untuk membuat populasi sebanyak ukuranPopulasi (50), 
# artinya dalam 1 buah populasi terdapat 50 kromosom
    arrPopulasi = []
    for i in range(ukuranPopulasi):
        arrPopulasi.append(kromosom(10))
    return arrPopulasi

def decode(arr): 
# fungsi konversi genotype (kromosom) menjadi phenotype (individu)
    sum1 = ((arr[0] * 10**-1) + (arr[1] * 10**-2) + (arr[2] * 10**-3) + (arr[3] * 10**-4) + (arr[4] * 10**-5))
    sum2 = ((arr[5] * 10**-1) + (arr[6] * 10**-2) + (arr[7] * 10**-3) + (arr[8] * 10**-4) + (arr[9] * 10**-5))

    x = xmin + ((xmax-xmin) / (9 * (10**-1 + 10**-2 + 10**-3 + 10**-4 + 10**-5))) * sum1
    y = ymin + ((ymax-ymin) / (9 * (10**-1 + 10**-2 + 10**-3 + 10**-4 + 10**-5))) * sum2
    return [x, y]

def Fitness(arr):
# fungsi untuk mencari nilai minimum fitness dari suatu phenotype (kromosom yang sudah di decode)
    x = decode(arr)
    h = ((math.cos(x[0])+math.sin(x[1]))**2)/((x[0]**2)+(x[1]**2))
    fitness = 1/(h+0.1)
    return fitness

def parent(populasi, k, ukuranPopulasi): 
# fungsi untuk memilih orang tua dengan metode tournament selection
# mengambil sampling sebanyak k (5) dari sebuah populasi berukuran 50 kromosom
    best = []
    for i in range(1, k):
        indv = populasi[rd.randint(0, ukuranPopulasi-1)]
        if (best == [] or Fitness(indv) > Fitness(best)):
            best = indv      
    return best

def silang(p1, p2, probC): 
# fungsi untuk melakukan crossover atau pindah silang (satu titik)
    rand = rd.random()
    if (rand < probC):
        n = rd.randint(0,8)
        for i in range(n):
            p1[i], p2[i] = p2[i], p1[i]
    return p1, p2

def mutasi(p1, p2, probM): 
# fungsi untuk melakukan mutasi menggunakan metode memilih nilai secara acak
    rand = rd.random()
    if (rand < probM):
        p1[rd.randint(0,9)] = rd.randint(0,9)
        p2[rd.randint(0,9)] = rd.randint(0,9)
    return p1, p2

def indeksMaksFitness(arrFitness): 
# fungsi untuk mengetahui index dari nilai fitness terbaik digenerasi
    terbaik = max(arrFitness)
    return arrFitness.index(terbaik)

def semuaFitness(populasi, ukuranPopulasi): 
# fungsi untuk mengumpulkan nilai fitness satu populasi (50 kromosom) menjadi satu array
    arrFitness = []
    for i in range(ukuranPopulasi):
        arrFitness.append(Fitness(populasi[i]))
    return arrFitness

#main program

#membuat sebuah populasi dengan banyak 50 kromosom bertipe integer
#per kromosom terdiri dari bilangan acak antara 0-9
pop = populasi(ukuranPopulasi)

#melakukan perulangan sebanyak 100 kali (membuat 100 generasi)
for i in range(generasi):
    #membuat array yang isinya hasil konversi populasi kromosom 
    #menjadi nilai fitness pada generasi i
    ft = semuaFitness(pop, ukuranPopulasi)
    populasiBaru = []
    #index nilai fitness terbaik pada generasi i
    best = indeksMaksFitness(ft)
    #memasukkan kromosom terbaik pada array populasiBaru
    populasiBaru.append(pop[best])

    i = 0
    
    #pergantian generasi
    while (i < ukuranPopulasi-1):
        
        #seleksi orang tua menggunakan seleksi turnamen
        #sampling 5 kromosom dari 1 populasi (50 kromosom)
        p1 = parent(pop, ukuranTurnamen, ukuranPopulasi)
        p2 = parent(pop, ukuranTurnamen, ukuranPopulasi)
        
        while (p1 == p2):
            p2 = parent(pop, ukuranTurnamen, ukuranPopulasi)
        
        anak = silang(p1, p2, probC)
        anak = mutasi(anak[0], anak[1], probM)
        populasiBaru += anak
        i += 1
        
    pop = populasiBaru
    
ft = semuaFitness(pop, ukuranPopulasi)
hasil = indeksMaksFitness(ft)
xHasil = decode(pop[hasil])

#output
print('Kromosom terbaik: ', pop[hasil])
print('Fitness: ', Fitness(pop[hasil]))
print('Nilai x dan y hasil dekode')
print('     x:', xHasil[0])
print('     y:', xHasil[1])