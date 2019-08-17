import sys
import copy

stu_dict = {}
sorted_s1 = []

#1.show
def show(f):
    global sorted_s1
    global stu_dict
    sorted_s1 = sorted(stu_dict.items(),key=lambda a: a[1][3], reverse=True)
    print(' Student','\t\tName','\tMidterm','   Final','  Average', '  Grade')
    print('--------------------------------------------------------------------')

    for k,v in sorted_s1:
        print(k,"{:>19}{:^15}{:^5}{:^14}{:^4}" .format(*v))
    
#2.search
def search(f):
    global sorted_s1
    global stu_dict
    stu_id = int(input("Student ID:"))
    k_student=[]
    for k,v in sorted_s1:
        k_student.append(k)
    if stu_id not in k_student:
        print("NOT SUCH PERSON")
    else:
        print(' Student','\t\tName','\tMidterm','   Final','  Average', '  Grade')
        print('--------------------------------------------------------------------')
        vv=stu_dict[stu_id]
        print(stu_id,"{:>19}{:^15}{:^5}{:^14}{:^4}" .format(*vv))
        
#3.changescore
def changescore(f):
    global sorted_s1
    global stu_dict
    stuu_dict = copy.deepcopy(stu_dict)
    stu_id = int(input("Student ID:"))
    k_student=[]
    for k,v in sorted_s1:
        k_student.append(k)
    if stu_id not in k_student:
        print("NOT SUCH PERSON")
    else:
        testtype = input("Mid/Final?")
        if testtype == 'mid':
            new_score = int(input("Input new score:"))
            if new_score <=100 and new_score >=0:
                print(' Student','\t\tName','\tMidterm','   Final','  Average', '  Grade')
                print('--------------------------------------------------------------------')
                vv=stuu_dict[stu_id]
                stu_dict[stu_id][1] = new_score
                stu_dict[stu_id][3] = (stu_dict[stu_id][1]+stu_dict[stu_id][2])/2
                if stu_dict[stu_id][3] >= 90:
                    stu_dict[stu_id][4] = 'A'
                elif stu_dict[stu_id][3] >= 80:
                    stu_dict[stu_id][4] = 'B'
                elif stu_dict[stu_id][3] >= 70:
                    stu_dict[stu_id][4] = 'C'
                elif stu_dict[stu_id][3] >= 60:
                    stu_dict[stu_id][4] = 'D'
                else:
                    stu_dict[stu_id][4] = 'F'
                      
                vvm=stu_dict[stu_id]
                print(stu_id,"{:>19}{:^15}{:^5}{:^14}{:^4}" .format(*vv))
                print("Score changed.")
                print(stu_id,"{:>19}{:^15}{:^5}{:^14}{:^4}" .format(*vvm))
        elif testtype == 'final':
            new_score = int(input("Input new score:"))
            if new_score <= 100 and new_score >=0:
                print(' Student','\t\tName','\tMidterm','   Final','  Average', '  Grade')
                print('--------------------------------------------------------------------')
                vv=stuu_dict[stu_id]
                stu_dict[stu_id][2] = new_score
                stu_dict[stu_id][3] = (stu_dict[stu_id][1]+stu_dict[stu_id][2])/2
                if stu_dict[stu_id][3] >= 90:
                    stu_dict[stu_id][4] = 'A'
                elif stu_dict[stu_id][3] >= 80:
                    stu_dict[stu_id][4] = 'B'
                elif stu_dict[stu_id][3] >= 70:
                    stu_dict[stu_id][4] = 'C'
                elif stu_dict[stu_id][3] >= 60:
                    stu_dict[stu_id][4] = 'D'
                else:
                    stu_dict[stu_id][4] = 'F'
                
                vvm=stu_dict[stu_id]
                print(stu_id,"{:>19}{:^15}{:^5}{:^14}{:^4}" .format(*vv))
                print("Score changed.")
                print(stu_id,"{:>19}{:^15}{:^5}{:^14}{:^4}" .format(*(stu_dict[stu_id])))
                
