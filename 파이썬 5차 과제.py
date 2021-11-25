counts, idx1, idx2, idx3 = 0, 0, 0, 0

form = ["name", "number", "email"]
ch, box, information, name, number, email, search, change, delete = [], [], [], [], [], [], [], [], []

while (1) :
    ch = input("명령어를 입력하세요 : ")
    
    if ch == "add" :
        name.append(input("이름 입력 : "))
        number.append(input("전화번호 입력 : "))
        email.append(input("이메일 주소 입력 : "))

        box = []

        for i in form :
            box.append(i)

        information.append(box)
        print(information)
        

