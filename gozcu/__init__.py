#__init__.py yani import edilebilir ilk çalışan __init__.py
#pass-> bisey yapma


def ana_fonksiyon():
    pass;
def temel_turleri_goster():
    s="merhaba";
    i=18;
    f=18.000000004;
    t=(s,i,f);
    #demetler ,,tapıllar
    t2=s,i,f;
    l=["yeliz",2.71,37500000,t];
    #listeler
    d={"yavuz" : "yeliz", "eren": l, "bin":1000,55:"ellibes"};
    #sözlükler
    la=lamda x,y:x**y;

def fn(x,y):
    return x**y;
