# Language Detection

Gathered language detection dataset using lexicon, all steps in [notebook](notebook).

## download

- Download dataset from here, https://huggingface.co/datasets/mesolitica/language-detection/resolve/main/train-test.json

Splitted 80% to train and 20% to test.

Labels,

1. english, 2215975, 553739
2. malay, 7202654, 1800649
3. indonesia, 2295708, 576059
4. rojak, 757559, 189678
5. manglish, 726678, 181442
6. others, 5720022, 1428083

- Download dataset from here, https://huggingface.co/datasets/mesolitica/language-detection/resolve/main/sublanguages.json

Labels,

1. malay 7179851
2. kedah 14071
3. johor 2172
4. melaka 7714
5. terengganu 4436
6. sarawak 6429
7. negeri-sembilan 7717
8. kelantan 2305
9. pahang 3647
10. perak 1307
11. sabah 1253

## Citation

```bibtex
@misc{Malay-Dataset, We gather Bahasa Malaysia corpus!, Lexicon based Language Detection dataset,
  author = {Husein, Zolkepli},
  title = {Malay-Dataset},
  year = {2018},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/huseinzol05/malay-dataset/tree/master/corpus/language-detection}}
}
```