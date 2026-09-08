import json, re, glob, csv, html, os
from xml.etree import ElementTree as ET
pool = {}   # key -> record
def norm_title(t): return re.sub(r'[^a-z0-9]+',' ', t.lower()).strip()
def add(rec, src):
    key = rec.get('arxiv') or (rec.get('doi') or '').lower() or norm_title(rec['title'])
    if key in pool:
        pool[key]['sources'].add(src); 
        for k,v in rec.items():
            if v and not pool[key].get(k): pool[key][k]=v
    else:
        rec['sources']={src}; pool[key]=rec
n_raw=0
for f in glob.glob("raw/inspire_*.json"):
    src="inspire:"+os.path.basename(f)[8:-5]
    d=json.load(open(f,encoding='utf-8'))
    for h in d['hits']['hits']:
        m=h['metadata']; n_raw+=1
        add({'arxiv':(m.get('arxiv_eprints') or [{}])[0].get('value',''),
             'title':m['titles'][0]['title'],'date':m.get('earliest_date',''),
             'cites':m.get('citation_count',0),
             'authors':'; '.join(a['full_name'] for a in m.get('authors',[])[:4]),
             'abstract':(m.get('abstracts') or [{}])[0].get('value',''),
             'doi':(m.get('dois') or [{}])[0].get('value',''),'recid':m.get('control_number')}, src)
ns={'a':'http://www.w3.org/2005/Atom'}
for f in glob.glob('raw/arxiv_*.xml'):
    src='arxiv:'+os.path.basename(f)[6:-4]
    try: root=ET.parse(f).getroot()
    except Exception as e: print('parse fail',f,e); continue
    for e in root.findall('a:entry',ns):
        n_raw+=1
        aid=e.find('a:id',ns).text.split('/abs/')[-1]; aid=re.sub(r'v\d+$','',aid)
        add({'arxiv':aid,'title':' '.join(e.find('a:title',ns).text.split()),
             'date':e.find('a:published',ns).text[:10],'cites':'',
             'authors':'; '.join(x.find('a:name',ns).text for x in e.findall('a:author',ns)[:4]),
             'abstract':' '.join(e.find('a:summary',ns).text.split()),'doi':'','recid':''}, src)
print('raw records:',n_raw,' after dedup:',len(pool))
KW = {'higuchi':r'higuchi','gradient':r'gradient instab','varying':r'varying[- ]mass|mass[- ]varying|time[- ]dependent (graviton )?mass|chameleon|dilaton|field[- ]dependent|scalar[- ]dependent|environment',
      'bimetric':r'bimetric|bigravity|bi-gravity|two metrics','scalar-coupled':r'scalar field|scalar-tensor|quintessence','branch':r'infinite branch|finite branch',
      'ghost':r'ghost|boulware'}
rows=[]
for k,r in pool.items():
    text=(r['title']+' '+r['abstract']).lower()
    flags=[n for n,p in KW.items() if re.search(p,text)]
    r['flags']=','.join(flags); rows.append(r)
rows.sort(key=lambda r:r['date'],reverse=True)
with open('pool.csv','w',newline='',encoding='utf-8') as fh:
    w=csv.DictWriter(fh,fieldnames=['arxiv','date','cites','title','authors','flags','sources','doi','recid','abstract']); w.writeheader()
    for r in rows:
        r2=dict(r); r2['sources']=';'.join(sorted(r['sources'])); w.writerow(r2)
# screening list: bimetric AND (higuchi or varying or gradient or scalar-coupled)
sel=[r for r in rows if 'bimetric' in r['flags'] and any(x in r['flags'] for x in ('higuchi','varying','gradient','scalar-coupled','branch'))]
print('screen-in (bimetric & topical):',len(sel))
for r in sel:
    print(f"{r['date'][:7]} | {r['arxiv'] or '-':>12} | c={r['cites'] or '-':>3} | {r['flags']:<45} | {r['title'][:95]}")
print('--- non-bimetric but Higuchi/varying (massive gravity side) ---')
sel2=[r for r in rows if 'bimetric' not in r['flags'] and any(x in r['flags'] for x in ('higuchi','varying'))]
print(len(sel2))
for r in sel2[:80]:
    print(f"{r['date'][:7]} | {r['arxiv'] or '-':>12} | c={r['cites'] or '-':>3} | {r['flags']:<30} | {r['title'][:95]}")

# ---- per-source counts for the search log
from collections import Counter
c=Counter()
for r in rows:
    for s in r['sources']: c[s]+=1
print('--- per-source (deduplicated records touching each source) ---')
for s,n in sorted(c.items()): print(f'{n:5d}  {s}')
print('TOTAL unique:',len(rows))
