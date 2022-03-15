class funArray:
    def __init__(self):
        self.leng =0 
        self.dis = {}
        
    def get(self,index):
        return self.dis[index]
    
    def push(self,value):
        self.dis[self.leng]=value
        self.leng+=1
        
    def pop(self):
        del self.dis[self.leng-1]
        self.leng-=1
        
    def delete(self,index):
        for i in range(index,self.leng-1):
            self.dis[i] = self.dis[i+1]
        del self.dis[self.leng-1]
        self.leng-=1
        
    def __str__(self):
        return str(self.dis)
    
    

array = funArray()

array.push('d')

array.push('i')

array.push('n')

array.push('e')

array.push('s')

print(array)

print(array.get(2))

array.pop()

print(array)

array.delete(1)

# printing array of index and value separately.
for i,j in array.dis.items():
    print(i,j)
