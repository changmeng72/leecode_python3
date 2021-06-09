class Solution:
    def average(self, salary: List[int]) -> float:
        max_s,min_s = salary[0],salary[0]
        s = salary[0]
        for i in range(1,len(salary)):
            s += salary[i]
            if salary[i]>max_s:
                max_s = salary[i]
            elif salary[i]<min_s:
                min_s = salary[i]
        return (s-max_s-min_s) /( len(salary)-2)
            