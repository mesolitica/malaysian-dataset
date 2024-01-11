# Mixtral Magicoder: Source Code Is All You Need on various programming languages

We sampled programming languages from https://huggingface.co/datasets/bigcode/the-stack-dedup and pushed to https://huggingface.co/datasets/malaysia-ai/starcoderdata-sample

After that, we use [Magicoder: Source Code Is All You Need on various programming languages](https://github.com/ise-uiuc/magicoder) template, we target at least 10k rows for each programming languages.

1. C++, 10747 rows
2. C#, 10193 rows
3. CUDA, 13843 rows
4. Dockerfile, 13286 rows
5. Go, 10143 rows
6. Java, 11221 rows
7. JavaScript, 11758 rows
8. Kotlin, 12790 rows
9. PHP, 10176 rows
10. Python, other than `pandas` and `sklearn` and `matplotlib` and `plotly`, 10925 rows
11. Python, must have `pandas` or `sklearn` or `matplotlib` or `plotly`, focused on data analytics, 53959 rows
12. Ruby, 10201 rows
13. Rust, 10271 rows
14. Scala, 10017 rows
15. Shell, 10848 rows
16. SQL, 27668 rows
17. Swift, 10187 rows
18. TypeScript, 14248 rows

## precaution

1. There is no validation for the output generated.
2. Always filter short answers.

## download

Entire dataset at https://huggingface.co/datasets/mesolitica/mixtral-magicoder