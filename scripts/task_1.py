import telethon
from telethon.sync import TelegramClient
import re
import pandas as pd
from sklearn.model_selection import train_test_split

class EthioMartNER:
    def __init__(self, api_id, api_hash, phone_number):
        self.client = TelegramClient('ethio_mart', api_id, api_hash)
        self.phone_number = phone_number

    def connect_to_telegram(self):
        """Connect to the Telegram client."""
        self.client.connect()
        if not self.client.is_user_authorized():
            self.client.send_code_request(self.phone_number)
            self.client.sign_in(self.phone_number, input('Enter the code: '))

    def fetch_data(self, channels, output_file):
        """Fetch messages from specified Telegram channels."""
        data = []
        
        for channel in channels:
            try:
                for message in self.client.iter_messages(channel):
                    if message.text or message.media:
                        data.append({
                            'channel': channel,
                            'message_id': message.id,
                            'sender': message.sender_id,
                            'timestamp': message.date,
                            'content': message.text or '',
                        })
            except Exception as e:
                print(f"Error fetching data from {channel}: {e}")

        df = pd.DataFrame(data)
        df.to_csv(output_file, index=False)
        print(f"Data saved to {output_file}")

    def preprocess_text(self, input_file, output_file):
        """Preprocess and clean the text data."""
        df = pd.read_csv(input_file)
        
        # Tokenization, normalization, and handling Amharic-specific linguistic features
        df['cleaned_content'] = df['content'].apply(lambda x: self._clean_text(x))
        
        # Save preprocessed data
        df.to_csv(output_file, index=False)
        print(f"Preprocessed data saved to {output_file}")

    def _clean_text(self, text):
        """Tokenize and clean text for Amharic-specific features."""
        text = re.sub(r'[\n\r]+', ' ', text)
        text = re.sub(r'[^ሀ-፿\s]', '', text)  # Keep Amharic characters
        text = re.sub(r'\s+', ' ', text).strip()
        return text

    def label_data_conll(self, input_file, output_file):
        """Label a subset of the dataset in CoNLL format."""
        df = pd.read_csv(input_file)
        messages = df['cleaned_content'].sample(n=50, random_state=42).tolist()

        with open(output_file, 'w', encoding='utf-8') as f:
            for message in messages:
                tokens = message.split()
                for token in tokens:
                    label = self._get_label(token)
                    f.write(f"{token} {label}\n")
                f.write("\n")

        print(f"Labeled data saved in CoNLL format to {output_file}")

    def _get_label(self, token):
        """Determine the label for a given token."""
        if re.match(r'^\d+\s*ብር$', token):
            return 'B-PRICE'
        elif re.match(r'^\d+$', token):
            return 'I-PRICE'
        elif token in ['ቦሌ', 'አዲስ', 'ቤተሰብ']:
            return 'B-LOC'
        elif re.match(r'^[A-Za-z]+$', token):
            return 'B-Product'
        else:
            return 'O'

