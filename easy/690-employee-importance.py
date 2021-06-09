 def getImportance(self, employees: List['Employee'], id: int) -> int:
        id_dict = {}
        start = 0
        ans = 0
        stack = []
        for i in range(len(employees)):
            id_dict[employees[i].id] = i
            if(employees[i].id==id):
                start = i
        stack.append(employees[start])
        
        while stack:
            e = stack.pop()
            ans += e.importance
            for s in e.subordinates:
                stack.append(employees[id_dict.get(s,0)])
        return ans
        