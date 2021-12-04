import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
from sklearn.decomposition import PCA
from sklearn.linear_model import LinearRegression

if __name__ == '__main__':
    df = pd.read_csv("follow.csv")

    print(df.isnull().sum())

    # one hot de las categoricas
    # columns = df.columns
    # for col in columns:
    #     if df[col].dtype == 'object':
    #         print(col)
    #         df = pd.concat([df, pd.get_dummies(df[col],prefix=col)], axis=1)
    #
    #
    # # Gestionar nans
    # columns = df.columns
    # max_nans = .4 * df.shape[0]
    # strategy = 'zeros'
    # for col in columns:
    #     nans = df[col].isnull().sum()
    #     if nans > 0:
    #         if nans >= max_nans:
    #             df.drop(columns=col, inplace=True)
    #         else:
    #             if strategy == 'zeros':
    #                 df.loc[df[col].isnull(), col] = 0
    #
    #
    # plt.figure(figsize=(14,12))
    # sns.heatmap(df.corr(), annot=True, linewidth=0.5)
    # plt.show()
    #
    # print(df.isnull().sum())
    #
    # df = (df - df.mean()) / df.std()
    #
    # plt.figure(figsize=(14,12))
    # sns.heatmap(df.corr(), annot=True, linewidth=0.5)
    # plt.show()
    #
    # features_set = [
    #     ['speed'],
    #     ['distance'],
    #     ['hours'],
    #     ['inv_dist'],
    #     ['sun'],
    #     ['rain'],
    #     ['hours', 'rain']
    #
    # ]
    # for features in features_set:
    #     lineal = LinearRegression()
    #     lineal.fit(df[features].values, df['consume'].values[..., None])
    #     score = lineal.score(df[features].values, df['consume'].values[..., None])
    #     print(features, score)
    #
    # for i in range(1,10):
    #     pca = PCA(n_components=i)
    #     cols = df.columns.tolist()
    #     cols.remove('consume')
    #     data = pca.fit_transform(df[cols].values)
    #
    #     lineal = LinearRegression()
    #     lineal.fit(data, df['consume'].values[..., None])
    #     score = lineal.score(data, df['consume'].values[..., None])
    #     print(f"pca-{i}", score)
