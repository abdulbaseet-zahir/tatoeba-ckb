import unittest
import pandas as pd
from tatoeba_ckb import Tatoeba


class TestTatoeba(unittest.TestCase):
    def test_bz2url_to_df(self):
        tatoeba = Tatoeba()

        df = tatoeba.bz2url_to_df(
            "https://downloads.tatoeba.org/exports/per_language/eng/eng_sentences_detailed.tsv.bz2"
        )
        df.columns = [
            "eng_id",
            "language",
            "eng_sentence",
            "eng_username",
            "created_date",
            "updated_date",
        ]

        self.assertIsInstance(df, pd.DataFrame)
        self.assertEqual(
            df.columns.tolist(),
            [
                "eng_id",
                "language",
                "eng_sentence",
                "eng_username",
                "created_date",
                "updated_date",
            ],
        )
        self.assertEqual(df[:10_000].shape, (10_000, 6))


if __name__ == "__main__":
    unittest.main()
