"""Monthly water-balance model for the candidate towns — v2.
Two PET methods so the semi-arid signal is not masked:
  * Thornthwaite (1948): temperature-only -> LOWER bound on demand (understates sunny valleys).
  * Hargreaves (FAO-56): radiation-aware (uses extraterrestrial radiation + diurnal T range)
    -> better for sunny semi-arid valleys; used as the PRIMARY index.
Scenarios: baseline; 2050 (dept warming, flat P); 2085-high (more warming, -10% P);
El Nino drought (P x0.60 = documented -40% class event that drove 2016 rationing).
Single-bucket soil store (WHC=100 mm). Inputs: code/data_inputs.py (IDEAM normals).
"""
import numpy as np, pandas as pd, sys, math
sys.path.insert(0,'code')
from data_inputs import NORMALS

DAYS=np.array([31,28,31,30,31,30,31,31,30,31,30,31]); MID_DOY=np.array([15,45,74,105,135,166,196,227,258,288,319,349])
MONTHS=['J','F','M','A','M','J','J','A','S','O','N','D']; WHC=100.0
# est. diurnal temperature range (Tmax-Tmin, degC): sunny dry valleys large; humid/cold smaller
# Moniquira = 10 (humid class, same as arcabuco/el_colegio): NASA POWER mean diurnal range there
# is 9.1 C and climate-data.org's own max-min spread ~9.9 C. POWER is NOT used to reset the dry
# valleys' DTR - its cells put Villa de Leyva and Sachica in one grid box and would flatten the
# semi-arid signal this model exists to preserve.
DTR={'villa_de_leyva':14,'sachica':15,'tunja':12,'arcabuco':10,'el_colegio':10,'moniquira':10}
# department warming (IDEAM ensemble): Boyaca vs Cundinamarca
DEPT_DT={'villa_de_leyva':(1.6,2.4),'sachica':(1.6,2.4),'tunja':(1.6,2.4),'arcabuco':(1.6,2.4),
         'el_colegio':(1.5,2.3),'moniquira':(1.6,2.4)}

def ra_mm(lat):  # extraterrestrial radiation, mm/day equivalent, per month (FAO-56)
    phi=math.radians(lat); out=[]
    for doy in MID_DOY:
        dr=1+0.033*math.cos(2*math.pi*doy/365); dec=0.409*math.sin(2*math.pi*doy/365-1.39)
        x=-math.tan(phi)*math.tan(dec); x=max(-1,min(1,x)); ws=math.acos(x)
        Ra=(24*60/math.pi)*0.0820*dr*(ws*math.sin(phi)*math.sin(dec)+math.cos(phi)*math.cos(dec)*math.sin(ws))
        out.append(0.408*Ra)
    return np.array(out)

def daylength(lat):
    phi=math.radians(lat)
    return np.array([2*math.degrees(math.acos(max(-1,min(1,-math.tan(phi)*math.tan(math.radians(23.45*math.sin(math.radians(360*(284+d)/365))))))))/15 for d in MID_DOY])

def pet_thornthwaite(T,lat):
    T=np.array(T,float); I=np.sum([(max(t,0)/5)**1.514 for t in T])
    a=6.75e-7*I**3-7.71e-5*I**2+1.792e-2*I+0.49239
    petu=np.array([16*(10*max(t,0)/I)**a if t>0 else 0 for t in T]); N=daylength(lat)
    return petu*(N/12)*(DAYS/30)

def pet_hargreaves(T,lat,dtr):
    T=np.array(T,float); Ra=ra_mm(lat); tmax=T+dtr/2; tmin=T-dtr/2
    return 0.0023*(T+17.8)*np.sqrt(np.maximum(tmax-tmin,0))*Ra*DAYS

