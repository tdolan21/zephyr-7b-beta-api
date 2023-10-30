# Zephyr 7B β API

[Zephyr](assets/thumbnail.png)

This repo contains an api and demo application for the zephyr-7b-beta model from HuggingFace. The base model is mistral-7b-v0.1 and this is the second zephyr finetune from the huggingface team.


More details can be found in the [model card](https://huggingface.co/HuggingFaceH4/zephyr-7b-beta) or the [technical report](https://arxiv.org/abs/2310.16944)

## Requirements

    Transformers 4.35.0.dev0
    Pytorch 2.0.1+cu118
    Datasets 2.12.0
    Tokenizers 0.14.0

Make sure these are properly installed before using the application. If you are running locally, the recommended virtual env is conda.

## Installation

Linux:

```bash
git clone https://github.com/tdolan21/zephyr-7b-beta-api
cd zephyr-7b-beta-api
pip install -r requirements.txt
chmod +x run.sh
```

Windows: 

```bash 
git clone https://github.com/tdolan21/zephyr-7b-beta-api
cd zephyr-7b-beta-api
pip install -r requirements.txt
```

## Usage

Once the requirements are installed, you will run the application using:

Linux:

```bash
./run.sh
```

Windows:

```bash
run.bat
```

## License

This application follows the same MIT license the model was originally released with. 

## Citations 

```
@misc{tunstall2023zephyr,
      title={Zephyr: Direct Distillation of LM Alignment}, 
      author={Lewis Tunstall and Edward Beeching and Nathan Lambert and Nazneen Rajani and Kashif Rasul and Younes Belkada and Shengyi Huang and Leandro von Werra and Clémentine Fourrier and Nathan Habib and Nathan Sarrazin and Omar Sanseviero and Alexander M. Rush and Thomas Wolf},
      year={2023},
      eprint={2310.16944},
      archivePrefix={arXiv},
      primaryClass={cs.LG}
}
```

