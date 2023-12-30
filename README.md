# Tatoeba Data Processor

This Python module allows you to download and process data from the Tatoeba website, specifically focusing on English and Central Kurdish sentences.

## Installation

Ensure you have Python 3 installed. Clone this repository and install the required dependencies using:

```bash
pip install .
```

## Usage

### Importing the Module

```python
from tatoeba_ckb import Tatoeba
```

### Initializing the Tatoeba Class

```python
tatoeba = Tatoeba()
```

### Methods

#### `bz2url_to_df(url: str) -> pd.DataFrame`

Download a bz2-compressed file from a URL and return a pandas DataFrame.

Example:

```python
data_frame = tatoeba.bz2url_to_df('https://your-url.com/your-file.bz2')
```

#### `download_eng_ckb_data_from_tatoeba(ckb_eng_links_url: str = CKB_ENG_LINKS_URL, ckb_sentences_detailed_url: str = CKB_SENTENCES_DETAILED_URL, eng_sentences_detailed_url: str = ENG_SENTENCES_DETAILED_URL) -> None`

Download and merge English and Central Kurdish data from the Tatoeba website.

Example:

```python
tatoeba.download_eng_ckb_data_from_tatoeba()
```

#### `get_data(data_path: str = "data", source: str = "eng_ckb_tatoeba") -> pd.DataFrame`

Get the data from a given source.

Example:

```python
data = tatoeba.get_data()
```

#### `get_data_sources() -> list`

Get the list of supported data sources.

Example:

```python
sources = tatoeba.get_data_sources()
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[UNLICENSED](LICENSE)
