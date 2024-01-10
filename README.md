# TatoebaCKB: Data Download and Processing Tool for Tatoeba Website

This repository hosts a suite of tools designed to facilitate the download and processing of parallel sentence data sourced from Tatoeba for the English and Central Kurdish (ckb) languages.

## Key Features

- Directly downloads data from Tatoeba's public datasets.
- Efficiently processes and consolidates English and Central Kurdish sentences for enhanced accessibility.
- Persists prepared data in a tab-separated (TSV) file format, ensuring seamless integration with various tools.

## Installation from Repository

Ensure Python 3 is installed. Clone this repository and install necessary dependencies using the following command:

```bash
pip install git+https://github.com/abdulbaseet-zahir/tatoeba-ckb.git
```

### Usage

1. Import the `TatoebaCKB` class

```python
from tatoeba_ckb import TatoebaCKB
```

2. Create an instance of the class

```python
tatoeba_ckb = TatoebaCKB()
```
3. Get the data:
```python
data = tatoeba_ckb.get_data()
```

 This will download the data if it's not already present, and return a pandas DataFrame containing the parsed data.

### Data Structure

**The DataFrame contains the following columns:**

- eng_id: ID of the English sentence
- ckb_id: ID of the Central Kurdish sentence
- eng_sentence: The English sentence
- ckb_sentence: The Central Kurdish sentence
- eng_username: Username of the English sentence contributor
- ckb_username: Username of the Central Kurdish sentence contributor


### Explore and Use the Data

**Access and manipulate the data using pandas operations:**
```python
print(data.head())  # View the first few rows
print(data.shape)   # Check the dimensions of the DataFrame
```

**Use the data for various tasks, such as:**
- Building machine translation models
- Creating language learning resources
- Researching language patterns

### Additional Information

- For more details on available methods, refer to the class documentation within the code.
- If you encounter any issues, please open an issue on the repository.

### Contribute

We welcome contributions to this project! Feel free to submit issues or pull requests.

### License
[UNLICENSED](LICENSE)

