def getWinner(board):
  # 오목 게임에서 누가 이겼는지를 알아내는 함수 


  # 승부 판단 결과를 담는 변수 (default값은 승리가 결정되지 않은 None 상태)
  result = None

  # 검은돌, 하얀돌 총 갯수를 세는 변수
  black = 0
  white = 0

  # 검은돌, 하얀돌 몇 콤보인지 세는 변수
  bcombo = 0
  wcombo = 0

  # 중복 승리를 판단하기 위한 승리 횟수 세는 변수
  bWin = 0
  wWin = 0



  # 우상 좌하 대각선 콤보 검사 (top-right to bottom left diagonal) - 마지막 행을 시작으로 검사하는 case 
  for i in range(len(board)):
    for j in range(len(board)):

      # 검은돌 검사
      if board[len(board)-1-j][j+i] == 'B':
        bcombo = bcombo + 1

        if bcombo == 5:
          result = 'B'
          bWin = bWin + 1
        
      else :
        bcombo = 0


      # 하얀돌 검사 
      if board[len(board)-1-j][j+i] == 'W':
        wcombo = wcombo + 1

        if wcombo == 5:
          result = 'W'
          wWin = wWin + 1

      else :
        wcombo = 0

      # 하나의 라인 끝났을 때 콤보 갯수 초기화 
      if j + i == len(board)-1:
        bcombo = 0
        wcombo = 0
        break      



  # 우상 좌하 대각선 콤보 검사 (top-right to bottom left diagonal) - 마지막 열을 시작으로 검사하는 case 
  for i in range(len(board)):
    for j in range(len(board)):

      # 검은돌 검사
      if board[j+i][len(board)-1-j] == 'B': #[0][12], [1][11], [2][10], ... 
        bcombo = bcombo + 1

        if bcombo == 5:
          result = 'B'
          bWin = bWin + 1

      else :
        bcombo = 0


      # 하얀돌 검사
      if board[j+i][len(board)-1-j] == 'W': #[0][12], [1][11], [2][10], ... 
        wcombo = wcombo + 1

        if wcombo == 5:
          result = 'W'
          wWin = wWin + 1

      else :
        wcombo = 0      


      # 하나의 라인 끝났을 때 콤보 갯수 초기화 
      if j + i == len(board)-1:
        bcombo = 0
        wcombo = 0
        break  







  # 좌상 우하 대각선 콤보 검사 (top-left to bottom right diagonal) - 첫번째 행을 시작으로 검사하는 case 
  for i in range(len(board)):
    for j in range(len(board)):

      # 검은돌 검사 
      if board[j][j+i] == 'B':
        bcombo = bcombo + 1

        if bcombo == 5:
          result = 'B'
          bWin = bWin + 1

      else :
        bcombo = 0

      # 하얀돌 검사 
      if board[j][j+i] == 'W':
        wcombo = wcombo + 1

        if wcombo == 5:
          result = 'W'
          wWin = wWin + 1

      else :
        wcombo = 0

      # 하나의 라인 끝났을 때 콤보 갯수 초기화
      if j + i == len(board)-1:
        bcombo = 0
        wcombo = 0
        break  




  # 좌상 우하 대각선 콤보 검사 (top-left to bottom right diagonal) - 첫번째 열을 시작으로 검사하는 case 
  for i in range(len(board)):
    for j in range(len(board)):

      # 검은돌 검사 
      if board[j+i][j] == 'B':
        bcombo = bcombo + 1

        if bcombo == 5:
          result = 'B'
          bWin = bWin + 1

      else :
        bcombo = 0

      # 하얀돌 검사 
      if board[j+i][j] == 'W':
        wcombo = wcombo + 1

        if wcombo == 5:
          result = 'W'
          wWin = wWin + 1

      else :
        wcombo = 0


      # 하나의 라인 끝났을 때 콤보 갯수 초기화 
      if j + i == len(board)-1:
        bcombo = 0
        wcombo = 0
        break  





 # 세로 콤보 검사하기 (vertical)
  for i in range(len(board)):
    for j in range(len(board[i])):

      # 검은돌 검사 
      if board[j][i] == 'B':
         bcombo = bcombo + 1

         if bcombo == 5:
           result = 'B'
           bWin = bWin + 1

      else :
        bcombo = 0


      # 하얀돌 검사 
      if board[j][i] == 'W':
         wcombo = wcombo + 1

         if wcombo == 5:
           result = 'W'
           wWin = wWin + 1

      else :
        wcombo = 0

      # 하나의 라인 끝났을 때 콤보 갯수 초기화 
      if j == 12: 
        bcombo = 0
        wcombo = 0







  # 가로 콤보 검사하기 (horizontal)
  for i in range(len(board)):
    for j in range(len(board[i])):


      # 검은돌 검사 
      if board[i][j] == 'B':
        bcombo = bcombo + 1
        black = black + 1

        if bcombo == 5:
          result = 'B'
          bWin = bWin + 1

      else :
        bcombo = 0

      # 하얀돌 검사 
      if board[i][j] == 'W':
        wcombo = wcombo + 1
        white = white + 1

        if wcombo == 5:
          result = 'W'
          wWin = wWin + 1

      else :
        wcombo = 0

      # 하나의 라인 끝났을 때 콤보 갯수 초기화 
      if j == 12:
        bcombo = 0
        wcombo = 0





  # 비정상인 경우 체크 
  # 1) 하얀 돌의 갯수가 검은 돌보다 많을 때 
  if white > black:
    result = 'X'
  # 2) 검은 돌의 갯수가 하얀 돌보다 2개 이상 많을 때 
  elif black >= white + 2:
    result = 'X'
  # 3) 하얀 돌과 검은 돌 모두 승리 상태를 지닐 때 
  elif bWin != 0 and wWin != 0:
    result = 'X'





  # 승부 결과 리턴 
  return result
