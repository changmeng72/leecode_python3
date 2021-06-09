class Solution:
    def reformatDate(self, date: str) -> str:
        month_dict = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        [day,month,year] = date.split(' ')
        month = month_dict.index(month) + 1
        if month<10:
            month = "0" + str(month)
        else:
            month = str(month)
        if len(day)==3:
            day = "0" + day[0]
        else:
            day = day[:2]
        return "-".join([year,month,day])
        