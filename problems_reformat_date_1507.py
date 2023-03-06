class Solution:
    def reformatDate(self, date: str) -> str:
        new_date = []
        month = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        if len(date) == 13:
            new_date.append(list(date)[0] + list(date)[1])

        elif len(date) == 12:
            new_date.append(f'0{list(date)[0]}')

        new_date.append(str(month.index(date.split()[1]) + 1) if month.index(date.split()[1]) + 1 >= 10
                        else f'0{month.index(date.split()[1]) + 1}')
        new_date.append(date.split()[2])
        new_date = new_date[::-1]

        return '-'.join(new_date)
