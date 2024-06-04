# excel-link-nomenclatures

A `Python` program using `pandas` library to aggregate data form an excel of a given format.

### Scope

Input : an Excel spreadsheet dataset, with dozens of thousands of rows, each being a step of industrial production. 
A step is caracterized by its `final product` and the required material to produce it, referred as `parent`.
Though that list of steps, there is a need to link these steps and ouput an excel file where each `nomenclature` is presented in ordered manner. the final production of the chain being at the top with level 1 and followed by the 

#### Input data format

An Excel spreadsheet dataset. As the original data is confidential, here is a mock example of what it looks like.



Final product_A can be produced by 3 different ways. Whereas product

#### Output

Output is a list of each chain of production.
From there, data aggregation data from my original dataframe with this dataframe where products are sorted.
