class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        result = set([])
        for email in emails:
            [local,domain] = email.split('@')
            result.add( local.split('+')[0].replace('.','') + '@' + domain)
        return len(result)
        
        """
        result = set([])
        for email in emails:
            formatedEmail = ""
            s = 0
            ignored = False
            for i in range(len(email)):
                if email[i] =='@':
                    if(ignored==False):
                        formatedEmail = formatedEmail + email[s:]
                    else:
                         formatedEmail = formatedEmail + email[i:]
                    break
                elif email[i]=='+':
                    if(ignored==False):
                        formatedEmail = formatedEmail + email[s:i]
                        ignored = True
                elif email[i] =='.':
                    if(ignored==False):
                        formatedEmail = formatedEmail + email[s:i]
                        s = i+1
            result.add(formatedEmail)
        return len(result)
     """               
                           
        