#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""extract_nomenclatures.py"""

__authors__ = ['jmouaike']

import pandas as pd
import csv

from config import config
import utils.print_out as po

class Nomenclature:
    """_summary_

    Returns:
        _type_: _description_
    """        
    def __init__(self, id1, id2, final_product:str, parent:str):
        self.ids=[id1, id2]
        self.final_product = final_product
        self.parents = []
        self.append_parent(parent)

    def append_parent(self, parent:str) -> None:
        self.parents.append(parent)

    def to_dataframe(self) -> pd.DataFrame:
        headers = ['Nomenclature', 'N noeud poste', 'Article de tete', 'Article fabrique',
                   'Niveau de nomenclature', 'Article consomme']
        # Create the 'parent' column with self.final_product at the first row
        article_column = [self.final_product] + self.parents[:-1]
        # Create the DataFrame
        df = pd.DataFrame({
            'Nomenclature': [self.ids[0]] * len(article_column),
            'N noeud poste': [self.ids[1]] * len(article_column),
            'Article de tete': [self.final_product] * len(article_column),
            'Article': article_column,
            'niveau de nomenclature': range(1, len(article_column) + 1),
            'Composant': self.parents
            })
        return df

    def __repr__(self):
        ans = f"{self.ids[0]},{self.ids[1]},{self.final_product}"
        for parent in self.parents:
            ans = ans + f",{parent}"
        return ans 
    

def trace_article(df:pd.DataFrame, component:str) -> list:
    all_prev_components = df[df['Article'] == component]['Composant'].tolist()
    components = []
    prefixes = config.useful_prefixes
    for prev_component in all_prev_components:
        if  prev_component.startswith(tuple(prefixes)):
            components.append(prev_component)
    return components

def get_final_products(df:pd.DataFrame) -> pd.DataFrame:
    """Select rows where 'Article' column values start with '101' """
    final_products_df = df[df['Article'].str.startswith(config.final_products_prefix)]
    final_products_df.to_csv(f'{config.data_dir}/final_products.csv', index=False)
    return final_products_df

def instanciate_processes(df):
    """
    Ensure the 'Article' column is treated as a string
    """
    df['Article'] = df['Article'].astype(str)
    df['Composant'] = df['Composant'].astype(str)
    final_products_df = get_final_products(df)
    processes = []
    for index, row in final_products_df.iterrows():
        process = Nomenclature(id1=row['Nomenclature'],
                               id2=row['N noeud poste'],
                               final_product=row['Article'],
                               parent=row['Composant'])
        processes.append(process)
        if row['Composant'].startswith('4'):
            is_not_last = True
            while is_not_last:
                prev_components = trace_article(df, process.parents[-1])
                if len(prev_components) > 0:
                    # only first is appended
                    process.append_parent(prev_components[0])
                else :
                    is_not_last = False
    """extract linked-lists"""
    file_name = f'{config.data_dir}/output_levels.csv'
    with open(file_name, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(config.output_headers)
        for process in processes:
            writer.writerow(str(process).split(','))
    print(f"Data has been written to {file_name}")
    # Read the CSV file into a DataFrame
    linked_df = pd.read_csv(file_name)
    # Write the DataFrame to an Excel file
    output_excel_file_path = f'{config.data_dir}/output_levels.xlsx'
    linked_df.to_excel(output_excel_file_path, index=False)
    
    # List to hold individual DataFrames
    dataframes = []
    for process in processes:
        nomenclature_df = process.to_dataframe()
        dataframes.append(nomenclature_df)
        # Concatenate all DataFrames vertically
        result_df = pd.concat(dataframes, ignore_index=True)
        # test one nomenclature
        if process.final_product == '101013':
            # print(process)
            print("\n")
            print(nomenclature_df)            
    # Export the DataFrame to a CSV file
    csv_file_path = f'{config.data_dir}/results3.csv'
    result_df.to_csv(csv_file_path, index=False)
    print(f"The DataFrame has been exported to {csv_file_path}")
    results_to_excel_file_path = f'{config.data_dir}/results3.xlsx'
    result_df.to_excel(results_to_excel_file_path, index=False)

    # Merge 
    merged_df = pd.merge(result_df,
                         df,
                         on=['Article', 'Composant'],
                         how='left'
                         )
    # Export the DataFrame to a CSV file
    merged_df.to_csv(f'{config.data_dir}/results_merged.csv', index=False)
    print("The Merged DataFrame has been exported to /results_merged.csv")
    merged_df.to_excel(f'{config.data_dir}/results_merged.xlsx', index=False)

def main():
    """  """
    try:
        df=pd.read_excel(f'{config.data_dir}/{config.input_filename}',
                         sheet_name=config.sheet_name)
        df.columns = config.input_headers
        df.to_csv(f'{config.data_dir}/modified_dataset.csv', index=False)
        instanciate_processes(df)
    except (FileNotFoundError, IsADirectoryError) as e:
        print("!!! File Error :", e)
    except pd.errors.EmptyDataError as e:
        print("!!! File Content Error :", e)


if __name__ == "__main__":
    """_summary_
    """
    main()