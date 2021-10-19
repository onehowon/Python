import numpy as np
import mlxtend
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules
import pandas as pd
from mlxtend.preprocessing import TransactionEncoder


X = np.array([1.0,2.0,3.0,4.0,5.0,6.0])
print("E(X)=", np.mean(X))
print("V(X)=", np.var(X))
print("sigma(X)=", np.std(X))



dataset = [['Milk', 'Cookie', 'Apple', 'Beans', 'Eggs', 'Yogurt'],
           ['Coke', 'Cookie', 'Apple', 'Beans', 'Eggs', 'Yogurt'],
           ['Milk', 'Apple', 'Kidney Beans', 'Eggs'],
           ['Milk', 'Orange', 'Corn', 'Beans', 'Yogurt'],
           ['Corn', 'Cookie', 'Cookie', 'Beans', 'Ice cream', 'Eggs']]
print(type(dataset))

te = TransactionEncoder()
te_ary = te.fit(dataset).transform(dataset)
print(te_ary)

df = pd.DataFrame(te_ary, columns = te.columns_)
print(df)

apriori(df, min_support = 0.6)

apriori(df, min_support = 0.6, use_colnames = True)

frequent_itemsets = apriori(df, min_support = 0.6, use_colnames = True)
frequent_itemsets['length'] = frequent_itemsets['itemsets'].apply(lambda x: len(x))

print(frequent_itemsets)

frequent_itemsets[(frequent_itemsets['length'] == 2) & (frequent_itemsets['support'] >= 0.6)]

rules = association_rules(frequent_itemsets, metric = "confidence", min_threshold = 0.7)
print(rules)

rules2 = association_rules(frequent_itemsets, metric = "lift", min_threshold = 1.2)
print(rules2)

rules["antecedent_len"] = rules["antecedents"].apply(lambda x : len(x))
rules[(rules['antecedent_len'] >= 2) & (rules['confidence'] > 0.75) & (rules['lift'] > 1.2)]