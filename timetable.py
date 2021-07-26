import flask
#import sklearn
from flask import Flask,redirect, url_for, request,render_template,send_file,jsonify
#from bottle import static_file
import werkzeug
import pandas as pd
from werkzeug.utils import secure_filename
from flask import get_flashed_messages
from flask import flash
#from werkzeug import FileWrapper
#from io import BytesIO
from flask import Flask, Response
from flask import send_from_directory
import sys
global d
global d1
global labs,lablist
import warnings
warnings.filterwarnings("ignore")

app=Flask(__name__)
@app.route("/viewresult/<string:name>")
def viewresult(name):
    global d
    global d1
    global nl
    global labs ,lablist
    import pandas as pd
    global th,tl,nl
 
    """
    tl=int(input("enter no of types of labs in the curriculum: "))
    for typ in range(tl):
        nty=int(input("no of labs of type {}: ".format(typ)))
        nl.append(nty)"""
    s=pd.read_csv(name)
    print(s.head())
    #s.columns=["Unnamed: 0","Year","Course Teachers","Section","Course Name","theorey","lab","labavil","xcom","labtype","CBCS"]


        #for i in range(len(s)):
        
    co=s["Course Teachers"]
    for i in range(len(co)):
        co[i]=str(co[i])
        if(co[i]=="nan"):
            co[i]=co[i-1]

        co[i]=str(co[i])
        co[i]=co[i].replace(".","")
        co[i]=co[i].lower()
        co[i]=co[i].replace(" ","")
        co[i]=co[i].replace("\n","")

    s["Course Teachers"]=co
    grouped=[]
    data=[]






    s["x com"]=s["x com"].astype(float)
    s["theorey"]=s["theorey"].astype(float)
    s["labtype"]=s["labtype"].astype(float)
    s["lab"]=s["lab"]+(s["labavil"]*0.1)
    s["lab"]=s["lab"].astype(float)
    s.drop(columns=["labavil"],inplace=True)
    for i in range(len(s)):
        if(s["CBCS"][i]!=0):
            g=list(s.iloc[i,:])
            g.insert(0,s["CBCS"][i])
            grouped.append(g)
        else:
            data.append(list(s.iloc[i,:]))
    print(grouped,"---------------------------------------------------------")
    s.drop(s.columns[0],axis=1,inplace=True)
    colsn=s.columns
    grouped.sort()
    classes=[]
    cl=[]
    fl=[];col=[]
    t1=[]
    ind=0
    import warnings
    warnings.filterwarnings("ignore")

    for i in range(len(grouped)-1):
        if(grouped[i][0]==grouped[i+1][0]):
            classes=grouped[i][4].split("/")
            for j in range(len(classes)):
                cl.append(grouped[i][2]+" "+classes[j])
                col.append(grouped[i][5])
                fl.append(grouped[i][3])
        else:
            if("/" in grouped[i][4]):
                classes=grouped[i][4].split("/")
                for j in range(len(classes)):
                    cl.append(grouped[i][2]+" "+classes[j])
                    col.append(grouped[i][5])
                    fl.append(grouped[i][3])

        
            else:
                cl.append(grouped[i][2]+" "+grouped[i][4])
                col.append(grouped[i][5])
                fl.append(grouped[i][3])
            
            k="/".join(sorted(list(set(cl))));grouped[i][2]=k;grouped[i][4]="CBCS"
            print(grouped[i],"***********************************************")
            print(fl)
            print(col)
            k1="/".join(sorted(list(set(fl))));grouped[i][3]=k1
            k2="/".join(sorted(list(set(col))));grouped[i][5]=k2
            t1.extend(list(set(fl)))
            t1.append(k1)
            cl=[]
            fl=[]
            col=[]
            ind=i

            
    cl=[]
    fl=[]
    col=[]
    for i in range(ind+1,len(grouped)):
        classes=grouped[i][4].split("/")
        for j in range(len(classes)):
            cl.append(grouped[i][2]+" "+classes[j])
            col.append(grouped[i][5])
            fl.append(grouped[i][3])
    if(len(grouped)!=0):
        k1="/".join(sorted(list(set(fl))));grouped[i][3]=k1
        k="/".join(sorted(list(set(cl))));grouped[i][2]=k;grouped[i][4]="CBCS"
        k2="/".join(sorted(list(set(col))));grouped[i][5]=k2
        t1.extend(list(set(fl)))
        t1.append(k1)

    grp=[]
    for i in grouped:
        if(i[4]=="CBCS"):
            i.pop(0)
            grp.append(i)
            data.insert(0,i)
    dd=pd.DataFrame(data)

    dd.drop(dd.columns[0],inplace=True,axis=1)
    dd.columns=s.columns
    s["Course Teachers"]=co
    u=list(set(s["Year"].unique()))
    t=list(set(s["Course Teachers"].unique()))

    t.extend(t1)

    t=list(set(t))
    for i in range(len(t)):
        if("/" in t[i]):
            x=t[i].split("/")
            t.extend(x)

    t=list(set(t))

    cla=[]
    for i in range(len(dd)):
        cla.append(str(dd["Year"][i]+" "+dd["Section"][i]))

    dd["cla"]=cla
    d={}
    s=dd

    "----------------------------------------------------------------------------------------"
    nofl=3
    nohl=4
    lablist=[]
    for i in range(len(nl)):
        for j in range(nl[i]):
            lstr="lab{} type({})".format(j,i)
            lablist.append(lstr)

    """
    for i in range(nohl):
        lstr="hlab "+str(i)
        lablist.append(lstr)
    for i in range(nofl):
        lstr="flab " +str(i)
        lablist.append(lstr)"""

    labs={};#lablist=["8601ab","8501ab","computerLabMain","newlab","8501c","8601c","mtechlab"]
    s["theorey"]=s["lab"]+s["theorey"]+s["x com"]
    for i in range(len(s["theorey"])):
        s["theorey"][i]=int(s["theorey"][i])

    for i in range(len(lablist)):
        allot=[]
        for j in range(5):
            if(th<=6):
                nh=[""]*(th+1)
            else:
                nh=[""]*(th)
            allot.append(nh)
        labs[lablist[i]]=allot
    for j in range(len(cla)):
        l=[]
        for i in range(len(s)):
            if(s["cla"][i]==cla[j]):

                l.append([s["theorey"][i],s["Course Teachers"][i],s["lab"][i],s["x com"][i],s["labtype"][i]])

        l.sort()
        l.reverse()
        d.update({cla[j]:[l]})
    d1={}


    "------------------------------------------------------------------------------------------"

    for j in range(len(t)):
        l=[]
        for i in range(len(s)):
            if(s["Course Teachers"][i]==t[j]):

                l.append([s["theorey"][i],s["cla"][i],s["lab"][i],s["x com"][i],s["labtype"][i]])
        l.sort()
        d1.update({t[j]:[l]})
    sch=[]

    for i in range(5):
        allot=[""]*th
        sch.append(allot)
    for i in d1:
        d1[i].append(sch)
    for i in d:
        d[i].append(sch)
    import random
    from random import randint
    from random import choice


    "--------------------------------------------------------------------------------------------"


    def fixed():
        fix=pd.read_csv("twofixed.csv",header=None)
        for i in range(0,(len(fix)//8)+1):
            na=fix.iloc[(i*8)+2:(i+1)*8,1:]
            x=fix.iloc[i*8,4]
            temp=na.values
            y=tuple(d[x])
            y1=str(y[1])
            y3=y[0]
            y2=eval(y1)
            y2=temp
            for it in range(len(temp)):
                for jt  in range(len(temp[it])):
                    temp[it][jt]=str(temp[it][jt])
                    temp[it][jt]=temp[it][jt].replace("nan","")
            temp1=[]
            for it in range(len(temp)):
                y5=[]
                for kt in range(len(temp[it])):
                    y5.append(temp[it][kt])
                    if(temp[it][kt]!=""):
                        sus=temp[it][kt].lower()
                        sus=sus.replace(" ","")
                        sus=sus.replace(".","")
                        if(temp[it][kt] in d1):
                            req=d1[sus]
                            fe=tuple(d1[sus])
                            fe1=str(fe[1])
                            fex=fe[0]
                            print(fe1)
                            fe2=eval(fe1);fe2[it][kt]=x
                            print(fe2)
                            d1.update({sus:[fex,fe2]})
                            for l in range(len(d[x][0])):
                                if(d[x][0][l][1]==sus):
                                    d[x][0][l][0]-=1

                y5.append("")
                y5.append("")
                temp1.append(y5)

            d.update({x:[y3,temp1]})
            if(i!=6):
                temp1.pop(-1)
    global lab_copy,d_copy,d1_copy
    lab_copy=str(labs)
    d_copy=d.copy()
    d1_copy=d1.copy()


    return render_template("Squadfree/block3.html",generated=False,assigned=True,filebool=False,submitted=True)

"------------------------------------------------------------------------------------"
import random
from random import randint

@app.route("/generate_final",methods=["POST","GET"])
def generate_final():
    global blocked
    global d_copy
    global lablist
    global lab_copy,nl
    global d1_copy,tl,th
    d=d_copy.copy()
    d1=d1_copy.copy()
    labs=eval(lab_copy)
    print(lab_copy)
    print(d)

 
    blocked=[]

    rand=[th-2]
    print("----------------------------------------------")
    for i in range(5):
        i1=i
        for j in d:
            if("CBCS" in j):
                for k in range(len(d[j][0])):
                    if(int(d[j][0][k][3])>0):
                        print(d[j][0][k])
                        index=randint(0,th-2)
                        count=0;count1=0;count2=0
                        labind=randint(0,3)
                        flag=0
                        myflag=True
                        toteval=""
                        duc=j
                        toteval1=""
                        totevalc=""
                        totevalc1=""
                        if("/" in duc):
                            duc=duc[:-5]
                            fc=duc.split("/");orgc=fc[0];
                            for i in range(1,len(duc)):
                                totevalc+="d[fc[{}]][1][i1][index]!='' or".format(i)
                                totevalc1+="d[fc[{}]][1][i1][index+1]!='' or".format(i)
                            totevalc=totevalc[:-3];totevalc1=totevalc1[:-3]
                        else:
                            totevalc="False"
                            totevalc1="False"
                            orgc=duc
                        dum=d[j][0][k][1]
                        if("/" in dum):
                            fl=dum.split("/");org=fl[0];dup="d1[fl[1]][1][i1][index]!=''";dup1="d1[fl[1]][1][i1][index+1]!=''";
                            for i in range(1,len(fl)):
                                toteval+="d1[fl[{}]][1][i1][index]!='' or ".format(i)
                                toteval1+="d1[fl[{}]][1][i1][index+1]!='' or ".format(i)
                            toteval=toteval[:-3]
                            toteval1=toteval1[:-3]
                    
                        else:
                            org=dum;dup="False";dup1="False";toteval="False";toteval1="False"
                        if(d[j][0][k][2]==3):
                            # print("yes thresssslotss lab***********************************************")
                            ll="d1[org][1][i1][index+2]!=''  or d[j][1][i1][index+2]!='' or labs[lablist[labind]][i1][index+2]!=''"
                        else:
                            ll="False"
                        """if(j=="II Year G" or j=="II Year C"):
                            labind=randint(4,5)
                        if(j=="I Mtech CSE A"):
                            labind=6"""
                        labavil='False'
                        """else:
                            labavil="labs[lablist[labind]][i1][index]!='' or labs[lablist[labind]][i1][index+1]!=''"""


                        while(d1[org][1][i1][index]!=""  or d[orgc][1][i1][index]!="" or eval(totevalc) or eval(totevalc1) or d1[org][1][i1][index+1]!=""  or d[orgc][1][i1][index+1]!="" or eval(labavil) or eval(toteval) or eval(toteval1) or eval(ll) or index%2==1):
                            count+=1
                            cbox=randint(0,2)
                            if(cbox==0):
                                labind=randint(0,5)
                            elif(cbox==1):
                                i1=randint(0,4)
                            else:
                                index=randint(0,th-2)

                            if(j=="I Mtech CSE A"):
                                labind=6

                            flag+=1

                            if(flag==50000):

                                print(j)
                                print()
                                print(d[j])
                                print()
                                print()
                                print("faculty")
                                print(d[j][0][k][1])
                                print(d1[d[j][0][k][1]])
                                print("-----------Not generating lab----------------")
                                blocked.append([j,d[j][0][k][1],"xcom slots(2)"])
                                break
                            continue
                        r=d1[dum]
                        if("/" in dum):
                            for ma in range(len(fl)):
                                r=d1[fl[ma]]
                                r=str(r);r1=eval(r)
                                if(d[j][0][k][2]==3):
                                    r1[1][i1][index+2]=j


                                r1[1][i1][index]=j
                                r1[1][i1][index+1]=j
                                r=eval(r)
                                d1[fl[ma]]=r1

                        r=str(r);r1=eval(r)


                        if(d[j][0][k][2]==3):

                                r1[1][i1][index+2]=j


                        r1[1][i1][index]=j
                        r1[1][i1][index+1]=j
                        r=eval(r)
                        if("/" in duc):
                            for mc in range(len(fc)):
                                r2=d[fc[mc]]
                                r2=str(r2);r3=eval(r2)
                                if(d[j][0][k][2]==3):
                                    r3[1][i1][index+2]=r3[0][k][1]+" x com"

                                r3[1][i1][index]=r3[0][k][1]+" x com"
                                r3[1][i1][index+1]=r3[0][k][1]+" x com"

                        r2=d[j]
                        r2=str(r2);r3=eval(r2)
                        if(d[j][0][k][3]==3):
                            r3[1][i1][index+2]=r3[0][k][1]+" x com"

                        r3[1][i1][index]=r3[0][k][1]+" x com"
                        r3[1][i1][index+1]=r3[0][k][1]+" x com"

                        if(r3[0][k][0]==1):
                                r3[0][k][0]-=1
                                r3[0][k][3]-=1
                        else:
                            r3[0][k][0]-=2
                            r3[0][k][3]-=2
                        if(d[j][0][k][2]==3):
                            r3[0][k][0]-=1
                            r3[0][k][3]-=1
                        if(d[j][0][k][3]==3 and labavil!="False"):
                            labs[lablist[labind]][i1][index+2]=str(d[j][0][k][1])+" | " +str(j)

                        d[j]=r3
                        d1[d[j][0][k][1]]=r1


                        if(labavil!="False"):
                            labs[lablist[labind]][i1][index]=str(d[j][0][k][1])+" | "+ str(j)
                            labs[lablist[labind]][i1][index+1]=str(d[j][0][k][1])+" | " +str(j)




    #sys.stdout = open('blocks', 'w') 
    "******************************this is for lab hours  cbcs***************************************************"
    rand=[th-2]
    print("----------------------------------------------")
    for i in range(5):
        i1=i
        for j in d:
            if("CBCS" in j):
                for k in range(len(d[j][0])):
                    if(int(d[j][0][k][2])>0):
                        index=randint(0,4)
                        count=0;count1=0;count2=0
                        las=d[j][0][k][4]
                        stind=sum(nl[:las]);endind=stind+nl[las]
                        labind=randint(stind,endind-1)
                        flag=0
                        myflag=True
                        toteval=""
                        duc=j
                        toteval1=""
                        totevalc=""
                        totevalc1=""
                        if("/" in duc):
                            duc=duc[:-5]
                            fc=duc.split("/");orgc=fc[0];
                            for i in range(1,len(duc)):
                                totevalc+="d[fc[{}]][1][i1][index]!='' or".format(i)
                                totevalc1+="d[fc[{}]][1][i1][index+1]!='' or".format(i)
                            totevalc=totevalc[:-3];totevalc1=totevalc1[:-3]
                        else:
                            totevalc="False"
                            totevalc1="False"
                            orgc=duc
                        dum=d[j][0][k][1]
                        if("/" in dum):
                            fl=dum.split("/");org=fl[0];dup="d1[fl[1]][1][i1][index]!=''";dup1="d1[fl[1]][1][i1][index+1]!=''";
                            for i in range(1,len(fl)):
                                toteval+="d1[fl[{}]][1][i1][index]!='' or ".format(i)
                                toteval1+="d1[fl[{}]][1][i1][index+1]!='' or ".format(i)
                            toteval=toteval[:-3]
                            toteval1=toteval1[:-3]
                    
                        else:
                            org=dum;dup="False";dup1="False";toteval="False";toteval1="False"
                        if(d[j][0][k][2]==3):
                            # print("yes thresssslotss lab***********************************************")
                            ll="d1[org][1][i1][index+2]!=''  or d[j][1][i1][index+2]!='' or labs[lablist[labind]][i1][index+2]!=''"
                        else:
                            ll="False"
                        """if(j=="II Year G" or j=="II Year C"):
                            labind=randint(4,5)"""
                        if(j=="I Mtech CSE A"):
                            labind=0
                        if(".1"  in str(d[j][0][k][2])):
                            labavil='False'
                        else:
                            labavil="labs[lablist[labind]][i1][index]!='' or labs[lablist[labind]][i1][index+1]!=''"


                        while(d1[org][1][i1][index]!=""  or d[orgc][1][i1][index]!="" or eval(totevalc) or eval(totevalc1) or d1[org][1][i1][index+1]!=""  or d[orgc][1][i1][index+1]!="" or eval(labavil) or eval(toteval) or eval(toteval1) or eval(ll) or index%2==1):
                            count+=1
                            cbox=randint(0,2)
                            if(cbox==0):
                                stind=sum(nl[:las]);endind=stind+nl[las]
                                labind=randint(stind,endind-1)
                            elif(cbox==1):
                                i1=randint(0,4)
                            else:
                                index=randint(0,th-2)

                            if(j=="I Mtech CSE A"):
                                labind=0

                            flag+=1

                            if(flag==50000):

                                print(j)
                                print()
                                print(d[j])
                                print()
                                print()
                                print("faculty")
                                print(d[j][0][k][1])
                                print(d1[d[j][0][k][1]])
                                blocked.append([j,d[j][0][k][1],"Lab slots(2)"])
                                print("-----------Not generating lab----------------")
                                break
                            continue
                        r=d1[dum]
                        if("/" in dum):
                            for ma in range(len(fl)):
                                r=d1[fl[ma]]
                                r=str(r);r1=eval(r)
                                if(d[j][0][k][2]==3):
                                    r1[1][i1][index+2]=j


                                r1[1][i1][index]=j
                                r1[1][i1][index+1]=j
                                r=eval(r)
                                d1[fl[ma]]=r1

                        r=str(r);r1=eval(r)


                        if(d[j][0][k][2]==3):

                                r1[1][i1][index+2]=j


                        r1[1][i1][index]=j
                        r1[1][i1][index+1]=j
                        r=eval(r)
                        if("/" in duc):
                            for mc in range(len(fc)):
                                r2=d[fc[mc]]
                                r2=str(r2);r3=eval(r2)
                                if(d[j][0][k][2]==3):
                                    r3[1][i1][index+2]=r3[0][k][1]+" lab"

                                r3[1][i1][index]=r3[0][k][1]+" lab"
                                r3[1][i1][index+1]=r3[0][k][1]+" lab"

                        r2=d[j]
                        r2=str(r2);r3=eval(r2)
                        if(d[j][0][k][2]==3):
                            r3[1][i1][index+2]=r3[0][k][1]+" lab"

                        r3[1][i1][index]=r3[0][k][1]+" lab"
                        r3[1][i1][index+1]=r3[0][k][1]+" lab"

                        if(r3[0][k][0]==1):
                                r3[0][k][0]-=1
                                r3[0][k][2]-=1
                        else:
                            r3[0][k][0]-=2
                            r3[0][k][2]-=2
                        if(d[j][0][k][2]==3):
                            r3[0][k][0]-=1
                            r3[0][k][2]-=1
                        if(d[j][0][k][2]==3 and labavil!="False"):
                            labs[lablist[labind]][i1][index+2]=str(d[j][0][k][1])+" | " +str(j)

                        d[j]=r3
                        d1[d[j][0][k][1]]=r1

                        if(labavil!="False"):
                            labs[lablist[labind]][i1][index]=str(d[j][0][k][1])+" | "+ str(j)
                            labs[lablist[labind]][i1][index+1]=str(d[j][0][k][1])+" | " +str(j)



    for i in range(5):
        i1=i
        for j in d:
            if("CBCS" in j):
                for k in range(len(d[j][0])):
                    dum=d[j][0][k][1]
                    toteval=""
                    duc=j


                    toteval1=""
                    totevalc=""
                    totevalc1=""
                    if("/" in duc):
                        duc=duc[:-5]
                        flt=d[j][0][k][1]

                        fc=duc.split("/");orgc=fc[0];

                        for i in range(1,len(fc)):
                            totevalc+="d[fc[{}]][1][i1][index]!='' or ".format(i)
                            totevalc1+="d[fc[{}]][1][i1][index+1]!='' or ".format(i)
                        totevalc=totevalc[:-3];totevalc1=totevalc1[:-3]
                    else:
                        totevalc="False"
                        totevalc1="False"
                        orgc=duc
                    if("/" in dum):
                        fl=dum.split("/");org=fl[0];dup="d1[fl[1]][1][i1][index]!=''";dup1="d1[fl[1]][1][i1][index+1]!=''";
                        for i in range(1,len(fl)):
                            toteval+="d1[fl[{}]][1][i1][index]!='' or ".format(i)
                        toteval=toteval[:-3]
                    else:
                        org=dum;dup="False";toteval="False";

                    if(int(d[j][0][k][0])>0):

                        index=randint(0,6)
                        count=0
                        flag=0
                        count1=0

                        while(d1[org][1][i1][index]!="" or d[orgc][1][i1][index]!="" or eval(toteval) or eval(totevalc) ):
                            flag+=1
                            cbox=randint(0,1)
                            if(cbox==0):
                                index=randint(0,6)
                            else:
                                i1=randint(0,4)
                            flag+=1

                            if(flag==100000):


                                print(j)
                                print("class timetable");print()
                                print(d[j])
                                print()
                                print("faculty name ")
                                print(d[j][0][k][1])
                                print();print("faculty time table")
                                print(d1[d[j][0][k][1]][1])
                                print("---------------- NOT GENERATING ----------------")
                                print()
                                print()
                                blocked.append([j,d[j][0][k][1],"Normal slot"])
                                break



                            continue


                            #print(d1[d[j][0][k][1]][1][i][index],d[j][1][i][index])

                        if("/" in dum):
                            for ma in range(len(fl)):
                                r=d1[fl[ma]]
                                r=str(r);r1=eval(r)
                                if(d[j][0][k][2]==3):
                                    r1[1][i1][index+2]=j


                                r1[1][i1][index]=j

                                r=eval(r)
                                d1[fl[ma]]=r1
                        if("/" in duc):
                            for mc in range(len(fc)):
                                r2=d[fc[mc]]



                                r2=str(r2);r3=eval(r2)
                                if(d[j][0][k][2]==3):
                                    r3[1][i1][index+2]=r3[0][k][1]

                                r3[1][i1][index]=flt
                                r3[1][i1][index]=flt
                                d[fc[mc]]=r3
                                print()
                                print()



                        r=d1[d[j][0][k][1]]
                        r=str(r);r1=eval(r)

                        r1[1][i1][index]=j
                        r=eval(r)
                        r2=d[j]
                        r2=str(r2);r3=eval(r2)
                        r3[1][i1][index]=r3[0][k][1]
                        r3[0][k][0]-=1
                        d[j]=r3


                        d1[d[j][0][k][1]]=r1






    "########################## x com  slots #########################################################"
    for i in range(5):
        i1=i
        for j in d:
            for k in range(len(d[j][0])):
                if(int(d[j][0][k][3])>0):
                    index=randint(0,4)
                    count=0;count1=0;count2=0
                    labind=randint(0,3)
                    flag=0
                    myflag=True
                    toteval=""
                    duc=j
                    toteval1=""
                    totevalc=""
                    totevalc1=""
                    if("/" in duc):
                        duc=duc[:-5]
                        fc=duc.split("/");orgc=fc[0];
                        for i in range(1,len(duc)):
                            totevalc+="d[fc[{}]][1][i1][index]!='' or".format(i)
                            totevalc1+="d[fc[{}]][1][i1][index+1]!='' or".format(i)
                        totevalc=totevalc[:-3];totevalc1=totevalc1[:-3]
                    else:
                        totevalc="False"
                        totevalc1="False"
                        orgc=duc
                    dum=d[j][0][k][1]
                    if("/" in dum):
                        fl=dum.split("/");org=fl[0];dup="d1[fl[1]][1][i1][index]!=''";dup1="d1[fl[1]][1][i1][index+1]!=''";
                        for i in range(1,len(fl)):
                            toteval+="d1[fl[{}]][1][i1][index]!='' or ".format(i)
                            toteval1+="d1[fl[{}]][1][i1][index+1]!='' or ".format(i)
                        toteval=toteval[:-3]
                        toteval1=toteval1[:-3]

                    else:
                        org=dum;dup="False";dup1="False";toteval="False";toteval1="False"
                    if(d[j][0][k][3]==3):
                        #print("yes thresssslotss lab***********************************************")
                        ll="d1[org][1][i1][index+2]!=''  or d[j][1][i1][index+2]!='' or labs[lablist[labind]][i1][index+2]!=''"
                    else:
                        ll="False"
                    if(j=="II Year G" or j=="II Year C"):
                        labind=randint(4,5)
                    if(j=="I Mtech CSE A"):
                        labind=6
                    #if(".1"  in str(d[j][0][k][2])):
                    labavil='False'
                    """
                    else:
                        labavil="labs[lablist[labind]][i1][index]!='' or labs[lablist[labind]][i1][index+1]!=''"""


                    while(d1[org][1][i1][index]!=""  or d[orgc][1][i1][index]!="" or eval(totevalc) or eval(totevalc1) or d1[org][1][i1][index+1]!=""  or d[orgc][1][i1][index+1]!="" or eval(labavil) or eval(toteval) or eval(toteval1) or eval(ll) or index%2==1):
                        count+=1
                        cbox=randint(0,2)
                        if(cbox==0):
                            labind=randint(0,5)
                        elif(cbox==1):
                            i1=randint(0,4)
                        else:
                            index=randint(0,4)

                        if(j=="I Mtech CSE A"):
                            labind=6


                        flag+=1

                        if(flag==50000):

                            print(j)
                            print()
                            print(d[j])
                            print()
                            print()
                            print("faculty")
                            print(d[j][0][k][1])
                            print(d1[d[j][0][k][1]])
                            print("-----------Not generating lab----------------")
                            blocked.append([j,d[j][0][k][1],"xcom slots(2)"])
                            break
                        continue
                    r=d1[dum]
                    if("/" in dum):
                        for ma in range(len(fl)):
                            r=d1[fl[ma]]
                            r=str(r);r1=eval(r)
                            if(d[j][0][k][3]==3):
                                r1[1][i1][index+2]=j


                            r1[1][i1][index]=j
                            r1[1][i1][index+1]=j
                            r=eval(r)
                            d1[fl[ma]]=r1

                    r=str(r);r1=eval(r)


                    if(d[j][0][k][2]==3):

                            r1[1][i1][index+2]=j


                    r1[1][i1][index]=j
                    r1[1][i1][index+1]=j
                    r=eval(r)
                    if("/" in duc):
                        for mc in range(len(fc)):
                            r2=d[fc[mc]]
                            r2=str(r2);r3=eval(r2)
                            if(d[j][0][k][3]==3):
                                r3[1][i1][index+2]=r3[0][k][1]+" xcom"

                            r3[1][i1][index]=r3[0][k][1]+" xcom"
                            r3[1][i1][index+1]=r3[0][k][1]+" xcom"

                    r2=d[j]
                    r2=str(r2);r3=eval(r2)
                    if(d[j][0][k][3]==3):
                        r3[1][i1][index+2]=r3[0][k][1]+" xcom"

                    r3[1][i1][index]=r3[0][k][1]+" xcom"
                    r3[1][i1][index+1]=r3[0][k][1]+" xcom"

                    if(r3[0][k][0]==1):
                            r3[0][k][0]-=1
                            r3[0][k][3]-=1
                    else:
                        r3[0][k][0]-=2
                        r3[0][k][3]-=2
                    if(d[j][0][k][2]==3):
                        r3[0][k][0]-=1
                        r3[0][k][3]-=1
                    if(d[j][0][k][3]==3 and labavil!="False"):
                        labs[lablist[labind]][i1][index+2]=str(d[j][0][k][1])+" | " +str(j)

                    d[j]=r3
                    d1[d[j][0][k][1]]=r1


                    if(labavil!="False"):
                        labs[lablist[labind]][i1][index]=str(d[j][0][k][1])+" | "+ str(j)
                        labs[lablist[labind]][i1][index+1]=str(d[j][0][k][1])+" | " +str(j)







    for i in range(5):
        i1=i
        for j in d:
            for k in range(len(d[j][0])):
                if(int(d[j][0][k][2])>0):
                    index=randint(0,th-2)
                    count=0;count1=0;count2=0
                    las=int(d[j][0][k][4])
                
                    stind=sum(nl[:las]);endind=stind+nl[las]
                    labind=randint(stind,endind-1)
                    flag=0
                    myflag=True
                    toteval=""
                    duc=j
                    toteval1=""
                    totevalc=""
                    totevalc1=""
                    if("/" in duc):
                        duc=duc[:-5]
                        fc=duc.split("/");orgc=fc[0];
                        for i in range(1,len(duc)):
                            totevalc+="d[fc[{}]][1][i1][index]!='' or".format(i)
                            totevalc1+="d[fc[{}]][1][i1][index+1]!='' or".format(i)
                        totevalc=totevalc[:-3];totevalc1=totevalc1[:-3]
                    else:
                        totevalc="False"
                        totevalc1="False"
                        orgc=duc
                    dum=d[j][0][k][1]
                    if("/" in dum):
                        fl=dum.split("/");org=fl[0];dup="d1[fl[1]][1][i1][index]!=''";dup1="d1[fl[1]][1][i1][index+1]!=''";
                        for i in range(1,len(fl)):
                            toteval+="d1[fl[{}]][1][i1][index]!='' or ".format(i)
                            toteval1+="d1[fl[{}]][1][i1][index+1]!='' or ".format(i)
                        toteval=toteval[:-3]
                        toteval1=toteval1[:-3]

                    else:
                        org=dum;dup="False";dup1="False";toteval="False";toteval1="False"
                    if(d[j][0][k][2]==3):
                        index=4
                        #print("yes thresssslotss lab***********************************************")
                        ll="d1[org][1][i1][index+2]!=''  or d[j][1][i1][index+2]!='' or labs[lablist[labind]][i1][index+2]!=''"
                    else:
                        ll="False"
                    """if(j=="II Year G" or j=="II Year C"):
                        labind=randint(4,5)"""
                    if(j=="I Mtech CSE A"):
                        labind=0
                    if(".1"  in str(d[j][0][k][2])):
                        labavil='False'
                    else:
                        labavil="labs[lablist[labind]][i1][index]!='' or labs[lablist[labind]][i1][index+1]!=''"
                    print("....................................................................")
                    """print(j)
                    print(d1[org][1][i1][index],index,i1)
                    print(d[orgc][1][i1][index],index,i1)
                    print(eval(labavil))
                    print(eval(toteval1))
                    print(eval(totevalc))
                    print(eval(toteval))
                    print(eval(totevalc1))
                    print(eval(ll))
                    print(d1[org][1][i1][index+1])
                    print(d[orgc][1][i1][index+1])"""


                    while(d1[org][1][i1][index]!=""  or d[orgc][1][i1][index]!="" or eval(totevalc) or eval(totevalc1) or d1[org][1][i1][index+1]!=""  or d[orgc][1][i1][index+1]!="" or eval(labavil) or eval(toteval) or eval(toteval1) or eval(ll) or index%2==1):
                        count+=1
                        cbox=randint(0,2)
                        if(cbox==0):
                            stind=sum(nl[:las]);endind=stind+nl[las]
                            labind=randint(stind,endind-1)
                        elif(cbox==1):
                            i1=randint(0,4)
                        else:
                            index=randint(0,th-2)
                            if(d[j][0][k][2]==3):
                                index=4
                          

                        if(j=="I Mtech CSE A"):
                            labind=0


                        flag+=1

                        if(flag==50000):

                            print(j)
                            print()
                            print(d[j])
                            print()
                            print()
                            print("faculty")
                            print(d[j][0][k][1])
                            print(d1[d[j][0][k][1]])
                            print("-----------Not generating lab----------------")
                            blocked.append([j,d[j][0][k][1],"Lab slots(2)"])
                            break
                        continue
                    r=d1[dum]
                    if("/" in dum):
                        for ma in range(len(fl)):
                            r=d1[fl[ma]]
                            r=str(r);r1=eval(r)
                            if(d[j][0][k][2]==3):
                                r1[1][i1][index+2]=j


                            r1[1][i1][index]=j
                            r1[1][i1][index+1]=j
                            r=eval(r)
                            d1[fl[ma]]=r1

                    r=str(r);r1=eval(r)


                    if(d[j][0][k][2]==3):

                            r1[1][i1][index+2]=j


                    r1[1][i1][index]=j
                    r1[1][i1][index+1]=j
                    r=eval(r)
                    if("/" in duc):
                        for mc in range(len(fc)):
                            r2=d[fc[mc]]
                            r2=str(r2);r3=eval(r2)
                            if(d[j][0][k][2]==3):
                                r3[1][i1][index+2]=r3[0][k][1]+" lab"

                            r3[1][i1][index]=r3[0][k][1]+" lab"
                            r3[1][i1][index+1]=r3[0][k][1]+" lab"

                    r2=d[j]
                    r2=str(r2);r3=eval(r2)
                    if(d[j][0][k][2]==3):
                        r3[1][i1][index+2]=r3[0][k][1]+" lab"

                    r3[1][i1][index]=r3[0][k][1]+" lab"
                    r3[1][i1][index+1]=r3[0][k][1]+" lab"

                    if(r3[0][k][0]==1):
                            r3[0][k][0]-=1
                            r3[0][k][2]-=1
                    else:
                        r3[0][k][0]-=2
                        r3[0][k][2]-=2
                    if(d[j][0][k][2]==3):
                        r3[0][k][0]-=1
                        r3[0][k][2]-=1
                    if(d[j][0][k][2]==3 and labavil!="False"):
                        labs[lablist[labind]][i1][index+2]=str(d[j][0][k][1])+" | " +str(j)

                    d[j]=r3
                    d1[d[j][0][k][1]]=r1


                    if(labavil!="False"):
                        labs[lablist[labind]][i1][index]=str(d[j][0][k][1])+" | "+ str(j)
                        labs[lablist[labind]][i1][index+1]=str(d[j][0][k][1])+" | " +str(j)



    i1=randint(0,4)
    j2="IV Year CBCS"
    count=0
    count1=0



    for i in range(5):
        i1=i
        for j in d:
            for k in range(len(d[j][0])):
                dum=d[j][0][k][1]
                toteval=""
                duc=j


                toteval1=""
                totevalc=""
                totevalc1=""
                if("/" in duc):
                    duc=duc[:-5]
                    flt=d[j][0][k][1]

                    fc=duc.split("/");orgc=fc[0];

                    for i in range(1,len(fc)):
                        totevalc+="d[fc[{}]][1][i1][index]!='' or ".format(i)
                        totevalc1+="d[fc[{}]][1][i1][index+1]!='' or ".format(i)
                    totevalc=totevalc[:-3];totevalc1=totevalc1[:-3]
                else:
                    totevalc="False"
                    totevalc1="False"
                    orgc=duc
                if("/" in dum):
                    fl=dum.split("/");org=fl[0];dup="d1[fl[1]][1][i1][index]!=''";dup1="d1[fl[1]][1][i1][index+1]!=''";
                    for i in range(1,len(fl)):
                        toteval+="d1[fl[{}]][1][i1][index]!='' or ".format(i)
                    toteval=toteval[:-3]
                else:
                    org=dum;dup="False";toteval="False";

                if(int(d[j][0][k][0])>0):
        

                    index=randint(0,6)
                    count=0
                    flag=0
                    count1=0
                    print(d1[org][1][i1][index],j)
                    print(d[orgc][1][i1][index])
                    print(eval(toteval))
                    
                    while(d1[org][1][i1][index]!="" or d[orgc][1][i1][index]!="" or eval(toteval) or eval(totevalc) ):
                        flag+=1
                        cbox=randint(0,1)
                        if(cbox==0):
                            index=randint(0,6)
                        else:
                            i1=randint(0,4)
                        flag+=1

                        if(flag==100000):


                            print(j)
                            print("class timetable");print()
                            print(d[j])
                            print()
                            print("faculty name ")
                            print(d[j][0][k][1])
                            print();print("faculty time table")
                            print(d1[d[j][0][k][1]][1])
                            print("---------------- NOT GENERATING ----------------")
                            blocked.append([j,d[j][0][k][1],"Normal slots(1)"])
                            print()
                            print()
                            break



                        continue


                        #print(d1[d[j][0][k][1]][1][i][index],d[j][1][i][index])

                    if("/" in dum):
                        for ma in range(len(fl)):
                            r=d1[fl[ma]]
                            r=str(r);r1=eval(r)
                            if(d[j][0][k][2]==3):
                                r1[1][i1][index+2]=j


                            r1[1][i1][index]=j

                            r=eval(r)
                            d1[fl[ma]]=r1
                    if("/" in duc):
                        for mc in range(len(fc)):
                            r2=d[fc[mc]]



                            r2=str(r2);r3=eval(r2)
                            if(d[j][0][k][2]==3):
                                r3[1][i1][index+2]=r3[0][k][1]

                            r3[1][i1][index]=flt
                            r3[1][i1][index]=flt
                            r3[0][k][0]-=1
                            d[fc[mc]]=r3
                            



                    r=d1[d[j][0][k][1]]
                    r=str(r);r1=eval(r)

                    r1[1][i1][index]=j
                    r=eval(r)
                    r2=d[j]
                    r2=str(r2);r3=eval(r2)
                    r3[1][i1][index]=r3[0][k][1]
                    r3[0][k][0]-=1
                    d[j]=r3

                    d1[d[j][0][k][1]]=r1
                    
    faculty=d1
    student=d

    import csv

    days=["monday","tuesday","wednsday","thursday","friday"]
    with open('Faculty_gen.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        for i in faculty:
            writer.writerows([["-"*30,"-"*30,"-"*30,"-"*30,i.upper(),"-"*30,"-"*30,"-"*30,"-"*30]])
            rw=["Day"];ex=[lt+1 for lt in range(th)];rw.extend(ex)
            writer.writerows([rw])
            for j in range(len(faculty[i][1])):
                faculty[i][1][j].insert(0,days[j])
            writer.writerows(faculty[i][1])
            #writer.writerows([[""]*(th+1)])

    with open('Students_gen.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        for i in student:
            writer.writerows([["-"*30,"-"*30,"-"*30,"-"*30,i.upper(),"-"*30,"-"*30,"-"*30,"-"*30]])
            rw=["Day"];ex=[lt+1 for lt in range(th)];rw.extend(ex)
            writer.writerows([rw])
            for j in range(len(student[i][1])):
                student[i][1][j].insert(0,days[j])

            writer.writerows(student[i][1])
            #writer.writerows([[""]*(th+1)])
    days=["monday","tuesday","wednsday","thursday","friday"]

    with open('Lab_gen.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        for i in labs:
            writer.writerows([["-"*30,"-"*30,"-"*30,"-"*30,i.upper(),"-"*30,"-"*30,"-"*30,"-"*30]])
            rw=["Day"];ex=[lt+1 for lt in range(th)];rw.extend(ex)

            writer.writerows([rw])
            
            for j in range(len(labs[i])):
                labs[i][j].insert(0,days[j])
            writer.writerows(labs[i])
           # writer.writerows([[""]*(th+1)])
    print("Helooooooooooooooooooooooooo")
   
  

    return render_template("Squadfree/block2.html",generated=True,assigned=True)
    return send_file("fourthsemStudents.csv",as_attachment=True)



@app.route("/stud")
def stud():
    return send_from_directory("","Students_gen.csv", as_attachment=True)

@app.route("/blockings")
def blockings():
    global blocked
    return render_template("blockings.html",blocks=blocked)

@app.route("/facu")
def facu():
    return send_from_directory("","Faculty_gen.csv", as_attachment=True)
    #return send_file("Faculty_gen.csv",as_attachment=True)



@app.route("/labs")
def labs():
    return send_from_directory("","Lab_gen.csv", as_attachment=True)

   # return static_file("Faculty_gen.csv", root='/home/pshiridikumar')
    #return send_file("Lab_gen.csv",as_attachment=True)








@app.route("/download2")
def download2():
    return send_file("trial.csv",as_attachment=True)

@app.route("/viewfile")
def viewfile():
    import pandas as pd
    d=pd.read_csv("trial.csv")
    d.fillna("nill",inplace=True)

    return render_template("viewfile.html",file=d,headb=False)


@app.route("/viewfile1")
def viewfile1():
    import pandas as pd
    d=pd.read_csv("Students_gen.csv")
    d.fillna("nill",inplace=True)

    return render_template("viewfile.html",file=d,headb=False)

@app.route("/viewfile2")
def viewfile2():
    import pandas as pd
    d=pd.read_csv("Faculty_gen.csv")
    d.fillna("nill",inplace=True)
 
    return render_template("viewfile.html",file=d,headb=False)

@app.route("/viewfile3")
def viewfile3():
    import pandas as pd
    d=pd.read_csv("Lab_gen.csv")
    d.fillna("nill",inplace=True)
 
    return render_template("viewfile.html",file=d,headb=False)

@app.route("/")
def ind():
    return render_template("Squadfree/block1.html",filebool=False,submitted=False)
    #return render_template("first.html",filebool=False,submitted=False)

global orgdata
@app.route("/finalsub")
def finalsub():
    return redirect(url_for('gen'))
    return render_template("Squadfree/block2.html",filebool=False,submitted=True,assigned=False)
    return redirect(url_for('viewresult',name ="submitted1.csv"))


@app.route('/pie',methods=['POST'])
def pie():
    global orgdata
    tmp1 = request.form.get('array')
    tmp2= int(request.form.get('rowlen'))
    tmp3= int(request.form.get('arrlen'))
  

    fin=tmp1.split(",")
    l=[]
 
    for i in range((len(fin)//tmp2)):
        x=fin[i*tmp2:tmp2*(i+1)]
        l.append(x)
    cols=l[0]
    l.pop(0)
    d2=pd.DataFrame(l)



    d2.columns=cols
 
    orgdata=d2
    orgdata.to_csv("submitted1.csv")


    return render_template("viewfile.html",file=d2)



@app.route("/gen")
def gen():
    global orgdata
    orgdata.to_csv("submitted1.csv")
    import pandas as pd
    print(orgdata)
    return redirect(url_for('viewresult',name ="submitted1.csv"))

@app.route("/stud_choices",methods=["POST"])
def stud_choices():
    global d
    return jsonify(keys1=list(d.keys()));

@app.route("/fac_choices",methods=["POST"])
def fac_choices():
    global d1
    return jsonify(keys=list(d1.keys()));




@app.route("/fac_sel",methods=["POST"])
def fac_sel():
    global d1
    selected=request.form.get("selected")
    print(d1[selected])
    print(d1)
    return jsonify(dic=d1[selected])

@app.route("/stud_sel",methods=["POST"])
def stud_sel():
    global d
    selected=request.form.get("selected")
    return jsonify(dic=d[selected])

@app.route("/teams")
def teams():
    return render_template("team.html")

@app.route("/fix_submit_class",methods=["POST"])
def fix_clas():
    global d,d1,nl
    name=request.form.get("name")

    nar=request.form.get("narr")

    l=nar.replace("\nLab slot ","")
    l=l.replace("\n","")
    l=l.split(",")
    import numpy as np
    nar=np.array(l).reshape(5,7)
    lar=request.form.get("labarr")
    l1=lar.replace("\nLab slot ","")
    l1=l1.replace("\n","")
    l1=l1.split(",")
    labind=0
    lar=np.array(l1).reshape(5,7)
    if(name in d):

        x=str(d[name])
        y=eval(x);y1=y[1];y0=y[0];las=0;flag=0

        for i in range(len(lar)):
            for j in range(len(lar[i])):
                if(lar[i][j]!=""):

                    if(lar[i][j] in d1):
                        x1=str(d1[lar[i][j]])
                        if("/" in lar[i][j]):
                            fl=lar[i][j].split("/")
                            for fac in fl:
                                if(fac in d1):
                                    fc=str(d1[fac]);fc0=eval(fc);fc1=fc0[1];fc2=fc0[0]
                                    fc1[i][j]=name+" lab"
                                    d1.update({fac:[fc2,fc1]})
                        if("/" in name):
                            name1=name[:-5]
                            sl=name1.split("/")
                            for stu in sl:
                                if stu in d:
                                    st=str(d[stu]);st0=eval(st);st1=st0[1];st2=st0[0]
                                    st1[i][j]=lar[i][j]+" lab"
                                    d.update({stu:[st2,st1]})



                        y2=eval(x1);y3=y2[1]
                        y3[i][j]=name+" lab"
                        d1.update({lar[i][j]:[y2[0],y3]})
                        y1[i][j]=lar[i][j]+" lab"
                    for t in range(len(y0)):
                        if(y0[t][1]==lar[i][j]):
                            y0[t][2]-=1
                            y0[t][0]-=1
                            las=int(y0[t][4])
                    stind=sum(nl[:las]);endind=stind+nl[las]

                    if(flag==0):
                        flag=1
                        labind=randint(stind,endind-1)

                    print(labind)

                    while(labs[lablist[labind]][i][j]!=""):
                        labind=randint(stind,endind-1)
                    labs[lablist[labind]][i][j]=name+"|"+lar[i][j]
                    y1[i][j]=lar[i][j]+" lab"
                else:
                    flag=0

        d.update({name:[y0,y1]})
        x=str(d[name])
        y=eval(x);y1=y[1];y0=y[0]
        for i in range(len(nar)):
            for j in range(len(nar[i])):
                if(nar[i][j]!=""):
                    x1=str(d1[nar[i][j]])
                    if("/" in nar[i][j]):
                        fl=nar[i][j].split("/")
                        for fac in fl:
                            if(fac in d1):
                                fc=str(d1[fac]);fc0=eval(fc);fc1=fc0[1];fc2=fc0[0]
                                fc1[i][j]=name
                                d1.update({fac:[fc2,fc1]})
                    if("/" in name):
                        name1=name[:-5]
                        sl=name1.split("/")
                        for stu in sl:
                            if stu in d:
                                st=str(d[stu]);st0=eval(st);st1=st0[1];st2=st0[0]
                                st1[i][j]=nar[i][j]
                                d.update({stu:[st2,st1]})
                    y2=eval(x1);y3=y2[1]
                    y3[i][j]=name
                    d1.update({nar[i][j]:[y2[0],y3]})
                    y1[i][j]=nar[i][j]
                    for t in range(len(y0)):
                        if(y0[t][1]==nar[i][j]):
                            y0[t][0]-=1
                            print(y0)
                    y1[i][j]=nar[i][j]

        d.update({name:[y0,y1]})
        print(d)
    flag=0

    if(name in d1):
        x=str(d1[name])
        y=eval(x);y1=y[1];y0=y[0]

        for i in range(len(lar)):
            for j in range(len(lar[i])):
                if(lar[i][j]!=""):
                    if(lar[i][j] in d):
                        x1=str(d[lar[i][j]])
                        if("/" in lar[i][j]):
                            name1=lar[i][j][:-5]
                            sl=name1.split("/")
                            for stu in sl:
                                if stu in d:
                                    st=str(d[stu]);st0=eval(st);st1=st0[1];st2=st0[0]
                                    st1[i][j]=name+" lab"
                                    d.update({stu:[st2,st1]})
                        if("/" in name):
                            fl=name.split("/")
                            for fac in fl:
                                if(fac in d1):
                                    fc=str(d1[fac]);fc0=eval(fc);fc1=fc0[1];fc2=fc0[0]
                                    fc1[i][j]=lar[i][j]+" lab"
                                    d1.update({fac:[fc2,fc1]})
                  

                        y2=eval(x1);y3=y2[1]
                        y3[i][j]=name+" lab"
                        for it in range(len(y2[0])):
                            if(y2[0][it][1]==name):
                                y2[0][it][2]-=1;y2[0][it][0]-=1
                                las=int(y2[0][it][4])
                        d.update({lar[i][j]:[y2[0],y3]})
                        y1[i][j]=lar[i][j]+" lab"
                    y1[i][j]=lar[i][j]+" lab"
                    stind=sum(nl[:las]);endind=stind+nl[las]
                    print(stind,endind,las,nl)
                    if(flag==0):
                        flag=1
                        labind=randint(stind,endind-1)
                    while(labs[lablist[labind]][i][j]!=""):
                        labind=randint(0,3)
                    labs[lablist[labind]][i][j]=name+"|"+lar[i][j]
                else:
                    flag=0
        d1.update({name:[y0,y1]})
        x=str(d1[name])
        y=eval(x);y1=y[1];y0=y[0]

        for i in range(len(nar)):
            for j in range(len(nar[i])):
                if(nar[i][j]!=""):
                    x1=str(d[nar[i][j]])
                    if("/" in nar[i][j]):
                        name1=nar[i][j][:-5]
                        sl=name1.split("/")
                        for stu in sl:
                            if stu in d:
                                st=str(d[stu]);st0=eval(st);st1=st0[1];st2=st0[0]
                                st1[i][j]=name
                                d.update({stu:[st2,st1]})
                    if("/" in name):
                        fl=name.split("/")
                        for fac in fl:
                            if(fac in d1):
                                fc=str(d1[fac]);fc0=eval(fc);fc1=fc0[1];fc2=fc0[0]
                                print(fc1,fc)
                                fc1[i][j]=nar[i][j]
                                d1.update({fac:[fc2,fc1]})
                    y2=eval(x1);y3=y2[1];y4=y2[0]
                    y3[i][j]=name
                    for k in range(len(y4)):
                        if(y4[k][1]==name):
                            y4[k][0]-=1
                    d.update({nar[i][j]:[y4,y3]})
                    y1[i][j]=nar[i][j]
                    for t in range(len(y0)):
                        if(y0[t][1]==nar[i][j]):
                            y0[t][0]-=1
                    y1[i][j]=nar[i][j]

    d1.update({name:[y0,y1]})
    global lab_copy,d_copy,d1_copy
    lab_copy=str(labs)
    d_copy=d.copy()
    d1_copy=d1.copy()
    return ("hello world")



@app.route('/index1',methods = ['POST'])
def index1():
    if request.method == 'POST':
        print(11111111111)
        global nl,th,tl
        user = request.files['myfile']
        
        user.save(secure_filename("main.csv"))
        import pandas as pd
        user1="main.csv"
        print(user1)
        d=pd.read_csv(user1)
        print(d.columns)
        print(d["CBCS"])
        
       
        
        if("Unnamed: 0" in d.columns):
            d.drop(columns=["Unnamed: 0"],inplace=True)
        csm=d.columns
        if("labtype" not in csm):
            d["labtype"]=[0 for i in range(len(d))]
        if("x component" not in csm):
            d["x component"]=[0 for i in range(len(d))]
        if("lab_availablity" not in  csm):
            d["lab_availability"]=[0 for i in range(len(d))]
        if("CBCS" not in d.columns):
            d["CBCS"]=[0 for i in range(len(d))]
        else:
            dc=[]

            for i in range(len(d)):
                if(str(d["CBCS"][i])!="nan"):
                    dc.append(int(d["CBCS"][i]))
                    print(d["CBCS"][i])
                else:
                    dc.append(int(0))
            d.drop(columns=["CBCS"],inplace=True,axis=1)
            d["CBCS"]=dc
            print(d["CBCS"])

        tl=int(request.form["labtypes"])
        th=int(request.form["totalhrs"])
        print(d.columns)
        d.columns=["Year","Course Teachers","Section","Course Name","theorey","lab","labavil","x com","labtype","CBCS"]
        filebool=True
        return render_template("Squadfree/block1.html",file=d,filebool=filebool,submitted=False,entered=False,tl=tl)

@app.route("/samplefile")
def samplefile():
    return send_from_directory("","samplefile.csv", as_attachment=True)

@app.route("/index2",methods=["POST"])
def index2():
    if(request.method=="POST"):
        print(22222)
        global nl
        global tl,th
        ln=request.form
        nl=[]
        for i in ln:
            if(ln[i]==""):
                nl.append(0)
            else:
                nl.append(int(ln[i]))
        print(nl)
        filebool=True
        d=pd.read_csv("main.csv")

        csm=d.columns
        if("labtype" not in csm):
            d["labtype"]=[0 for i in range(len(d))]
        if("x component" not in csm):
            d["x component"]=[0 for i in range(len(d))]
        if("lab_availability" not in  csm):
            d["lab_availability"]=[0 for i in range(len(d))]
        if("CBCS" not in d.columns):
            d["CBCS"]=[0 for i in range(len(d))]
        else:
            dc=[]
            for i in range(len(d)):
                if(str(d["CBCS"][i])!="nan"):
                    dc.append(int(d["CBCS"][i]))
                else:
                    dc.append(int(0))
            d.drop(columns=["CBCS"],inplace=True,axis=1)
            d["CBCS"]=dc
        ma=max(d["labtype"])
        print(ma)
        error="True"
        if("Unnamed: 0" in d.columns):
            d.drop(columns=["Unnamed: 0"],inplace=True)
        print(d.columns)
        d.columns=["Year","Course Teachers","Section","Course Name","theorey","lab","labavil","x com","labtype","CBCS"]
        
        for i in range(len(nl)):
            temp=d[d.labtype==i]
            temp1=temp[temp.labavil==0]
            tots=sum(temp1["lab"])
            print(tots)
            if(tots>nl[i]*th*5):
                return render_template("Squadfree/block1.html",file=d,filebool=filebool,submitted=False,entered=False,tl=tl,error=True,avil=True,lt=i)
            
        if( (ma+1)!=len(nl) ):
            return render_template("Squadfree/block1.html",file=d,filebool=filebool,submitted=False,entered=False,tl=tl,error=True)
        else:
            return render_template("Squadfree/block1.html",file=d,filebool=filebool,submitted=False,entered=True,tl=tl,error=False)



        #return render_template("Squadfree/block1.html",file=d,filebool=filebool,submitted=False,entered=True,error=error)
        


if __name__ == '__main__':
   app.run(debug=True)

