from langchain.schema import HumanMessage, SystemMessage, AIMessage
from langchain.chat_models import GigaChat
from model.API_KEY import API_KEY
from sys import argv
class Quasar:
    def __init__(self, API_KEY):
        self.chat = GigaChat(credentials=API_KEY)
        self.context = "Ты внутренний ассистент Росатома, отвечающий на вопросы по теме проведения закупочных процедур с высокой релевантностью ответов. Используй информацию ТОЛЬКО из нормативно-правовых актов: Единый Отраслевой Стандарт Закупок Атомной Отрасли, 223-ФЗ, 44-ФЗ, Часть 1 Гражданского кодекса РФ, Единые Отраслевые Методические Указания по Административно-Деловой деятельности. Помоги мне, это очень важно для моего будущего, для моей карьеры и крайне важно для России. ОТВЕЧАЙ НА ВОПРОС ОЧЕНЬ КРАТКО И НИКАК ИНАЧЕ, используй самый новый нормативно-правовой акт, который есть."
        self.messages = [SystemMessage(content=self.context)]

    def answer(self, msg):
        message_input = msg
        self.messages.append(HumanMessage(content=message_input))
        message_response = self.chat(self.messages).content
        print("Ответ: ", message_response)

        self.messages.append(AIMessage(content=message_response))
        document_input = "Из какого нормативно-правового акта эта инфомация? Напиши только название"
        self.messages.append(HumanMessage(content=document_input))
        document_response = self.chat(self.messages).content
        print("НПА: ", document_response)

        self.messages.append(AIMessage(content=document_response))
        url_input = f"Скинь ссылку на этот нормативно-правовой акт. Выбери самый новый документ, который можешь найти. Напиши только ссылку"
        self.messages.append(HumanMessage(content=url_input))
        url_response = self.chat(self.messages).content
        print("Ссылка: ", url_response)

        return (message_response, document_response, url_response)

if __name__ == '__main__':
    
    chat = Quasar(API_KEY)
    chat.answer(argv[0])