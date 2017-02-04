#__init__.py yani import edilebilir ilk çalışan __init__.py
#pass-> bisey yapma


def ana_fonksiyon():
    pass;
def temel_turleri_goster():
    s="merhaba";
    i=18;
    f=18.000000004;
    t=(s,i,f);
    print(s,i,f,t,"\n");
    #demetler ,,tapıllar
    t2=s,i,f;
    l=["yeliz",2.71,37500000,t];
    #listeler
    d={"yavuz" : "yeliz", "eren": l, "bin":1000,55:"ellibes"};
    #sözlükler
    la=lambda x,y:x**y;

    def fn(x,y):
        return x**y;
    class c():
        def __init__(self,arg1,arg2):
            self.x=arg1;
            self.y=arg2;
        def calculate(self):
            return self.x**self.y;
    nesne=c(1,5);
