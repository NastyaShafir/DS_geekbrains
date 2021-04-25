words = list(map(lambda x: x[:10] if len(x) > 10 else x, input().split()))
print("\n".join([f"{i + 1}. {words[i]}" for i in range(len(words))]))
