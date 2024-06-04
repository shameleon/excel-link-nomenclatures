"""
Nomenclature module
nomenclature/config.py

"""


class Configuration(object):
    """_summary_
        dataset configuration 
    """
    def __init__(self, dataset_directory, excel_file_name, sheet_name=0 ) -> None:
        """
        Parameters :
        - location of the dataset directory 
        - the excel file name in there
        - sheet_name is first sheet by default (=0). See pandas Documentations
        """
        self.data_dir = dataset_directory
        self.input_filename = excel_file_name
        self.input_original = f'{dataset_directory}{excel_file_name}'
        self.sheet_name = sheet_name
        self.setup_input_headers()
        self.setup_output_headers()
        self.setup_target_labels()
        self.setup_product_prefixes()

    
    def setup_product_prefixes(self):
        """Tails : final products all start with 101
         Head : initial products all start with 900 """
        self.final_products_prefix = '101'
        self.initial_products_prefix = '900'
        self.initial_products_to_be_removed = True
        self.useful_prefixes = ['2', '4', '9']

    def setup_target_labels(self):
        """current is the Item column label
        previous is the parent product require to produce the current one"""
        self.current='Article'
        self.previous='Composant'

    def setup_input_headers(self):
        """
        """
        new_headers = ['Nomenclature', 'N noeud poste', 'Article', 'Désignation article',
                'Division', 'Quantite de base', 'Unité de qté de base',
                'Statut nomenclature', 'Composant', 'Designation composant',
                'Type de poste', 'Numero de poste', 'UQ du composant', 'Quantite',
                'Quantité fixe', 'RebutNivCompos. (%)', 'Rebut niv. oper. en %',
                'Pertinence fabrication', 'Pertinence pour CCR']
        self.input_headers = new_headers

    def setup_output_headers(self):
        """
        """
        self.output_headers = ['Nomenclature', 'N noeud poste', 'Article de tete',
                               '2','3', '4', '5', '6', '7', '8', '9', '10','11', 
                               '12', '13', '14', '15', '16', '17', '18', '19',
                               '20'
                               ]

        self.extraction_headers = ['Article de tete', 'Article fabrique',
                                   'Niveau de nomeclature', 'Article consomme',
                                   'Designation article', 'Type'
                                   ]


"""
Datasets properties are set through the instanciation of Configuration.

Parameters :
    - location of the dataset directory 
    - the excel file name in there.
    - sheet_name is first sheet by default (=0). See pandas Documentations
"""
config = Configuration(dataset_directory = '../../datasets',
                       excel_file_name='Nomenclatures.xlsx',
                       )
