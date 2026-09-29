stdCode = 34551001
stdMidterm = 80
stdFinal = 98
stdName = 'Fatine'
stdLastname = 'Mamouni'
print('Student Name: Fatine Mamouni - Student Code: ' + str(stdCode))
print('Student Grade Final: ' + str(stdFinal))
print(stdName , stdLastname)

#print(stdFinal + ' ' + stdLastname)

print(stdFinal == stdMidterm)

print(stdFinal != stdMidterm)


print('Average (Midterm and Final) is: ' + str((stdMidterm + stdFinal) / 2))

# 8.
#stdCode = 1<br>print('New Student Code:', stdCode)

# 10.
print((not(stdName == 'Ayesha') or (stdFinal > stdMidterm)) and (stdMidterm != stdFinal))

print('345' in str(stdCode))
# The 'not in' operator checks if a substring does NOT exist in the string. Since '345' does exist in '34551001', the not in check returns False.
print('345' not in str(stdCode))

# To make print(5 _ 2 % 5) output 0, the blank should be filled with: *
print(5 * 2 % 5) 
print('Final is : ' + str(stdFinal))
print("3" * 3)