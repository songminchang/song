def exchange(charge):
  
  500w=charge//500
  100w=(charge-500w*500)//100
  50w=(charge-500w*500-100w*100)//50
  10w=(charge-500w*500-100w*100-50w*50)//10
  
  def integer():
     charge=int(input("금액을 입력해주세요:"))
     exchange(charge)
    
    get_integer()
