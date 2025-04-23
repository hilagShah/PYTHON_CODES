class weather:
    def __init__(self,parameters):
        self.parameters = parameters
    
    def __contains__(self,item):
        return item in self.parameters

weather_today = weather(["temperature", "humidity", "rainfall", "wind"])

print("temperature" in weather_today)
print("snowfall" in weather_today)
        
    