#4.add
def add(f):
    global sorted_s1
    global stu_dict
    stu_id = int(input("Student ID:"))
    k_student=[]
    for k,v in sorted_s1:
        k_student.append(k)
    if stu_id in k_student:
        print("ALREADY EXISTS.")
    else:
        name = input("Name:")
        midterm = int(input("Midterm Score:"))
        final = int(input("Final Score:"))        
        stu_dict[stu_id]=[name,midterm,final,(midterm+final)/2]
        if stu_dict[stu_id][3] >= 90:
            stu_dict[stu_id].append('A')
        elif stu_dict[stu_id][3] >= 80:
            stu_dict[stu_id].append('B')
        elif stu_dict[stu_id][3] >= 70:
            stu_dict[stu_id].append('C')
        elif stu_dict[stu_id][3] >= 60:
            stu_dict[stu_id].append('D')
        else:
            stu_dict[stu_id].append('F')
        print("Student added.")
        
#5.searchgrade
def searchgrade(f):
    global sorted_s1
    global stu_dict
    grade = input("Grade to search:")
    if grade in ['A','B','C','D','F']:
        g_student=[]
        for k,v in sorted_s1:
            g_student.append(v[4])
        if grade not in g_student:
            print("NO RESULTS.")
        else:
            print(' Student','\t\tName','\tMidterm','   Final','  Average', '  Grade')
            print('--------------------------------------------------------------------')
            for k,v in sorted_s1:
                if grade == v[4]:
                    print(k,"{:>19}{:^15}{:^5}{:^14}{:^4}" .format(*v))
                    
#6.remove
def remove(f):
    global sorted_s1
    global stu_dict
    k_student=[]
    for k,v in sorted_s1:
        k_student.append(k)
       
    if stu_dict =={}:
        print('List is empty.')
    else:
        stu_id = int(input("Student ID:"))
        if stu_id not in k_student:
            print("NO SUCH PERSON.")
        else:
            del stu_dict[stu_id]
            print("Student removed.")
        
#7.quit
def quit():
    global sorted_s1
    save = input("Save data?[yes/no]")
    if save == 'yes':
        file_name = input("File name:")
        f2=open(file_name,'w')
        for i in sorted_s1:
            f2.write('{0}\t{1}\t{2}\t{3}\t{4}\t{5}\n'.format(i[0],i[1][0],i[1][1],i[1][2],i[1][3],i[1][4]))
        f2.close()
        
#main
def main():
    global sorted_s1
    global stu_dict
    print(' Student','\t\tName','\tMidterm','   Final','  Average', '  Grade')
    print('--------------------------------------------------------------------')
    if len(sys.argv) == 1 :
        f =open('students.txt', 'r')
    else:
        f = open(sys.argv[1], 'r')
#     f =open('students.txt', 'r')
        
    stu_dict = {}
    for line in f.readlines():
        line=line.strip()
        line1 = line.split('\t')
        average=(int(line1[2])+int(line1[3]))/2
        if average >= 90:
            grade = 'A'
        elif average >= 80:
            grade = 'B'
        elif average >= 70:
            grade = 'C'
        elif average >= 60:
            grade = 'D'
        else:
            grade = 'F'
        line1.append(average)
        line1.append(grade)
        stu_dict[int(line1[0])] = [line1[1],int(line1[2]), int(line1[3]), line1[4], line1[5]]
        sorted_s1 = sorted(stu_dict.items(),key=lambda a: a[1][3], reverse=True)


    for k,v in sorted_s1:
        print(k,"{:>19}{:^15}{:^5}{:^14}{:^4}" .format(*v))
        
    while 1:
        command = input('#')
    
        if command.lower() == 'show':
            show(f)
        elif command.lower() == 'search':
            search(f)
        elif command.lower() == 'changescore':
            changescore(f)
        elif command.lower() == 'searchgrade':
            searchgrade(f)
        elif command.lower() == 'add':
            add(f)
        elif command.lower() == 'remove':
            remove(f)
        elif command.lower() == 'quit':
            quit()
            print('$')
            break

if __name__ == '__main__':
    main()