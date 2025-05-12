"""
문제 요약
- 각 직원은 행사에 참석할 경우 고유한 비용(sales)이 든다.
- 조직은 트리 구조(links)로 주어지며, links[i] = [a, b]는 a가 상사이고 b가 부하임을 의미한다.
- 조건: 어떤 팀(=자식이 있는 노드)이든 최소한 1명 이상은 반드시 행사에 참석해야 한다. 
- 목표: 이 조건을 지키면서 행사 참석 비용을 최소화하는 것이다. 

풀이 방법(트리 DP)
- dp[i][0]: i번 노드가 행사에 불참할 때의 최소 비용
- dp[i][1]: i번 노드가 행사에 참석할 때의 최소 비용
  - 참석하는 경우: dp[i][1] = sales[i-1] + 자식들의 최소 비용
  - 불참하는 경우: 자식들 중 최소 1명은 반드시 참석해야 하므로, 예외 처리를 해줘야 함.
"""

from collections import defaultdict

def solution(sales, links):
    n = len(sales)
    tree = defaultdict(list)

    # 트리 구조 생성
    for a, b in links:
        tree[a].append(b)

    # DP 테이블 초기화
    # dp[i][0]: i번 노드가 불참했을 때의 최소 비용
    # dp[i][1]: i번 노드가 참석했을 때의 최소 비용
    dp = [[0, 0] for _ in range(n + 1)]
    visited = [False] * (n + 1)

    def dfs(node):
        visited[node] = True
        dp[node][1] = sales[node - 1]  # 현재 노드가 참석할 경우 본인의 비용

        # 리프 노드는 자식이 없으므로 return
        if not tree[node]:
            return

        cost = float('inf')           # 자식 중 하나를 참석시키기 위한 추가 비용
        is_all_child_opt_out = True   # 모든 자식이 불참했는지 여부 체크

        for child in tree[node]:
            dfs(child)  # 자식 먼저 처리

            # 현재 노드가 참석할 경우: 자식은 참석/불참 중 더 작은 비용 선택 가능
            dp[node][1] += min(dp[child][0], dp[child][1])

            # 현재 노드가 불참할 경우: 자식도 모두 불참이면 안 됨
            dp[node][0] += min(dp[child][0], dp[child][1])

            # 자식 중 하나라도 참석하면 조건 만족
            if dp[child][0] > dp[child][1]:
                is_all_child_opt_out = False

            # 불참한 자식만 있을 경우, 참석한 자식 하나를 강제로 선택해야 하므로 비용 계산
            cost = min(cost, dp[child][1] - dp[child][0])

        # 자식이 모두 불참한 경우 -> 예외 처리: 자식 하나는 반드시 참석시켜야 함
        if is_all_child_opt_out:
            dp[node][0] += cost

    # 1번이 루트 노드
    dfs(1)

    # 루트 노드가 참석/불참 중 더 작은 비용을 선택
    return min(dp[1][0], dp[1][1])
