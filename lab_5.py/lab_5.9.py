def superset(set_1, set_2):
    if set_1>set_2:
        print(f"обект {set_1} является чистым супер множеством")
    elif set_1==set_2:
        print("множества равны")
    elif set_1<set_2:
        print(f"обект {set_2} является чистым супер множеством")
    else:
        print("супермножеств не обнаружено")

superset({1,2,6,4,5,3}, {2,3,1})
superset({2,3,1},{1,2,3,4,5,6})
superset({2,3,1},{1,2,3})
superset({2,3,1,7},{1,2,3,4,5,6})