data = ([1, 2, 3, 1, 1, 1, 1], 6)
def solution(data):
    data,s = data
    new_data = data * 2
    for i in range(len(data)):
        if (i + 1) ==  1:
            for j in data:
                if j == s:
                    return (i + 1)
        else:
            for k in range(len(new_data)):
                if s == sum(new_data[k:k+i+1]):  
                    return (i + 1)
    return 0 

print(solution(data))



    

        
    


