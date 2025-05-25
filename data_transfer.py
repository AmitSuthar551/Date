import json
import os

db_file = 'ld_data.json'  


def rd():
 if os.path.isfile(db_file):
    with open(db_file, 'r') as ff:
        return json.load(ff)
 return []

def sv(d):
 f = open(db_file, 'w')
 json.dump(d, f, indent=2)
 f.close()

def new():
    print("==ADD LEAD==")
    nm = input("Name: ")
    em = input("Email: ")
    ph = input("Phone: ")
    cmp = input("Company: ")

    lead = {
        'nm': nm,
        'em': em,
        'ph': ph,
        'cmp': cmp,
        'sts': 'new'
    }
# for adding the detail of any person
    x = rd()
    x.append(lead)
    sv(x)
    print(">> Added")

def show():
    z = rd()
    if len(z)==0:
        print("No data bro")
        return
    c = 1
    for l in z:
        print(f"{c}) {l['nm']} | {l['em']} | {l['ph']} | {l['cmp']} | {l['sts']}")
        c+=1


def chg():
    data = rd()
    show()
    if len(data)==0:
        return
    try:
        ix = int(input("Which #: ")) - 1
        st = input("Status (new/contacted/done): ").lower()
        if st in ['new','contacted','done']:
            data[ix]['sts'] = st
            sv(data)
            print(">> Updated")
        else:
            print("Wrong status")
    except:
        print("Err")


def rem():
    dt = rd()
    show()
    if len(dt)==0:
        return
    try:
        ch = int(input("Delete #: ")) - 1
        del dt[ch]
        sv(dt)
        print(">> Removed")
    except:
        print("Error")

def GO():
 while True:
  print("\n--- Lead Thing ---")
  print("1 > Add")
  print("2 > Show")
  print("3 > Change Status")
  print("4 > Delete")
  print("5 > Bye")

  x = input(">> ")

  if x=='1':
    new()
  elif x=='2':
    show()
  elif x=='3':
    chg()
  elif x=='4':
    rem()
  elif x=='5':
    print("Exiting, cya!")
    break
  else:
    print("??")


if __name__=="__main__":
 GO()
