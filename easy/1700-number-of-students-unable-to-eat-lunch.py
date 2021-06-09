class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        flag = 0
        n_stu = len(students)
        queue = deque(students)
        san_index = 0
        while flag < n_stu:
            s = queue.popleft()
            if s== sandwiches[san_index]:
                san_index += 1
                n_stu = n_stu-1
                flag = 0
            else:
                queue.append(s)
                flag += 1
        return len(queue)
            
        
        
        