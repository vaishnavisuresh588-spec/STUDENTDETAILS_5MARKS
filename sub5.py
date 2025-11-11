import sys

if len(sys.argv) == 5:
  m1 = sys.argv[1]
  m2 = sys.argv[2]
  m3 = sys.argv[3]
  m4 = sys.argv[4]
  m5 = sys.argv[5]

else:
  m1 = "80"
  m2 = "90"
  m3 = "85"
  m4 = "88"
  m5 = "92"
  print("No command line arguments provided. Using default marks.")

  #calculate total and average of 5 subjects 
total = m1 + m2 + m3 + m4 + m5
average = total / 5

if average >= 90:
    grade = "A"
elif average >= 80:
    grade = "B"
elif average >= 70:
    grade = "C"
elif average >= 60:
    grade = "D"
else:
    grade = "fail"

    print("MARKS 1 IS:", m1)
    print("MARKS 2 IS:", m2)
    print("MARKS 3 IS:", m3)
    print("MARKS 4 IS:", m4)
    print("MARKS 5 IS:", m5)
    print("TOTAL MARKS IS:", total)
    print("AVERAGE IS:", average)
    print("GRADE IS:", grade)