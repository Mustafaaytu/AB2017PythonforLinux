def str():
    s="eren";
    s1="esen";
    print(s+s1);
    print(s.split("r"));
    print (s*5);
    periler="-";
    print(periler.join([s,s1]));

    print(periler.join(["yeliz","yavuz","eren","mustafa"]));
    s2=" eren";
    print(s2,s2.strip());

def tapıllar():
    t=("yavuz","eren","yelz");
    t1=(28,29,"Hello World");
    print(t+t1);
def listeler():
    l=["15","a,","ayse","veli","ali",5];
    l1=[4];
    print(l+l1);
    l1.append("msi");
    print(l1);
    l1.pop(0);
    print(l1);
    print(l[1]);
    #print(l[:-2];
    print(l[-2:]);
    print("istenilen aralık = ",l[0:2]);
def sozlukler():
    d={"akademik":"bilisim","eren":"esen",3:"uc"};
    print(d.items());
    print(d.keys());
    print(d.values());
    d[5]="bes";
    print(d.items());
    print(d[3]);
    d["self"]=d;
    print(d.items());
    del d["eren"];
    print(d.items());

sozlukler();
