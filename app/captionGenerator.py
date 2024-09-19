import torch
from torchvision import transforms

from config import Config
from vocab import Vocab
from model import Encoder, DecoderLSTM, DecoderGPT1

config = Config()
vocab = Vocab()
vocab.load_vocab(config.vocab_file)
transform = transforms.Compose([
        transforms.Resize((256, 256)),
        transforms.CenterCrop(224),
        transforms.ToTensor()
        ])

normalize = transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])

encoder = Encoder(word_emb_dim=config.word_emb_dim).to(config.device)
emb_layer = torch.nn.Embedding(num_embeddings=config.vocab_size,
                            embedding_dim=config.word_emb_dim,
                            padding_idx=vocab.word2index[vocab.pad]).to(config.device)

def get_caption_lstm(image):
    image_ori = transform(image).to(config.device)
    image_norm = normalize(image_ori)

    decoder = DecoderLSTM(word_emb_dim=config.word_emb_dim,
                          hidden_dim=config.hidden_dim,
                          num_layers=config.num_lstm_layers,
                          vocab_size=config.vocab_size).to(config.device)
    
    encoder.load_state_dict(torch.load(config.encoder_lstm_file, map_location=config.device))
    emb_layer.load_state_dict(torch.load(config.embedding_lstm_file, map_location=config.device))
    decoder.load_state_dict(torch.load(config.decoder_lstm_file, map_location=config.device))

    encoder.eval()
    emb_layer.eval()
    decoder.eval()

    image_norm = image_norm.unsqueeze(0)

    hidden = decoder.hidden_0
    cell = decoder.cell_0

    sentence = []
    word_indices = torch.tensor([vocab.word2index[vocab.sos]], dtype=torch.long, device=config.device).unsqueeze(0) 

    image_emb = encoder(image_norm).unsqueeze(0)

    for i in range(config.max_length - 1):

        word_seq = emb_layer(word_indices).permute(1, 0, 2)
        # word_seq: (sequence_length, batch: 1, word_emb_dim)

        decoder_input = torch.cat([image_emb, word_seq], dim=0)
        next_pred, (hidden, cell) = decoder(decoder_input, hidden, cell)
        next_pred = torch.argmax(next_pred[-1, 0, :])

        word_indices = torch.cat([word_indices, next_pred.view(1, 1)], dim=-1)

        next_word = vocab.index2word[next_pred.item()]
        if next_word == vocab.eos:
            break

        sentence.append(next_word)
    
    sentence = ' '.join(sentence).strip().capitalize() + '.'
    print(sentence)

    return sentence

def get_caption_gpt1(image):
    image_ori = transform(image).to(config.device)
    image_norm = normalize(image_ori)

    decoder = DecoderGPT1(word_emb_dim=config.word_emb_dim,
                          nhead=config.n_head,
                          hidden_dim=config.hidden_dim,
                          num_layers=config.num_gpt1_layers,
                          vocab_size=config.vocab_size).to(config.device)
    
    encoder.load_state_dict(torch.load(config.encoder_gpt1_file, map_location=config.device))
    emb_layer.load_state_dict(torch.load(config.embedding_gpt1_file, map_location=config.device))
    decoder.load_state_dict(torch.load(config.decoder_gpt1_file, map_location=config.device))

    encoder.eval()
    emb_layer.eval()
    decoder.eval()

    image_norm = image_norm.unsqueeze(0)

    sentence = []
    word_indices = torch.tensor([vocab.word2index[vocab.sos]], dtype=torch.long, device=config.device).unsqueeze(0)

    # get image embedding
    image_emb = encoder(image_norm).unsqueeze(0)

    for i in range(config.max_length - 1):

        word_seq = emb_layer(word_indices).permute(1, 0, 2)
        # word_seq: (sequence_length, batch: 1, word_emb_dim)

        decoder_input = torch.cat([image_emb, word_seq], dim=0)
        next_pred = decoder(decoder_input)
            
        next_pred = torch.argmax(next_pred[-1, 0, :])

        word_indices = torch.cat([word_indices, next_pred.view(1, 1)], dim=-1)

        next_word = vocab.index2word[next_pred.item()]
        if next_word == vocab.eos:
            break

        sentence.append(next_word)
    
    sentence = ' '.join(sentence).strip().capitalize() + '.'
    print(sentence)

    return sentence