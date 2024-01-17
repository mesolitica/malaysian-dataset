# Pseudostreaming Malaysian Youtube videos

Original dataset at https://github.com/mesolitica/malaysian-dataset/tree/master/speech-to-text-semisupervised/pseudolabel-whisper

We use https://huggingface.co/mesolitica/conformer-medium-mixed to generate pseudostreaming dataset.

If we have an audio with the transcribe, eg,

```
hi, my name is husein, (0.0, 6.0)
```

We can generate streaming dataset like below if you have the force alignment,

```
hi (0.0, 0.5)
hi, my (0.0, 1.0)
hi, my name (0.0, 2.0)
```