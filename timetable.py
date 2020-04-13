import prettytable
import random

no_of_teachers=int(input("Enter number of teachers:"))

if(no_of_teachers<=4):
    print("No need Of Time table,Thank U")
else:
        
    # VARIABLES AND DATA STRUCTURES USED 
    flag=no_of_teachers

    subject=[]
    teachers=[]

    time=['9-10','10-11','11-12','12-1','1-2','2-3','3-4','4-5']
    days=['Mon','Tue','Wed','Thur','Fri','Sat']
    Mon=[]
    Tue=[]
    Wed=[]
    Thur=[]
    Fri=[]
    Sat=[]


    flag_list=[]
    ex=[]
    ex1=[]
    ex2=[]
    ex3=[]
    ex5=[]
    ex4=[]


    fulldaylist=[Mon,Tue,Wed,Thur,Fri,Sat]
    absenties=[]


    while no_of_teachers>0:
        print("")
        name=input("Enter name of teacher:")
        subject_name=input("Enter subject name of "+name +" :")
        print("")
        subject.append(subject_name)
        teachers.append(name)
        no_of_teachers=no_of_teachers-1



    def display_details():
        display=prettytable.PrettyTable()
        display.add_column('Teachers Name ',teachers)
        display.add_column('Subjects',subject)
        print(display)

    display_details()

    #PART 1:Arranging Table
    def switch(dy):
        if dy=='Mon':
            Mon.append(teachers[i])
            

        elif dy=='Tue':
            Tue.append(teachers[i])
            
            
        elif dy=='Wed':
            Wed.append(teachers[i])
            
            
        elif dy=='Thur':
            Thur.append(teachers[i])
            
            
        elif dy=='Fri':
            Fri.append(teachers[i])
            
        elif dy=='Sat':
            Sat.append(teachers[i])
        


    def stoper(nhrs,s):
        if nhrs<8 and nhrs>0:
            if len(Mon)<8 and len(Mon)>0:
                pass
            elif len(Tue)<8 and len(Tue)>0:
                pass
            elif len(Wed)<8 and len(Wed)>0:
                pass
            elif len(Thur)<8 and len(Thur)>0:
                pass
            elif len(Fri)<8 and len(Fri)>0:
                pass
            elif len(Sat)<8 and len(Sat)>0:
                pass
            else:
                s=s+1
                return s
        else:
            s=s+1
            return s
        


    def length_equalizer():
        for i in range(len(fulldaylist)):
            if(len(fulldaylist[i])<8):
                extra=8-len(fulldaylist[i])
                for j in range(0,extra):
                    fulldaylist[i].append(0)
                extra=0



    def randomer(fulldaylist_modified):
        for i in range(len(fulldaylist_modified)):
            random.shuffle(fulldaylist_modified[i])



    def printer():
        length_equalizer()
        fulldaylist_modified=[Mon,Tue,Wed,Thur,Fri,Sat]
        flag_list=fulldaylist_modified
        randomer(fulldaylist_modified)
        pretty=prettytable.PrettyTable()
        pretty.add_column(' ',time)
        pretty.add_column('Mon',Mon)
        pretty.add_column('Tue',Tue)
        pretty.add_column('Wed',Wed)
        pretty.add_column('Thur',Thur)
        pretty.add_column('Fri',Fri)
        pretty.add_column('Sat',Sat)
        print(pretty)
    v=0

    b=0
    for i in range(0,flag):
        for d in range(len(days)):
            nhrs=int(input("Enter number of hours for " +teachers[i]+" for "+ days[d] +" :"))
            if(nhrs<=8):    
                for x in range(0,nhrs):
                    switch(days[d])
                    s=0
                    o=stoper(nhrs,s)
                if(o==1):
                    break
                else:
                    v=v+1
            else:
                print("Please Don\'t be Insane.")
                b=b+1
                break
                
        print("")
        if(b==1):
            break


        



    #PART -2:Absenties Handling
    if(v>0 and b!=1):


        printer()

        no_of_teachers_absents=int(input("Enter number of teacher be absents?:"))
        
        if(no_of_teachers_absents>=1):
                
            for i in range(0,no_of_teachers_absents):
                name_of_absenties=input("Enter name of absenties:")
                absenties.append(name_of_absenties)
            print("Absenties are:",absenties)
            

            for s in range(len(Mon)):
                if(Mon[s]!=0):
                    if Mon[s] not in absenties:
                        ex.append(Mon[s])
                            
            for i in range(len(absenties)):
                for j in range(len(Mon)):
                    if absenties[i]==Mon[j]:
                        del Mon[j]
                        if(len(ex)!=0):
                            Mon.insert(j,ex[random.randint(0,len(ex)-1)])
                        else:
                            Mon.insert(j,0)
        # --------------------------------------------------------------------



            for s in range(len(Tue)):
                if(Tue[s]!=0):
                    if Tue[s] not in absenties:
                        ex1.append(Tue[s])
                        
            for i in range(len(absenties)):
                for j in range(len(Tue)):
                    if absenties[i]==Tue[j]:
                        del Tue[j]
                        if(len(ex1)!=0):
                            Tue.insert(j,ex1[random.randint(0,len(ex1)-1)])
                        else:
                            Tue.insert(j,0)

        # --------------------------------------------------------------------

            for s in range(len(Wed)):
                if(Wed[s]!=0):
                    if Wed[s] not in absenties:
                        ex2.append(Wed[s])
                        
            for i in range(len(absenties)):
                for j in range(len(Wed)):
                    if absenties[i]==Wed[j]:
                        del Wed[j]
                        if(len(ex2)!=0):
                            Wed.insert(j,ex2[random.randint(0,len(ex2)-1)])
                        else:
                            Wed.insert(j,0)

        # --------------------------------------------------------------------

            for s in range(len(Thur)):
                if(Thur[s]!=0):
                    if Thur[s] not in absenties:
                        ex3.append(Thur[s])
                        
            for i in range(len(absenties)):
                for j in range(len(Thur)):
                    if absenties[i]==Thur[j]:
                        del Thur[j]
                        if(len(ex3)!=0):
                            Thur.insert(j,ex3[random.randint(0,len(ex3)-1)])
                        else:
                            Thur.insert(j,0)

        # --------------------------------------------------------------------

            for s in range(len(Fri)):
                if(Fri[s]!=0):
                    if Fri[s] not in absenties:
                        ex4.append(Fri[s])
                        
            for i in range(len(absenties)):
                for j in range(len(Fri)):
                    if absenties[i]==Fri[j]:
                        del Fri[j]
                        if(len(ex4)!=0):
                            Fri.insert(j,ex4[random.randint(0,len(ex4)-1)])
                        else:
                            Fri.insert(j,0)
        # --------------------------------------------------------------------

            for s in range(len(Sat)):
                if(Sat[s]!=0):
                    if Sat[s] not in absenties:
                        ex5.append(Sat[s])
                        
            for i in range(len(absenties)):
                for j in range(len(Sat)):
                    if absenties[i]==Sat[j]:
                        del Sat[j]
                        if(len(ex5)!=0):
                            Sat.insert(j,ex5[random.randint(0,len(ex5)-1)])
                        else:
                            Sat.insert(j,0)

            def printer2(Mon,Tue,Wed,Thur,Fri,Sat):
                pretty2=prettytable.PrettyTable()
                pretty2.add_column(' ',time)
                pretty2.add_column('Mon',Mon)
                pretty2.add_column('Tue',Tue)
                pretty2.add_column('Wed',Wed)
                pretty2.add_column('Thur',Thur)
                pretty2.add_column('Fri',Fri)
                pretty2.add_column('Sat',Sat)
                print(pretty2)
            printer2(Mon,Tue,Wed,Thur,Fri,Sat)
        else:
            print("No need of New Table")


    else:
        print("Please,try to write the number of working hours in a day from 0 to till 8 hrs")




