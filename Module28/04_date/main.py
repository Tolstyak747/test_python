class Date:
    def __init__(self, day: int, month: int, year: int) -> None:
        self.day = day
        self.month = month
        self.year = year

    def __str__(self) -> str:
        return f"День: {self.day}\tМесяц: {self.month} \tГод: {self.year}"

    @classmethod
    def from_string(cls, date: str):
        date = date.split("-")
        date = [int(x) for x in date]
        day, month, year = date
        cls_obj = cls(day, month, year)
        return cls_obj

    @classmethod
    def is_date_valid(cls, date: str) -> bool:
        date = date.split("-")
        date = [int(x) for x in date]
        day, month, year = date
        if month in [1, 3, 5, 7, 8, 10, 12]:
            if 1 <= day <= 31:
                return True
            return False
        elif month in [4, 6, 9, 10]:
            if 1 <= day <= 30:
                return True
            return False
        elif month == 2:
            if year % 4 == 0:
                if 1 <= day <= 29:
                    return True
                return False
            else:
                if 1 <= day <= 28:
                    return True
                return False
        return False


date = Date.from_string('10-12-2077')
print(date)
print(Date.is_date_valid('10-12-2077'))
print(Date.is_date_valid('40-12-2077'))
