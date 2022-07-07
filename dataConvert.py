import pandas as pd

df = pd.read_excel('./dataset/2002年.xlsx')
nodes = df.loc[:,["公开（公告）号","标题","摘要","申请人","IPC主分类","CPC","引证次数","被引证次数","公开（公告）日"]]
# 缺省值替换为0
nodes["引证次数"] = nodes["引证次数"].fillna(0)
nodes["被引证次数"] = nodes["被引证次数"].fillna(0)
# 填充节点
citeNodes = pd.DataFrame(df["引证专利"].dropna(axis=0, how='any'))
citeNodesBy = pd.DataFrame(df["被引证专利"].dropna(axis=0, how='any'))

for row in citeNodes.itertuples():
    list = row[1].split(";")
    listDF = pd.DataFrame(list,columns=["公开（公告）号"])
    nodes = pd.concat([nodes,listDF],ignore_index=True)

for row in citeNodesBy.itertuples():
    list = row[1].split(";")

    listDF = pd.DataFrame(list,columns=["公开（公告）号"])
    nodes = pd.concat([nodes,listDF],ignore_index=True)
nodes.drop_duplicates(subset=["公开（公告）号"],keep='first',inplace=True)
nodes = nodes.reset_index(drop=True)
writer = pd.ExcelWriter('./output/nodes.xlsx')
nodes.to_excel(writer)
writer.save()
print(nodes)

# print(citeNodes)
# print(citeNodesBy)