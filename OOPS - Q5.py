class Time:
    def __init__(self,hours = 0,minutes = 0,seconds = 0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        self.normalize_time()
    
    def to_seconds(self):
        return self.hours * 3600 + self.minutes * 60 + self.seconds
    
    def normalize_time(self):
        self.minutes += self.seconds//60
        self.seconds %= 60
        self.hours += self.minutes//60
        self.minutes %= 60
        self.hours %= 24
        
    def add_time(self,other):
        new_hour = self.hours + other.hours
        new_minutes = self.minutes + other.minutes
        new_seconds = self.seconds + other.seconds
        return Time(new_hour, new_minutes, new_seconds)
        
    def subtract_time(self, other):
        total_seconds1 = self.to_seconds()
        total_seconds2 = other.to_seconds()
        diff_seconds = abs(total_seconds1 - total_seconds2)  
        return Time.from_seconds(diff_seconds)
    
    @staticmethod    
    def from_seconds(seconds):
        hours = seconds // 3600
        seconds %= 3600
        minutes = seconds // 60
        seconds %= 60
        return Time(hours, minutes, seconds)

    def display(self):
        return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"

h1,m1,s1 = map(int, input("ENTER TIME (IN HH::MM::SS) : ").split()) 
h2,m2,s2 = map(int, input("ENTER TIME (IN HH::MM::SS) : ").split()) 

time1 = Time(h1,m1,s1)
time2 = Time(h2,m2,s2)

added_time = time1.add_time(time2)
subtracted_time = time1.subtract_time(time2)
total_seconds = time1.to_seconds()

print(f"\nTime 1: {time1.display()}")
print(f"Time 2: {time2.display()}")
print(f"Added Time: {added_time.display()}")
print(f"Time Difference: {subtracted_time.display()}")
print(f"Time 1 in Seconds: {total_seconds} sec")
    
