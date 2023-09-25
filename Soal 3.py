a = int(input())

#kondisi 1
pecahan_5 = a // 5000
kondisi_1 = a - pecahan_5 * 5000
if kondisi_1 != 0 :
    pecahan_2 = kondisi_1 // 2000
    kondisi_1 = kondisi_1 - pecahan_2 * 2000
    if kondisi_1 != 0 :
        pecahan_1 = kondisi_1 // 1000
        print("pecahan 5000 = " + str(pecahan_5), "pecahan 2000 = " + str(pecahan_2), "pecahan 1000 = " + str(pecahan_1))
    else:
        print("pecahan 5000 = " + str(pecahan_5), "pecahan 2000 = " + str(pecahan_2), "pecahan 1000 = 0")
else:
    print("pecahan 5000 = " + str(pecahan_5), "pecahan 2000 = 0", "pecahan 1000 = 0")

#kondisi 2
pecahan_2 = a // 2000
kondisi_2 = a - pecahan_2 * 2000
if kondisi_2 != 0 :
    pecahan_1 = kondisi_2 // 1000
    print("pecahan 5000 = 0", "pecahan 2000 = " + str(pecahan_2), "pecahan 1000 = " + str(pecahan_1))
else:
    print("pecahan 5000 = 0", "pecahan 2000 = " + str(pecahan_2), "pecahan 1000 = 0")

#kondisi 3
pecahan_1 = a // 1000
print("pecahan 5000 = 0", "pecahan 2000 = 0", "pecahan 1000 = " + str(pecahan_1))