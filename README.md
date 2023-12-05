# fakeDetect: an enhanced version of the RawNet model to detect deepfake audios.

>Statistics show that the amount of DeepFake cases has doubled in North America from 2022 until the first quarter of 2023, while printed forgeries have decreased significantly (Sumsub, 2023). Accordingly, we assume this happens as well in other >countries due to the popularity of deepfake tools since last year when ChatGPT became popular. Statistics show that the amount of DeepFake cases has doubled in North America from 2022 until the first quarter of 2023, while printed forgeries have >decreased significantly (Sumsub, 2023). Accordingly, we assume this happens as well in other countries due to the popularity of deepfake tools since last year when ChatGPT became popular.
>In this project we are building on the work we found in the literature review to improve the algorithms that can detect Deepfake audio. Most of these audios are attended to affect people’s opinions if not stelling their money. 

# Dataset & Pre-trained Models

You can find the wavefake dataset on [zenodo](https://zenodo.org/record/5642694) or  [kaggle](https://www.kaggle.com/datasets/andreadiubaldo/wavefake-test).
Orignal RawNet model [here](https://github.com/asvspoof-challenge/2021/tree/main/LA/Baseline-RawNet2) 

## Setup
We use Cuda so run the following after installing it
```
conda create myenv python=3.8

conda activate myenv
```
You can install all needed dependencies by running:

```
pip install -r requirements.txt
```

## Training models

You can use the training script as follows:

```
python train_models.py -h

usage: train_models.py [-h] [--amount AMOUNT] [--clusters CLUSTERS] [--batch_size BATCH_SIZE] [--epochs EPOCHS] [--retraining RETRAINING] [--ckpt CKPT] [--use_em] [--raw_net] [--cuda] [--lfcc] [--debug] [--verbose] REAL FAKE

positional arguments:
  REAL                  Directory containing real data.
  FAKE                  Directory containing fake data.

optional arguments:
  -h, --help            show this help message and exit
  --amount AMOUNT, -a AMOUNT
                        Amount of files to load from each directory (default: None - all).
  --clusters CLUSTERS, -k CLUSTERS
                        The amount of clusters to learn (default: 128).
  --batch_size BATCH_SIZE, -b BATCH_SIZE
                        Batch size (default: 8).
  --epochs EPOCHS, -e EPOCHS
                        Epochs (default: 5).
  --retraining RETRAINING, -r RETRAINING
                        Retraining tries (default: 10).
  --ckpt CKPT           Checkpoint directory (default: trained_models).
  --use_em              Use EM version?
  --raw_net             Train raw net version?
  --cuda, -c            Use cuda?
  --lfcc, -l            Use LFCC instead of MFCC?
  --debug, -d           Only use minimal amount of files?
  --verbose, -v         Display debug information?
```

**Example**

To train all EM-GMMs use:

`python train_models.py /dataset/LJSpeech-1.1/wavs /dataset/generated_audio -b 32 --raw_net -a 700 --epochs 20 `



## Evaluation

For evaluation, you can use the evaluate_models script:

```
python evaluate_models.p -h

usage: evaluate_models.py [-h] [--output OUTPUT] [--clusters CLUSTERS] [--amount AMOUNT] [--raw_net] [--debug] [--cuda] REAL FAKE MODELS

positional arguments:
  REAL                  Directory containing real data.
  FAKE                  Directory containing fake data.
  MODELS                Directory containing model checkpoints.

optional arguments:
  -h, --help            show this help message and exit
  --output OUTPUT, -o OUTPUT
                        Output file name.
  --clusters CLUSTERS, -k CLUSTERS
                        The amount of clusters to learn (default: 128).
  --amount AMOUNT, -a AMOUNT
                        Amount of files to load from each directory (default: None - all).
  --raw_net, -r         RawNet models?
  --debug, -d           Only use minimal amount of files?
  --cuda, -c            Use cuda?
```

**Example**

` python evaluate_models.py /data/LJSpeech-1.1/wavs /data/generated_audio trained_models/lfcc/em`

Make sure to move the out-of-distribution models to a seperate directory first!

## Attribution

We provide a script to attribute the GMM models:
```
python attribute.py -h

usage: attribute.py [-h] [--clusters CLUSTERS] [--steps STEPS] [--blur] FILE REAL_MODEL FAKE_MODEL

positional arguments:
  FILE                  Audio sample to attribute.
  REAL_MODEL            Real model to attribute.
  FAKE_MODEL            Fake Model to attribute.

optional arguments:
  -h, --help            show this help message and exit
  --clusters CLUSTERS, -k CLUSTERS
                        The amount of clusters to learn (default: 128).
  --steps STEPS, -m STEPS
                        Amount of steps for integrated gradients.
  --blur, -b            Compute BlurIG instead.
```

**Example**

`python attribute.py /data/LJSpeech-1.1/wavs/LJ008-0217.wav  path/to/real/model.pth path/to/fake/model.pth`

# BibTeX

When you cite our work feel free to use the following bibtex entry:
```
@inproceedings{
  frank2021wavefake,
  title={{WaveFake: A Data Set to Facilitate Audio Deepfake Detection}},
  author={Joel Frank and Lea Sch{\"o}nherr},
  booktitle={Thirty-fifth Conference on Neural Information Processing Systems Datasets and Benchmarks Track},
  year={2021},
}
```
# DeepML_FakeDetect
