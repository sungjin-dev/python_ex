def menuInfos(menudict):

    sortedDict = sorted(menudict.items(), key=lambda x:x[1]['mCheck'])

    print(f'메뉴 목록: {sortedDict}')

    return menudict