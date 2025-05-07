import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)


def metadata(df):
    columns_list = list(df.columns.values)
    type_list = [str(item) for item in list(df.dtypes)]
    missing_list = [round(float(num), 2)
                    for num in list((df.isnull().sum()/len(df)*100))]
    unique_list = [int(nunique) for nunique in list(df.nunique())]
    metadata = pd.DataFrame(columns_list, columns=['column_name'])
    metadata['datatype'] = type_list
    metadata['missing_percent'] = missing_list
    metadata['unique'] = unique_list
    try:
        desc_interval = df[[item for item in columns_list if str(df[item].dtypes) != 'category'
                            and df[item].nunique() >= 10
                            and str(df[item].dtypes) != 'object']].describe().loc[['mean', 'std', 'min', '25%', '50%', '75%', 'max']].transpose().reset_index().rename(columns={'index': 'column_name'})
        metadata = pd.merge(metadata, desc_interval,
                            on='column_name', how='left')
    except:
        metadata
    return metadata


def data_exploration(df, column):
    if (str(df[column].dtypes) == 'object' or str(df[column].dtypes) == 'category'):
        if df[column].nunique() < 10:
            count_value = df.groupby(
                [column]).size().reset_index(name='counts')
            count_value['%count'] = [
                round(num / len(df) * 100, 2) for num in list(count_value['counts'])]
            print(count_value)
            value_list = count_value[column].tolist()
            count_list = count_value['counts'].tolist()
            fig = plt.figure(figsize=(8, 4))
            plt.bar(x=value_list, height=count_list)
            plt.xticks(fontsize=12)
            plt.show()
        else:
            print(column + ' has more than 10 unique values')

    elif pd.api.types.is_numeric_dtype(df[column]) or pd.api.types.is_bool_dtype(df[column]):
        mean = df[column].mean()
        std = df[column].std()

        if std != 0:
            outlier = df[((df[column] - mean) / std > 3) |
                         ((df[column] - mean) / std < -3)][column].tolist()
            if len(outlier) > 0:
                print('There are ' + str(len(outlier)) +
                      ' outliers for ' + column + '.')
                print(outlier)
            else:
                print('There are no outliers in ' + column + '.')
        else:
            print('Standard deviation is 0, skipping outlier detection.')

        print('----------------------Box plot----------------------')
        # Convert boolean to int for plotting, if needed
        plot_data = df[column].astype(int) if pd.api.types.is_bool_dtype(
            df[column]) else df[column]
        plot_data.plot.box(title=column, whis=(5, 95))
        plt.grid()
        plt.show()

        # Convert bool to int if necessary
        col_data = df[column].astype(int) if pd.api.types.is_bool_dtype(
            df[column]) else df[column]

        min_value = float(col_data.min())
        max_value = float(col_data.max())

        if df[column].nunique() >= 10:
            para = (max_value - min_value) / 10
            para_list = np.arange(min_value, max_value,
                                  para).round(decimals=2).tolist()
            count_table = col_data.to_frame().copy()
            for num in para_list:
                count_table.loc[count_table[column] >= num, 'range'] = num
            count_table_sum = count_table.groupby(
                ['range']).size().reset_index(name='counts')
            value_list = count_table_sum['range'].tolist()
            count_list = count_table_sum['counts'].tolist()
            print('----------------------Distribution plot----------------------')
            fig = plt.figure(figsize=(8, 4))
            plt.bar(x=value_list, height=count_list, width=para,
                    tick_label=value_list, align='edge')
            plt.xticks(rotation=40, fontsize=12)
            plt.grid()
            plt.show()
    else:
        print(f"{column} data type is not supported for exploration.")
