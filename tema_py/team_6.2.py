dat_1 = (1, 2, 3)
dat_2 = (1, 2, 3, 1, 2, 3, 4, 5, 2, 3, 4, 2, 4, 2)
dat_3 = (2, 4, 6, 6, 4, 2)


def delit(dat_mod, elm):
    dat_list = list(dat_mod)
    if elm in dat_list:
        inrem = dat_list.index(elm)
        del dat_list[inrem]
    dat_mod = tuple(dat_list)
    return dat_mod


dat_1 = delit(dat_1, 1)
dat_2 = delit(dat_2, 3)
dat_3 = delit(dat_3, 9)

print(dat_1)
print(dat_2)
print(dat_3)