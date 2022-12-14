from src.chat_statistics.chat_statistics import ChatStatistics
from src.data import DATA_DIR

if __name__ == '__main__':
    chat_data = ChatStatistics(file_path=DATA_DIR / 'CS-Stack.json')
    chat_data.generate_word_cloud(output_file_path=DATA_DIR)
