class State:
  INIT = 0
  PROCESS = 1
  DONE = 2

class Solution:
  INT_MAX = 2147483647
  INT_MIN = -2147483648
  
    
  def checkOverflow(self, num, is_pos):
    if (is_pos and num >= self.INT_MAX): 
      return True
    elif ( (not is_pos) and num >= self.INT_MIN):
      return True 
    else:
      return False 

  def myAtoi(self, str):
    num = 0; 
    state = State()
    state = State.INIT
    is_pos = True
    is_overflow = False

    for i in range(0, len(str)):
      c = str[i]
      if (state == State.INIT):
        if (c == ' '):
          continue
        is_bad = False
        if (c == '+'):
          is_pos = True
        elif ( c == '-'):
          is_pos = False
        elif ( c >= '0' and c <= '9'):
          num = int(c)
        else:
          is_bad = True

        if (is_bad):
          state = State.DONE
        else:
          state = State.PROCESS
        
      elif (state == State.PROCESS):
        if ( c >= '0' and c <= '9'):
          num = (num *10) + (int(c) )
          is_overflow = self.checkOverflow(num, is_pos)
          if (is_overflow):
            if (is_pos):
              num = self.MAX_VALUE;
            else:
              num = ((-1))*self.MIN_VALUE;            
        else:
            state = State.DONE;
        
      if ( state == State.DONE ):
        break
  

    if (is_pos):
      return num
    else:
      return (-1*num)
  
  
if __name__ == "__main__":
    sol = Solution();
    str = "+123"
    print(sol.myAtoi(str))
    
    