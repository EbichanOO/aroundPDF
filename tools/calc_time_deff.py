class Time:
  def __init__(self, hour, minute):
    self.hour = hour
    self.minute = minute
  
  def __add__(self, other):
    return Time(self.hour+other.hour, self.minute+other.minute)

  def Print(self):
    print('deff is {} hour {} minute.'.format(self.hour, self.minute))

class DiffTimes:
  def __init__(self,time1,time2):
    self.MODE = "NOMAL"
    self.time1 = time1
    self.time2 = time2
    self.checkDate(time1,time2)
    if self.MODE=="NEXTDAY":
      self.beforeTime = DiffTimes(time1, Time(24,00))
      self.afterTime = DiffTimes(Time(00,00),time2)

  def set(self,time1,time2):
    self.time1 = time1
    self.time2 = time2

  def calc(self):
    sum_minute = 0
    time1 = self.time1
    time2 = self.time2

    if self.MODE=="NEXTDAY":
      before_day_time = self.beforeTime.calc()
      after_day_time = self.afterTime.calc()
      sum_minute = (before_day_time.hour+after_day_time.hour)*60 + before_day_time.minute+after_day_time.minute
    elif self.MODE=="SAME":
      sum_minute = 0
    # later time's minute has small than first
    elif(time2.minute < time1.minute):
      sum_minute = 60-time1.minute
      sum_minute = sum_minute+ (time2.hour-time1.hour-1)*60+time2.minute
    else:
      sum_minute = (time2.hour-time1.hour)*60+time2.minute-time1.minute
    
    self.diffTime = Time(int(sum_minute/60), sum_minute%60)
    return self.diffTime
  
  def checkDate(self,time1, time2):
    if(time2.hour<time1.hour):
      self.MODE = "NEXTDAY"
    elif(time2.hour==time1.hour and time2.minute==time1.minute):
      self.MODE = "SAME"

class Runner:
  def __init__(self):
    self.datas = []
  
  def dataAppend(self, data):
    self.datas.append(data)
  
  def run(self):
    totalDiff = Time(0,0)
    for data in self.datas:
      totalDiff += data.calc()
    return totalDiff


class MainFlow:
  def __init__(self):
    pass
  
  def run(self):
    runner = Runner()
    loop = True
    while(loop):
      print("前の時間を教えて下さい")
      x = input("時: ")
      y = input("分: ")
      time1 = Time(int(x), int(y))
      print("後の時間を教えて下さい")
      x = input("時: ")
      y = input("分: ")
      time2 = Time(int(x), int(y))
      check = input("続けるならyを入力してください")
      if(check!="y"):
        loop = False
      
      runner.dataAppend(DiffTimes(time1, time2))
    totalDiff = runner.run()
    print("合計経過時間{}時間{}分".format(totalDiff.hour, totalDiff.minute))


if __name__=='__main__':
  FLOW = MainFlow()
  FLOW.run()
