import pandas as pd
from typing import Tuple


class DataIngestion:

    def expand_columns(self, df: pd.DataFrame, target: str) -> pd.DataFrame:
        """Expand the column in the dataframe.

        Args:
            df (pd.DataFrame): DataFrame to expand.
            target (str): Column to expand.

        Returns:
            pd.DataFrame: DataFrame with expanded column.
        """

        df = df.explode(target).reset_index(drop=True)

        columns = list(df[target][0].keys())

        for col in columns:
            df[col] = df[target].str.get(col)

        df = df.drop(target, axis=1)

        return df


    def normalize_data(self, df: pd.DataFrame) -> Tuple:
        """Split DataFrame into two normalized dataframe.

        Args:
            df (pd.DataFrame): Dataframe to normalize.

        Returns:
            List[pd.DataFrame]: Normalized dataframes.
        """

        discount_col = df.pop('Discount')
        df.insert(4, 'Discount', discount_col)

        first_df = df.iloc[:, :4]
        first_df = first_df.groupby('NFeID').first()

        second_df = df.iloc[:, 3:]
        second_df = second_df.set_index('NFeID')

        return first_df, second_df


    def main(self):

        # read json as dataframe
        df = pd.read_json('data.json')

        df = self.expand_columns(df=df, target="ItemList")
        first_df, second_df = self.normalize_data(df=df)

        print(first_df)
        print(second_df)


dataIngestion = DataIngestion()
dataIngestion.main()