def soil_balance(P,PET):
    P=np.array(P,float); PET=np.array(PET,float); st=WHC
    for _ in range(3):
        for i in range(12):
            d=P[i]-PET[i]; st=min(WHC,st+d) if d>=0 else max(0,st+d)
    AET=np.zeros(12); DEF=np.zeros(12); SUR=np.zeros(12)
    for i in range(12):
        d=P[i]-PET[i]
        if d>=0: AET[i]=PET[i]; SUR[i]=max(0,(st+d)-WHC); st=min(WHC,st+d)
        else: draw=min(st,-d); AET[i]=P[i]+draw; st-=draw; DEF[i]=PET[i]-AET[i]
    return AET,DEF,SUR

def cls(ai): return 'arid' if ai<0.2 else 'semi-arid' if ai<0.5 else 'dry-subhumid' if ai<0.65 else 'sub-humid' if ai<1.0 else 'humid'

rows=[]; detail={}
for name,d in NORMALS.items():
    P=np.array(d['P'],float); T=np.array(d['T'],float); lat=d['lat']; dtr=DTR[name]
    petH=pet_hargreaves(T,lat,dtr); petT=pet_thornthwaite(T,lat)
    _,defH,surH=soil_balance(P,petH)
    dt50,dt85=DEPT_DT[name]
    petH50=pet_hargreaves(T+dt50,lat,dtr); _,def50,_=soil_balance(P,petH50)
    petH85=pet_hargreaves(T+dt85,lat,dtr); _,def85,_=soil_balance(P*0.90,petH85)
    _,defEN,_=soil_balance(P*0.60,petH)          # El Nino drought year
    detail[name]=dict(P=P,petH=petH,petT=petT,defH=defH,surH=surH,defEN=defEN)
    rows.append(dict(town=name,elev=d['elev'],reliab=d['reliability'],P=round(P.sum()),
        PET_HG=round(petH.sum()),PET_Th=round(petT.sum()),
        AI_HG=round(P.sum()/petH.sum(),2),climate=cls(P.sum()/petH.sum()),
        deficit=round(defH.sum()),def_mo=int((defH>1).sum()),surplus=round(surH.sum()),
        def_2050=round(def50.sum()),def_2085hi=round(def85.sum()),
        def_ElNino=round(defEN.sum()),defmo_ElNino=int((defEN>1).sum())))

df=pd.DataFrame(rows).sort_values('AI_HG')
df.to_csv('outputs/water_balance_summary.csv',index=False)
pd.set_option('display.width',200,'display.max_columns',30)
print(df.to_string(index=False))

import matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
order=df.sort_values('AI_HG',ascending=False)['town'].tolist()   # wettest -> driest margin
fig,axes=plt.subplots(1,len(order),figsize=(3.6*len(order),3.7),sharey=True)
for ax,name in zip(axes,order):
    b=detail[name]; x=np.arange(12)
    ax.bar(x,b['P'],color='#3a7bd5',alpha=.75,label='P')
    ax.plot(x,b['petH'],color='#c0392b',lw=2,marker='o',ms=3,label='PET (Hargreaves)')
    ax.plot(x,b['petT'],color='#e08a1e',lw=1.2,ls='--',label='PET (Thornthwaite)')
    ax.fill_between(x,b['P'],b['petH'],where=b['P']<b['petH'],color='#c0392b',alpha=.16,interpolate=True)
    ai=b['P'].sum()/b['petH'].sum()
    ax.set_title(f"{name.replace('_',' ').title()} · {NORMALS[name]['elev']}m\nP{round(b['P'].sum())} PET{round(b['petH'].sum())} · AI {ai:.2f} ({cls(ai)})",fontsize=8.5)
    ax.set_xticks(x); ax.set_xticklabels(MONTHS,fontsize=7); ax.grid(alpha=.25)
axes[0].set_ylabel('mm/month'); axes[0].legend(fontsize=7.5,loc='upper left')
plt.suptitle('Monthly water balance — P vs radiation-aware PET (red fill = deficit). Ordered wettest→driest margin.',fontsize=11,y=1.03)
plt.tight_layout(); plt.savefig('outputs/fig_water_balance.png',dpi=130,bbox_inches='tight')
print('\nSaved outputs/water_balance_summary.csv + fig_water_balance.png')
