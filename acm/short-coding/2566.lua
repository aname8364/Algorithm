a=-1;for i=0,80 do x=io.read"n"if x>a then a,b,c=x,i//9+1,i%9+1;end;end;p=print;p(a)p(b..' '..c)