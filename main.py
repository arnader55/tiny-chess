import json,os,sys,urllib.request as w,urllib.error as x
U=os.environ.get("MAKEFUN_ENV_URL") or sys.exit("no env")
def P(p,b):
 try:return json.load(w.urlopen(w.Request(U+p,json.dumps(b).encode(),{"content-type":"application/json"})))
 except x.HTTPError as e:sys.exit(e)
V=[0,100,320,330,500,900,0];CF=[0,0,3,2,0,1,-4]
BD=(-17,-15,15,17);RD=(-16,-1,1,16);KD=BD+RD;ND=(-31,-33,-18,-14,14,18,31,33)
SD=[(d,3)for d in BD]+[(d,4)for d in RD]
JD=[(d,2)for d in ND]+[(d,6)for d in KD]
N=[0];L=40000
def F(f):
 p=f.split();B=[0]*128;r=7;d=0
 for z in p[0]:
  if z=="/":r-=1;d=0
  elif z.isdigit():d+=int(z)
  else:
   q=".PNBRQK".index(z.upper());B[r*16+d]=q if z.isupper()else-q;d+=1
 s=1 if p[1]=="w"else-1;c=0;e=-1
 for z in p[2]:c|={"K":1,"Q":2,"k":4,"q":8}.get(z,0)
 if p[3]!="-":e=ord(p[3][0])-97+(ord(p[3][1])-49)*16
 return B,s,c,e
def A(B,q,b):
 if q&0x88:return 0
 for d in(-15*b,-17*b):
  y=q+d
  if not y&0x88 and B[y]==b:return 1
 for d,t in JD:
  y=q+d
  if not y&0x88 and B[y]==t*b:return 1
 for d,t in SD:
  y=q
  while 1:
   y+=d
   if y&0x88:break
   v=B[y]
   if v:
    if v==t*b or v==5*b:return 1
    break
 return 0
def G(B,s,c,e):
 for f,p in enumerate(B):
  if p*s<=0:continue
  a=abs(p)
  if a==1:
   d=16*s;t=f+d
   if not t&0x88 and not B[t]:
    if t>>4==7*(s>0):
     for q in(5,4,3,2):yield f,t,q
    else:
     yield f,t,0
     if f>>4==6-5*(s>0):
      u=f+2*d
      if not B[u]:yield f,u,0
   for dt in(d-1,d+1):
    t=f+dt
    if t&0x88:continue
    if B[t]*s<0:
     if t>>4==7*(s>0):
      for q in(5,4,3,2):yield f,t,q
     else:yield f,t,0
    elif t==e:yield f,t,0
  elif a==2 or a==6:
   for d in(ND if a==2 else KD):
    t=f+d
    if not t&0x88 and B[t]*s<=0:yield f,t,0
  else:
   for d in(BD if a==3 else RD if a==4 else KD):
    t=f
    while 1:
     t+=d
     if t&0x88:break
     if B[t]*s>0:break
     yield f,t,0
     if B[t]:break
 for K0,bt,tg in((4,1,6),(4,2,2),(116,4,118),(116,8,114)):
  if c&bt:
   g=1 if tg>K0 else -1
   if not B[K0+g] and not B[K0+2*g] and(g>0 or not B[K0+3*g])and not A(B,K0,-s) and not A(B,K0+g,-s) and not A(B,K0+2*g,-s):yield K0,tg,0
def D(B,s,f,t,p,c,e):
 M=B[:];q=M[f];M[f]=0
 M[t]=p*s if p else q
 if abs(q)==1 and t==e and not B[t]:M[t-16*s]=0
 if abs(q)==6 and abs(t-f)==2:
  rs=t+1 if t>f else t-2;rt=t-1 if t>f else t+1;M[rs]=0;M[rt]=4*s
 n=c
 if abs(q)==6:n&=~(3 if s>0 else 12)
 for z,b in((0,2),(7,1),(112,8),(119,4)):
  if f==z or t==z:n&=~b
 return M,n,f+16*s if abs(q)==1 and abs(t-f)==32 else -1
def E(B,s):
 t=0
 for q,p in enumerate(B):
  if p:
   a=abs(p);f=q&7;r=q>>4;m=7-(abs(f-3)+abs(r-3))
   b=CF[a]*m
   if a==1:b+=6*((r-1) if p>0 else 6-r)+(3 if f in(3,4)else 0)
   if a==4 and r==(6 if p>0 else 1):b+=12
   t+=(V[a]+b)*(1 if p>0 else -1)
 return t*s
def K(B,s):
 for q,p in enumerate(B):
  if p==6*s:return q
def O(ms,B):
 return sorted(ms,key=lambda m:V[abs(B[m[0]])]-10*V[abs(B[m[1]])]-(50 if m[2]else 0))
def S(B,s,c,e,d,a,b):
 N[0]+=1
 if N[0]>L:raise StopIteration
 k=K(B,s);ck=A(B,k,-s)
 if d==0:
  st=E(B,s)
  if not ck:
   if st>=b:return b
   if st>a:a=st
 ms=list(G(B,s,c,e)) if d or ck else[m for m in G(B,s,c,e) if B[m[1]] or(m[1]==e and abs(B[m[0]])==1)]
 fd=0
 for f,t,p in O(ms,B):
  M,n,o=D(B,s,f,t,p,c,e);kk=t if abs(B[f])==6 else k
  if A(M,kk,-s):continue
  fd=1
  z=-S(M,-s,n,o,d-1 if d else 0,-b,-a)
  if z>a:a=z
  if a>=b:break
 if not fd:return -20000-d if ck else(0 if d else a)
 return a
def u(f,t,p):
 return chr(97+f%8)+str(f//16+1)+chr(97+t%8)+str(t//16+1)+("nbrq"[p-2] if p else"")
def C(fen,lg):
 B,s,c,e=F(fen);N[0]=0;bs=lg[0];k=K(B,s)
 for d in range(1,7):
  try:
   ms=[m for m in G(B,s,c,e) if u(*m) in lg]
   bb=None;bv=-99999
   for f,t,p in O(ms,B):
    M,n,o=D(B,s,f,t,p,c,e);kk=t if abs(B[f])==6 else k
    if A(M,kk,-s):continue
    z=-S(M,-s,n,o,d-1,-99999,99999)
    if z>bv:bv=z;bb=(f,t,p)
   if bb:bs=u(*bb)
  except StopIteration:break
 return bs
if __name__=="__main__":
 g=P("/game",{})
 while g["status"]!="done":
  while g["status"]=="your_move":g=P("/move",{"game":g["game"],"move":C(g["fen"],g["legal_moves"])})
  g=P("/game",{})
