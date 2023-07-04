# 직사각형 네 꼭짓점의 좌표 [[x1, y1], [x2, y2], [x3, y3], [x4, y4]]가 담겨있는 배열 dots가 매개변수로 주어질 때, 직사각형의 넓이를 return 하도록 solution 함수를 완성해보세요.
# x의 가장 큰수와 작은수의 차랑 y의 가장 큰수와 작은 수의 차를 곱하면 되는 문제


# 내 풀이

def solution(dots):
    x = []
    y = []
    for dot in dots:
        x.append(dot[0])
        y.append(dot[1])
        
    x_dot = max(x)-min(x)
    y_dot = max(y)-min(y)
    
    return x_dot*y_dot

# 다른사람 풀이1

def solution(dots):
    x = [dot[0] for dot in dots]
    y = [dot[1] for dot in dots]
        
    return (max(x)-min(x))*(max(y)-min(y))
  

# 다른사람 풀이2
# 사각형이 축에 평행하니까 max(dots) 좌표가 1시방향 끝점, min(dots) 좌표가 5시 방향 끝점임

def solution(dots):
    return (max(dots)[0] - min(dots)[0])*(max(dots)[1] - min(dots)[1])
