#เกรด + เกรดเฉลี่ย

def tolgrade(P): #คะแนนเแลี่ย
  return sum(P)/len(P)

def grade(P): #เกรด
  if 80 <= P <= 100:
    return 'A'
  elif 70 <= score < 80:
        return 'B'
  elif 60 <= score < 70:
        return 'C'
  elif 50 <= score < 60:
        return 'D'
  else:
        return 'F'

input("ชื่อ = " )
A = int(input("จำนวนวิชา = "))

P = []
for i in range(1,A+1): #วนลูปตามจำนวนวิชาเก็บค่าไว้ที่ i
  while True:
    try:
      x = float(input(f"คะแนนวิชาที่ {i} = "))
      if 0 <= x <= 100:
        P.append(x) #เอาไว้ตรวจสอบเงื่อนไข
        break
      else: #ป้องกันเลขที่ติดลบหรือมีค่ามากกว่า 100
        print("คะแนนต้องอยู่ระหว่าง 0-100")
    except ValueError: #ป้องกันการกรอกอย่างอื่นนอกจากตัวเลข
      print("กรุณากรอกคะแนนเป็นตัวเลข")

D = tolgrade(P)
G = grade(D)

print(f"คะแนนเฉลี่ย = {D:.2f}") #คะแนนเฉลี่ย
print(f"เกรด = {G}") #เกรด
