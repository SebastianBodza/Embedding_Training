from datasets import load_dataset, Dataset, DatasetDict
import re
dataset = load_dataset("SebastianBodza/synthetic_RAG_dataset_ger_de_v02")
df = dataset["train"].to_pandas()
df['Positive'].fillna('', inplace=True)
df['Hard Negative'].fillna('', inplace=True)
df['Positive'] = df['Positive'].astype(str)
df['Hard Negative'] = df['Hard Negative'].astype(str)
df_train = df.copy()
df_train = df_train.set_index("index")

df['Positive'] = df['raw_texts'].str.extract(r'Positive german document .*?:\s*(.*)', expand=False)
df['Hard Negative'] = df['raw_texts'].str.extract(
    r'Hard negative german document \(not containing the viable information for the queries!\):\s*(.*?)\n\nPositive german document', 
    flags=re.DOTALL, 
    expand=False
)
filtered_df = df.dropna(subset=["Positive", "Hard Negative"])
filtered_dataset = Dataset.from_pandas(filtered_df.set_index("index"))
new_dataset_dict = DatasetDict({
    'raw': Dataset.from_pandas(df_train),
    'filtered': filtered_dataset 
})
new_dataset_dict.push_to_hub("SebastianBodza/synthetic_RAG_dataset_ger_de_v02", token="")
