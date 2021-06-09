class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        d = {}
        r = []
        
        for cpdomain in cpdomains:
            count_doamin = cpdomain.split(' ')
            domains = count_doamin[1].split('.')
            n = int(count_doamin[0])
            for i in range(len(domains)-2,-1,-1):
                domains[i] = domains[i] + '.' + domains[i+1]
                d[domains[i]] = d.get(domains[i],0) + n
            d[domains[-1]] = d.get(domains[-1],0) + n
                
        for item in d.items():
            r.append(str(item[1])+' '+ item[0])
        return r
        