import os
import torch

from dataclasses import dataclass


@dataclass
class Config:
    seed = 2024
    device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')

    access_key = "YOUR_ACESS_KEY"

    vocab_size = 7500
    word_emb_dim = 512
    hidden_dim = 1024
    num_lstm_layers = 1
    num_gpt1_layers = 6
    n_head = 8

    batch = 32
    epoch = 5
    lr_lstm = 5e-4
    lr_gpt1 = 2e-4

    train_size = 0.8

    max_length = 128

    caption_file = "captions.txt"
    vocab_file = "vocab.txt"

    @property
    def encoder_lstm_file(self) -> str:
        return (
                'models/lstm/encoder' +
                '_lstm.pt'
        )

    @property
    def decoder_lstm_file(self) -> str:
        return (
                'models/lstm/decoder' +
                '_lstm.pt'
        )

    @property
    def embedding_lstm_file(self) -> str:
        return (
                'models/lstm/embedding' +
                '_lstm.pt'
        )

    @property
    def encoder_gpt1_file(self) -> str:
        return (
                'models/gpt1/encoder' +
                '_gpt1.pt'
        )

    @property
    def decoder_gpt1_file(self) -> str:
        return (
                'models/gpt1/decoder' +
                '_gpt1.pt'
        )

    @property
    def embedding_gpt1_file(self) -> str:
        return (
                'models/gpt1/embedding' +
                '_gpt1.pt'
        )
