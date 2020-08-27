import pandas as pd

data = pd.read_csv('./ntst/nswords.csv')

data = data.dropna(axis=0)
data.columns = ['kp', 'kr']

# for i in range(len(data)):
#     kr_string = data.loc[i, 'kr']
#     kp_string = data.loc[i, 'kp']
#     index = kr_string.find('.')
#
#     if index != -1:
#         data.loc[i, 'kr'] = kr_string[:index]
    ############ [예] 없애주기 ############
    # if '[예]' in kr_string:
    #     index = kr_string.find('  [예]')
    #     data.loc[i, 'kr'] = kr_string[:index]

    # if len(kr_string) >= 20:
    #     print(kr_string)
    #     data = data.drop(i, axis=0)

    # if kr_string[-1] == '것':
    #     print(data.loc[i, 'kp'], ", ", kr_string)
    #     data = data.drop(i, axis=0)

    # if len(kr_string) > len(kp_string)*2:
    #     print(kp_string, ",", kr_string)
    #     data = data.drop(i, axis=0)

    # ############ () 사이 단어 없애주기 ############
    # start = kr_string.find('(')
    # if start != -1:
    #     end = kr_string.find(')')
    #     if end != -1:
    #         data.loc[i, 'kp'] = kr_string[:start] + kr_string[end+1:]
data_re = data[['kr', 'kp']]
data_re.to_csv('./ntst/nswords.csv', index=False)
# data.to_csv('./ntst/nswords.csv', index=False)

