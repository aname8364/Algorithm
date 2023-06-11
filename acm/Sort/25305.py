score_count, pass_count = map(int, input().split())
score = list(map(int, input().split()))
print(sorted(score, reverse=True)[pass_count-1])
