# iTRANSLIT
__iTRANSLIT__ is a deep learning based transliteration package for indic language

## Installation
```pip install itranslit```

## Dependency
- `pytorch 1.7.0 or 1.7.0+`

NB: No `GPU` need. It's `CPU` based.

## Supported Language and Language Code
| __Language Name__ | __Langauage Code__ |
| --- | :-- |
| Bangla | bn |
| Gujarati| gu |
| Hindi | hi |
| Punjabi | pa |
| Sindhi | sd |
| Urdu | ur |
| Malayalam | ml |
| Tamil | ta |
|    |      |


## API

```py
from itranslit import Translit

translit = Translit('bn')
word = "aami"
output = translit.predict(word, topk=10)
print(output)

```

## Datasets and Training Details
- We used [Google Dakshina Dataset](https://github.com/google-research-datasets/dakshina)
- Thanks to [AI4Bharat](https://github.com/AI4Bharat/IndianNLP-Transliteration) for providing training notebook with details explanation
- We trained Google Dakshina lexicons train datasets for 10 epochs with batch size 128, 1e-3, embedding dim = 300, hidden dim = 512, lstm, used attention
- We evaluated our trained model with Google Dakshina lexicon test data using [AI4Bharat evaluation script](https://raw.githubusercontent.com/AI4Bharat/IndianNLP-Transliteration/jgeob-dev/tools/accuracy_reporter/accuracy_news.py)
- You can find evaluation summary [here]()