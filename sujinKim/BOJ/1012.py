from collections import deque

dr = [-1,1,0,0]
dc = [0,0,-1,1]
q = deque()
T = int(input())

for tc in range(1,T+1):
    M,N,K = list(map(int,input().split()))
    arr = [[0]*M for _ in range(N)]  #배추밭 빈 배열 만들어서 
    visited = [[False]*M for _ in range(N)]

    for j in range(K):
        X,Y = list(map(int,input().split())) #배추의 위치
        arr[X][Y] = 1   #배추밭에 배추위치 도입 
        sr,sc = X,Y #1의 시작위치 
        q.append((sr,sc))
        visited[sr][sc] = True

    cnt = 0
    while q:
        cr,cc = q.popleft()

        for i in range(4):
            for j in range(1,50):
                nr = cr + dr[i]*j #주변좌표 근데 가로세로 길이 다른데 3중 for문;?
                nc = cc + dc[i]*j

            

                if 0<=nr<N and 0<=nc<M and visited[nr][nc] = False:
                    if arr[nr][nc] == 1:
                        q.append((nr,nc))
                        visited[nr][nc] = True
                    else:
                        cnt +=1

                        break
    print(cnt)








                   


