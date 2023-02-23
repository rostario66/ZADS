def create_array(n):
 k = [{"key":None, "data":None}for x in range(n)]
 s = {"keys":k,"top":0}
 return s


def insert(ar,k):
 if ar["top"] < len(ar["keys"]):
  ar["keys"][ar["top"]] = k
  ar["top"] = ar["top"] + 1

def delete(ar,i):
 if i < ar["top"]:
  ar["keys"][i] = ar["keys"][ar["top"]-1]
  ar["top"] = ar["top"] - 1

def print_array(ar):
 for i in range(ar["top"]):
    print(ar["keys"][i]["data"], end=" ")
 print()


f = create_array(20)
insert(f,{"key":1,"data":"Jirka"})
insert(f,{"key":15,"data":"Alice"})
insert(f,{"key":12,"data":"Petr"})
insert(f,{"key":21,"data":"Klara"})

print_array(f)
delete(f,0)
print_array(f)

def search(ar,k):
  for i in range(ar["top"]):
     if ar["keys"][i]["key"] == k:
        return i
     return -1

print(search(f,3)) 



def search_sort(ar,k):
    for i in range(len(ar["keys"])):
        if ar["keys"][i]["key"] == k:
            return i 
        if ar["keys"][i]["key"] > k:
            return -1
print(search_sort(f,15))
print(search_sort(f,3))

def binary_search(ar,k):
    l = 0
    p = ar["top"] - 1
    while l <= p:
        s = (l + p) // 2
        if ar["keys"][s]["key"] == k:
            l = s
        if ar["keys"][s]["key"] > k:
            l =  s - 1
        if ar["keys"][s]["key"] < k:
            l =  s + 1
    return -1

print(binary_search(f,15))
print(binary_search(f,3))
