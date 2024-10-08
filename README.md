# Image Summarize

This project takes an input image and generates a sentence summarizing the content of the image. Inspired by the work in [ImageCaption](https://github.com/haoyu-he/ImageCaption), it focuses on using deep learning models to generate accurate captions for images.

<table>
  <tr>
    <th colspan=2> Results</th>
  </tr>
  <tr>
    <td><img width="602" alt="Screenshot 2024-09-18 at 6 35 33 PM" src="https://github.com/user-attachments/assets/d7b70c7e-788f-4a05-af3d-5bd98ca07a92"></td>
    <td><img width="604" alt="Screenshot 2024-09-18 at 6 35 44 PM" src="https://github.com/user-attachments/assets/e80b03e4-f21f-436a-be3b-0890b4c9881d"></td>
  </tr>
</table>

### Output on Random Images

<table>
  <tr>
    <th>LSTM Output</th>
    <th>GPT-1 Output</th>
  <tr>
    <td><img width="550" alt="random image1 output on lstm model" src="https://github.com/user-attachments/assets/17ec1c0f-e784-4e06-8662-b61f5c9071eb"></td>
    <td><img width="550"  alt="random image1 output on gpt1 model" src="https://github.com/user-attachments/assets/0bd016b0-913a-46ca-b5ad-0cca2e297da9"></td>
  </tr>
  <tr>
    <td><img width="550"  alt="random image2 output on lstm model" src="https://github.com/user-attachments/assets/4e020ddc-0d57-4f2d-9098-4fccb49323b2"></td>
    <td><img width="550" alt="random image2 output on gpt1 model" src="https://github.com/user-attachments/assets/d76436c7-5c6a-47bd-b030-2276208a543e"></td>
  </tr>
</table>

## Dataset

The project utilizes the **Flickr30k** dataset from Kaggle. This dataset provides a rich set of images with corresponding captions, which are used for training and testing the model.

## Model Architecture

### Image Encoder
The image encoder uses a pre-trained **ResNet-50** model. The last layer of ResNet-50 is removed and replaced with a linear layer to map the image embeddings to the same size as the word embeddings. The output of the image encoder is used as the first token for the text decoder.

### Text Decoder
For text generation, two different architectures were implemented:
1. **LSTM (Long Short-Term Memory)** for sequential text decoding.
2. **Stacked GPT-like Transformer Blocks**, using a Transformer encoder with masks to simulate GPT architecture.

The models are defined in the `model.py` file.

## Training

To train the model, refer to the step-by-step instructions provided in the `ImageSummarize.ipynb` notebook. During training:
- The model achieved approximately **40-43% accuracy** for 5-10 epochs.
- Both LSTM and GPT models showed similar performance in generating image captions.

## Training Results
<table>
  <tr>
    <th>LSTM Accuracy for 5 epochs</th>
    <th>GPT-1 Accuracy for 5 epochs</th>
  </tr>
  <tr>
    <td><img width="834" alt="lstm_output" src="https://github.com/user-attachments/assets/3f859dec-b5eb-4132-bbca-8780375307a0"></td>
    <td><img width="809" alt="gpt_output" src="https://github.com/user-attachments/assets/3da3bed3-bb56-4a7d-bc36-c13a6cdbe9bd"></td>
  </tr>
  <tr>
    <th>LSTM Accuracy for 10 epochs</th>
    <th>GPT-1 Accuracy for 10 epochs</th>
  </tr>
  <tr>
    <td><img width="767" alt="lstm_10e" src="https://github.com/user-attachments/assets/675504ab-e471-47bc-892a-942bc6016973"></td>
    <td><img width="739" alt="gpt1_10e" src="https://github.com/user-attachments/assets/46b10d94-eca1-44aa-bd7d-6684825a77eb">
</td>
  </tr>
</table>

### Issues During Training
- Configuration file paths and variables must be properly set before training.
- Initial training on **MacBook M1** was slow due to hardware limitations.
- Training was shifted to **Google Colab**, where GPU resources were used, but later reverted to CPU, which also proved to be slow.
- Finally, training was successfully completed on **Kaggle's GPU T4x2**, where the models achieved about 40% accuracy.

## Running the Image Summarizer App

An **Image Summarizer Generator App** is provided to generate captions for images interactively. To run the app:
1. Navigate to the `app` folder.
2. Run the `app.py` file using the command:
   ```
   python app.py
   ```

### App Features
- **Upload Image**: You can choose to upload an image for caption generation.
- **Load Sample Image**: The app can randomly load a sample image using the **Unsplash API**.
- The uploaded or generated image is previewed in the GUI.
- Users can choose between the **LSTM** or **GPT-1** models for caption generation.
- The generated caption is displayed, and both the image and its caption can be saved to a folder.
<table>
  <tr>
    <th>LSTM Output</th>
    <th>GPT-1 Output</th>
  <tr>
    <td><img width="542" alt="Screenshot 2024-09-18 at 6 01 13 PM" src="https://github.com/user-attachments/assets/78a2feee-7b79-4245-96b7-69955b708e03"></td>
    <td><img width="541" alt="Screenshot 2024-09-18 at 6 01 26 PM" src="https://github.com/user-attachments/assets/6f7962ed-de9b-45af-b052-2ac9d65ff2fd"></td>
  </tr>
</table>

## Notes
- Ensure all configurations (paths and variables) are correctly set before training or running the app.
- Performance may vary depending on the computational resources available during training.
