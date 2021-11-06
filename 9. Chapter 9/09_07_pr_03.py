

for s in range(2, 21):
    with open(f"tables by vipul/table of {s}.txt", 'w') as f:
        for v in range(1, 11):
            f.write(f"{s}X{v}={s*v}")
            if v!=10:
                f.write('\n')